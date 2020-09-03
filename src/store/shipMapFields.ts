import playField from "@/constants/playField.json";
import Point from "@/classes/Point";

export default {
  namespaced: true,
  state: () => ({
    myField: playField.horizontalMarks.map(() => {
      return new Array(playField.verticalMarks.length);
    }),
    enemyField: playField.horizontalMarks.map(() => {
      return new Array(playField.verticalMarks.length);
    }),
  }),
  mutations: {
    hit(state, field: string, position: Point, fieldState: string) {
      if (!(fieldState in playField.fieldStates)) {
        console.error(fieldState + " not allowed!");
      }
      switch (field) {
        case "enemy":
          state.enemyField[position.x][position.y] = fieldState;
          break;
        case "my":
          state.myField[position.x][position.y] = fieldState;
          break;
        default:
          console.error("WRONG! What is the " + field + " is?");
          break;
      }
    },
  },
  actions: {
    hit({ commit }, field, position, fieldState) {
      commit("setShips", field, position, fieldState);
    },
  },
};
