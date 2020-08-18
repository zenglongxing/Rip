<template>
    <div class="main">
        <a-form :form="form" class="user-layout-login" ref="formLogin" id="formLogin">
            <a-tabs
                    :activeKey="customActiveKey"
                    :tabBarStyle="{ textAlign: 'center', borderBottom: 'unset' }"
                    @change="handleTabClick">
                <a-tab-pane key="tab1" tab="账号密码登录">
                    <a-form-item :wrapperCol="wrapperCol">
                        <a-input
                                size="large"
                                v-decorator="['username',validatorRules.username,{ validator: this.handleUsernameOrEmail }]"
                                type="text"
                                placeholder="请输入账户名">
                            <a-icon slot="prefix" type="user" :style="{ color: 'rgba(0,0,0,.25)' }"/>
                        </a-input>
                    </a-form-item>

                    <a-form-item :wrapperCol="wrapperCol">
                        <a-input
                                v-decorator="['password',validatorRules.password]"
                                size="large"
                                type="password"
                                autocomplete="false"
                                placeholder="密码">
                            <a-icon slot="prefix" type="lock" :style="{ color: 'rgba(0,0,0,.25)' }"/>
                        </a-input>
                    </a-form-item>


                    <!--           <a-row :gutter="0">
                                <a-col :span="14">
                                  <a-form-item>
                                    <a-input
                                      v-decorator="['inputCode',validatorRules.inputCode]"
                                      size="large"
                                      type="text"
                                      @change="inputCodeChange"
                                      placeholder="请输入验证码">
                                      <a-icon slot="prefix" v-if=" inputCodeContent==verifiedCode " type="smile" :style="{ color: 'rgba(0,0,0,.25)' }"/>
                                      <a-icon slot="prefix" v-else type="frown" :style="{ color: 'rgba(0,0,0,.25)' }"/>
                                    </a-input>
                                  </a-form-item>
                                </a-col>
                                <a-col  :span="10">
                                  <j-graphic-code @success="generateCode" ref="jgraphicCodeRef" style="float: right" remote></j-graphic-code>
                                </a-col>
                              </a-row>

                     -->
                </a-tab-pane>

                <!-- <a-tab-pane key="tab2" tab="手机号登陆">
                  <a-form-item>
                    <a-input
                      v-decorator="['mobile',validatorRules.mobile]"
                      size="large"
                      type="text"
                      placeholder="手机号">
                      <a-icon slot="prefix" type="mobile" :style="{ color: 'rgba(0,0,0,.25)' }"/>
                    </a-input>
                  </a-form-item>

                  <a-row :gutter="16">
                    <a-col class="gutter-row" :span="16">
                      <a-form-item>
                        <a-input
                          v-decorator="['captcha',validatorRules.captcha]"
                          size="large"
                          type="text"
                          placeholder="请输入验证码">
                          <a-icon slot="prefix" type="mail" :style="{ color: 'rgba(0,0,0,.25)' }"/>
                        </a-input>
                      </a-form-item>
                    </a-col>
                    <a-col class="gutter-row" :span="8">
                      <a-button
                        class="getCaptcha"
                        tabindex="-1"
                        :disabled="state.smsSendBtn"
                        @click.stop.prevent="getCaptcha"
                        v-text="!state.smsSendBtn && '获取验证码' || (state.time+' s')"></a-button>
                    </a-col>
                  </a-row>
                </a-tab-pane> -->

            </a-tabs>
            <a-form-item>
                <a-checkbox v-decorator="['rememberMe', {initialValue: true, valuePropName: 'checked'}]"
                            style="font-size:16px;">自动登陆
                </a-checkbox>
                <router-link :to="{ name: 'alteration'}" class="forge-password" style="float: right;font-size:16px;">
                    忘记密码
                </router-link>
                <router-link :to="{ name: 'register'}" class="forge-password"
                             style="float: right;margin-right: 10px;font-size:16px;">
                    注册账户
                </router-link>
            </a-form-item>

            <a-form-item style="margin-top:24px">
                <a-button
                        size="large"
                        type="primary"
                        htmlType="submit"
                        class="login-button"
                        :loading="loginBtn"
                        @click.stop.prevent="handleSubmit"
                        :disabled="loginBtn">确定
                </a-button>
            </a-form-item>

            <!-- <div class="user-login-other">
              <span>其他登陆方式</span>
              <a><a-icon class="item-icon" type="alipay-circle"></a-icon></a>
              <a><a-icon class="item-icon" type="taobao-circle"></a-icon></a>
              <a><a-icon class="item-icon" type="weibo-circle"></a-icon></a>
              <router-link class="register" :to="{ name: 'register' }">
                注册账户
              </router-link>
            </div>-->
        </a-form>

    </div>
</template>

<script>
//import md5 from "md5"
import api from '@/api'
import {timeFix} from "@/utils/util"
import Vue from 'vue'
import {mapActions} from 'vuex'
import {ACCESS_TOKEN} from "@/store/mutation-types"
import {putAction} from '@/api/manage'
import {postAction} from '@/api/manage'
import store from '@/store/'
import {USER_INFO} from "@/store/mutation-types"

