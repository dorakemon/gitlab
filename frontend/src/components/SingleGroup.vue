  
<template>
  <v-card>
    <v-card-media
      height="200px"
      :src="group.background"
    ></v-card-media>
    <v-card-title primary-title>
      <div class="headline">{{group.name}}</div>
    </v-card-title>
    <v-card-actions>
      <v-btn color="primary" :to="{ name: 'group', params: { id: group._id } }">Go</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['group'],
};
</script>