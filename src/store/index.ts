import Vue from "vue";
import Vuex from "vuex";
import routerStore from "./routerStore";
import authStore from "./authStore";
import shipMapStore from "./shipMapStore.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    pageOptions: {
      title: "Страница",
      menuVisible: false,
    },
  },
  mutations: {
    setOptions(state, options) {
      state.pageOptions = options;
    },
  },
  actions: {
    setOptions({ commit }, options) {
      commit("setOptions", options);
    },
  },
  modules: {
    routerStore,
    authStore,
    shipMapStore,
  },
});
