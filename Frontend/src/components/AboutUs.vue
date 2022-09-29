<template>
  <v-app id="inspire">
    <v-main class="light-blue darken-4">
      <v-container pa-16 me-n4>
        <v-row>

            <v-col sm="8">
            <v-sheet
              min-height="785"
              rounded="lg"
              elevation="20"
            >
            <p class="text-h2 text--primary text-center">
                <br>SeCo System
            </p>

            <v-sheet class="d-block text-center mx-auto mb-9 pa-12 text-h5" width="700"><br>
              Somos un grupo de programadores, estudiantes de la Universidad Nacional de San Agustín de Arequipa que busca aprender cada día más y buscar resolver diferentes problemas usando la programación.
En esta ocasión, el proyecto desarrollado es referido es una herramienta para los taquigrafos de los  jusgados. Los taquigrafos son las personas encargadas de transcribir las declaraciones que se realizan en los juicios, ellos toman apuntes a partir de las grabaciones y luego las convierten a documentos oficiales que pasan a ser archivados. Esta herramienta busca  realizar todo ello usando el servicio de Amazon Transcript
          </v-sheet>

            </v-sheet>
            </v-col>

          <v-col>
            <v-sheet rounded="lg" width="400" height="50" elevation="20">
              <div>
                <p class="text-h5 text--primary text-center pa-2">
                  Integrantes
                </p>
              </div>
            </v-sheet>
            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">John Sanchez
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGJohn"> Instagram</v-list-item-title>
                </v-btn>

                    <v-btn>
                    <v-list-item-icon>
                      <v-icon> mdi-facebook</v-icon>
                    </v-list-item-icon>
              
                    <v-list-item-title link @click="setFBJohn">Facebook</v-list-item-title>
                    </v-btn>
                </v-list-item>
              </v-sheet>

            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">Gabriel Pacco
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGGabriel"> Instagram</v-list-item-title>
                </v-btn>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBGabriel">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>
            <v-sheet class="text-h5 text-center my-5 pa-1" height="85" width="400" rounded elevation="20">Erick Perez
              <v-list-item>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-instagram </v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setIGErick"> Instagram</v-list-item-title>
                </v-btn>
                <v-btn>
                  <v-list-item-icon>
                    <v-icon> mdi-facebook</v-icon>
                  </v-list-item-icon>

                  <v-list-item-title link @click="setFBErick">Facebook</v-list-item-title>
                </v-btn>
              </v-list-item>
            </v-sheet>
            
            
            
            
          </v-col>
        </v-row>
        <v-row align-xl>
          <v-img
              lazy-src="@/img/carpincho.png"
              max-height="1800"
              max-width="1500"
              src="@/img/carpincho.png"

            ></v-img>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    selectedItem: 0,
    items: [
      { text: 'John Sanchez', instagram: "https://www.instagram.com/diego_aquino_7w7/", facebook: 'https://www.facebook.com/Diego.AquinoQ/' },
      { text: 'Gabriel Pacco', instagram: 'https://www.instagram.com/gabriel_pacco_/', facebook: 'https://www.facebook.com/gabriel.pacco.3' },
      { text: 'Kerito Won', instagram: 'https://www.instagram.com/kerito_17/', facebook: 'https://www.facebook.com/profile.php?id=100004004602419' }
    ],
    social: [
      ['Instagram', 'mdi-instagram'],
      ['Facebook', 'mdi-facebook'],
    ],
  }),
  methods: {

    setIGJohn() {
      window.location.href = "https://www.instagram.com/diego_aquino_7w7/";
    },
    setIGGabriel() {
      window.location.href = "https://www.instagram.com/gabriel_pacco_/";
    },
    setIGErick() {
      window.location.href = "https://www.instagram.com/kerito_17/";
    },

    ///////////////////

    setFBJohn() {
      window.location.href = "https://www.facebook.com/Diego.AquinoQ/";
    },
    setFBGabriel() {
      window.location.href = "https://www.facebook.com/gabriel.pacco.3";
    },
    setFBErick() {
      window.location.href = "https://www.facebook.com/profile.php?id=100004004602419";
    },
  }
};

</script>

