<template>
  <div class="Auth">
    <h2>Морской бой</h2>
    <Authenticate />
  </div>
</template>

<script>
// @ is an alias to /src
import Authenticate from "@/components/Authenticate.vue";

export default {
  name: "Auth",
  components: {
    Authenticate,
  },
};
</script>
