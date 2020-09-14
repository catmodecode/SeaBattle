import playField from "@/constants/playField.json";
import ShipType from "../classes/ShipType";
import Ship from "@/classes/Ship";

export default {
  namespaced: true,
  state: () => ({
    ships: Array.from(
      playField.ships.map((ship) => {
        const shipType = new ShipType({
          type: ship.type,
          name: ship.name,
          size: ship.size,
          count: ship.count,
        });
        const indexArr = new Array(shipType.count);
        indexArr.fill(shipType);
        const shipsResult = indexArr.map((val) => {
          return new Ship(val);
        });
        return shipsResult;
      })
    ).flat(),
    ready: false,
  }),
  mutations: {
    setShips(state, ships) {
      state.ships = ships;
    },
    setReady(state, readyState) {
      state.ready = readyState;
    },
  },
  actions: {
    setShips({ commit }, ships) {
      commit("setShips", ships);
    },
    setReady({ commit }, readyState) {
      commit("setReady", readyState);
    },
  },
};
