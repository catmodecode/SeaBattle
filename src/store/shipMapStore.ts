import playField from "@/constants/playField.js";
import ShipType from "../classes/ShipType";

export default {
  namespaced: true,
  state: () => ({
    ships: Object.fromEntries(
      Object.keys(playField.ships).map((shipName) => {
        console.log(playField.ships[shipName]);
        const shipTypeData = playField.ships[shipName];
        console.log(shipTypeData);
        // let shipType = new ShipType(
        //   shipTypeData.name,
        //   shipTypeData.count,
        //   shipTypeData.size
        // );
        console.log(ShipType);
        return [
          shipName,
          ((ships) => {
            const arShips = [];
            for (let shipsCount = 0; shipsCount < ships.count; shipsCount++) {
              const qShip = [];
              for (let shipsSize = 0; shipsSize < ships.size; shipsSize++) {
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
    setShip(state, { shipType, shipIndex, coords }) {
      state.ships[shipType][shipIndex] = coords;
    },
  },
  actions: {
    addShip({ commit }, shipType, shipIndex, coords) {
      commit("setShip", {
        shipType: shipType,
        shipIndex: shipIndex,
        coords: coords,
      });
    },
  },
};
