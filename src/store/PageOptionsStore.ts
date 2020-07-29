import PageOptions from "@/classes/PageOptions";

export default {
  namespaced: true,
  state: {
    pageOptions: new PageOptions({
      title: "Страница",
      menuVisible: false,
    }),
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
};
