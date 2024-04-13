import useAccountRoutes from './account';
import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', name: 'Home', component: () => import('pages/HomePage.vue') }],
  },
  {
    path: '/account/',
    component: () => import('layouts/AccountLayout.vue'),
    children: useAccountRoutes(),
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
