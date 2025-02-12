import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from './views/LandingPage.vue';
import UserLogin from './views/UserLogin.vue';
import UserRegister from './views/UserRegister.vue';
import UserManagement from './views/UserManagement.vue';

const routes = [
  { path: '/', component: LandingPage },
  { path: '/login', component: UserLogin },
  { path: '/register', component: UserRegister },
  { path: '/users', component: UserManagement }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

const app = createApp(App);
app.use(router);
app.mount('#app');