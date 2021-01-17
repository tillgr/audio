<template>
<div class="zoomControls">
  <div id="plus" class="zoomControl">
    +
  </div>
  <div id="minus" class="zoomControl">
    -
  </div>
</div>
</template>

<script>
export default {
  name: "ZoomControls"
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
    flex-direction: column;
    width: fit-content;
  }
</style>