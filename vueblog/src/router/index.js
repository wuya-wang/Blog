import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
// import store from '../store'
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
        redirect: '/wakatime',
        // beforeEnter:(to, form, next) =>{
        //     if (store.state.userinfo.token){
        //         next()
        //     } else {
        //         next("/login")
        //     }
        // },
        children:[
            {
                path:'/wakatime',
                name:'WakaTime',
                component:() => import('../components/WakaTime'),
                meta: {
                    title: "wakatime"
                },
            },
            {
                path:'/user',
                name:'User',
                component:() => import('../components/User'),
                meta: {
                    title: "用户中心"
                },
            },
            {
                path: '/other-world',
                name: 'OtherWorld',
                component: () => import('../components/OtherWorld.vue'),
                meta: {
                    title: "里世界"
                },
            },
            {
                path:'/visualization',
                name:'Visualization',
                component:() => import('../components/Visualization'),
                meta: {
                    title: "可视化"
                },
            },
            {
                path:'/data-analysis',
                name:'DataAnalysis',
                component:() => import('../components/DataAnalysis'),
                meta: {
                    title: "数据分析"
                },
            },
            {
                path:'/e-commerce',
                name:'E-Commerce',
                component:() => import('../components/E-Commerce'),
                meta: {
                    title: "电商"
                },
            },
            {
                path:'/chat',
                name:'chat',
                component:() => import('../components/Chat'),
                meta: {
                    title: "数据分析"
                },
            },
            {
                path:'/blog',
                name:'Blog',
                component:() => import('../components/Blog'),
                meta: {
                    title: "博客"
                },
                redirect: '/article-list',
                children:[
                    {
                        path: '/article-list',
                        name: 'ArticleList',
                        component: () => import('../components/ArticleList'),
                        meta: {
                            title: "文章列表"
                        }
                    },
                    {
                        path: '/article',
                        name: 'Article',
                        component: () => import('../components/Article'),
                        meta: {
                            title: "文章详情"
                        }
                    },
                ]
            },
            {
                path:'/add-article',
                name:'AddArticle',
                component:() => import('../components/AddArticle'),
                meta: {
                    title: "编辑"
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
    mode: 'history',
})

export default router
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}