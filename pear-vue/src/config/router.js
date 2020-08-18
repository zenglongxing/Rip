import {UserLayout,PearLayout} from '@comp/layouts'

export const constantRouterMap = [
    {
        path: '/user',
        component: UserLayout,
        redirect: '/user/login',
        hidden: true,
        children: [
            {
                path: 'login',
                name: 'login',
                component: () => import(/* webpackChunkName: "user" */ '@/views/user/Login')
            },
            {
                path: 'register',
                name: 'register',
                component: () => import(/* webpackChunkName: "user" */ '@/views/user/Register')
            },
            {
                path: 'register-result',
                name: 'registerResult',
                component: () => import(/* webpackChunkName: "user" */ '@/views/user/RegisterResult')
            },
            {
                path: 'alteration',
                name: 'alteration',
                component: () => import(/* webpackChunkName: "user" */ '@/views/user/Alteration')
            },
        ]
    },
    {
        path: '/',
        component: PearLayout,
        hidden: true,
        meta: {title: '热门女星'},
        redirect: '/star',
        children: [
            {
                path: '/movie/:starId',
                name: 'movie',
                component: () => import(/* webpackChunkName: "user" */ '@/views/movie/movieList')
            },
            {
                path: '/star',
                name: 'star',
                component: () => import(/* webpackChunkName: "user" */ '@/views/star/starList')
            },
            {
                path: '/video/:movieId',
                name: 'video',
                component: () => import(/* webpackChunkName: "user" */ '@/views/video/videoDetail')
            },
            {
                path: '/source',
                name: 'source',
                component: () => import(/* webpackChunkName: "user" */ '@/views/community/sourceList')
            }
        ]
    },
    {
        path: '/404',
        component: () => import(/* webpackChunkName: "fail" */ '@/views/exception/404')
    }
];
