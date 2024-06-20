import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main.vue'
import Purchase from '../views/purchase.vue'
import Client from '../views/Client.vue'
import Commodity from '../views/Commodity.vue'
import Login from '../views/login.vue'
import Sale from '../views/sale.vue'
import Staff from '../views/staff.vue'

Vue.use(VueRouter)
//添加组件（跳转页面）
const routes = [
  {
    path: '/', 
    component: Login,
  },

  {
    path: '/main', 
    component: Main,
    children:[
      //子路由
      { path: '/purchase', component: Purchase},
      { path: '/staff', component: Staff},
      { path: '/client', component: Client},
      { path: '/commodity', component: Commodity},
      { path: '/sale', component: Sale}
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
