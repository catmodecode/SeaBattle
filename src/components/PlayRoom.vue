<template>
  <div calss="play-room">
    <div id="prepare-map" v-if="!ready">
      <ShipMapPrepare />
    </div>
    <div id="ready-map" v-else>
      <div class="play-map" id="my-map">
        <shipMap v-bind:ships="ships" />
      </div>
      <div class="play-map" id="enemy-map">
        <shipMap v-bind:ships="[]" />
      </div>
    </div>
  </div>
</template>

<script>
import shipMap from "./ShipMap";
import ShipMapPrepare from "./ShipMapPrepare";
import { mapState } from "vuex";
// import store from "@/store";

export default {
  name: "PlayRoom",
  components: {
    shipMap,
    ShipMapPrepare,
  },
  computed: mapState({
    ships: (state) => state.shipMapStore.ships,
    ready: (state) => state.shipMapStore.ready,
  }),
  sockets: {
    shipmap: function (data) {
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

.play-map {
  margin: auto;
}

#ready-map {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
