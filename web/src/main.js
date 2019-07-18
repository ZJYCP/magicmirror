import Vue from 'vue'
import App from './App.vue'
import api from './api/index'
import echarts from 'echarts'
import './assets/js/rem'
Vue.config.productionTip = false

Vue.prototype.$echarts = echarts
Vue.prototype.$http = api
new Vue({
  render: h => h(App),
}).$mount('#app')
