<template>
  <div class="Group">
    <h1>This is a Group page</h1>
    <p>{{ todos }}</p>
    <DAD />
  </div>
</template>

<script>
  import DAD from "@/components/DAD.vue";
  import axios from "axios";

  export default {
    name: "Group",
    components: {
      DAD
    },
    data() {
      return {
        url: "http://127.0.0.1:8000/api/",
        todos: ""
      }
    },
    mounted() {
    axios.get(this.url + "group/")
    .then(response => {
      this.todos = response
    })
  }
  };
</script>