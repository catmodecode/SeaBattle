import Auth from '../views/Auth.vue'
import Room from '../views/Room.vue'

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
        path: "/room/:roomId",
        name: "Room",
        component: Room,
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
