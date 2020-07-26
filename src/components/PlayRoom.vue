<template>
  <div calss="play-room">
    <a v-on:click="showShip">SHIIIIPS!</a>
    <div id="my-map">
      <shipMap></shipMap>
    </div>
    <div id="enemy-map">
      <shipMap></shipMap>
    </div>
  </div>
</template>

<script>
import shipMap from "./ShipMap"
import { mapState } from "vuex";

export default {
  name: "PlayRoom",
  components: {
    shipMap
  },
  params: {
    horizontalMarks: [],
    verticalMarks: []
  },
  computed: mapState({
    ships: (state) => state.shipMapStore.ships,
  }),
  methods: {
    showShip: function() {
      console.log(this.ships)
    }
  },
  sockets: {
    ship_map: function(data) {
      console.log(
        'this method was fired by the socket server. eg: io.emit("customEmit", ' +
          data +
          ")"
      );
    },
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
