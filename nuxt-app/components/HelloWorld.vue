<script setup>
const { data, pending, refresh, error } = await useFetch("/api/time");
</script>

<template>
  <div>
    <div>The time right now is: {{ data }}</div>
    <p v-if="pending" class="loading">Loading</p>
    <button v-else-if="!error" :disabled="pending" @click="refresh">
      Refresh
    </button>
    <div v-else>Woooooah there nelly!</div>
  </div>
</template>

<style scoped>
/* loading dots */

.loading:after {
  content: " .";
  animation: dots 1s steps(5, end) infinite;
}

@keyframes dots {
  0%,
  20% {
    color: rgba(0, 0, 0, 0);
    text-shadow: 0.25em 0 0 rgba(0, 0, 0, 0), 0.5em 0 0 rgba(0, 0, 0, 0);
  }
  40% {
    color: white;
    text-shadow: 0.25em 0 0 rgba(0, 0, 0, 0), 0.5em 0 0 rgba(0, 0, 0, 0);
  }
  60% {
    text-shadow: 0.25em 0 0 white, 0.5em 0 0 rgba(0, 0, 0, 0);
  }
  80%,
  100% {
    text-shadow: 0.25em 0 0 white, 0.5em 0 0 white;
  }
}
</style>
