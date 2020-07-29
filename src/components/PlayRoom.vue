<template>
  <div calss="play-room">
    <a v-on:click="showShip">SHIIIIPS!</a>
    <a v-on:click="setShip">SET SHIIIIPS!</a>
    <div id="prepare-map" v-if="prepearShips">
      <ShipMapPrepare />
    </div>
    <div id="ready-map" v-else>
      <div id="my-map">
        <shipMap />
      </div>
      <div id="enemy-map">
        <shipMap />
      </div>
    </div>
  </div>
</template>

<script>
import shipMap from "./ShipMap";
import ShipMapPrepare from "./ShipMapPrepare";
import { mapState } from "vuex";
import store from "@/store";

export default {
  name: "PlayRoom",
  components: {
    shipMap,
    ShipMapPrepare,
  },
  params: {
    prepearShips: true,
  },
  computed: mapState({
    ships: (state) => state.shipMapStore.ships,
  }),
  methods: {
    showShip: function () {
      console.log(this.ships);
    },
    setShip: function () {
      store.dispatch("shipMapStore/addShip", {
        shipType: "Corvette",
        shipIndex: 2,
        coords: [{ x: 1, y: 2 }],
      });
    },
  },
  sockets: {
    ship_map: function (data) {
      console.log(
        'this method was fired by the socket server. eg: io.emit("customEmit", ' +
          data +
          ")"
      );
    },
  },
  created: function () {
    this.prepearShips = true;
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
