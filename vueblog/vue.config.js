// 设置了vue.config.js之后，就不会生成map文件
// map文件的作用在于项目打包后，代码都是经过压缩加密的，如果运行时报错，输出的错误信息无法准确得知是哪里的代码报错
// map文件相当于是查看源码的一个东西
// 如果不需要定位问题，并且不想被看到源码，就把productionSourceMap 置为false，既可以减少包大小，也可以加密源码
module.exports = {
    productionSourceMap : false
}
// 在vue.config.js文件中还有很多配置可以自由的配置
// 虽然create vue已经给我们提供了极简配置，但是想要自由定制，还是需要配合vue.config.js的配置