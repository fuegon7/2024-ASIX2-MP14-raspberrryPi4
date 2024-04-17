import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/lara-dark-teal/theme.css';
import router from './router';
import mysql from 'mysql'
import dotenv from 'dotenv';

dotenv.config()

const app = createApp(App);
app.use(PrimeVue);
app.use(router);
app.mount('#app');