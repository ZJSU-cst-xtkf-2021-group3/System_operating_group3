import VueRouter from "vue-router"
import Vue from 'vue'
import Home from '../components/Home'
import Signin from "../components/Signin";
import Recommend from "../components/Home/Recommend";
import Attention from "../components/Home/Attention";
import AttentionTopic from "../components/Home/Attention/AttentionTopic";
import AttentionPeople from "../components/Home/Attention/AttentionPeople";

Vue.use(VueRouter)

export default new VueRouter({
    routes:[
        {
            path:'/',
            name:'Home',
            component:Home,
            children:[
                {
                    path:'/',
                    component:Recommend
                },
                {
                    path:'/attention',
                    component:Attention,
                    children:[
                        {
                            path:'/attention/topic',
                            component:AttentionTopic
                        },
                        {
                            path:'/attention/people',
                            component:AttentionPeople
                        },
                    ]

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