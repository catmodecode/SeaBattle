<template>
  <form class="authenticate">
    <div class="row-item">
      <label for="user-name">Ваше имя</label>
      <input type="text" id="user-name" v-model="name" />
    </div>
    <div class="row-item">
      <input
        class="row-button"
        type="button"
        v-on:click="login"
        value="Быстрая игра"
      />
      <input
        class="row-button"
        type="button"
        v-on:click="login"
        value="Частная игра"
      />
    </div>
  </form>
</template>

<script>
import store from "@/store";

export default {
  name: "Authenticate",
  data: function () {
    return {
      name: "",
    };
  },
  methods: {
    login: function () {
      this.$socket.emit("auth", this.name);
      store.dispatch("authStore/authenticate", {
        user: this.name,
        sid: this.$socket.id,
      });
      this.$socket.emit("quickroom", "", (reply) => {
        this.$router.push({ name: "Room", params: { roomId: reply } });
      });
    },
  },
  created: function () {
    this.name = localStorage.user;
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.authenticate {
  display: flex;
  flex-direction: column;
}

.row-item {
  margin: 10px;
}

.row-button {
  margin: 0px 10px;
}
</style>
