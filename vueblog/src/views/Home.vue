<template>
  <div id="home">
    <div v-if="this.screenWidth >= 400" :class="{'max-aside': maxAside, 'min-aside': minAside}">
      <div class="block">
        <el-avatar :size="56" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
      </div>
      <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          :router=true>
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-user" ></i>
            <span v-if="userinfo.username" v-text="userinfo.username "></span>
            <span v-else v-text="username"></span>
          </template>
          <el-menu-item-group v-if="this.$store.getters.userLoginStatus">
            <el-menu-item index="/user">个人中心</el-menu-item>
            <el-menu-item @click="logout()">登出</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group v-else>
            <el-menu-item index="/login"><i class="el-icon-s-promotion"></i>登录</el-menu-item>
            <el-menu-item index="register"><i class="el-icon-s-custom"></i>注册</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-menu-item index='/blog'>
          <i class="el-icon-notebook-1"></i>
          <span slot="title">个人博客</span>
        </el-menu-item>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-folder-opened"></i>
            <span>Demo</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/visualization"><i class="el-icon-data-line"></i>可视化</el-menu-item>
            <el-menu-item index="/data-analysis"><i class="el-icon-pie-chart"></i>数据分析</el-menu-item>
            <el-menu-item index="/e-commerce"><i class="el-icon-shopping-bag-1"></i>电商</el-menu-item>
            <el-menu-item index="/chat"><i class="el-icon-chat-dot-square"></i>在线聊天</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <div v-if="this.$store.state.userinfo.username === this.superuser">
          <el-menu-item index="/add-article">
            <i class="el-icon-edit"></i>
            <span slot="title">文章编辑</span>
          </el-menu-item>
          <el-submenu index="5" >
            <template slot="title">
              <i class="el-icon-c-scale-to-original"></i>
              <span>管理员</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="5-1">文章管理</el-menu-item>
              <el-menu-item index="5-2">用户管理</el-menu-item>
              <el-menu-item index="5-3">管理</el-menu-item>
              <el-menu-item index="5-4">管理</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </div>
        <el-menu-item index="/other-world">
          <i class="el-icon-picture-outline"></i>
          <span slot="title">里世界</span>
        </el-menu-item>
      </el-menu>
    </div>
    <div v-else>
      <el-drawer
          title="我是标题"
          :size="'70%'"
          :direction="'ltr'"
          :visible.sync="drawer"
          :with-header="false">
        <div>
          <div class="block">
            <el-avatar :size="56" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
          </div>
          <el-menu
              default-active="1"
              class="el-menu-vertical-demo"
              :router=true>
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-user" ></i>
                <span v-if="userinfo.username" v-text="userinfo.username "></span>
                <span v-else v-text="username"></span>
              </template>
              <el-menu-item-group v-if="this.$store.getters.userLoginStatus">
                <el-menu-item @click="drawer = false" index="/user">个人中心</el-menu-item>
                <el-menu-item  @click="logout(); drawer = false">登出</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group v-else>
                <el-menu-item @click="drawer = false" index="/login"><i class="el-icon-s-promotion"></i>登录</el-menu-item>
                <el-menu-item @click="drawer = false" index="register"><i class="el-icon-s-custom"></i>注册</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-menu-item @click="drawer = false" index='/blog'>
              <i class="el-icon-notebook-1"></i>
              <span slot="title">个人博客</span>
            </el-menu-item>
            <el-submenu index="3">
              <template slot="title">
                <i class="el-icon-folder-opened"></i>
                <span>Demo</span>
              </template>
              <el-menu-item-group>
                <el-menu-item @click="drawer = false" index="/visualization"><i class="el-icon-data-line"></i>可视化</el-menu-item>
                <el-menu-item @click="drawer = false" index="/data-analysis"><i class="el-icon-pie-chart"></i>数据分析</el-menu-item>
                <el-menu-item @click="drawer = false" index="/e-commerce"><i class="el-icon-shopping-bag-1"></i>电商</el-menu-item>
                <el-menu-item @click="drawer = false" index="/chat"><i class="el-icon-chat-dot-square"></i>在线聊天</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <div v-if="this.$store.state.userinfo.username === this.superuser">
              <el-menu-item @click="drawer = false" index="/add-article">
                <i class="el-icon-edit"></i>
                <span slot="title">文章编辑</span>
              </el-menu-item>
              <el-submenu index="5" >
                <template slot="title">
                  <i class="el-icon-c-scale-to-original"></i>
                  <span>管理员</span>
                </template>
                <el-menu-item-group>
                  <el-menu-item @click="drawer = false" index="5-1">文章管理</el-menu-item>
                  <el-menu-item @click="drawer = false" index="5-2">用户管理</el-menu-item>
                  <el-menu-item @click="drawer = false" index="5-3">管理</el-menu-item>
                  <el-menu-item @click="drawer = false" index="5-4">管理</el-menu-item>
                </el-menu-item-group>
              </el-submenu>
            </div>
            <el-menu-item @click="drawer = false" index="/other-world">
              <i class="el-icon-picture-outline"></i>
              <span slot="title">里世界</span>
            </el-menu-item>
          </el-menu>
        </div>
      </el-drawer>
    </div>
    <div v-if="this.screenWidth >= 400" :class="{'min-panel':minPanel, 'max-panel':maxPanel}">
      <div class="header">
        <div>
          <i v-if="this.screenWidth >= 400" @click="setAside()" class="el-icon-s-operation pc-icon"></i>
          <i v-else @click="drawer = true" class="el-icon-s-operation el-icon"></i>
        </div>
      </div>
      <div class="main">
        <router-view v-wechat-title="$route.meta.title"></router-view>
      </div>
      <div class="footer">
        <a href="https://beian.miit.gov.cn/#/home"><p>粤ICP备20054363号</p></a>
        <p>Copyright © 2021 Hosted by 浮生无涯</p>
      </div>
    </div>
    <div v-else class="max-panel">
      <div class="header">
        <div>
          <i v-if="this.screenWidth >= 400" @click="setAside()" class="el-icon-s-operation pc-icon"></i>
          <i v-else @click="drawer = true" class="el-icon-s-operation el-icon"></i>
        </div>
      </div>
      <div class="main">
        <router-view v-wechat-title="$route.meta.title"></router-view>
      </div>
      <div class="footer">
        <a href="https://beian.miit.gov.cn/#/home"><p>粤ICP备20054363号</p></a>
        <p>Copyright © 2021 Hosted by 浮生无涯</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      superuser:'wuya',
      username:'游客',
      userinfo: this.$store.state.userinfo,
      screenWidth: document.body.clientWidth,
      maxAside:true,
      minAside:false,
      maxPanel:false,
      minPanel:true,
      drawer: false,
    }
  },
  created() {
    window.onresize = () => {
      this.screenWidth = document.body.clientWidth;
    };
  },
  mounted() {
  },
  computed: {},
  watch: {
    screenWidth(val){
      this.screenWidth = val
    },
  },
  methods: {
    setAside(){
      this.maxAside = !this.maxAside
      this.minAside = !this.minAside
      this.maxPanel = !this.maxPanel
      this.minPanel = !this.minPanel
    },
    logout(){
      this.$store.dispatch('logout',this.$store.getters.userLoginStatus)
    },
  },
}
</script>

