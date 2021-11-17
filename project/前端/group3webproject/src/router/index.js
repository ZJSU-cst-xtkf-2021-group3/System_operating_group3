import VueRouter from "vue-router"
import Vue from 'vue'
import Home from '../components/Home'
import Signin from "../components/Signin";
import Recommend from "../components/Recommend";
import Attention from "../components/Attention";

Vue.use(VueRouter)

export default new VueRouter({
    routes:[
        {
            path:'/',
            name:'Home',
            component:Home,
            children:[
                {
                    path:'recommend',
                    component:Recommend
                },
                {
                    path:'attention',
                    component:Attention
                },
            ]
        },
        {
            path:'/signin',
            name:'Signin',
            component:Signin
        }
    ]
})