// axios拦截器
import axios from "axios";
const request = axios.create({
    headers: {'content-type': 'application/x-www-form-urlencoded'}
})
request.interceptors.request.use(
    config => {
        const token =localStorage.getItem('token')
        if (token){
             // DRF认证 token格式为Token 2a1sdwadadwdff
             config.headers.authorization = 'Token ' + token
        }
        return config
    },
    err => {
    return Promise.reject(err)
    }
)
export default request
