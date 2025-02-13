import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from './views/LandingPage.vue';
import UserLogin from './views/UserLogin.vue';
import UserManagement from './views/UserManagement.vue';
import PageHeader from './components/PageHeader.vue';
import PageFooter from './components/PageFooter.vue';
import LoginForm from './components/LoginForm.vue';
import useToast from './toast.js';


const routes = [
  { path: '/', component: LandingPage },
  { path: '/login', component: UserLogin },
  { 
    path: '/admin', 
    component: UserManagement,
    beforeEnter: (to, from, next) => {
      const isAuthenticated = !!localStorage.getItem('access_token');
      if (!isAuthenticated) {
        next('/login');
      } else {
        next();
      }
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

const app = createApp(App);

app.component('PageHeader', PageHeader);
app.component('PageFooter', PageFooter);
app.component('LoginForm', LoginForm);

app.use(router);
useToast(app);

app.mount('#app');