<template>
  <div id="article">
    <div class="article__title">
<!--      <h4 v-text="article_title"></h4>-->
    </div>
    <div class="article__text" v-html="article_text"></div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Article",
  data(){
    return {
      'id': this.$route.query.id,
      'article_text':'',
      'article_title':'',
    }
  },
  created() {
    this.getArticle()
  },
  methods:{
    getArticle(){
      axios({
        url: 'http://127.0.0.1:9999/api/article/',
        method: 'get',
        params:{
          top_article_id: 1,
          id:this.id,
        }
      }).then((res) => {
        this.article_title = res.data.article_title
        this.article_text = res.data.article_text
      })
    },
  }
}
</script>

<style scoped>
.article__text >>> img {
  width: -moz-available;
  margin: 5px 0;
}
</style>