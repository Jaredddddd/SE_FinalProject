// import Vue from 'vue'
// import App from './App.vue'
// import router from './router'

// Vue.config.productionTip = false

// new Vue({
//   router,
//   render: function (h) { return h(App) }
// }).$mount('#app')

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import request from "@/utils/request"
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// 关闭生产模式下的提示
Vue.config.productionTip = false

// 设置axios为Vue的原型属性
Vue.prototype.$axios = request

Vue.use(ElementUI);

new Vue({
  router,
  render: function (h) { return h(App) }
}).$mount('#app')
