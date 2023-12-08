import { createRouter, createWebHistory } from 'vue-router';
import One from './components/One';
import Two from './components/Two';
import Login from './components/Login';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      name: 'One',
      path: '/one',
      component: One
    },
    {
      name: 'Two',
      path: '/two',
      component: Two
    },
    {
      name: 'Login',
      path: '/login',
      component: Login
    },
  ],
});

export default router;