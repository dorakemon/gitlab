<template>
  <!-- <v-app-bar color="dark accent-4" dark dense>
    <v-toolbar-items><v-btn href="/" elevation=0 flat class="white--text">App</v-btn></v-toolbar-items>
    <div class="flex-grow-1"></div>
      <v-toolbar-items>
        <v-btn elevation=0 flat><router-link :to="{ name:'Home' }" class="white--text">Home</router-link></v-btn>
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
  </v-app-bar> -->
  <v-toolbar
    app>
    <v-toolbar-title>
      <v-btn flat :to="{ name: 'home' }">App Name</v-btn>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items v-if="!user">
      <v-btn flat :to="{ name: 'login' }">Login</v-btn>
      <v-btn flat :to="{ name: 'signup' }">SignUp</v-btn>
    </v-toolbar-items>
    <v-toolbar-items v-if="user">
      <app-avatar :user="user.user"></app-avatar>
      <v-btn flat @click="logout">LogOut</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
  import AppAvatar from '@/components/AppAvatar';

  export default {
    props: ['user', 'logout'],
    components: {
      AppAvatar
    },
    name: "AppNavbar",
    methods: {
      logOut() {
        this.$router.push("/login")
      }
    }
  };
</script>

<style scoped>
</style>