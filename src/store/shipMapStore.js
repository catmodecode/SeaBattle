import playField from "@/constants/playField.js";

export default {
  namespaced: true,
  state: () => ({
    ships: Object.fromEntries(
      Object.keys(playField.ships).map((shipName) => {
        return [
          shipName,
          ((ships) => {
            var arShips = [];
            for (var shipsCount = 0; shipsCount < ships.count; shipsCount++) {
              var qShip = [];
              for (var shipsSize = 0; shipsSize < ships.size; shipsSize++) {
                qShip.push({ x: null, y: null });
              }
              arShips.push(qShip);
            }
            return arShips;
          })(playField.ships[shipName]),
        ];
      })
    ),
    // map: Array.from({ length: playField.verticalMarks }, (v) =>
    //   Array.from({ length: playField.horizontalMarks }, (v) => null)
    // ),
  }),
  mutations: {
    setShip(state, {shipType, shipIndex, coords}) {
      state.ships[shipType][shipIndex] = coords;
    },
  },
  actions: {
    addShip({ commit }, shipType, shipIndex, coords) {
      commit("setShip", {shipType: shipType, shipIndex: shipIndex, coords: coords});
    },
  },
};
