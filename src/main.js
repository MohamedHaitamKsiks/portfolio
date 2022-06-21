import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueMobileDetection from 'vue-mobile-detection'


const app = createApp(App)

app.use(VueMobileDetection)
app.use(router)

app.mount('#app')
