<template>
  <div class="prepare">
    <table class="ship-map-prepare">
      <tr>
        <td></td>
        <td v-for="markH in horizontalMarks" :key="markH">
          {{ markH }}
        </td>
      </tr>
      <tr v-for="markV in verticalMarks" :key="markV">
        <td>
          {{ markV }}
        </td>
        <td v-for="index in horizontalMarks.length" :key="index"></td>
      </tr>
    </table>

    <div class="ship-list">
      <div
        v-for="shipType in Object.keys(ships)"
        :key="shipType"
        v-bind:id="shipType"
      >
        <div>{{ ships[shipType][0].name }}</div>
        <div class="ship-container">
          <div
            v-for="shipIndex in ships[shipType].length"
            v-on:click="choseShip"
            :key="shipIndex"
          >
            <div v-bind:id="shipType + '-' + shipIndex" class="ship-draw">
              {{ ships[shipType][shipIndex] }}
              <table>
                <tr>
                  <td v-for="i in ships[shipType][shipIndex]" :key="i">{{ i }}</td>
                </tr>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import constMap from "@/constants/playField.json";
import { mapState } from "vuex";

export default {
  name: "ShipMapPrepare",
  params: {
    horizontalMarks: [],
    verticalMarks: [],
    ships: {},
  },
  computed: mapState({
    ships: (state) => state.shipMapStore.ships,
  }),
  methods: {
    choseShip: function (event) {
      console.log(event.target);
    },
  },
  created: function () {
    this.horizontalMarks = constMap.horizontalMarks;
    this.verticalMarks = constMap.verticalMarks;
    console.log(this.ships['Battleship'][0].size);
    // var ships = this.ships;
    // this.ships = Object.keys(ships).map((shipType) => {
    // })
  },
};
</script>

<style lang="scss" scoped>
$cellSize: 25px;

.prepare {
  display: flex;
  flex-direction: row;
}

.ship-container {
  display: flex;
  flex-direction: row;
}

.ship-draw {
  padding: 10px;
}

.ship-map-prepare td,
.ship-draw td {
  width: $cellSize;
  height: $cellSize;
  border: solid;
}
</style>
