import { createRouter, createWebHistory } from 'vue-router';
import Inicio from '../views/Inicio.vue';
import Grafiques from '../views/GraphViews.vue';

const routes = [
  { path: '/',  component: Inicio },
  { path: '/graphics', component: Grafiques,},
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;