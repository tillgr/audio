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
// import * as d3 from "d3";

export default {
  name: "MainView",
  components:{
    ZoomControls
  },

  mounted() {

    const data = [{x: 200, y: 400},
                  {x: 100, y: 200},
                  {x: 600, y: 400},
                  {x: 0.9, y: 0.5}];
    const graph = new GlyphGraph(data, "graph");
    graph.drawGlyphGraph();

    /*const dataSet = [{x: 0.5, y: 0.5},
      {x: 0.1, y: 0.9},
      {x: 2.5, y: 80},
      {x: 0.9, y: 0.5}];

    const containerWidth = document.getElementById("graph").clientWidth;
    const containerHeight = document.getElementById("graph").clientHeight;

    const svg = d3.select(`#graph`)
        .append('svg')
        .attr('width', containerWidth)
        .attr('height', containerHeight)
    const graph = svg.append('g')

    graph.selectAll('circle').data(dataSet)
        .enter()
        .append('circle')
        .attr('class', 'circle')
        .attr('r', '20px')
        .attr('cx', d => d.x )
        .attr('cy', d => d.y )*/
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