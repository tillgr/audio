<template>
  <div class="MainView">
    <ZoomControls></ZoomControls>
    <div id= "graph" class="d3js-container">
    </div>
  </div>
</template>

<script>
import ZoomControls from "@/components/ZoomControls";
import soundData from "../../../AudioKPPython/coord/completeDict.json"
import * as d3 from "d3";

export default {
  name: "MainView",
  components:{
    ZoomControls
  },
  data() {
    return {
      dataSet: soundData,
      id: "",
      graph: Object,
      visibleCoordinates: {}
    };
  },
  methods: {
    init() {
      this.id = "graph";
      let xMinMax = d3.extent(this.dataSet.reduce(function(a,b) { return a.concat(b.x) }, []));
      let yMinMax = d3.extent(this.dataSet.reduce(function(a,b) { return a.concat(b.y) }, []));
      this.visibleCoordinates = { xMin: xMinMax[0] - 1,
                                  xMax: xMinMax[1] + 1,
                                  yMin: yMinMax[0] - 1,
                                  yMax: yMinMax[1] + 1};
    },
    drawGlyphGraph() {
      // create svg object of the graph in the correct DOM Object (this.id)

      // TODO get graph to fill whole height
      const graphWidth = document.getElementById("graph").clientWidth;
      const graphHeight = document.getElementById("graph").clientHeight;
      console.log(graphWidth, graphHeight);

      const svg = d3.select(`#${this.id}`)
          .append('svg')
          .attr('width', graphWidth)
          .attr('height', graphHeight)
          .attr('position', 'absolute');
      // scales
      const xScale = d3.scaleLinear()
          .domain([this.visibleCoordinates.xMin, this.visibleCoordinates.xMax])
          .range([0, graphWidth]);
      const yScale = d3.scaleLinear()
          .domain([this.visibleCoordinates.yMin, this.visibleCoordinates.yMax])
          .range([graphHeight, 0]);


      const graph = svg.append('g')

      graph.selectAll('circle').data(this.dataSet)
          .enter()
          .append('circle')
          .attr('class', 'circle')
          .attr('r', '5px')
          .attr('cx', d => xScale(d.x) )
          .attr('cy', d => yScale(d.y) )
    }
  },
  mounted() {
    this.init();
    this.drawGlyphGraph();


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