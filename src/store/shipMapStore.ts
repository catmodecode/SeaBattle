import playField from "@/constants/playField.json";
import ShipType from "../classes/ShipType";
import Point from "@/classes/Point";
import Ship from "@/classes/Ship";

export default {
  namespaced: true,
  state: () => ({
    ships: Object.fromEntries(
      Object.keys(playField.ships).map((shipName) => {
        const shipTypeData = playField.ships[shipName];
        const shipType = new ShipType(
          shipTypeData.name,
          shipTypeData.count,
          shipTypeData.size
        );
        const shipsResult = new Array(shipType.count);
        shipsResult.fill(new Ship(shipType));
        return [shipName, shipsResult];
        // return [
        //   shipName,
        //   ((ships) => {
        //     let arShips = [];
        //     for (let shipsCount = 0; shipsCount < ships.count; shipsCount++) {
        //       let qShip = [];
        //       for (let shipsSize = 0; shipsSize < ships.size; shipsSize++) {
        //         qShip.push(Point(0,0));
        //       }
        //       arShips.push(qShip);
        //     }
        //     return arShips;
        //   })(playField.ships[shipName]),
        // ];
      })
    ),
    // map: Array.from({ length: playField.verticalMarks }, (v) =>
    //   Array.from({ length: playField.horizontalMarks }, (v) => null)
    // ),
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
