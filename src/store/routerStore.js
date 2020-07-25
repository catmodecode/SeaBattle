import Auth from '../views/Auth.vue'
import About from '../views/About.vue'

export default {
  namespaced: true,
  state: () => ({
    links: [
      {
        path: "/",
        name: "Auth",
        component: Auth,
      },
      {
        path: "/about",
        name: "About",
        component: About,
      },
    ],
  }),
  mutations: {
    pushLink(state, link) {
      state.links.push(link);
    }
  },
  actions: {
    pushLink({ commit }, link) {
      commit('pushLink', link);
    },
  },
};
