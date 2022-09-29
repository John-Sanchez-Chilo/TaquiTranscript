<template>
  <v-app>
    
    <v-app-bar app>
      <v-row
        align="center"
        justify="space-around"
        class="text-h4 font-weight-bold"
      >
      <img
        class="my-1"
        height = "60"
        width = "200"
        src="@/img/logo3.png"
        alt="secosystem"
        link @click="$router.push({ path: '/' })"
      >
      &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj;
        <v-btn
          elevation="2"
          link @click="$router.push({ path: '/login' })"
        >
        Ingresa aquí
        </v-btn>

        <v-btn
          right
          x-small
          height=28
          link @click="$router.push({ path: '/aboutus' })"
          >
            Sobre nosotros
        </v-btn>

      </v-row>
      
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import Index from './components/Index';
import Login from './components/Login';
import Configuracion from './components/Configuracion';
import Caso from './components/Caso';
import Sesion from './components/Sesion';
import Participante from './components/Participante';
import Declaracion from './components/Declaracion';
import AboutUs from './components/AboutUs';

export default {
  name: 'App',
  
  Components: {
    Index,
    Login,
    Configuracion,
    Caso,
    Sesion,
    Participante,
    Declaracion,
    AboutUs
  },
};
</script>
