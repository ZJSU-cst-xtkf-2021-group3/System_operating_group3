import VueRouter from "vue-router"
import Vue from 'vue'
import Home from '../components/Home'
import Signin from "../components/Signin";

Vue.use(VueRouter)

export default new VueRouter({
    routes:[
        {
            path:'/',
            name:'Home',
            component:Home
        },
        {
            path:'/signin',
            name:'Signin',
            component:Signin
        }
    ]
})