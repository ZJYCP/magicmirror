/***
 请求和响应拦截等相关配置
 */
import axios from 'axios'
import browser from '../assets/js/browser'


const config = {
    // headers: {'Content-Type': 'application/json'},
    timeout: 60000,
    withCredentials: false
}

if(process.env.NODE_ENV === 'development') {
    config.baseURL = "/api";
    // 开发环境
} else if(process.env.NODE_ENV === 'production') {
    // 生产环境
    config.baseURL = "https://evp.51job.com";   //这里是线上api请求地址
}

// 创建 axios 实例
let http = axios.create(config)

// 设置 post、put 默认 Content-Type
http.defaults.headers.post['Content-Type'] = 'multipart/form-data'
http.defaults.headers.put['Content-Type'] = 'application/json'

// 添加请求拦截器
http.interceptors.request.use(config => {
    if (config.method === 'post' || config.method === 'put') {
        // form-data 不处理
        // config.data = JSON.stringify(config.data)
    } else if (config.method === 'get' && browser.isIE) {
        // 给GET 请求后追加时间戳， 解决IE GET 请求缓存问题
        let symbol = config.url.indexOf('?') >= 0 ? '&' : '?'
        config.url += symbol + '_=' + Date.now()
    }
    // 请求发送前进行处理
    return config
}, error => {
    // 请求错误处理
    return Promise.reject(error)
})

// 添加响应拦截器
http.interceptors.response.use(response => {
    let { data } = response
    return data
}, error => {
    let info = {}
    let { status, statusText, data } = error.response
    if (!error.response) {
        info = {
            code: 5000,
            msg: 'Network Error'
        }
    } else {
        // 此处整理错误信息格式
        info = {
            code: status,
            data: data,
            msg: statusText
        }
    }
    return Promise.reject(info)
})

/**
 * 创建统一封装过的 axios 实例
 * @return {AxiosInstance}
 */
export default function () {
    return http
}
