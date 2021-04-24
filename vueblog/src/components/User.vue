<template>
 <div>
   <el-input
       placeholder="请输入内容"
       v-model="eMail"
       clearable>
   </el-input>
   <el-button @click="postMail()">提交</el-button>
 </div>
</template>

<script>
// import axios from "axios";
import Qs from "qs";

export default {
  name: "User",
  data(){
    return {
      eMail: ""
    }
  },
  methods:{
    postMail(){
      this.$axios({
        url:"http://127.0.0.1:9999/api/blog/v1/celery/",
        method:'post',
        data:Qs.stringify({
          email: this.eMail,
        })
      }).then((res) => {
        console.log(res.data)
        // this.eMail = ''
      })
    }
  },

}
</script>

<style scoped>

</style>