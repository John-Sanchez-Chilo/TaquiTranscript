<template>
  <v-app light>
    <v-main class="">
    <v-content>
      <section>
        <v-parallax src="https://i.blogs.es/8ad7c5/notebook_work_girl_computer_woman_operator_design_business-1407325/1366_2000.jpg" height="700">
          <v-layout column align-center justify-center class="white--text">
            <h1 class="white--text mb-2 display-1 text-xs-center" style="font-weight: 900; text-shadow: 3px 2px #000000">La herramienta de trabajo para taquigrafos judiciales</h1>
            <div class="white--text subheading mb-3 text-xs-center" style="font-weight: 900; text-shadow: 2px 2px #000000">Deja que Taquitranscript se encargue de todo y relajate</div>
            <v-btn class="blue lighten-2 mt-5" dark large link @click="$router.push({ path: '/login' })">
              Empieza ahora
            </v-btn>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-layout
          column
          wrap
          class="my-5"
          align-center
        >
          <v-flex xs12 sm4 class="my-3">
            <div class="text-xs-center">
              <h2 class="headline">La mejor manera de almacenar tus transcripciones</h2>
              <span class="subheading">
                No mas restricciones, no mas limites
              </span>
            </div>
          </v-flex>
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">public</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">Entorno amigable</div>
                    </v-card-title>
                    <v-card-text>
                      Nuestro software esta destinado a los taquigrafos judiciales, y esta pensado y creado con una interfaz sencilla y amigable facilitando su uso. De esta forma, los nuevos usuarios pueden aprender rapidamente su fucionamiento
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline">Transcripciones precisas</div>
                    </v-card-title>
                    <v-card-text>
                      Nuestro software hace uso del servicio de Amazon (AWS) el cual se encarga de hacer las transcripciones mas precisas a  partir de los audios que recibe. De esta manera no tendras que pasar largas horas escuchando y escribiendo tus audios
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">share</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">Almacenamiento eficaz</div>
                    </v-card-title>
                    <v-card-text>
                      Gracias a nuestra interfaz amigable, se puede acceder a los diferentes transcripciones almacenadas, ingresando a estas a traves de filtros de acceso rapido y divisiones a travès de casos, sesiones, participantes y declaraciones. 
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </section>
    </v-content>
  </v-main>
</v-app>
</template>



  
  
  <script>
  import axios from 'axios'
    export default {
      data () {
        return {
          tasks: [],
          postURL: 'https://backendsecosystem.herokuapp.com',
          config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          },
        }
      },
      methods:{
        setmeet(){
          window.location.href = "https://meet.google.com/ydt-sxvb-uwg";
        }
      },
      created(){ 
          axios.post(this.postURL + '/actividad/get_actividades')
              .then(res => { this.tasks = res.data; })
              .catch((error) => { console.log(error) })
      },
    }
  </script>
