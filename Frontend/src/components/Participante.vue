<template>
  <v-app>
    <v-main class="light-blue darken-4">
    <v-container fill-height>
      <v-row
        align ="center"
        justify="center"
        no-gutters
      >
        <v-dialog
            max-width="700px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="white"
              v-bind="attrs"
              v-on="on"
            >
              Agregar Nueva declaracion
            </v-btn>
            &zwnj; &zwnj;
          </template>
          <v-card>
            <br>
            <v-card-title>
              <span class="text-h5 mx-auto">Nueva Declaracion</span>
            </v-card-title>
            <v-card-text class="text-h6 text-center">

              <v-text-field
                class="mx-10"
                v-model='newTask.titulo'
                :rules="nameRules"
                label="Titulo"
                required
              ></v-text-field>

              <v-text-field
                class="mx-10"
                v-model='newTask.tipo'
                :rules="nameRules"
                label="Tipo"
                required
              ></v-text-field>

              <v-file-input
                counter
                truncate-length="17"
                class="mx-10"
                v-model='newTask.audio'
                :rules="nameRules"
                label="Audio"
                required
              ></v-file-input>

            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="success"
                class="mr-4"
                @click="addTask"
              >
                AGREGAR
              </v-btn>
            </v-card-actions>
            <br>
          </v-card>
        </v-dialog>
        <v-btn
          color="white"
          v-bind="attrs"
          v-on="on"
          link @click="$router.push({ path: '/admin' })"
        >
          Volver a actividades
        </v-btn>
      </v-row>
  
      <v-card
        class="mx-auto"
        width="1000"
      >
        <v-card-text>
          <p class="text-h4 text--primary">
            Titulo
          </p>
          <p>Tipo de declaracion</p>
          <div class="text--primary">
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.".
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
          </div>
        </v-card-text>
      </v-card>

      <v-card
        class="mx-auto"
        width="1000"
      >
        <v-card-text>
          <p class="text-h4 text--primary">
            Titulo
          </p>
          <p>Tipo de declaracion</p>
          <div class="text--primary">
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.".
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
            relating to or dependent on charity; charitable.
            "an eleemosynary educational institution.". 
          </div>
        </v-card-text>
      </v-card>
      <v-row v-for="task in tasks" :key="task">
        <v-card
        class="mx-auto"
        width="1000"
      >
        <v-card-text>
          <p class="text-h4 text--primary">
            task.titulo
          </p>
          <p>task.tipo</p>
          <div class="text--primary">
            task.declaracion
          </div>
        </v-card-text>
      </v-card>
      </v-row>
    </v-container>
    </v-main>
  </v-app>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default{    
      data(){ 
          return { 
              tasks: [],
              newTask: {},
              postURL: 'https://backend-taquitranscript.herokuapp.com',
              config_request: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*'
              }       
          }
      },
      methods:{
          addTask(){ 
              axios.post(this.postURL + '/declaracion/add_declaracion', this.newTask, this.config_request)
                  .then(res => {                                         
                      this.tasks.push(res.data);
                      console.log(res.data)        ;
                  })
                  .catch((error) => {
                      console.log(error)
                  });
  
              this.newTask = {};
          },
  
          deleteTask(task){                      
              axios.post(this.postURL + '/declaracion/delete_declaracion', {id_declaracion: task.id_declaracion}, this.config_request)
                  .then(() => {                      
                      this.tasks.splice(this.tasks.indexOf(task), 1);                    
                  })
                  .catch((error) => {
                      console.log(error)
                  });  
          },
          reset(){                      
              this.newTask = {};
          }
      },
      
      created(){ 
          axios.post(this.postURL + '/declaracion/get_declaraciones')
              .then(res => { this.tasks = res.data; })
              .catch((error) => { console.log(error) })
      }
  }
  </script>
