import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

import VueRouter from 'vue-router'
Vue.use(VueRouter);

import Login from './components/Login';
import Caso from './components/Caso';
import Index from './components/Index';
import AboutUs from './components/AboutUs';
import Configuracion from './components/Configuracion';
import Sesion from './components/Sesion';
import Participante from './components/Participante';
import Declaracion from './components/Declaracion';

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/login',
      component: Login
    },
    {
      path: '/caso',
      component: Caso
    },
    {
      path: '/',
      component: Index
    },

    { 
      path: '/aboutus',
      component: AboutUs
    },
    {
      path: '/configuracion',
      component: Configuracion
    },
    {
      path: '/sesion',
      component: Sesion
    },
    {
      path: '/participante',
      component: Participante
    },

    {
      path: '/declaracion',
      component: Declaracion
    }
  ]
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
