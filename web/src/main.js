import Vue from 'vue'
import App from './App.vue'
import api from './api/index'
import echarts from 'echarts'
import './assets/js/rem'

Vue.config.productionTip = false
// import VueEcho from 'vue-echo'
// import 'pusher-js'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'

Vue.use(VueAwesomeSwiper, /* { default global options } */)


Vue.prototype.$echarts = echarts
Vue.prototype.$http = api
new Vue({
    render: h => h(App),
}).$mount('#app')
