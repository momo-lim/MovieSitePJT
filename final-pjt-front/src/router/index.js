import Vue from 'vue'
import VueRouter from 'vue-router'
import Profile from '@/views/accounts/Profile'
import Community from '@/views/community/Community'
import Article from '@/views/community/Article'
import ArticleCreate from '@/views/community/ArticleCreate'
import ArticleUpdate from '@/views/community/ArticleUpdate'
import Home from '@/views/home/Home'
import ReviewIndex from '@/views/reviews/ReviewIndex'
import ReviewCreate from '@/views/reviews/ReviewCreate'
import ReviewDetail from '@/views/reviews/ReviewDetail'
import ReviewUpdate from '@/views/reviews/ReviewUpdate'

Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/profile/:username/',
    name: 'Profile',
    component: Profile,
  },  
  {
    path: '/community/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community/article/:articleNum',
    name: 'Article',
    component: Article,
    
  },
  {
    path:'/community/articlecreate',
    name:'ArticleCreate',
    component:ArticleCreate,
  },
  {
    path: '/community/articleupdate/:articleNum',
    name: 'ArticleUpdate',
    component: ArticleUpdate,
    props:true,
    
  },
  {
    path:'/home',
    name:'Home',
    component:Home
  },
  {
    path: '/reviews/index',
    name: 'ReviewIndex',
    component: ReviewIndex
  },
  {
    path: '/reviews/create',
    name: 'ReviewCreate',
    component: ReviewCreate
  },
  {
    path: '/reviews/detail/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/reviews/update/:reviewId',
    name: 'ReviewUpdate',
    component: ReviewUpdate
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
