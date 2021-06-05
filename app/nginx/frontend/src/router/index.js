import Vue from 'vue'
import VueRouter from 'vue-router'
import NotFound from '@/views/NotFound.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/energy',
        name: 'Energy',
        component: () =>
            import ('../views/Energy.vue')
    },

    {
        path: '/cpu',
        name: 'Cpu',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ('../views/Cpu.vue')
    },

    {
        path: '*',
        name: 'NotFound',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: NotFound
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router