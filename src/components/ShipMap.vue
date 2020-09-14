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
          v-bind:class="{
            placed: isShip(index - 1, verticalMarks.indexOf(markV)),
            fire: isOnFire(index - 1, verticalMarks.indexOf(markV)),
            miss: isMiss(index - 1, verticalMarks.indexOf(markV)),
          }"
          v-for="index in horizontalMarks.length"
          :key="index"
        >
          <p></p>
        </td>
      </tr>
    </table>
  </div>
</template>
<script>
import constMap from "@/constants/playField.json";
import Point from "@/classes/Point";
// ╳
// local_fire_department
export default {
  name: "ShipMap",
  params: {
    horizontalMarks: [],
    verticalMarks: [],
    myMap: [],
    enemyMap: [],
  },
  props: ["ships"],
  created: function () {
    this.horizontalMarks = constMap.horizontalMarks;
    this.verticalMarks = constMap.verticalMarks;
    const hMarksLength = this.horizontalMarks;
    this.myMap = Array(10)
      .fill(0)
      .map((row) => (row = Array(10).fill("")));
    this.enemyMap = Array(10)
      .fill(0)
      .map((row) => (row = Array(10).fill("")));
    this.myMap[1][5] = "S";
  },
  methods: {
    fire: function (x, y) {
      this.$socket.emit("shot", new Point(x, y), (reply) => {
        console.log(reply);
      });
    },
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
    isOnFire: function (x, y) {
      return Math.random() * 10 < 3 && this.isShip(x, y);
    },
    isMiss: function (x, y) {
      return Math.random() * 10 < 3 && !this.isShip(x, y);
    },
  },
};
</script>

<style lang="scss" scoped>
$cellSize: 25px;
$shipColor: #5c4c2f;

.ship-map td {
  width: $cellSize;
  height: $cellSize;
  max-width: $cellSize;
  max-height: $cellSize;
  border: solid;
}

.placed {
  background-color: $shipColor;
  color: $shipColor;
}

td p {
  max-width: $cellSize;
  max-height: $cellSize;
  display: inline;
}

.fire {
  animation: pulse 3s infinite;
}

@keyframes pulse {
  0% {
    color: #ff7b00;
  }
  25% {
    color: #feb747;
  }
  100% {
    color: #ff7b00;
  }
}

.fire :after {
  font-family: Material Icons;
  font-size: 16pt;
  content: "local_fire_department";
}

.miss {
  color: rgb(204, 231, 53);
}

.miss :after {
  font-family: Material Icons;
  font-size: 16pt;
  color: black;
  content: "clear";
}
</style>
