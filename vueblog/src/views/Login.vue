<template>
  <div class="login">
    <div class="login-main">
      <div class="navbar">
        <div class="navbar-register" @click="goRegister()">
          <i class="iconfont icon-zhuce"></i>
          <p>REGISTER</p>
        </div>
        <div class="navbar-login" @click="goLogin()">
          <i class="iconfont icon-zhiwendenglu"></i>
          <p>LOGIN</p>
        </div>
      </div>
      <el-row>
        <el-col :xs="20" :sm="16" :md="10" :lg="6" :xl="6">
          <div class="login-box">
            <el-card class="box-card">
              <div slot="header" class="clearfix login__card_title">
                <span>LOGIN</span>
              </div>
              <div class="form">
                <div class="input" :class="{'focus':focusUsername}" placeholder="Username">
                  <el-input @focus="inUsername()" @blur="outUsername()" v-model="userinfo.username" type="text"></el-input>
                </div>
                <div class="input" :class="{'focus':focusPassword}" placeholder="Password">
                  <el-input @focus="inPassword()" @blur="outPassword()" v-model="userinfo.password" type="password" show-password></el-input>
                </div>
                <span><a href="#">Forget?</a></span>
              </div>
              <el-button class="login__button" type="text" @click="loginUser()">Let's go</el-button>
            </el-card>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>

export default {
  name: "Login",
  data(){
    return{
      focusUsername:false,
      focusPassword:false,
      userinfo:{
        username:'',
        password:"",
      }
    }
  },
  methods:{
    // 输入框焦点事件
    inUsername(){this.focusUsername = true},
    outUsername(){if (this.userinfo.username.length===0){this.focusUsername = false}},
    inPassword(){this.focusPassword = true},
    outPassword(){if (this.userinfo.password.length===0){this.focusPassword = false}},
    goRegister(){
      this.$router.push({name:'Register'})
    },
    goLogin(){
      this.$router.push({name:'Login'})
    },
    loginUser(){
      if (this.userinfo.username.length===0 || this.userinfo.password.length===0){
        this.$message({
          showClose: true,
          message: '用户名或密码为空',
          type: 'error',
          center: true,
        });
        return
      }
      this.$store.dispatch('loginUser', this.userinfo)

    }
  },
}
</script>

<style scoped>
.login{
  height: 100vh;
  width: 100vw;
  background: url("../assets/img/IMG_0102.png") center;
  background-size: cover;
}
.login-main{
  position: relative;
}
.navbar{
  position: absolute;
  right: 0;
  padding: 10px 10px;
  z-index: 10;
}
.navbar-register{
  display: flex;
  margin: 0 10px;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.navbar-login{
  display: flex;
  margin: 0 10px;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.navbar-register p,
.navbar-login p{
  margin: 0 5px;
}
.navbar-register:hover,
.navbar-login:hover{
  color: #bf1438;
  background-color: #bf143840;
  border-radius: 8px;
}
.iconfont{
  font-size: 20px;
  margin: 0 5px;
}
p{
  margin: 0;
  line-height: 30px;
}
.el-col{
  position: absolute;
  left: 50%;
  top: 200px;
  transform: translate(-50%);
  animation: login_card 1s ease-out 1 forwards;
}
@keyframes login_card {
  0% {
    left:-200px;
  }
  100% {
   left: 50%;
  }
}
.el-card {
    border: 1px solid #f4b2ce30;
    background-color: #f4b2ce50;
}
.login__card_title{
  text-align: center;
  font-size: 32px;
  font-weight: 600;
  color: pink;
}
/*卡片身体*/
.form .input {
  position: relative;
  margin: 1.5rem;
}
.input::after{
  content: attr(placeholder);
  position: absolute;
  left: 0;
  top: -1%;
  font-size: 1.4rem;
  color: #ba6a71;
  transition: all .5s;
}
.input.focus::after{
  top: -85%;
  transition: all .5s;
}
.form span{
  margin-left: 1.5rem;
  color: #ba6a71;
}
.login__button{
  position:relative;
  padding: 5px;
  color: #bd156e;
  font-size: 1.5rem;
  left: 50%;
  bottom: 0;
  transform: translate(-50%);
}
/*输入框*/
.login >>> .el-input__inner {
    -webkit-appearance: none;
    background-color: rgba(0, 0, 0, 0);
    background-image: none;
    border: none;
    border-radius: 0;
    border-bottom: .1rem solid pink;
    padding: 0 0 0 2px;
    box-sizing: border-box;
    color: #000;
    display: inline-block;
    font-size: 20px;
    height: 30px;
    line-height: 30px;
    outline: none;
}
.login >>> .el-input__inner:focus{
    border-bottom: .1rem solid pink;
}
.login >>> .el-input__inner:hover{
    border-color: rgba(0, 0, 0, 0);
    border-bottom: .1rem solid pink;
}
/*密码眼睛*/
.login >>> .el-input .el-input__clear:hover {
    color: pink;
}
.login >>> .el-input .el-input__clear {
    color: #C0C4CC;
    font-size: 20px;
    cursor: pointer;
    transition: color .2s cubic-bezier(.645,.045,.355,1);
}
.login >>> .el-input__icon {
    height: 100%;
    width: 17px;
    text-align: center;
    transition: all .3s;
    line-height: 30px;
}
</style>