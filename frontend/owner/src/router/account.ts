import { RouteRecordRaw } from 'vue-router';

export default (): RouteRecordRaw[] => [
  {
    path: '',
    redirect: { name: 'account/LoginUser' },
  },
  {
    path: 'login',
    name: 'account/LoginUser',
    component: () => import('pages/account/LoginUser.vue'),
  },
  {
    path: 'register',
    name: 'account/RegisterUser',
    component: () => import('pages/account/RegisterUser.vue'),
  },
  {
    path: 'forget-password',
    name: 'account/ForgotPassword',
    component: () => import('pages/account/ForgotPassword.vue'),
  },
  {
    path: 'reset-password',
    name: 'account/ResetPassword',
    component: () => import('pages/account/ResetPassword.vue'),
  },
];
