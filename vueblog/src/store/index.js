import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";
import Qs from "qs";
import $router from "../router";
import createPersistedState from "vuex-persistedstate"
Vue.use(Vuex)

export default new Vuex.Store({
  // state就是Vuex中的公共的状态, 将state看作是所有组件的data, 用于保存所有组件的公共数据
  state: {
    userinfo:{}
  },

  // getters属性理解为所有组件的computed属性,也就是计算属性
  // vuex的官方文档也是说到可以将getter理解为store的计算属性
  // getters的返回值会根据它的依赖被缓存起来,且只有当它的依赖值发生了改变才会被重新计算
  getters:{
    userLoginStatus(state){
      return state.userinfo.token
    }
  },

  // mutations理解为store中的methods
  // mutations对象中保存着更改数据的回调函数,该函数名官方规定叫type
  // 第一个参数是state, 第二参数是payload, 也就是自定义的参数
  // 调用mutations中回调函数, 只能使用store.commit(type, payload)
  mutations: {
    // 保存用户登录状态
    saveUserinfo(state, userinfo){
      state.userinfo = userinfo
    },
    // 清空用户登录状态
    clearUserinfo(state){
      state.userinfo = {}
    },
  },
  // actions类似于mutations,不同在于：
  //  actions提交的是mutations而不是直接变更状态
  //  actions中可以包含异步操作, mutations中绝对不允许出现异步
  //  actions中的回调函数的第一个参数是context, 是一个与store实例具有相同属性和方法的对象
  //  使用store.dispatch()调用actions中回调函数
  actions: {
    // 登录
    loginUser({commit}, userinfo){
      axios({
        url: 'http://127.0.0.1:9999/api/login/',
        method: 'post',
        data: Qs.stringify(userinfo)
      }).then((res) => {
        // console.log(res.data)
        if (res.data === '用户名不存在'){
          Vue.prototype.$message({
            showClose: true,
            message: '用户名不存在',
            type: 'error',
            center: true,
          });
          return;
        }
        if (res.data === '密码错误'){
          // 不使用全局就将组件中的this传递过来
          Vue.prototype.$message({
            showClose: true,
            message: '密码错误',
            type: 'error',
            center: true,
          });
          return;
        }
        commit('saveUserinfo', res.data)
        // 缓存
        localStorage.setItem('token',res.data.token)
        $router.push({path: '/'}).then(()=>{});
      })
    },
    // 注册
    registerUser({commit}, userinfo){
    axios({
      url:'http://127.0.0.1:9999/api/register/',
      method:'post',
      data:Qs.stringify(userinfo)
    }).then((res) => {
      if (res.data === 'error_email'){
        Vue.prototype.$message({
          showClose: true,
          message: '邮箱格式错误',
          type: 'error',
          center: true,
        });
        return;
      }
      if (res.data === 'error_username'){
        Vue.prototype.$message({
          showClose: true,
          message: '用户名格式错误',
          type: 'error',
          center: true,
        });
        return;
      }
      if (res.data === 'error_password'){
        Vue.prototype.$message({
          showClose: true,
          message: '密码错误',
          type: 'error',
          center: true,
        });
        return;
      }
      if (res.data === '密码不一致'){
        Vue.prototype.$message({
          showClose: true,
          message: '密码不一致',
          type: 'error',
          center: true,
        });
        return;
      }
      commit('saveUserinfo', res.data)
      localStorage.setItem('token', res.data.token)
      $router.push({path: '/'}).then(()=>{});
    })
  },
    // 登出
    logout({commit},token){
      axios({
        url:'http://127.0.0.1:9999/api/logout/',
        method:'post',
        data:Qs.stringify({token})
      }).then()
      commit('clearUserinfo')
      localStorage.removeItem('token')
      $router.push({name:'Login'}).then(()=>{})
    }
  },

  modules: {
  },

  // 数据持久化
  plugins: [createPersistedState({
    reducer(val) {
      return {
        // 只储存state中的userinfo
        userinfo: val.userinfo
      }
    }
  })],
})
