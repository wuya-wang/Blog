<template>
 <div id="blog">
    <el-row :gutter="10">
      <el-col :xs="24" :sm="24" :md="6" :lg="6" :xl="6">
        <div class="blog__choose">
          <el-card class="box-card" shadow="never">
            <div slot="header" class="clearfix">
              <span>分类</span>
            </div>
            <div v-for="(category, index) in category_list" :key="index" class="text item">
              <el-button class="blog__category_btn" @click="getCategoryArticle(category)">{{ category }}</el-button>
            </div>
          </el-card>
          <el-card class="box-card tag" shadow="never">
            <div slot="header" class="clearfix">
              <span>标签</span>
            </div>
            <div v-for="(tag, index) in tag_list" :key="index">
              <el-button round class="blog__tag_btn" @click="getTagArticle(tag)">{{ tag }}</el-button>
            </div>
          </el-card>
          <el-card class="box-card time" shadow="never">
            <div slot="header" class="clearfix">
              <span>时间</span>
            </div>
            <div v-for="(time, index) in time_list" :key="index">
              <el-button round class="blog__time_btn">{{ time }}</el-button>
            </div>
          </el-card>
          <el-button class="blog__all_article_btn" round @click=" toArticleList()">全部文章</el-button>
        </div>
      </el-col>

      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl='12' style="margin-top: 10px">
          <router-view v-wechat-title="$route.meta.title" :ArticleData="article_data"></router-view>
      </el-col>

      <el-col v-if="show" :xs="24" :sm="24" :md="6" :lg="6" :xl="6" style="margin-top: 10px">
        <div class="card">
          <el-row class="article-icon">
            <el-col :span="8">
              <i v-if="article_data.likes" class="iconfont icon-dianzan" style="color: #2496e2" @click="toLikes(article_data.likes)"></i>
              <i v-else class="iconfont icon-dianzan" @click="toLikes(article_data.likes)"></i>
              <span  style="margin-left: 5px"></span>
            </el-col>
            <el-col :span="8">
              <i v-if="article_data.collections"  class="iconfont icon-shoucang" style="color: red;" @click="toCollections(article_data.collections)"></i>
              <i v-else class="iconfont icon-shoucang"  @click="toCollections(article_data.collections)"></i>
              <span  style="margin-left: 5px"></span>
            </el-col>
            <el-col :span="8">
              <i v-if="article_data.comments"  class="iconfont icon-liuyanpinglun" style="color: #efb738"></i>
              <i v-else  class="iconfont icon-liuyanpinglun"></i>
            </el-col>
          </el-row>
          <div class="comment" style="padding: 0 .5rem .5rem .5rem">
            <div v-for="(comments, index) in article_data.comments_data" :key="index">
              <div class="clearfix">
                <span v-text="comments.user"></span>
                <p v-text="comments.text"></p>
                <p class="reply">回复</p>
              </div>
              <el-divider></el-divider>
            </div>
            <el-input
                type="textarea"
                :rows="2"
                placeholder="请输入内容"
                v-model="textarea">
            </el-input>
            <el-button style="width: 100%; margin-top: .5rem" round @click="makeComment()">发表</el-button>
          </div>
        </div>
      </el-col>

      <el-col v-else :xs="24" :sm="24" :md="6" :lg="6" :xl="6" style="margin-top: 10px">
          <el-carousel height=700px>
            <el-carousel-item v-for="(img, index) in img_list" :key="index">
              <el-image
                  style="height: 700px; width: 100%"
                  :src="img"
                  :fit="'cover'">
              </el-image>
            </el-carousel-item>
          </el-carousel>
      </el-col>
    </el-row>
 </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
  name: "Blog",
  data() {
    return {
      show:0,
      category_list: [],
      tag_list: [],
      img_list:[
          'http://127.0.0.1:9999/media/img/1616058747906-05_2009_11.jpg',
          'http://127.0.0.1:9999/media/img/1616060212342-005.jpg',
      ],
      time_list:[
          '2021-3', '2021-2', '2021-1'
      ],
      article_data:'',
      textarea:''
    }
  },
  created() {
    this.getTag()
    this.getCategory()
    this.Renovate()
  },
  mounted() {
  },
  components:{
  },
  watch:{
    $route(){
      if (this.$route.query.id){
        this.show = 1
        // console.log(this.$route.query.id)
        this.getArticle(this.$route.query.id)
      } else {
        this.show = 0
      }
    },
  },
  methods: {
    makeComment(){
      axios({
        url: 'http://127.0.0.1:9999/api/comment/',
        method: 'post',
        data:Qs.stringify({
          token: this.$store.getters.userLoginStatus,
          article_id:this.$route.query.id,
          comment:this.textarea,
        })
      }).then((res) => {
        if (res.data === 'ok'){
          this.$message({
            showClose: true,
            message: '发表成功',
            type: 'success',
            center: true,
          });
          this.textarea = ''
          this.getArticle()
        }
      })
    },
    Renovate(){
      if (this.$route.query.id){
        this.show = 1
        this.getArticle()
      }
    },
    getArticle(){
      axios({
        url: 'http://127.0.0.1:9999/api/article/',
        method: 'post',
        data:Qs.stringify({
          token: this.$store.getters.userLoginStatus,
          id:this.$route.query.id,
        })
      }).then((res) => {
        console.log(res.data)
        this.article_data = res.data
      })
    },
    toLikes(state){
      axios({
        url:'http://127.0.0.1:9999/api/like/',
        method:'post',
        data:Qs.stringify({
          article_id: this.$route.query.id,
          token: this.$store.getters.userLoginStatus,
          state: !state,
        })
      }).then(() => {
        this.getArticle()
      })
    },
    toCollections(state){
      axios({
        url:'http://127.0.0.1:9999/api/collection/',
        method:'post',
        data:Qs.stringify({
          article_id: this.$route.query.id,
          token: this.$store.getters.userLoginStatus,
          state: !state,
        })
      }).then(() => {
        this.getArticle()
      })
    },
    getCategory(){
      axios({
        url:'http://127.0.0.1:9999/api/category/',
        method:'get',
      }).then((res) => {
        res.data.forEach((value) => {
          this.category_list.push(value.value)
        })
      })
    },
    getCategoryArticle(category) {
      this.$router.push({name:'ArticleList', query:{category: category}})
    },
    getTag(){
      axios({
        url:'http://127.0.0.1:9999/api/tag/',
        method:'get',
      }).then((res) => {
        res.data.forEach((value) => {
          this.tag_list.push(value.value)
        })
      })
    },
    getTagArticle(tag){
        this.$router.push({name:'ArticleList', query:{tag:tag}})
    },
    toArticleList(){
      this.$router.push({name:'ArticleList'})
    }
  },
}
</script>

<style scoped>
.box-card{
  margin-top: 10px;
}
#blog >>> .el-card__body {
    padding: 5px 10px;
}
#blog >>> .blog__category_btn {
  width: 100%;
  margin: 5px 0;
  padding: 8px 20px;
  font-size: 16px;
}
#blog >>> .el-button.is-round {
    border-radius: 20px;
    padding: 10px 23px;
}
.blog__all_article_btn{
  width: 100%;
  margin-top: 10px;
}
.article-icon{
  text-align: center;
}
#blog >>> .tag .el-card__body div{
  display: inline-block;
  margin: 3px;
}
#blog >>> .time .el-card__body div{
  display: inline-block;
  margin: 3px;
}
#blog >>> .el-divider--horizontal{
  margin: .5rem 0;
}
.iconfont{
  font-size: 1.5rem;
}
.comment p{
  line-height: 25px;
}
.reply{
  float: right;
  padding: 0 .3rem;
  font-size: .8rem;
  color: darkgray;
}
.reply:hover{
  color: #2496e2;
  background-color: #c7c7c7;
  border-radius: .4rem;
}
</style>