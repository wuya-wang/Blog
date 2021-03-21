<template>
  <div id="article-list">
    <div class="card" v-for="(article, index)  in article_list" :key="index">
      <div  class="card-body">
        <h5 class="card-title" @click="getArticle(article.article_id)">{{ article.article_title }}</h5>
        <p class="card-text">{{ article.article_desc }}</p>
        <div>
          <p class="card-text text-black-50" style="float: left">{{ article.article_time }}</p>
          <div style="float: right">
            <i  class="iconfont icon-dianzan" @click="toLikes(article.article_id)"></i>
            <i class="iconfont icon-shoucang" @click="toCollections(article.article_id)"></i>
            <i  class="iconfont icon-dashang" @click="toComments(article.article_id)"></i>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";

export default {
  name: "ArticleList",
  data(){
    return {
      article_list: '',
      category: this.$route.query.category,
      tag: this.$route.query.tag,
      // 点赞收藏评论状态
      state: {
        like: false,
        collection: false,
        reward: false
      },
    }
  },
  created() {
    this.getArticleList()
    this.operatingStatus()
  },
  watch: {
    // 监听路由变化
    $route(){
      this.category = this.$route.query.category
      this.tag = this.$route.query.tag
      this.getArticleList()
    }
  },
  methods:{
    getArticleList() {
      axios({
        url: 'http://127.0.0.1:9999/api/article-list/',
        method: 'get',
        params:{
          'category':this.category,
          'tag': this.tag,
        }
      }).then((res) => {
        this.article_list = res.data
      })
    },
    getArticle(id){
      // console.log(id)
      this.$router.push({name:'Article',query:{'id':id}})
    },
    // 用户对文章的点收评状态
    operatingStatus(){
      axios({
        url:'http://127.0.0.1:9999/api/operatingstatus/',
        method:'post',
        data:Qs.stringify({
          token: this.$store.getters.userLoginStatus,
        })
      }).then((res) => {
        console.log(res.data)
      })
    },
    toLikes(id){
      axios({
        url:'http://127.0.0.1:9999/api/like/',
        method:'post',
        data:Qs.stringify({
          article_id: id,
          token: this.$store.getters.userLoginStatus,
          state: !this.state.like,
        })
      }).then((res) => {
        console.log(res.data)
      })
    },
    toCollections(){},
    toComments(){},
  },
}
</script>

<style scoped>
.card{
  margin-bottom: 10px;
  cursor: pointer;
}
.card-body{
  padding: 0.5rem 0.5rem 0 0.5rem;
}
.card-title{
  margin-bottom: 0.3rem;

}
.card-title:hover{
  color: #3069e0;
}
.iconfont{
  font-size: 1.3rem;
}
</style>