<template>
  <div id="add-article">
    <el-row :gutter=10 style="margin: 0">
      <el-col :xs="24" :sm="24" :md="24" :lg="5" :xl="5">
        <div class="add-article__input">
          <div>
            <div class="add-article__header">标题</div>
            <el-input
                placeholder="请输入内容"
                v-model="article.title"
                clearable>
            </el-input>
          </div>
          <el-divider content-position="right">我是分割线</el-divider>
          <div>
            <div class="add-article__header">简介</div>
            <el-input
                type="textarea"
                :rows="2"
                placeholder="请输入内容"
                v-model="article.introduce">
            </el-input>
          </div>
          <el-divider></el-divider>
          <div>
            <div class="add-article__header">分类</div>
            <el-select v-model="category_value" placeholder="请选择">
              <el-option
                  v-for="item in category"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
              </el-option>
            </el-select>
            <div>
              <el-input
                  style="display: inline-block; width: calc(100% - 75px)"
                  placeholder="新建分类"
                  v-model="add_category_value"
                  clearable>
              </el-input>
              <el-button style="margin-left: 5px;" @click="addCategory()">确定</el-button>
            </div>
          </div>
          <el-divider></el-divider>
          <div>
            <div class="add-article__header">标签</div>
            <el-select v-model='tag_value' multiple placeholder="请选择">
              <el-option
                  v-for="item in tag"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
              </el-option>
            </el-select>
            <div>
              <el-input
                  style="display: inline-block; width: calc(100% - 75px)"
                  placeholder="新建标签"
                  v-model="add_tag_value"
                  clearable>
              </el-input>
              <el-button style="margin-left: 5px;" @click="addTag()">确定</el-button>
            </div>
          </div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="19" :xl="19">
        <div class="mavonEditor">
          <mavon-editor
              ref=md
              :toolbars="markdownOption"
              :ishljs = "true"
              :boxShadow="false"
              @save="saveArticle"
              @imgAdd="$imgAdd"
              v-model="article_value"
          />
    </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
name: "AddArticle",
   data() {
    return {
      article_value:'',
      handbook: "",
      article:{
        title:'',
        introduce:'',
      },
      category:[
        {
          value: '数据指南',
          label: '指南',
        },
      ],
      category_value:'',
      add_category_value:'',
      tag:[
        {
          value: '数据Python',
          label: 'Python',
        }
      ],
      tag_value: '',
      add_tag_value: "",
      img_list: {},
      markdownOption: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        strikethrough: true, // 中划线
        mark: true, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        imagelink: true, // 图片链接
        code: true, // code
        table: true, // 表格
        fullscreen: true, // 全屏编辑
        readmodel: true, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        help: true, // 帮助
        /* 1.3.5 */
        undo: true, // 上一步
        redo: true, // 下一步
        trash: true, // 清空
        save: true, // 保存（触发events中的save事件）
        /* 1.4.2 */
        navigation: true, // 导航目录
        /* 2.1.8 */
        alignleft: true, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        /* 2.2.1 */
        subfield: true, // 单双栏模式
        preview: true, // 预览
      },
    }
  },
  created() {
    this.getCategory()
    this.getTag()
  },
  methods:{
    // 保存文章
    saveArticle(value, render){
      if (this.article.title.length === 0){
        this.$message({
          showClose: true,
          message: '标题不能为空',
          type: 'warning',
          center: true,
        });
        return
      }
      if (this.article.introduce.length === 0){
        this.$message({
          showClose: true,
          message: '简介不能为空',
          type: 'warning',
          center: true,
        });
        return
      }
      if (this.article_value.length === 0){
        this.$message({
          showClose: true,
          message: '内容不能为空',
          type: 'warning',
          center: true,
        });
        return
      }
      if (this.$store.state.userinfo.username !== 'wuya'){
        this.$message({
          showClose: true,
          message: '无权限',
          type: 'warning',
          center: true,
        });
        return
      }
      axios({
        url: 'http://127.0.0.1:9999/api/add-article/',
        method: 'post',
        data:Qs.stringify({
          token: this.$store.getters.userLoginStatus,
          article_text: render,
          article_title: this.article.title,
          article_introduce: this.article.introduce,
          article_category: this.category_value,
          article_tag: JSON.stringify(this.tag_value),
        })
      }).then((res) => {
        if (res.data === 'OK'){
          this.$message({
            showClose: true,
            message: '保存成功',
            type: 'success',
            center: true,
          });
          this.article_value = ''
          this.article.title = ''
          this.article.introduce = ''
          this.category_value = ''
          this.tag_value = ''
        }
      })
    },

    // 图片上传
    $imgAdd(pos, file){
      axios({
        url: 'http://127.0.0.1:9999/api/add-article/',
        method: 'post',
        data:Qs.stringify({
          img: JSON.stringify({
            url:file['miniurl'],
            name:file['name']
          })
        })
      }).then((url) => {
        // console.log(url.data)
        this.$refs.md.$img2Url(pos, url.data)
      })
    },
    getCategory(){
      axios({
        url:'http://127.0.0.1:9999/api/category/',
        method:'get',
      }).then((res) => {
        this.category = res.data
      })
    },
    addCategory(){
      if (this.add_category_value.length === 0) {
        this.$message({
          showClose: true,
          message: '新增分类不能为空',
          type: 'warning',
          center: true,
        });
        return
      }
      axios({
        url:'http://127.0.0.1:9999/api/category/',
        method:'post',
        data:Qs.stringify({
          "new_category": this.add_category_value
        })
      }).then(() => {
        this.$message({
          showClose: true,
          message: '新增分类成功',
          type: 'success',
          center: true,
        });
        this.add_category_value = ''
        this.getCategory()
      })
    },
    getTag(){
      axios({
        url:'http://127.0.0.1:9999/api/tag/',
        method:'get',
      }).then((res) => {
        this.tag = res.data
      })
    },
    addTag(){
      if (this.add_tag_value.length === 0) {
        this.$message({
          showClose: true,
          message: '新增标签不能为空',
          type: 'warning',
          center: true,
        });
        return
      }
      axios({
        url:'http://127.0.0.1:9999/api/tag/',
        method:'post',
        data:Qs.stringify({
          "new_tag": this.add_tag_value
        })
      }).then(() => {
        this.$message({
          showClose: true,
          message: '新增标签成功',
          type: 'success',
          center: true,
        });
        this.add_tag_value = ''
        this.getTag()
      })
    },
  }
}
</script>

<style scoped>
#add-article >>> .markdown-body{
  min-height: calc(100vh - 112px) ;
}
#add-article >>> .markdown-body img {
    max-width: 50%;
    box-sizing: content-box;
    background-color: #fff;
}
#add-article >>> .fa-mavon-floppy-o::before {
    color: #f33900;
}
.add-article__input{
  margin-top: 10px;
}
.add-article__header{
  margin: 3px 0;
  font-size: 18px;
}
#add-article >>> .el-divider--horizontal {
    display: block;
    height: 1px;
    width: 100%;
    margin: 15px 0;
}
#add-article >>> .el-select {
  margin-bottom: 5px;
    width: 100%;
}
</style>