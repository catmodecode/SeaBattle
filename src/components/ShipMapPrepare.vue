<template>
  <div>
    <div>Клик правой кнопкой мыши повернет корабль</div>
    <div
      id="phantom-block"
      class="ship-draw"
      v-bind:style="{ left: phantomPos.x, top: phantomPos.y }"
      v-if="chosenShip !== null"
    >
      <table>
        <div v-if="chosenShip.direction">
          <tr>
            <td v-for="i in chosenShip.size" :key="i"></td>
          </tr>
        </div>
        <div v-else>
          <tr v-for="i in chosenShip.size" :key="i">
            <td></td>
          </tr>
        </div>
      </table>
    </div>
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
          <td
            v-for="index in horizontalMarks.length"
            @mouseover="hoverField(index - 1, verticalMarks.indexOf(markV))"
            @mouseleave="hoverField(-1, -1)"
            v-bind:class="{
              phantom: PhantomPlace(index - 1, verticalMarks.indexOf(markV)),
              placed: isShip(index - 1, verticalMarks.indexOf(markV)),
            }"
            :data-shipIndex="
              shipList.indexOf(
                findShip(index - 1, verticalMarks.indexOf(markV))
              )
            "
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
            :data-shipIndex="ships.indexOf(ship)"
          >
            <table :data-shipIndex="ships.indexOf(ship)">
              <tr :data-shipIndex="ships.indexOf(ship)">
                <td
                  v-for="i in ship.size"
                  :key="i"
                  :data-shipIndex="ships.indexOf(ship)"
                ></td>
              </tr>
            </table>
          </div>
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
      shipList: [],
      phantomPos: { x: "-1000px", y: "-1000px" },
    };
  },
  computed: {
    ships() {
      this.chosenShip;
      return this.shipList;
    },
    shipsPlaced() {
      this.chosenShip;
      return this.shipList.filter((ship) => {
        return ship.placed;
      });
    },
  },
  methods: {
    changeDirection: function (e) {
      if (e.button !== 2) {
        return;
      }
      if (this.chosenShip == null) {
        return;
      }
      this.chosenShip.direction = !this.chosenShip.direction;
      this.chosenShip.setPosition(
        new Point(this.chosenShip.position.x, this.chosenShip.position.y)
      );
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
      return this.findShip(x, y) !== undefined;
    },
    findShip: function (x, y) {
      return this.shipsPlaced.find((ship) => {
        const hx = ship.position.x;
        const hy = ship.position.y;
        const dx = ship.direction ? ship.size - 1 : 0;
        const dy = ship.direction ? 0 : ship.size - 1;
        return x >= hx && y >= hy && x <= hx + dx && y <= hy + dy;
      });
    },
    choseShip: function (index) {
      if (index < 0 || this.chosenShip !== null) {
        return;
      }
      this.chosenShip = this.shipList[index];
      this.chosenShip.setPosition(-1, -1);
      this.chosenShip.placed = false;

      window.oncontextmenu = () => {
        return false;
      };
      window.onmousemove = (e) => {
        this.phantomPos = { x: e.clientX + "px", y: e.clientY + "px" };
      };
      this.hoveredField = false;
      this.shipList[index].placed = false;
      console.log(this.chosenShip);
    },
    placeShip: function () {
      if (this.hoveredField == false && this.chosenShip !== null) {
        this.chosenShip.setPosition(-1, -1);
        this.chosenShip.placed = false;
        this.chosenShip = null;
      }
      if (this.chosenShip == null) {
        return;
      }
      const chosenShip = this.chosenShip;
      if (
        chosenShip.position.x < 0 ||
        chosenShip.position.x >= this.horizontalMarks.length ||
        chosenShip.position.y < 0 ||
        chosenShip.position.x >= this.verticalMarks.length
      ) {
        return;
      }
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
        this.chosenShip.placed = true;
        this.chosenShip = null;
        window.oncontextmenu = () => {
          return true;
        };
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
      this.$socket.emit("shipIn", shipsToSend, (reply) => {
        console.log(reply, shipsToSend);
      });
    },
  },
  created: function () {
    window.onmousedown = this.changeDirection;
    window.onmouseup = (e) => {
      if (e.button == 0) {
        if (this.chosenShip != null) {
          this.placeShip();
        } else {
          const index = e.target.dataset.shipindex;
          if (index === undefined || index < 0) {
            return;
          }
          this.choseShip(index);
        }
      }
    };
    this.horizontalMarks = constMap.horizontalMarks;
    this.verticalMarks = constMap.verticalMarks;
    const ships = this.$store.state.shipMapStore.ships;
    this.shipList = Object.keys(ships).flatMap((key) => {
      return ships[key].map((val) => {
        val.placed = false;
        return val;
      });
    });
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

.ship-draw td {
  background: #0099ff;
}

.ship-map-prepare td,
.ship-draw td {
  min-width: $cellSize;
  height: $cellSize;
  border-style: solid;
}

.phantom {
  border-color: #0099ff;
}

.placed {
  background-color: #0099ff;
}

#phantom-block {
  position: absolute;
  pointer-events: none;
  margin-left: -27px;
  margin-top: -27px;
}
</style>
