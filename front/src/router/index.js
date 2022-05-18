import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/dates',
    name: 'Dates',
    component: () => import('@/pages/dates/DatesPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
