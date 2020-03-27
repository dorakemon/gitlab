<template>
  <v-app>
    <app-navbar
      :user="user"
      :logout="logout"
      ></app-navbar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>
<script>
  import AppNavbar from '@/components/AppNavbar';

  export default {
    name: 'App',
    components:{
      AppNavbar
    },
    data: () => ({
      showPassword: false
    }),
  };
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
