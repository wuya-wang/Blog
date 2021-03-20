<template>
  <div id="article-list">
    <div class="card">
      <div v-for="(article, index)  in article_list" :key="index" class="card-body">
        <h5 class="card-title" @click="getArticle(article.article_id)">{{ article.article_title }}</h5>
        <p class="card-text">{{ article.article_desc }}</p>
        <div>
          <p class="card-text" style="float: left">点赞</p>
          <div style="float: right">
            <i  class="iconfont icon-dianzan"></i>
            <i class="iconfont icon-shoucang"></i>
            <i  class="iconfont icon-dashang"></i>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ArticleList",
  data(){
    return {
      article_list: '',
    }
  },
  created() {
    this.getArticleList()
  },
  watch: {
  },
  methods:{
    getArticleList() {
      axios({
        url: 'http://127.0.0.1:9999/api/article-list/',
        method: 'get',
      }).then((res) => {
        this.article_list = res.data
      })
    },
    getArticle(id){
      console.log(id)
      this.$router.push({name:'Article',query:{'id':id}})
    }
  },
}
</script>

<style scoped>

</style>