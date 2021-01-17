<template>
  <div class="sidebar">
    <div id="glyph-container">
      here goes the glyph
    </div>
    <div id="v-model-radiobutton">
      <span>
        <input type="radio" id="Stability" value="Stability" v-model="picked"/>
        <label for="Stability">Stability</label>
      </span>
      <span>
        <input type="radio" id="Loudness" value="Loudness" v-model="picked"/>
        <label for="Loudness">Loudness</label>
      </span>
      <span>
        <input type="radio" id="Tonality" value="Tonality" v-model="picked"/>
        <label for="Tonality">Tonality</label>
      </span>
      <span>
        <input type="radio" id="Raspiness" value="Raspiness" v-model="picked"/>
        <label for="Raspiness">Raspiness</label>
      </span>
      <span id="container-color">
        <span>
          <input type="radio" id="Color" value="Color" v-model="picked"/>
        <label for="Color">Color</label>
        </span>
        <svg version="1.1" id="LMH" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
             viewBox="0 0 269.8 269.8" style="enable-background:new 0 0 269.8 269.8;" xml:space="preserve"
        >
        <rect x="11.2" y="11.2" class="st0" width="247.5" height="247.5"/>
        <g>
          <g>
            <circle class="st1" cx="175.7" cy="175.8" r="83"/>
            <circle class="st2" cx="94.2" cy="175.8" r="83"/>
          </g>
          <circle class="st3" cx="134.9" cy="94.2" r="83"/>
        </g>
        </svg>

      </span>
      <span>Picked: {{ picked }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Sidebar",

  data() {
    return {
      picked: ''
    }
  }

}
</script>

<style scoped>
.sidebar {
  width: 14%;
  display: block;
  background-color: lightgray;
  left: 0;
}

#v-model-radiobutton {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

#glyph-container {
  display: flex;
  width: 100%;
  height: 12rem;
  background-color: #42b983;
  margin-bottom: 1rem;
  justify-content: center;
  align-items: center;
}

#container-color {
  margin-top: 1rem;
  padding-top: 0.5rem;
  border-top: solid #42b983 2px;
  width: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}

/*LMH*/
#LMH{
  width: 80%;
  align-self: center;
}
.st0 {
  display: none;
  fill: #009640;
}

.st1 {
  opacity: 0.51;
  fill: #2DABE3;
}

.st2 {
  opacity: 0.51;
  fill: #911F82;
}

.st3 {
  opacity: 0.51;
  fill: #E79258;
}
</style>