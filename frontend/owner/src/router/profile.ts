import { RouteRecordRaw } from 'vue-router';

export default (): RouteRecordRaw[] => [
  {
    path: '',
    redirect: { name: 'profile/UserProfile' },
  },
  {
    path: 'profile',
    name: 'profile/UserProfile',
    component: () => import('pages/profile/UserProfile.vue'),
  },
  {
    path: 'change-password',
    name: 'profile/ChangePassword',
    component: () => import('pages/profile/ChangePassword.vue'),
  },
];
