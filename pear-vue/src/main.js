import Vue from 'vue'
import Antd from 'ant-design-vue'
import App from './App.vue'
import Storage from 'vue-ls'
import 'ant-design-vue/dist/antd.css';
import router from './router'
import store from './store'
import preview from 'vue-photo-preview'
import 'vue-photo-preview/dist/skin.css'
import '@api/video'


import config from '@/defaultSettings'
import '@/permission' // permission control


Vue.config.productionTip = false;
Vue.use(Antd);
Vue.use(Storage, config.storageOptions);
Vue.use(preview)


new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app')
