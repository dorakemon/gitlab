<template>
  <div class="nav-bar">
    <b-navbar toggleable="lg" variant="light" fixed="top">
      <b-navbar-brand href="/">App</b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-item>
            <router-link :to="{ name:'Home' }">Home</router-link>
          </b-nav-item>
          <b-nav-item>
            <a @click="logOut">Logout</a>
          </b-nav-item>
        </b-navbar-nav>
    </b-navbar>
  </div>
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