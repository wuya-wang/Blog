<template>
  <div id="captcha" class="nc-container">
    <div>{{ callbackData }}</div>
  </div>
</template>

<script type="text/javascript" charset="utf-8" src="//g.alicdn.com/sd/ncpc/nc.js?t=2015052012"></script>

<script>
export default {
  name: "Captcha",
  data() {
    return {
      nc:'', // noCaptcha实例的值
    }
  },
  props: ['callbackData'],
  mounted() {
    // 初始化方法
    this.init()
  },
  methods: {
    init() {
      const self = this
      // 生成的随机token
      const nc_token = [
        'FFFF0N00000000009E4C', // appkey(自己填写)
        new Date().getTime(),
        Math.random()
      ].join(':')
      // 参数
      const NC_Opt = {
        // id的值
        renderTo: '#captcha',// 声明滑动验证需要渲染的目标元素ID
        appkey: 'FFFF0N00000000009E4C', // appkey(自己填写)
        scene: 'nc_register', // 场景值(当前pc登陆) 滑动验证码的主键，请勿将该字段定义为固定值。确保每个用户每次打开页面时，其token值都是不同的。系统默认的格式为：”您的appkey”+”时间戳”+”随机数”。
        token: nc_token, // token
        customWidth: '100%', // 滑动条的宽度
        trans: { key1: 'code0' }, // //业务键字段，可为空。为便于线上问题的排查，建议您按照线上问题定位文档中推荐的方法配置该字段值。
        elementID: ['usernameID'],
        is_Opt: 0,
        language: 'cn', // 中文
        isEnabled: true,// 是否启用。一般情况，保持默认值（true）即可
        timeout: 3000,// 内部网络请求的超时时间。一般情况建议保持默认值（3000ms）。
        times: 5,// 允许服务器超时重复次数，默认5次。超过重复次数后将触发报错。
        callback: function(data) {
          // 前端滑动验证通过时会触发该回调参数。您可以在该回调参数中将请求标识（token）、会话ID（sessionid）、签名串（sig）字段记录下来，随业务请求一同发送至您的服务端调用验签。
          // 在这里可以拿到返回的数据
          const param = {
            token: nc_token,
            sessionId: data.csessionid,
            sig: data.sig,
            scene: 'nc_register'
          }
          // 传给父组件  这里我是封装的组件 把值传出去了 然后请求接口
          self.$emit('handleSlideAly', param)
        }
      }
      this.nc = new noCaptcha(NC_Opt)
      // 用于自定义文案。详细配置方法请参见自定义文案与多语言文档。
      this.nc.upLang('cn', {
        _startTEXT: '请按住滑块，拖动到最右边',
        _yesTEXT: '验证通过',
        _error300:
          '哎呀，出错了，点击<a href="javascript:__nc.reset()">刷新</a>再来一次',
        _errorNetwork:
          '网络不给力，请<a href="javascript:__nc.reset()">点击刷新</a>'
      })
    },
    // 重置方法  api

    reset(){
      console.log(this.data)
      this.nc.reload()
    }
  }
}
</script>

<style  scoped>
    .nc_scale {
      background: #e8e8e8 !important;
      /* 默认背景色 */
    }

    .nc_scale div.nc_bg {
      background: #7ac23c !important;
      /* 滑过时的背景色 */
    }

    .nc_scale .scale_text2 {
      color: #fff !important;
      /* 滑过时的字体颜色 */
    }

    .nc_scale span {
      border: 1px solid #ccc !important;
    }

    .errloading {
      border: #faf1d5 1px solid !important;
      color: #ef9f06 !important;
    }
    #captcha >>> #nc_1_n1z {
      height: 34px;
    }
</style>