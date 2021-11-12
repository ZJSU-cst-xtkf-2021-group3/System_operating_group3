import VueRouter from "vue-router"
import Vue from 'vue'
import HelloWorld from '../components/HelloWorld'
import Signin from "../components/Signin";

Vue.use(VueRouter)

export default new VueRouter({
    routes:[
        {
            path:'/',
            name:'HelloWorld',
            component:HelloWorld
        },
        {
            path:'/signin',
            name:'Signin',
            component:Signin
        }
    ]
})