<style>
.wrapper {
  position: relative;
  top: 0;
  height: 100vh;
}
.max-aside {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 2;
  width: 250px;
  background: url("../assets/img/abg.jpg") rgba(0, 0, 0, 0.7) center;
  background-size: cover;
  background-blend-mode: multiply;
  transition: all .5s;
}
.min-aside {
  position: fixed;
  top: 0;
  bottom: 0;
  left: -250px;
  z-index: 2;
  width: 250px;
  background: url("../assets/img/abg.jpg") rgba(0, 0, 0, 0.7) center;
  background-size: cover;
  background-blend-mode: multiply;
  transition: all .5s;
}
.el-drawer__body{
  background: url("../assets/img/abg.jpg") rgba(0, 0, 0, .7) center ;
  background-size: cover;
  background-blend-mode: multiply;
}
.min-panel {
  position: relative;
  float: right;
  width: calc(100% - 250px);
  transition: all .5s;
  z-index: 1;
}
.max-panel{
  position: relative;
  float: right;
  width: calc(100%);
  transition: all .5s;
  z-index: 1;
}
.header {
  position: fixed;
  width: 100%;
  top: 0;
  height: 56px;
  z-index: 1000;
  text-align: center;
  background: #f9d0e2;
  transition: all .5s;
}
.header span{
  display: block;
  font-size: 1.5rem;
  margin: 10px 0;
}
.main{
  position: relative;
  top: 56px;
  min-height: 826px;
  margin-bottom: 56px;
  z-index: 900;
  background: rgb(255, 255, 255);
}
.footer{
  position: relative;
  width: 100%;
  bottom: 0;
  padding: 0 10px;
  height: 56px;
  z-index: 1000;
  text-align: center;
}
.footer p{
  line-height: 28px;
  font-weight: 600;
}
.footer a{
  text-decoration: none;
  color: inherit;
}
.footer a:hover{
  text-decoration: none;
  color: inherit;
}
.el-icon{
  position: absolute;
  left: -5px;
  padding: 10px 0;
  color: #ffffff;
  font-size: 36px;
  width: 56px;
  height: 56px;
  font-weight: 600;
  transition: all .5s;
}
.pc-icon{
  float: left;
  padding: 10px 0 ;
  margin-left: -5px;
  color: #fcfcfc;
  font-size: 40px;
  width: 56px;
  height: 56px;
  font-weight: 600;
  transition: all .5s;
}

/*头像*/
.block{
  margin: 5px;
  text-align: center;
  line-height: 0;
}
.el-menu-item.is-active {
    color: #ffffff;
}
.iconfont{
  font-size: 20px;
  margin: 0 5px;
}
p{
  margin: 0;
  line-height: 30px;
}
.el-menu-item-group__title{
 padding: 0;
}
.el-drawer__wrapper {
  min-height: 100vh;
}
</style>