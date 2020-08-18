import Vue from 'vue'
import router from './router'
import store from './store'
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css' // progress bar style
import {ACCESS_TOKEN} from '@/store/mutation-types'
import notification from 'ant-design-vue/es/notification'

NProgress.configure({showSpinner: false}) // NProgress Configuration

const whiteList = ['/user/login', '/user/register', '/user/register-result', '/user/alteration','/video'] // no redirect whitelist

router.beforeEach((to, from, next) => {
    NProgress.start() // start progress bar

    if (Vue.ls.get(ACCESS_TOKEN)) { //验证token
        /* has token */
        if (to.path === '/user/login') {
            next({path: '/star'})
            NProgress.done()
        } else {
            // const redirect = decodeURIComponent(from.query.redirect || to.path)
            // debugger
            // if (to.path === redirect) {
            //     // hack方法 确保addRoutes已完成 ,set the replace: true so the navigation will not leave a history record
            //     next({...to, replace: true})
            // } else {
            //     // 跳转到目的路由
            //     next({path: redirect})
            // }
            next()
        }
    } else {
        if (whiteList.indexOf(to.path) !== -1) {
            // 在免登录白名单，直接进入
            next()
        } else {
            notification.error({message: "请先登陆！", description: "禁止访问！", duration: 3})
            next({path: '/user/login', query: {redirect: to.fullPath}})
            NProgress.done() // if current page is login will not trigger afterEach hook, so manually handle it
        }
    }
});

router.afterEach(() => {
    NProgress.done() // finish progress bar
})
