<template>
  <div id="home">
    <div class="wrapper">
      <div :class="{'aside':Aside ,'min-side':minAside,}">
        <div class="block">
          <el-avatar :size="56" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
        </div>
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            :router=true>
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-user" ></i>
              <span>{{ userinfo.username }}</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1">个人中心</el-menu-item>
              <el-menu-item @click="logout()">登出</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index='/blog'>
            <i class="el-icon-menu"></i>
            <span slot="title">个人博客</span>
          </el-menu-item>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-user"></i>
              <span>Demo</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="3-1">个人中心</el-menu-item>
              <el-menu-item index="3-2">选项2</el-menu-item>
              <el-menu-item index="3-3">个人中心</el-menu-item>
              <el-menu-item index="3-4">选项2</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="/add-article">
            <i class="el-icon-setting"></i>
            <span slot="title">文章编辑</span>
          </el-menu-item>
          <el-submenu index="5">
            <template slot="title">
              <i class="el-icon-user"></i>
              <span>管理员</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="5-1">文章管理</el-menu-item>
              <el-menu-item index="5-2">用户管理</el-menu-item>
              <el-menu-item index="5-3">管理</el-menu-item>
              <el-menu-item index="5-4">管理</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="6">
            <i class="el-icon-setting"></i>
            <span slot="title">里世界</span>
          </el-menu-item>
        </el-menu>
      </div>
      <div  :class="{'panel':Panel, 'max-panel':maxPanel}">
        <div class="header" :class="{'max-header':maxHeader}">
          <div>
            <i @click="setAside()" class="el-icon-more-outline" :class="{'mobile-icon':mobileIcon, 'pc-icon':pcIcon, 'el-icon':elIcon}"></i>
          </div>
          1231564
        </div>
        <div class="main">

          <router-view></router-view>
        </div>
        <div class="footer">footer</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      conceal_main: true,
      userinfo: this.$store.state.userinfo,
      screenWidth: document.body.clientWidth,
      Aside:'',
      minAside:'',
      maxPanel:'',
      Panel:'',
      maxHeader:'',
      mobileIcon:'',
      pcIcon:'',
      elIcon:'',
    }
  },
  created() {
    window.onresize = () => {
      this.screenWidth = document.body.clientWidth;
    };
  },
  mounted() {
    this.inAside()
  },
  computed: {},
  watch: {
    screenWidth(val){
      this.screenWidth = val
    },
  },
  methods: {
    inAside(){
      if (this.screenWidth > 400){
        this.Aside = true
        this.minAside = false
        this.maxPanel = false
        this.Panel = true
        this.maxHeader=true
        this.pcIcon = true
      } else {
        this.Aside = false
        this.minAside = true
        this.maxPanel = true
        this.Panel = false
        this.maxHeader=false
        this.mobileIcon = false
        this.elIcon = true
      }
    },
    setAside(){
      // 移动端
      if (this.screenWidth<400){
        if (this.Aside){
          this.Aside = false
          this.minAside = true
          this.maxPanel = true
          this.mobileIcon = false
        } else {
          this.Aside = true
          this.minAside = false
          this.maxPanel = true
          this.mobileIcon = true
        }
      }else {
        if (this.Aside){
          this.Aside = false
          this.minAside = true
          this.maxPanel = true
          this.maxHeader = false
        } else {
          this.Aside = true
          this.minAside = false
          this.maxPanel = false
          this.maxHeader = true
        }
      }
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
.aside {
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
.min-side{
  position: fixed;
  left: -300px;
  top: 0;
  right: 0;
  bottom: 0;
  z-index: 2;
  width: 300px;
  background: url("../assets/img/abg.jpg") rgba(0, 0, 0, .7) center ;
  background-size: cover;
  background-blend-mode: multiply;
  transition: all .5s;
}
.panel {
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
.max-header{
  width: calc(100% - 250px);
  transition: all .5s;
}

.main{
  position: relative;
  top: 56px;
  margin-bottom: 112px;
  padding: 0 10px;;
  z-index: 900;
  background: rgb(255, 255, 255);
}
.footer{
  position: fixed;
  width: 100%;
  bottom: 0;
  padding: 0 10px;
  height: 56px;
  z-index: 1000;
  background: #f2a8c9;
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
.mobile-icon{
  left: 250px;
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

</style>