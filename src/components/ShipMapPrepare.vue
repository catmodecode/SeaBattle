<template>
  <div class="prepare" v-on:click.ctrl.exact="changeDirection">
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
        <td
          v-for="index in horizontalMarks.length"
          @mouseover="hoverField(index - 1, verticalMarks.indexOf(markV))"
          @mouseleave="hoverField(-1, -1)"
          v-bind:class="{
            phantom: PhantomPlace(index - 1, verticalMarks.indexOf(markV)),
            placed: isShip(index - 1, verticalMarks.indexOf(markV)),
          }"
          v-on:click.exact="placeShip"
          :key="index"
        ></td>
      </tr>
    </table>

    <div v-if="shipsPlaced.length == ships.length">
      <input
        type="button"
        class="readyButton"
        v-on:click="setReady"
        value="Готов"
      />
    </div>

    <div class="ship-container">
      <div
        v-for="ship in ships"
        :key="ships.indexOf(ship)"
        v-bind:id="ship.type + ships.indexOf(ship)"
      >
        <div
          class="ship-draw"
          v-show="!ship.placed"
          v-on:click="choseShip(ships.indexOf(ship))"
        >
          <table>
            <tr>
              <td v-for="i in ship.size" :key="i"></td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import constMap from "@/constants/playField.json";
import Point from "@/classes/Point";
import Ship from "@/classes/Ship";

export default {
  name: "ShipMapPrepare",
  data: () => {
    return {
      hoveredField: false,
      chosenShip: null,
      horizontalMarks: [],
      verticalMarks: [],
      shipsPlaced: [],
      shipList: [],
    };
  },
  computed: {
    ships() {
      return this.shipList;
    },
  },
  methods: {
    changeDirection: function () {
      if (this.chosenShip == null) {
        return;
      }
      this.chosenShip.direction = !this.chosenShip.direction;
    },
    hoverField: function (x, y) {
      if (this.chosenShip == null) {
        return;
      }
      if (x == -1 && y == -1) {
        this.hoveredField = false;
        return;
      }
      this.hoveredField = true;
      this.chosenShip.setPosition(new Point(x, y));
    },
    PhantomPlace: function (x, y) {
      if (this.chosenShip == null || !this.hoveredField) {
        return false;
      }
      const hx = this.chosenShip.position.x;
      const hy = this.chosenShip.position.y;
      const dx = this.chosenShip.direction ? this.chosenShip.size - 1 : 0;
      const dy = this.chosenShip.direction ? 0 : this.chosenShip.size - 1;
      return x >= hx && y >= hy && x <= hx + dx && y <= hy + dy;
    },
    isShip: function (x, y) {
      return (
        this.shipsPlaced.find((ship) => {
          const hx = ship.position.x;
          const hy = ship.position.y;
          const dx = ship.direction ? ship.size - 1 : 0;
          const dy = ship.direction ? 0 : ship.size - 1;
          return x >= hx && y >= hy && x <= hx + dx && y <= hy + dy;
        }) !== undefined
      );
    },
    choseShip: function (index) {
      this.chosenShip = this.shipList[index];
    },
    placeShip: function () {
      if (this.chosenShip == null) {
        return;
      }
      const chosenShip = this.chosenShip;
      if (
        this.shipsPlaced.find((ship) => {
          return chosenShip.isIntersect(ship);
        }) !== undefined
      ) {
        return;
      }
      const shipType = this.chosenShip.type;
      const index = this.shipList.indexOf(this.chosenShip);
      if (!this.isPlaced(shipType, index)) {
        this.shipsPlaced.push(this.chosenShip);
        this.chosenShip.placed = true;
        this.chosenShip = null;
        this.shipList.reverse().reverse();
      }
    },
    isPlaced: function (shipType, index) {
      return this.shipsPlaced.find((val) => {
        return val.type == shipType && val.index == index;
      });
    },
    setReady: function () {
      const shipsToSend = this.shipsPlaced.map((ship) => {
        const newShip = Ship.fromShip(ship);
        newShip.setPosition(new Point(ship.position.x, ship.position.y));
        return newShip;
      });
      this.$socket.emit("shipIn", JSON.stringify(shipsToSend));
    },
  },
  created: function () {
    this.horizontalMarks = constMap.horizontalMarks;
    this.verticalMarks = constMap.verticalMarks;
    this.shipsPlaced = [];
    const ships = this.$store.state.shipMapStore.ships;
    this.shipList = Object.keys(ships).flatMap((key) => {
      return ships[key].map((val) => {
        val.placed = false;
        return val;
      });
    });
    console.log(this.shipList);
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
  flex-direction: column;
}

.ship-draw {
  padding: 10px;
}

.ship-map-prepare td,
.ship-draw td {
  width: $cellSize;
  height: $cellSize;
  border-style: solid;
}

.phantom {
  border-color: #0099ff;
}

.placed {
  background-color: #0099ff;
}
</style>
