<template>
  <v-flex sm3 pa-2>
    <v-card>
      <v-card-title primary-title style="flex-direction: column;">
        <div class="headline">Create Group</div>
        <div>
          <v-form
            v-if="!creating"
            v-model="valid"
            @submit.prevent="onCreateBoard"
            @keydown.prevent.enter>
            <v-text-field
              v-model="board.name"
              :rules="notEmptyRules"
              label="Name"
              required
            ></v-text-field>
            <v-text-field
              v-model="board.background"
              :rules="notEmptyRules"
              label="Background"
              required
            ></v-text-field>
            <v-btn type="submit" :disabled="!valid">Create</v-btn>
          </v-form>
          <v-progress-circular
            v-if="creating"
            :size="70"
            :width="7"
            indeterminate
            color="primary">
          </v-progress-circular>
        </div>
      </v-card-title>
    </v-card>
  </v-flex>
</template>

<script>
import { notEmptyRules } from '@/validators';
export default {
  props: ['creating', 'createGroup'],
  data: () => ({
    valid: false,
    board: {
      name: '',
      background: '',
    },
    notEmptyRules,
  }),
  methods: {
    async onCreateGroup() {
      if (this.valid) {
        await this.createGroup(this.group);
        this.group = {
          name: '',
          background: '',
        };
      }
    },
  },
};
</script>