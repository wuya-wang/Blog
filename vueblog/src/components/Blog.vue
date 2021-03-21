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
          <router-view v-wechat-title="$route.meta.title"></router-view>
      </el-col>
      <el-col :xs="24" :sm="24" :md="6" :lg="6" :xl="6" style="margin-top: 10px">
        <div style="background-color: #999897;height: 500px">
          <el-row class="article-icon">
            <el-col :span="8">
              <i  class="iconfont icon-dianzan" style="color: #2496e2"></i>
<!--              <i  class="iconfont icon-dianzan"></i>-->
              <span  style="margin-left: 5px"></span>
            </el-col>
            <el-col :span="8">
              <i  class="iconfont icon-shoucang" style="color: red;"></i>
<!--              <i class="iconfont icon-shoucang"></i>-->
              <span  style="margin-left: 5px"></span>
            </el-col>
            <el-col :span="8">
              <i  class="iconfont icon-dashang" style="color: #efb738"></i>
<!--              <i  class="iconfont icon-dashang"></i>-->
              <div><a id="link" target="_blank"></a></div>
            </el-col>
          </el-row>
        </div>
      </el-col>
    </el-row>
 </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Blog",
  data() {
    return {
      // articleList:'',
      category_list: [],
      tag_list: [],
      time_list:[
          '2021-3', '2021-2', '2021-1'
      ]
    }
  },
  created() {
    this.getTag()
    this.getCategory()
  },
  components:{
  },
  methods: {
    getCategoryAndTag(){
      axios({
        url:'http://127.0.0.1:9999/api/article-list/',
        method:'get',
      }).then(() => {
        // console.log(res.data)

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
</style>