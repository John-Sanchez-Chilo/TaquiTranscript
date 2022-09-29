<template>
    <v-app>
      <v-main class="light-blue darken-4">
      <v-container fill-height>
    
            <v-row
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
                    AGREGAR UN NUEVO CASO
                  </v-btn>
    
                </template>
                <v-card>
                  <br>
                  <v-card-title>
                    <span class="text-h5 mx-auto">INGRESE LOS DATOS DEL NUEVO CASO</span>
                  </v-card-title>
                  <v-card-text class="text-h6 text-center">
    
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Nombre'
                      :rules="nameRules"
                      label="Titulo"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Descripcion'
                      :rules="nameRules"
                      label="Descripcion"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Fecha'
                      :rules="nameRules"
                      label="Fecha de inicio"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.HoraIn'
                      :rules="nameRules"
                      label="Fecha de finalizacion"
                      required
                    ></v-text-field>
                    <v-text-field
                      class="mx-10"
                      v-model='newTask2.Estado'
                      :rules="nameRules"
                      label="Estado"
                      required
                    ></v-text-field>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="success"
                      class="mr-4"
                      @click="addTask"
                    >
                      CREAR CASO
                    </v-btn>
                  </v-card-actions>
                  <br>
                </v-card>
              </v-dialog>
              &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj;
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
                link @click="$router.push({ path: '/concurso' })"
              >
                Configuracion
              </v-btn>
              &zwnj; &zwnj;
            </v-row>
    
          <v-layout row wrap align>
              <v-card
              height="650" text-h4 class="mx-auto my-2 text-center" width="1600" outlined elevation="20">
              <v-simple-table>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-center">
                        Id
                      </th>
                      <th class="text-center">
                        Titulo
                      </th>
                      <th class="text-center">
                        Descripcion
                      </th>
                      <th class="text-center">
                        Fecha de inicio
                      </th>
                      <th class="text-center">
                        Fecha de finalizacion
                      </th>
                      <th class="text-center">
                        Estado
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="task in tasks" :key="task"
                    >
                        <td>{{ task.id_act }} </td>
                        <td>{{ task.nombre }} </td>
                        <td>{{ task.descripcion }} </td>
                        <td>{{ task.fecha }} </td>
                        <td>{{ "-" }} </td>
                        <td>{{ "Activo" }} </td>
                        <td><v-btn
                            small
                            color="error"
                            dark
                            class="grey  mx-2"
                            
                            v-on="on"
                            link @click="$router.push({ path: '/sesion' })"
                          >
                            <v-icon dark>
                              mdi-lead-pencil
                            </v-icon>
                          </v-btn>
    
                          </td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
              </v-card>
            </v-layout>
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
                newTask2: {},
                postURL: 'https://backendsecosystem.herokuapp.com',
                config_request: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }       
            }
        },
        methods:{
            addTask(){ 
                axios.post(this.postURL + '/actividad/add_actividad', this.newTask2, this.config_request)
                    .then(res => {                                         
                        this.tasks.push(res.data);
                        console.log(res.data);
                    })
                    .catch((error) => {
                        console.log(error)
                    });
    
                this.newTask2 = {};
            },

            deleteTask(task){                      
                axios.post(this.postURL + '/actividad/delete_actividad', {CUI: task.ID_Actividad}, this.config_request)
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
            axios.post(this.postURL + '/actividad/get_actividades')
                .then(res => { this.tasks = res.data; })
                .catch((error) => { console.log(error) })
        },
    
    }
    </script>
    