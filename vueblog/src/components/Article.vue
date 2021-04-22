<template>
  <div id="article">

    <div class="article__title">
<!--      <h4 v-text="article_title"></h4>-->
    </div>
    <div class="article__text" v-html="article_text"></div>
  </div>
</template>

<script>
// import axios from "axios";

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
  mounted() {
  },
  watch: {
  },
  methods:{
    getArticle(){
      this.$axios.get("http://127.0.0.1:9999/api/blog/v1/article/", {
        params: {
          id: this.$route.query.id
        }
      // })
      // axios({
      //   url: 'http://127.0.0.1:9999/api/blog/v1/article/',
      //   method: 'get',
      //   params:{
      //     id: this.$route.query.id,
      //     token: this.$store.getters.userLoginStatus,
      //   },
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
  margin: 5px;
  max-width: 400px;
}
#article{
  border: #C0C4CC .1rem solid;
  border-radius: .2rem;
  padding: .4rem;
  background-color: #C0C4CC40;
}
</style>