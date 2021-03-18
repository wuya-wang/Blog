<template>
  <div id="add-article">
    <el-row :gutter="10">
      <el-col :xs="24" :sm="24" :md="24" :lg="5" :xl="5">
        <div class="add-article__input">
          <el-input
              placeholder="请输入内容"
              v-model="article.title"
              clearable>
          </el-input>
          <el-input
              type="textarea"
              :rows="2"
              placeholder="请输入内容"
              v-model="article.introduce">
          </el-input>
          <el-cascader
              v-model="category"
              :options="options"
              @change="handleChange">
          </el-cascader>
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
              v-model="value"
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
      value:'',
      handbook: "",
      article:{
        title:'',
        introduce:'',
      },
      category:[],
      options:[
        {
          value: '指南',
          label: '指南',
        }
      ],
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
      if (this.value.length === 0){
        this.$message({
          showClose: true,
          message: '内容不能为空',
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
        })
      }).then((res) => {
        if (res.data === 'OK'){
          this.value = ''
          this.$message({
            showClose: true,
            message: '保存成功',
            type: 'success',
            center: true,
          });
          return;
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
    handleChange(value) {
      console.log(value);
    },
  }
}
</script>

<style scoped>
#add-article >>> .markdown-body{
  min-height: calc(100vh - 111px) ;
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
</style>