export default {
  namespaced: true,
  state: () => ({
    sid:
      typeof localStorage.sid === "undefined" || localStorage.sid === "null"
        ? null
        : localStorage.sid,
    user:
      typeof localStorage.user === "undefined" || localStorage.user === "null"
        ? null
        : localStorage.user,
  }),
  mutations: {
    storeUser(state, { sid, user }) {
      state.sid = sid;
      localStorage.sid = sid;
      state.user = user;
      localStorage.user = user;
    },
  },
  actions: {
    authenticate({ commit }, user) {
      commit("storeUser", user);
    },
    logout({ commit }) {
      commit("storeUser", { sid: null, user: null });
    },
  },
};
