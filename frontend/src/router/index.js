// import Home from "../views/Home.vue";
// import Register from "../views/Register.vue"
// import Login from "../views/Login.vue"

// Vue.use(VueRouter);

// const routes = [
//   {
//     path: "/",
//     name: "Home",
//     component: Home
//   },
//   {
//     path: "/group/:groupId",
//     name: "Group",
//     component: () =>
//       import("../views/Group.vue")
//   },
//   {
//     path: "/register/",
//     name: "Register",
//     component: Register
//   },
//   {
//     path: "/login/",
//     name: "Login",
//     component: Login
//   },
// ];
import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
// import SignUp from '../views/SignUp.vue';
// import Login from '../views/Login.vue';
// import Boards from '../views/Boards.vue';
// import Board from '../views/Board.vue';

// import store from '../store';

Vue.use(VueRouter);

// function isLoggedIn(to, from, next) {
//   store.dispatch('auth/authenticate').then(() => {
//     next();
//   }).catch(() => {
//     next('/login');
//   });
// }

export default new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      // beforeEnter(to, from, next) {
      //   store.dispatch('auth/authenticate').then(() => {
      //     next('/groups');
      //   }).catch(() => {
      //     next('/login');
      //   });
      // },
    },
    // {
    //   path: '/signup',
    //   name: 'signup',
    //   component: SignUp,
    // },
    // {
    //   path: '/login',
    //   name: 'login',
    //   component: Login,
    // },
    // {
    //   path: '/groups',
    //   name: 'groups',
    //   component: groups,
    //   beforeEnter: isLoggedIn,
    // },
    // {
    //   path: '/groups/:id',
    //   name: 'group',
    //   component: group,
    //   beforeEnter: isLoggedIn,
    // },
  ],
});