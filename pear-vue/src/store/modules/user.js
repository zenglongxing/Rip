import Vue from 'vue'
import {login, logout, phoneLogin} from "@/api/login"
import {ACCESS_TOKEN, USER_NAME, USER_INFO, USER_AUTH, SYS_BUTTON_AUTH} from "@/store/mutation-types"
import {welcome} from "@/utils/util"
import {getAction} from '@/api/manage'

const user = {
    state: {
        token: '',
        username: '',
        realname: '',
        welcome: '',
        avatar: '',
        workdate: '',
        permissionList: [],
        info: {}
    },

    mutations: {
        SET_TOKEN: (state, token) => {
            state.token = token
        },
        SET_NAME: (state, {username, realname, welcome}) => {
            state.username = username
            state.realname = realname
            state.welcome = welcome
        },
        SET_AVATAR: (state, avatar) => {
            state.avatar = avatar
        },
        SET_WORKDATE: (state, workdate) => {
            state.workdate = workdate
        },
        SET_PERMISSIONLIST: (state, permissionList) => {
            state.permissionList = permissionList
        },
        SET_INFO: (state, info) => {
            state.info = info
        },
    },

    actions: {
        // CAS验证登录
        ValidateLogin({commit}, userinfo) {
            return new Promise((resolve, reject) => {
                getAction("/cas/client/validateLogin", userinfo).then(response => {
                    console.log("----cas 登录--------", response);
                    if (response.success) {
                        const result = response.result
                        const userInfo = result.userInfo
                        Vue.ls.set(ACCESS_TOKEN, result.token, 7 * 24 * 60 * 60 * 1000)
                        Vue.ls.set(USER_NAME, userInfo.username, 7 * 24 * 60 * 60 * 1000)
                        Vue.ls.set(USER_INFO, userInfo, 7 * 24 * 60 * 60 * 1000)
                        commit('SET_TOKEN', result.token)
                        commit('SET_INFO', userInfo)
                        commit('SET_NAME', {
                            username: userInfo.username,
                            realname: userInfo.realname,
                            welcome: welcome()
                        })
                        commit('SET_AVATAR', userInfo.avatar)
                        commit('SET_WORKDATE', userinfo.workdate)
                        sessionStorage.setItem("workdate", JSON.stringify(userinfo.workdate));
                        resolve(response)
                    } else {
                        resolve(response)
                    }
                }).catch(error => {
                    reject(error)
                })
            })
        },
        // 登录
        Login({commit}, userinfo) {
            return new Promise((resolve, reject) => {
                login(userinfo).then(response => {
                    if (response.code == '200') {
                        let token=response.token
                        const userInfo = response.userInfo
                        Vue.ls.set(ACCESS_TOKEN, token, 7 * 24 * 60 * 60 * 1000)
                        Vue.ls.set(USER_NAME, userInfo.username, 7 * 24 * 60 * 60 * 1000)
                        Vue.ls.set(USER_INFO, userInfo, 7 * 24 * 60 * 60 * 1000)
                        commit('SET_TOKEN', token)
                        // commit('SET_INFO', userInfo)
                        // commit('SET_NAME', {
                        //     username: userInfo.username,
                        //     realname: userInfo.realname,
                        //     welcome: welcome()
                        // })
                        // commit('SET_AVATAR', userInfo.avatar)
                        resolve(response)
                    } else {
                        reject(response)
                    }
                }).catch(error => {
                    reject(error)
                })
            })
        },
        //手机号登录
        PhoneLogin({commit}, userinfo) {
            return new Promise((resolve, reject) => {
                phoneLogin(userinfo).then(response => {
                    if (response.code == '200') {
                        const result = response.result
                        const userInfo = result.userInfo
                        Vue.ls.set(ACCESS_TOKEN, result.token, 7 * 24 * 60 * 60 * 1000)
                        Vue.ls.set(USER_NAME, userInfo.username, 7 * 24 * 60 * 60 * 1000)
                        Vue.ls.set(USER_INFO, userInfo, 7 * 24 * 60 * 60 * 1000)
                        commit('SET_TOKEN', result.token)
                        commit('SET_INFO', userInfo)
                        commit('SET_NAME', {
                            username: userInfo.username,
                            realname: userInfo.realname,
                            welcome: welcome()
                        })
                        commit('SET_AVATAR', userInfo.avatar)
                        commit('SET_WORKDATE', userinfo.workdate)
                        sessionStorage.setItem("workdate", JSON.stringify(userinfo.workdate));
                        resolve(response)
                    } else {
                        reject(response)
                    }
                }).catch(error => {
                    reject(error)
                })
            })
        },

        // 登出
        Logout({commit, state}) {
            return new Promise((resolve) => {
                let logoutToken = state.token;
                commit('SET_TOKEN', '')
                commit('SET_PERMISSIONLIST', [])
                Vue.ls.remove(ACCESS_TOKEN)
                //console.log('logoutToken: '+ logoutToken)
                logout(logoutToken).then(() => {
                    //var sevice = "http://"+window.location.host+"/";
                    //var serviceUrl = encodeURIComponent(sevice);
                    //window.location.href = window._CONFIG['casPrefixUrl']+"/logout?service="+serviceUrl;
                    resolve()
                }).catch(() => {
                    resolve()
                })
            })
        },

    }
}

export default user
