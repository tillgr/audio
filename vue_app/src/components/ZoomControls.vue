<template>
<div class="zoomControls">
  <button id="plus" class="zoomControl" v-on:click="$emit('zoom-in')">
    +
  </button>
  <button id="minus" class="zoomControl" v-on:click="$emit('zoom-out')">
    -
  </button>

<!--  <button id="up" class="zoomControl" v-on:click="$emit('move-up')">
    u
  </button>
  <button id="down" class="zoomControl" v-on:click="$emit('move-down')">
    d
  </button>
  <button id="left" class="zoomControl" v-on:click="$emit('move-left')">
    l
  </button>
  <button id="right" class="zoomControl" v-on:click="$emit('move-right')">
    r
  </button>-->

</div>
</template>

<script>
export default {
  name: "ZoomControls",
}
</script>

<style scoped>
  .zoomControl{
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #2c3e50;
    color: whitesmoke;
    width: 2rem;
    height: 2rem;
  }
  #plus{
    margin-bottom: 0.25rem;
  }
  .zoomControls{
    display: flex;
    flex-direction: row;
    width: fit-content;
  }
</style>