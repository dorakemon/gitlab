<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout row align-center wrap>
        <v-progress-circular
          v-if="loading"
          :size="70"
          :width="7"
          indeterminate
          color="primary">
        </v-progress-circular>
        <v-flex v-if="!loading" sm3 v-for="group in boards" :key="group._id" pa-2>
          <single-group :group="group"></single-group>
        </v-flex>
        <new-group-form
          :creating="creating"
          :createGroup="createGroup">
        </new-group-form>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
// import { mapState, mapGetters, mapActions } from 'vuex';
import NewGroupForm from '@/components/NewBoardForm';
import SingleGroup from '@/components/SingleBoard';
export default {
  name: 'groups',
  components: {
    NewGroupForm,
    SingleGroup,
  },
  mounted() {
    this.findGroups({ query: {} });
  },
//   methods: {
//     ...mapActions('boards', { findBoards: 'find' }),
//     async createBoard(board) {
//       const { Board } = this.$FeathersVuex;
//       const newBoard = new Board(board);
//       await newBoard.save();
//     },
//   },
//   computed: {
//     ...mapState('auth', { user: 'payload' }),
//     ...mapState('boards', {
//       loading: 'isFindPending',
//       creating: 'isCreatePending',
//     }),
//     ...mapGetters('boards', { findBoardsInStore: 'find' }),
//     boards() {
//       return this.user ? this.findBoardsInStore({
//         query: {
//           ownerId: this.user.userId,
//         },
//       }).data : [];
//     },
//   },
};
</script>