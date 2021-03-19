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
              {{ category + index }}
            </div>
          </el-card>
          <el-card class="box-card tag" shadow="never">
            <div slot="header" class="clearfix">
              <span>标签</span>
            </div>
            <div v-for="(tag, index) in tag_list" :key="index">
              <el-button type="primary" round>{{tag + index }}</el-button>
            </div>
          </el-card>
          <el-card class="box-card" shadow="never">
            <div slot="header" class="clearfix">
              <span>时间</span>
            </div>
            <div v-for="o in 4" :key="o" class="text item">
              {{'列表内容 ' + o }}
            </div>
          </el-card>
          <el-button type="primary" round @click="getAllArticle()">全部文章</el-button>
          <ArticleList :get-all-article="getAllArticle"></ArticleList>
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
import ArticleList from "@/components/ArticleList";
export default {
  name: "Blog",
  data() {
    return {
      category_list: [
        '前端', '后端', 'Python', 'Java'
      ],
      tag_list: [
        '数据库', 'Vue', 'Django', '网络协议',
      ],

    }
  },
  created() {
    this.getCategoryAndTag()
  },
  components:{
    ArticleList,
  },
  methods: {
    getCategoryAndTag(){
      axios({
        url:'http://127.0.0.1:9999/api/article-list/',
        method:'get',
      }).then((res) => {
        console.log(res.data)
      })
    },
    getAllArticle(){
      axios({
        url:'http://127.0.0.1:9999/api/article-list/',
        method:'get',
        params: {
          category: 'all'
        },
      }).then((res) => {
        console.log(res.data)
      })
    }
  },
}
</script>

<style scoped>
.box-card{
  margin-top: 10px;
}
.article-icon{
  text-align: center;
}
#blog >>> .tag .el-card__body div{
  display: inline-block;
  margin: 3px;
}

</style>