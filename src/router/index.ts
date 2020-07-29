import Vue from "vue";
import VueRouter from "vue-router";
import Auth from "../views/Auth.vue";
import Room from "../views/Room.vue";

Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    {
      path: "/",
      name: "Auth",
      component: Auth,
    },
    {
      path: "/room/:roomId",
      name: "Room",
      component: Room,
    },
  ],
});

export default router;
