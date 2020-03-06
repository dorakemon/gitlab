<template>
  <div class="home">
    <div>
      <h3>Group</h3>
      <router-link class="btn btn-outline-success" v-for="(group, groupId) in groups" :key="group.id" :to="{ name: 'Group', params: {groupId: groupId} }">{{ group.name }}</router-link>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      url: "http://127.0.0.1:8000/api/",
      groups: ""
    }
  },
  mounted() {
    axios.get(this.url + "user/")
    .then(response => {
      this.groups = response.data.personal_group
    })
  }
};
</script>

<style scoped>
</style>
