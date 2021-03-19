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
      }).then((res) => {
        console.log(res.data)
        this.article_title = res.data[0].article_title
        this.article_text = res.data[0].article_text
      })
    }
  }
}
</script>

<style scoped>
.article__text >>> img {
  width: -moz-available;
  margin: 5px 0;
}
</style>