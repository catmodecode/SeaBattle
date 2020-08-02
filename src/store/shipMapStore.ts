import playField from "@/constants/playField.json";
import ShipType from "../classes/ShipType";
import Point from "@/classes/Point";
import Ship from "@/classes/Ship";

export default {
  namespaced: true,
  state: () => ({
    ships: Object.fromEntries(
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
        return [ship.type, shipsResult];
      })
    ),
  }),
  mutations: {
    setShip(
      state,
      {
        shipType,
        shipIndex,
        coords,
      }: { shipType: string; shipIndex: number; coords: Point }
    ) {
      state.ships[shipType][shipIndex] = coords;
    },
  },
  actions: {
    addShip(
      { commit } /* shipType: string, shipIndex: number, coords: Point */
    ) {
      commit("setShip", {
        shipType: "shipType",
        shipIndex: 1, //shipIndex,
        coords: new Point(1, 1), //coords,
      });
    },
  },
};
