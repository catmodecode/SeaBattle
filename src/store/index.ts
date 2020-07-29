import Vue from "vue";
import Vuex from "vuex";
import authStore from "./authStore";
// import shipMapStore from "./shipMapStore.js";
import PageOptionsStore from "./PageOptionsStore";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    authStore,
    PageOptionsStore,
    // shipMapStore,
  },
});