export default {
    components: {},
    data() {
        return {
            labelCol: {
                span: 8
            },
            wrapperCol: {
                span: 24
            },
            customActiveKey: "tab1",
            loginBtn: false,
            // login type: 0 email, 1 username, 2 telephone
            loginType: 0,
            requiredTwoStepCaptcha: false,
            stepCaptchaVisible: false,
            form: this.$form.createForm(this),
            encryptedString: {
                key: "",
                iv: "",
            },
            state: {
                time: 60,
                smsSendBtn: false,
            },
            validatorRules: {
                username: {rules: [{required: true, message: '请输入用户名!', validator: 'click'}]},
                password: {rules: [{required: true, message: '请输入密码!', validator: 'click'}]},
                mobile: {rules: [{validator: this.validateMobile}]},
                workdate: {rules: [{required: true, message: '请输入时间!', validator: 'click'}]},
                // captcha:{rule: [{ required: true, message: '请输入验证码!'}]},
                // inputCode:{rules: [{ required: true, message: '请输入验证码!'},{validator: this.validateInputCode}]}
            },
            verifiedCode: "",
            inputCodeContent: "",
            inputCodeNull: true,
            departList: [],
            departVisible: false,
            departSelected: "",
            currentUsername: "",
            validate_status: ""
        }
    },
    created() {
        Vue.ls.remove(ACCESS_TOKEN)
        this.getRouterData();
        // update-begin- --- author:scott ------ date:20190805 ---- for:密码加密逻辑暂时注释掉，有点问题
        //this.getEncrypte();
        // update-end- --- author:scott ------ date:20190805 ---- for:密码加密逻辑暂时注释掉，有点问题
    },
    methods: {
        ...mapActions(["Login", "Logout", "PhoneLogin"]),
        // handler
        handleUsernameOrEmail(rule, value, callback) {
            const regex = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
            if (regex.test(value)) {
                this.loginType = 0
            } else {
                this.loginType = 1
            }
            callback()
        },
        dateFormat: function () {
            var date = new Date();
            var year = date.getFullYear();
            /* 在日期格式中，月份是从0开始的，因此要加0
                 * 使用三元表达式在小于10的前面加0，以达到格式统一  如 09:11:05
                 * */
            var month = date.getMonth() + 1 < 10 ? "0" + (date.getMonth() + 1) : date.getMonth() + 1;
            var day = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
            // 拼接
            return year + "-" + month + "-" + day;
        },
        handleTabClick(key) {
            this.customActiveKey = key
            // this.form.resetFields()
        },
        handleSubmit() {
            let that = this
            let loginParams = {};
            that.loginBtn = true;
            // 使用账户密码登陆
            if (that.customActiveKey === 'tab1') {
                that.form.validateFields(['username', 'password'], {force: true}, (err, values) => {
                    if (!err) {
                        loginParams.username = values.username
                        loginParams.password = values.password
                        that.Login(loginParams).then((res) => {
                            console.log(res);
                            this.loginSuccess()
                        }).catch((err) => {
                            that.requestFailed(err);
                        });


                    } else {
                        that.loginBtn = false;
                    }
                })
                // 使用手机号登陆
            }
        },
        loginSuccess() {
            // update-begin- author:sunjianlei --- date:20190812 --- for: 登录成功后不解除禁用按钮，防止多次点击
            // this.loginBtn = false
            // update-end- author:sunjianlei --- date:20190812 --- for: 登录成功后不解除禁用按钮，防止多次点击
            this.$router.push({name: "star"})
            this.$notification.success({
                message: '欢迎',
                description: `${timeFix()}，欢迎回来`,
            });
        },
        requestFailed(err) {
            this.$notification['error']({
                message: '登录失败',
                description: ((err.response || {}).data || {}).message || err.message || "请求出现错误，请稍后再试",
                duration: 4,
            });
            this.loginBtn = false;
        },
        getRouterData() {
            this.$nextTick(() => {
                this.form.setFieldsValue({
                    'username': this.$route.params.username
                });
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    .user-layout-login {
        label {
            font-size: 14px;
        }

        .getCaptcha {
            display: block;
            width: 100%;
            height: 40px;
        }

        .forge-password {
            font-size: 14px;
        }

        button.login-button {
            padding: 0 15px;
            font-size: 16px;
            height: 40px;
            width: 100%;
        }

        .user-login-other {
            text-align: left;
            margin-top: 24px;
            line-height: 22px;

            .item-icon {
                font-size: 24px;
                color: rgba(0, 0, 0, .2);
                margin-left: 16px;
                vertical-align: middle;
                cursor: pointer;
                transition: color .3s;

                &:hover {
                    color: #1890ff;
                }
            }

            .register {
                float: right;
            }
        }
    }

</style>
<style lang="scss">
    .valid-error .ant-select-selection__placeholder {
        color: #f5222d;
    }

    #formLogin {
        #username, #password, #password2, #email {
            background-color: #E8F0FE;
            border: 2px solid #DBDCDD;
        }

        .ant-tabs-nav-container {
            font-size: 16px !important;
        }

        .j-data-large input {
            height: 40px;
            padding: 6px 11px;
            font-size: 16px;
            background-color: #E8F0FE;
            border: 2px solid #DBDCDD;
        }
    }
</style>
