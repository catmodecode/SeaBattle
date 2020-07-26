import playField from "@/constants/playField.js";

export default {
  namespaced: true,
  state: () => ({
    ships: Object.fromEntries(
      Object.keys(playField.ships).map((shipName) => {
        return [shipName, playField.ships[shipName]];
      })
    ),
    // map: Array.from({ length: playField.verticalMarks }, (v) =>
    //   Array.from({ length: playField.horizontalMarks }, (v) => null)
    // ),
  }),
  mutations: {
    // setShip(state, coords) {
    //   state.sid = sid;
    //   localStorage.sid = sid;
    //   state.user = user;
    //   localStorage.user = user;
    // },
  },
  actions: {
    // authenticate({ commit }, user) {
    //   commit("storeUser", user);
    // },
    // logout({ commit }) {
    //   commit("storeUser", { sid: null, user: null });
    // },
  },
};
