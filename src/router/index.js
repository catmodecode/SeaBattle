import Vue from "vue";
import VueRouter from "vue-router";
import store from '../store'

Vue.use(VueRouter);

const routes = store.state.routerStore.links;

const router = new VueRouter({
  routes,
});

export default router;
