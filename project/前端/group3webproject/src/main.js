import Vue from 'vue'
import App from './App.vue'
import VueCookie from 'vue-cookie'
import Element from 'element-ui'
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from "vue-axios";
import router from  './router'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false
Vue.use(VueCookie)
Vue.use(VueRouter)
Vue.use(Element)
Vue.use(VueAxios,axios)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
