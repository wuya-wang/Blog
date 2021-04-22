<template>
  <div id="article-list">
    <div class="card" v-for="(article, index)  in article_list" :key="index">
      <div  class="card-body">
        <h5 class="card-title" @click="getArticle(article.article_id)">{{ article.article_title }}</h5>
        <p class="card-text">{{ article.article_desc }}</p>
        <div>
          <p class="card-text text-black-50" style="float: left">{{ article.article_time }}</p>
          <div style="float: right">
            <i v-if="article.likes" class="iconfont icon-dianzan" @click="toLikes(article.article_id, article.likes)" style="color: #2496e2"></i>
            <i v-else class="iconfont icon-dianzan" @click="toLikes(article.article_id)"></i>
            <span class="text-black-50">{{ article.all_likes }}</span>

            <i v-if="article.collections" class="iconfont icon-shoucang" @click="toCollections(article.article_id, article.collections)" style="color: #ee0d5e"></i>
            <i v-else class="iconfont icon-shoucang" @click="toCollections(article.article_id)"></i>
            <span class="text-black-50">{{ article.all_collections }}</span>

            <i v-if="article.comments"  class="iconfont icon-liuyanpinglun" style="color: #ffbb03"></i>
            <i v-else class="iconfont icon-liuyanpinglun"></i>
            <span class="text-black-50">{{ article.all_comments }}</span>
          </div>
        </div>

      </div>
    </div>
    <el-pagination
    layout="prev, pager, next"
    hide-on-single-page
    :page-size="PageSize"
    :current-page="CurrentPage"
    :total="Total"
    @current-change=currentChange>
  </el-pagination>
  </div>
</template>

<script>
import Qs from "qs";
// import Vue from "vue"
export default {
  name: "ArticleList",
  data(){
    return {
      article_list: [],
      category: this.$route.query.category,
      tag: this.$route.query.tag,
      PageSize: 7,  // 每页数量
      CurrentPage: 1,  // 默认页
      Total: 100,
    }
  },
  created() {
    this.getArticleList(this.CurrentPage)
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
    getArticleList(page) {
      this.$axios({
        url: 'http://127.0.0.1:9999/api/blog/v1/article-list/',
        method: 'get',
        params: {
          page,
          category: this.category,
          tag: this.tag,
        }
      }).then((res) => {
        // console.log(res.data)
        this.article_list = res.data.results
        this.Total = res.data.count
      })
    },
    currentChange(val){
      // console.log(val)
      this.CurrentPage = val
      this.getArticleList(val)
    },
    getArticle(id){
      // console.log(id)
      this.$router.push({name:'Article',query:{'id':id}})
    },
    toLikes(id, state){
      if (this.$store.getters.userLoginStatus){
      this.$axios({
        url:'http://127.0.0.1:9999/api/blog/v1/like/',
        method:'post',
        data:Qs.stringify({
          article_id: id,
          state: !state,
        })
      }).then(() => {
        this.getArticleList(this.CurrentPage)
        // Vue.set(this.article_list, index, {likes:!state})
      })
      }else{
        this.$message({
          showClose: true,
          message: '请先登录',
          type: 'error',
          center: true,
        })
      }
    },
    toCollections(id, state){
      if (this.$store.getters.userLoginStatus){
        this.$axios({
        url:'http://127.0.0.1:9999/api/blog/v1/collection/',
        method:'post',
        data:Qs.stringify({
          article_id: id,
          state: !state,
        })
      }).then(() => {
        this.getArticleList(this.CurrentPage)
        // Vue.set(this.article_list, index, {likes:!state})
      })
      } else {
        this.$message({
          showClose: true,
          message: '请先登录',
          type: 'error',
          center: true,
        })
      }
    },
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
.card .iconfont{
  font-size: 1.3rem;
  margin: 0 .1rem 0 .5rem;
}
#article-list >>> .el-icon {
  position: static;
  color: #000000;
}
</style>