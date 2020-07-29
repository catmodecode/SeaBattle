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
        v-for="shipType in Object.keys(shipTypes)"
        :key="shipType"
        v-bind:id="shipType"
      >
        <div>{{ shipTypes[shipType].name }}</div>
        <div class="ship-container">
          <div
            v-for="shipIndex in shipTypes[shipType].count"
            v-on:click="choseShip"
            :key="shipIndex"
          >
            <div v-bind:id="shipType + '-' + shipIndex" class="ship-draw">
              <table>
                <tr>
                  <td v-for="i in shipTypes[shipType].size" :key="i"></td>
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
// import ShipType from "@/classes/ShipType";

export default {
  name: "ShipMapPrepare",
  params: {
    horizontalMarks: [],
    verticalMarks: [],
    shipTypes: {},
  },
  methods: {
    choseShip: function (event) {
      console.log(event.target);
    },
  },
  created: function () {
    this.horizontalMarks = constMap.horizontalMarks;
    this.verticalMarks = constMap.verticalMarks;
    this.shipTypes = constMap.ships;
    // var shipTypes = this.shipTypes;
    // this.ships = Object.keys(shipTypes).map((shipType) => {
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
