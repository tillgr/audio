<template>
  <div class="MainView">
    <ZoomControls
        v-on:zoom-in="zoomIn()"
        v-on:zoom-out="zoomOut()">
<!--        v-on:move-up="move('up')"
        v-on:move-down="move('down')"
        v-on:move-left="move('left')"
        v-on:move-right="move('right')">-->
    </ZoomControls>
    <div id="graph" class="d3js-container"></div>
  </div>
</template>

<script>
import ZoomControls from "@/components/ZoomControls";
import soundData from "../../../AudioKPPython/coord/completeDict.json"
import * as d3 from "d3";

let zoomFactor = 1;
export default {
  name: "MainView",
  components: {
    ZoomControls
  },
  data() {
    return {
      dataSet: soundData,
      id: "",
      graph: Object,
      graphDimensions: {},
      visibleCoordinates: {},
      startingDimensions: {},
      audio: new Audio()
    };
  },
  methods: {
    init() {
      this.id = "graph";
      let xMinMax = d3.extent(this.dataSet.reduce(function (a, b) {
        return a.concat(b.x)
      }, []));
      let yMinMax = d3.extent(this.dataSet.reduce(function (a, b) {
        return a.concat(b.y)
      }, []));
      this.visibleCoordinates = {
        xMin: xMinMax[0] - 1,
        xMax: xMinMax[1] + 1,
        yMin: yMinMax[0] - 1,
        yMax: yMinMax[1] + 1
      };
      this.startingDimensions = this.visibleCoordinates;
    },
    drawGlyphGraph() {
      // create svg object of the graph in the correct DOM Object (this.id)
      // TODO get graph to fill whole height
      let headerHeight = document.getElementById("header").clientHeight;


      this.graphDimensions = {
        width: document.getElementById("graph").clientWidth,
        height: window.innerHeight - headerHeight - 25
      }
      console.log(this.graphDimensions.width, this.graphDimensions.height);

      /*.attr('width', this.graphDimensions.width)
      .attr('height', this.graphDimensions.height)*/

      const svg = d3.select(`#${this.id}`)
          .append('svg')
          .attr('viewBox', '0, 0,' + this.graphDimensions.width + ', ' + this.graphDimensions.height)
          .attr('width', this.graphDimensions.width)
          .attr('height', this.graphDimensions.height)
          /*.attr('width', 100)
          .attr('height', 100)*/
          .attr('position', 'absolute');
      // scales
      const xScale = d3.scaleLinear()
          .domain([this.visibleCoordinates.xMin, this.visibleCoordinates.xMax])
          .range([0, this.graphDimensions.width]);
      const yScale = d3.scaleLinear()
          .domain([this.visibleCoordinates.yMin, this.visibleCoordinates.yMax])
          .range([this.graphDimensions.height, 0]);


      const graph = svg.append('g')


      // set values for Glyphs
      const scalingFactor = (this.startingDimensions.xMax - this.startingDimensions.xMin) / (this.visibleCoordinates.xMax - this.visibleCoordinates.xMin);
      let glyphRadius = 2.0 * scalingFactor


      let glyphs = graph.selectAll('g').data(this.dataSet).enter();

      glyphs.append('circle')
          .attr('class', 'middleGlyphCircle')
          .attr('r', `${glyphRadius * 1.15}px`)
          .attr('cx', d => xScale(d.x))
          .attr('cy', d => yScale(d.y))
          .attr('fill', 'none')
          .attr('stroke-dasharray', d => this.circleAttr(d).strokeDasharray)
          .attr('stroke-width', `${glyphRadius / 15.0}px`)
          .attr('stroke', 'black')
          .attr('visibility', d => this.circleAttr(d).middle);
      glyphs.append('circle')
          .attr('class', 'outerGlyphCircle')
          .attr('r', `${glyphRadius * 1.3}px`)
          .attr('cx', d => xScale(d.x))
          .attr('cy', d => yScale(d.y))
          .attr('fill', 'none')
          .attr('stroke-dasharray', d => this.circleAttr(d).strokeDasharray)
          .attr('stroke-width', `${glyphRadius / 15.0}px`)
          .attr('stroke', 'black')
          .attr('visibility', d => this.circleAttr(d).outer);
      glyphs.append('circle')
          .attr('class', 'innerGlyphCircle')
          .attr('r', `${glyphRadius}px`)
          .attr('cx', d => xScale(d.x))
          .attr('cy', d => yScale(d.y))
          .attr('fill', d => this.circleAttr(d).innerFill)
          .attr('stroke-dasharray', d => this.circleAttr(d).strokeDasharray)
          .attr('stroke-width', `${glyphRadius / 15.0}px`)
          .attr('stroke', 'black')
          .attr('visibility', d => this.circleAttr(d).inner)
          .on("click", (d, i) => this.clickOnGlyph(d, i));
    },
    circleAttr(dataPoint) {
      let attr = {
        inner: 'hidden',
        middle: 'hidden',
        outer: 'hidden',
        innerFill: 'none',
        strokeDasharray: '5, 0'
      }
      // loudness
      if (dataPoint.loudness > 0.0) {
        attr.inner = 'visible';
      }
      if (dataPoint.loudness >= 0.33) {
        attr.middle = 'visible';
      }
      if (dataPoint.loudness >= 0.66) {
        attr.outer = 'visible';
      }
      // raspiness
      if (0.06 <= dataPoint.raspiness <= 0.12) {
        attr.strokeDasharray = '1, 0.1';
      } else if (dataPoint.raspiness > 0.12) {
        attr.strokeDasharray = '0.5, 0.1';
      }
      // tonality
      if (0.0 <= dataPoint.tonality <= 1.0) {
        const saturation = (dataPoint.tonality - 0.2) / 0.3 * 100;
        attr.innerFill = `hsl(202, ${saturation}%, 57%)`;
      }
      return attr

    },
    redrawGlyphGraph() {
      let canvas = document.getElementById("graph");
      canvas.removeChild(canvas.childNodes[0]);
      this.drawGlyphGraph();
    },

    clickOnGlyph(domObject, dataPoint) {
      this.audio.pause();
      console.log(`clicked on ${dataPoint.name}`);
      this.audio.src = require(`../../../../EXTRACT_FSDKaggle2018.audio_train/${dataPoint.name}.wav`);
      console.log(this.audio);
      this.audio.play();
    },
    /*zoom(direction) {
      let  diffX = (this.visibleCoordinates.xMax - this.visibleCoordinates.xMin)  * direction;
      let  diffY = (this.visibleCoordinates.yMax - this.visibleCoordinates.yMin)  * direction;
      this.visibleCoordinates = { xMin: this.visibleCoordinates.xMin + diffX,
                                  xMax: this.visibleCoordinates.xMax - diffX,
                                  yMin: this.visibleCoordinates.yMin + diffY,
                                  yMax: this.visibleCoordinates.yMax - diffY };
      /!*this.graphDimensions.width += this.graphDimensions.width * direction;
      this.graphDimensions.height += this.graphDimensions.height * direction;*!/
      this.redrawGlyphGraph();
    },
    move(directionString) {
      // console.log("key pressed up");
      let  diffX = (this.visibleCoordinates.xMax - this.visibleCoordinates.xMin) *0.2;
      let  diffY = (this.visibleCoordinates.yMax - this.visibleCoordinates.yMin) *0.2;
      switch(directionString) {
        case "up":
          this.visibleCoordinates.yMin += diffY;
          this.visibleCoordinates.yMax += diffY;
          break;
        case "down":
          this.visibleCoordinates.yMin -= diffY;
          this.visibleCoordinates.yMax -= diffY;
          break;
        case "left":
          this.visibleCoordinates.xMin -= diffX;
          this.visibleCoordinates.xMax -= diffX;
          break;
        case "right":
          this.visibleCoordinates.xMin += diffX;
          this.visibleCoordinates.xMax += diffX;
          break;
      }
      this.redrawGlyphGraph();
    }*/
    zoomIn() {
      zoomFactor = zoomFactor + 0.5;
      let svg = document.getElementsByTagName('svg')[1];
      let containerSVG = document.getElementsByClassName('d3js-container')[0];
      let scrollY = (containerSVG.scrollTop + containerSVG.clientHeight/(zoomFactor) * 0.25) / containerSVG.scrollHeight;
      let scrollX = (containerSVG.scrollLeft + containerSVG.clientWidth/(zoomFactor) * 0.25) / containerSVG.scrollWidth;

      console.log('=== adjust scroll ===')
      console.log('top: '+ containerSVG.scrollTop);
      console.log('scrollY: ' + scrollY);
      console.log('height: '+ containerSVG.scrollHeight);

      svg.style.transformOrigin = 'top left';
      svg.style.transform = 'scale(' + zoomFactor + ',' + zoomFactor + ')';


      containerSVG.scrollTop = scrollY*containerSVG.scrollHeight //+ zoomFactor * containerSVG.clientHeight * 0.25;
      containerSVG.scrollLeft = scrollX*containerSVG.scrollWidth //+ zoomFactor * containerSVG.clientWidth * 0.25;

      console.log('top: '+ containerSVG.scrollTop);
      console.log(containerSVG.scrollLeft);
      console.log('height: '+ containerSVG.scrollHeight);
    },
    zoomOut(){
      zoomFactor = zoomFactor - 0.5;
      let svg = document.getElementsByTagName('svg')[1];
      let containerSVG = document.getElementsByClassName('d3js-container')[0];
      let scrollY = (containerSVG.scrollTop - containerSVG.clientHeight/(zoomFactor) * 0.25) / containerSVG.scrollHeight;
      let scrollX = (containerSVG.scrollLeft - containerSVG.clientWidth/(zoomFactor) *0.25) / containerSVG.scrollWidth;

      console.log('=== adjust scroll ===')
      console.log('top: '+ containerSVG.scrollTop);
      console.log('height: '+ containerSVG.scrollHeight);

      svg.style.transformOrigin = 'top left';
      svg.style.transform = 'scale(' + zoomFactor + ',' + zoomFactor + ')';


      containerSVG.scrollTop = scrollY*containerSVG.scrollHeight;
      containerSVG.scrollLeft = scrollX*containerSVG.scrollWidth;

      console.log('top: '+ containerSVG.scrollTop);
      console.log('height: '+ containerSVG.scrollHeight);

    }
  },
  mounted() {
    this.init();
    this.drawGlyphGraph();
  }
}
</script>

<style scoped>
.MainView {

  width: 86%;
  height: available;
  right: 0;
}

.zoomControls {
  /*float: right;*/
  /*margin-right: 0.5rem;
  margin-top: 0.5rem;*/
  z-index: 3;
  position: absolute;
  right: 2vw;
  top: 4vw;
}

.d3js-container {
  width: 100%;
  height: 100%;
  display: block;
  /*background-color: #911F82;*/
  align-content: start;
  justify-content: start;
  overflow: scroll;
}

</style>