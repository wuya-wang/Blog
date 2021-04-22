import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueWechatTitle from 'vue-wechat-title'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css'
import './assets/css/all.css'
import './assets/iconfont/iconfont.css'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import axios from "./axios/interceptor";


Vue.use(VueWechatTitle)
Vue.use(mavonEditor)
Vue.use(ElementUI);
Vue.config.productionTip = false
Vue.prototype.$axios = axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')


