<template>
  <div class="MainView">
    <ZoomControls></ZoomControls>
    <div class="d3js-container">
      hier kommt der graph rein
    </div>
  </div>
</template>

<script>
import ZoomControls from "@/components/ZoomControls";

export default {
  name: "MainView",
  components:{
    ZoomControls
  }
}
</script>

<style scoped>
  .MainView{
    width: 86%;
    height: available;
    right: 0;
  }
  .zoomControls{
    float: right;
    margin-right: 0.5rem;
    margin-top: 0.5rem;
  }
  .d3js-container{
    width: 100%;
    height: 100%;
    display: block;
    background-color: #911F82;
  }
</style>