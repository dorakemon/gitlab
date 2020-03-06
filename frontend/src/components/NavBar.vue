<template>
  <v-app-bar color="dark accent-4" dark dense>
    <v-toolbar-items><v-btn href="/" elevation=0 flat class="white--text">App</v-btn></v-toolbar-items>
    <div class="flex-grow-1"></div>
      <v-toolbar-items>
        <!-- <v-btn elevation=0 flat><router-link :to="{ name:'Home' }" class="white--text">Home</router-link></v-btn> -->
        <v-btn elevation=0 flat :to="{ name:'Home' }">Home</v-btn>
      </v-toolbar-items>
      <v-toolbar-items>
        <v-btn elevation=0 flat class="white--text"><a class="white--text" @click="logOut">Logout</a></v-btn>
      </v-toolbar-items>
      <v-menu left bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-account-circle</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="n in 5" :key="n" @click="() => {}">
            <v-list-item-title>りんく {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
  </v-app-bar>
</template>

<script>
  export default {
    name: "NavBar",
    methods: {
      logOut() {
        this.$router.push("/login")
      }
    }
  };
</script>

<style scoped>
</style>