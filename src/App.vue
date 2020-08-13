<template>
  <div id="app">
    <router-view v-if="connected" />
    <noconnect v-else />
  </div>
</template>

<script>
import noconnect from "@/components/NoConnect.vue";

export default {
  name: "App",
  components: {
    noconnect,
  },
  data: function () {
    return {
      connected: false,
    };
  },
  created: function () {
    const socket = this.$socket;
    socket.on("disconnect", (reason) => {
      this.connected = false;
    });
    socket.on("connect", (reason) => {
      this.connected = true;
    });
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
