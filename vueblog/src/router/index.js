import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    // 首页
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            title: "浮生无涯"
        },
        children:[
            {
                path:'/blog',
                name:'Blog',
                component:() => import('../components/Blog'),
                meta: {
                    title: "博客"
                },
            },
            {
                path:'/helloWord',
                name:'HelloWorld',
                component:() => import('../components/HelloWorld')
            }
        ]
    },
    // 登录
    {
        path: '/login',
        name: 'Login',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue'),
        meta: {
            title: "登录"
        }
    },
    // 注册
    {
        path: '/register',
        name: 'Register',
        component: () => import('../views/Register.vue'),
        meta: {
            title: "注册"
        },
    },


]

const router = new VueRouter({
  routes,
})

export default router
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}