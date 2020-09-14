<template>
  <div>
    <table class="ship-map">
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
        <td
          class="fire"
          v-bind:class="{
            placed: isShip(index - 1, verticalMarks.indexOf(markV)),
          }"
          v-for="index in horizontalMarks.length"
          :key="index"
        >
          
        </td>
      </tr>
    </table>
  </div>
</template>
<script>
import constMap from "@/constants/playField.json";
// ╳
// local_fire_department
export default {
  name: "ShipMap",
  params: {
    horizontalMarks: [],
    verticalMarks: [],
  },
  props: ["ships"],
  created: function () {
    this.horizontalMarks = constMap.horizontalMarks;
    this.verticalMarks = constMap.verticalMarks;
  },
  methods: {
    isShip: function (x, y) {
      return this.findShip(x, y) !== undefined;
    },
    findShip: function (x, y) {
      return this.ships.find((ship) => {
        const hx = ship.position.x;
        const hy = ship.position.y;
        const dx = ship.direction ? ship.size - 1 : 0;
        const dy = ship.direction ? 0 : ship.size - 1;
        return x >= hx && y >= hy && x <= hx + dx && y <= hy + dy;
      });
    },
  },
};
</script>

<style lang="scss" scoped>
$cellSize: 25px;

.ship-map td {
  width: $cellSize;
  height: $cellSize;
  border: solid;
}

.placed {
  background-color: #0099ff;
}

.fire {
  font-family: Material Icons;
  font-size: 18pt;
  content: counter;
  color: red;
}
</style>
