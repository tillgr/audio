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
      featureColorMinMax: {},
      audio: new Audio(),
      lastScroll: {}
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

      this.lastScroll = {x: 0, y: 0};

      this.featureColorMinMax = d3.extent(this.dataSet.reduce(function (a, b) {
        return a.concat(b.color);
      }, []));
      console.log(`init with ${this.featureColorMinMax}`);
    },
    drawGlyphGraph(stability=false, loudness=true, tonality=true, color=true, raspiness=true) {
      // create svg object of the graph in the correct DOM Object (this.id)
      let mVue = this;
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
          .attr('id', 'sample_svg')
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

      if (stability) {console.log("stability not shown")}
      /*glyphs.append('circle')
          .attr('class', 'baseCircle')
          .attr('r', `${glyphRadius}px`)
          .attr('cx', d => xScale(d.x))
          .attr('cy', d => yScale(d.y) + this.circleAttr(d).yShift * glyphRadius)
          .attr('fill', "none")
          .attr('stroke-dasharray', '0.5, 0.1')
          .attr('stroke-width', `${glyphRadius / 10.0}px`)
          .attr('stroke', "rgb(150,150,0)");*/
      if (loudness) {
        glyphs.append('circle')
            .attr('class', 'middleGlyphCircle')
            .attr('r', `${glyphRadius * 1.2}px`)
            .attr('cx', d => xScale(d.x))
            .attr('cy', d => yScale(d.y))
            .attr('fill', 'none')
            .attr('stroke-dasharray', function(d) {
              if (raspiness) {
                return mVue.circleAttr(d).strokeDasharray;
              }
            })
            .attr('stroke-width', `${glyphRadius / 15.0}px`)
            .attr('stroke', 'black')
            .attr('visibility', d => this.circleAttr(d).middle);
        glyphs.append('circle')
            .attr('class', 'outerGlyphCircle')
            .attr('r', `${glyphRadius * 1.4}px`)
            .attr('cx', d => xScale(d.x))
            .attr('cy', d => yScale(d.y))
            .attr('fill', 'none')
            .attr('stroke-dasharray', function(d) {
              if (raspiness) {
                return mVue.circleAttr(d).strokeDasharray;
              }
            })
            .attr('stroke-width', `${glyphRadius / 15.0}px`)
            .attr('stroke', 'black')
            .attr('visibility', d => this.circleAttr(d).outer);
      }

      glyphs.append('circle')
          .attr('class', 'innerGlyphCircle')
          .attr('r', `${glyphRadius}px`)
          .attr('cx', d => xScale(d.x))
          .attr('cy', d => yScale(d.y))
          // tonality and color
          .attr('fill', function(d) {
            let hue= 202;
            let sat = 80;
            let lum = 57;
            // let attr = this.circleAttr(d);
            if (tonality) {
              sat = mVue.circleAttr(d).innerSat;
            }
            if (color) {
              hue = mVue.circleAttr(d).innerHue;
              lum = mVue.circleAttr(d).innerLum;
            }
            return `hsl(${hue}, ${sat}%, ${lum}%)`;
          })
          // raspiness
          .attr('stroke-dasharray', function(d) {
            if (raspiness) {
              return mVue.circleAttr(d).strokeDasharray;
            }
          })
          .attr('stroke-width', `${glyphRadius / 15.0}px`)
          .attr('stroke', 'black')
          .attr('visibility', d => this.circleAttr(d).inner)
          .on("click", (d, i) => this.clickOnGlyph(d, i));

      // stbility
      if (stability) {
        glyphs.append('line')
            .attr('class', 'stability line')
            .attr('x1', d => (xScale(d.x) - glyphRadius *0.4))
            .attr('y1', d => (yScale(d.y) - glyphRadius *0.3))
            .attr('x2', d => (xScale(d.x) + glyphRadius *0.4 * mVue.circleAttr(d).stab.top))
            .attr('y2', d => (yScale(d.y) - glyphRadius *0.3))
            .attr('stroke-width', `${glyphRadius / 15.0}px`)
            .attr('stroke', 'black');
        glyphs.append('line')
            .attr('class', 'stability line')
            .attr('x1', d => (xScale(d.x) - glyphRadius *0.4))
            .attr('y1', d => yScale(d.y))
            .attr('x2', d => (xScale(d.x) + glyphRadius *0.4 * mVue.circleAttr(d).stab.middle))
            .attr('y2', d => yScale(d.y))
            .attr('stroke-width', `${glyphRadius / 15.0}px`)
            .attr('stroke', 'black');
        glyphs.append('line')
            .attr('class', 'stability line')
            .attr('x1', d => (xScale(d.x) - glyphRadius *0.4))
            .attr('y1', d => (yScale(d.y) + glyphRadius *0.3))
            .attr('x2', d => (xScale(d.x) + glyphRadius *0.4))
            .attr('y2', d => (yScale(d.y) + glyphRadius *0.3))
            .attr('stroke-width', `${glyphRadius / 15.0}px`)
            .attr('stroke', 'black');
      }
    },
    circleAttr(dataPoint) {
      let attr = {
        inner: 'hidden',
        middle: 'hidden',
        outer: 'hidden',
        innerSat: 100,
        innerHue: 202,
        innerLum: 57,
        strokeDasharray: '5, 0',
        stab: { top: 0, middle: 0}
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
        attr.innerSat = (dataPoint.tonality *2)**2 *80;//(dataPoint.tonality - 0.15) / 0.35 * 100;
      }
      // color
      let color = (dataPoint.color - this.featureColorMinMax[0])
          / (this.featureColorMinMax[1] - this.featureColorMinMax[0]);
      // attr.innerHue = normLocation * 60 + 170;
      if (color < 0.2) {
        attr.innerHue = 230;
      } else if (color < 0.4) {
        attr.innerHue = 210;
      } else if (color < 0.6) {
        attr.innerHue = 190;
      } else if (color < 0.8) {
        attr.innerHue = 125;
      } else {
        attr.innerHue = 110;
      }
      // attr.innerHue = 202 //(normLocation * 40) + 196 // hue values from 196 to 236 linearly
      attr.innerLum = (color * 30)+40;

      // stability
      if(dataPoint.stability > 0.4) {
        attr.stab.middle = 1
      }
      if(dataPoint.stability > 0.6) {
        attr.stab.top = 1
      }
      return attr

    },
    redrawGlyphGraph(stability, loudness, tonality, color, raspiness) {

      let canvas = document.getElementById("graph");
      let containerSVG = document.getElementsByClassName('d3js-container')[0];

      this.lastScroll.x = containerSVG.scrollLeft;
      this.lastScroll.y = containerSVG.scrollTop;

      canvas.removeChild(canvas.childNodes[0]);
      this.drawGlyphGraph(stability, loudness, tonality, color, raspiness);
      this.zoomToRecent();
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
      let svg = document.getElementById('sample_svg');
      let containerSVG = document.getElementsByClassName('d3js-container')[0];
      let scrollY = (containerSVG.scrollTop + containerSVG.clientHeight/(zoomFactor) * 0.25) / containerSVG.scrollHeight;
      let scrollX = (containerSVG.scrollLeft + containerSVG.clientWidth/(zoomFactor) * 0.25) / containerSVG.scrollWidth;

      console.log('=== adjust scroll ===')
      console.log('top: '+ containerSVG.scrollTop);
      console.log('scrollY: ' + scrollY);
      console.log('height: '+ containerSVG.scrollHeight);

      svg.style.transformOrigin = 'top left';
      svg.style.transform = 'scale(' + zoomFactor + ',' + zoomFactor + ')';

      // dum save of scrolling position
      this.lastScroll.y = scrollY*containerSVG.scrollHeight;
      this.lastScroll.x = scrollX*containerSVG.scrollWidth;

      containerSVG.scrollTop = scrollY*containerSVG.scrollHeight //+ zoomFactor * containerSVG.clientHeight * 0.25;
      containerSVG.scrollLeft = scrollX*containerSVG.scrollWidth //+ zoomFactor * containerSVG.clientWidth * 0.25;

      console.log('top: '+ containerSVG.scrollTop);
      console.log(containerSVG.scrollLeft);
      console.log('height: '+ containerSVG.scrollHeight);
    },
    zoomOut(){
      zoomFactor = zoomFactor - 0.5;
      let svg = document.getElementById('sample_svg');
      let containerSVG = document.getElementsByClassName('d3js-container')[0];
      let scrollY = (containerSVG.scrollTop - containerSVG.clientHeight/(zoomFactor) * 0.25) / containerSVG.scrollHeight;
      let scrollX = (containerSVG.scrollLeft - containerSVG.clientWidth/(zoomFactor) *0.25) / containerSVG.scrollWidth;

      console.log('=== adjust scroll ===')
      console.log('top: '+ containerSVG.scrollTop);
      console.log('height: '+ containerSVG.scrollHeight);

      svg.style.transformOrigin = 'top left';
      svg.style.transform = 'scale(' + zoomFactor + ',' + zoomFactor + ')';

      // dum save of scrolling position
      this.lastScroll.y = scrollY*containerSVG.scrollHeight;
      this.lastScroll.x = scrollX*containerSVG.scrollWidth;

      containerSVG.scrollTop = scrollY*containerSVG.scrollHeight;
      containerSVG.scrollLeft = scrollX*containerSVG.scrollWidth;

      console.log('top: '+ containerSVG.scrollTop);
      console.log('height: '+ containerSVG.scrollHeight);
    },
    zoomToRecent() {
      let svg = document.getElementById('sample_svg');
      let containerSVG = document.getElementsByClassName('d3js-container')[0];

      svg.style.transformOrigin = 'top left';
      svg.style.transform = 'scale(' + zoomFactor + ',' + zoomFactor + ')';

      containerSVG.scrollTop = this.lastScroll.y;
      containerSVG.scrollLeft = this.lastScroll.x;
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
  float: right;
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