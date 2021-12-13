
// #ifndef VUE3
import Vue from 'vue'
import App from './App'
import uView from "./uview-ui";
import tmVuetify from "./tm-vuetify"

Vue.config.productionTip = false
Vue.use(uView)
Vue.use(tmVuetify)

App.mpType = 'app'

const app = new Vue({
    ...App
})
app.$mount()
// #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
import App from './App.vue'
export function createApp() {
  const app = createSSRApp(App)
  return {
    app
  }
}
// #endif