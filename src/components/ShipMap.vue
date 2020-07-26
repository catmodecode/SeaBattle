<template>
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
      <td v-for="index in horizontalMarks.length" :key="index"></td>
    </tr>
  </table>
</template>

<script>
import constMap from "@/constants/playField.js";

export default {
  name: "ShipMap",
  params: {
    horizontalMarks: [],
    verticalMarks: [],
  },
  created: function() {
    this.horizontalMarks = constMap.horizontalMarks;
    this.verticalMarks = constMap.verticalMarks;
  },
};
</script>

<style lang="scss" scoped>
$cellSize: 25px;

.play-room {
  display: block;
}

.ship-map td {
  width: $cellSize;
  height: $cellSize;
  border: solid;
}
</style>
