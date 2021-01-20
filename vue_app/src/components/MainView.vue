<template>
  <div class="MainView">
    <ZoomControls></ZoomControls>
    <div id= "graph" class="d3js-container">
    </div>
  </div>
</template>

<script>
import ZoomControls from "@/components/ZoomControls";
import GlyphGraph from "@/glyphGraph";
import soundData from "../../../AudioKPPython/coord/completeDict.json"

export default {
  name: "MainView",
  components:{
    ZoomControls
  },
  data() {
    return {
      dataSet: soundData
    };
  },
  methods: {
  },
  mounted() {
    console.log(this.dataSet);
    /*const data = [{x: 200, y: 400},
                  {x: 100, y: 200},
                  {x: 600, y: 400},
                  {x: 0.9, y: 0.5}];*/
    const graph = new GlyphGraph(this.dataSet, "graph");
    graph.drawGlyphGraph();


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