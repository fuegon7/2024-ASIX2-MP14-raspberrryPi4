import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/lara-dark-teal/theme.css';
import router from './router/routes';

const app = createApp(App);

app.use(PrimeVue, { ripple: true }, { inputStyle: "filled" });
app.use(router);
app.mount('#app');  


