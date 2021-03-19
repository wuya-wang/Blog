<template>
  <div id="article-list">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
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

  },
  props:{
    getAllArticle,
  },
  methods:{
    getArticleList() {
      axios({
        url: 'http://127.0.0.1:9999/api/article-list/',
        method: 'get',
      }).then((res) => {
        console.log(res.data)
      })
    }
  },
}
</script>

<style scoped>

</style>