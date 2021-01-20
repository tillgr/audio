import * as d3 from "d3";

export default class GlyphGraph {
  constructor(dataSet, id) {
    this.dataSet = dataSet;
    this.id = id;

    // set basic view coordinates so all data points are show
    let xMinMax = d3.extent(dataSet.reduce(function(a,b) { return a.concat(b.x) }, []));
    let yMinMax = d3.extent(dataSet.reduce(function(a,b) { return a.concat(b.y) }, []));
    this.visibleCoordinates = { xMin: xMinMax[0] - 10,
                                xMax: xMinMax[1] + 10,
                                yMin: yMinMax[0] - 10,
                                yMax: yMinMax[1] + 10};
  }

  drawGlyphGraph() {
    // create svg object of the graph in the correct DOM Object (this.id)

    // TODO get graph to fill whole height
    const graphWidth = document.getElementById(this.id).clientWidth;
    const graphHeight = document.getElementById(this.id).clientHeight;
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

  static createGlyph(dataPoint) {
    // create svg for single glyph from dataPoint
    return dataPoint;
  }
}