<template>
  <div class="sidebar">
    <div id="glyph-container">
      here goes the glyph
    </div>
    <div id="v-model-checkboxes">
      <p>
        <input type="checkbox" id="Stability" value="Stability" v-model="checked.stability"
               v-on:change="$emit('checkboxes-changed', checked)" class="check-input"/>
        <label for="Stability">Stability</label>
      </p>
      <p>
        <input type="checkbox" id="Loudness" value="Loudness" v-model="checked.loudness"
               v-on:change="$emit('checkboxes-changed', checked)" class="check-input"/>
        <label for="Loudness">Loudness</label>
      </p>
      <p>
        <input type="checkbox" id="Tonality" value="Tonality" v-model="checked.tonality"
               v-on:change="$emit('checkboxes-changed', checked)" class="check-input"/>
        <label for="Tonality">Tonality</label>
      </p>
      <p>
        <input type="checkbox" id="Raspiness" value="Raspiness" v-model="checked.raspiness"
               v-on:change="$emit('checkboxes-changed', checked)" class="check-input"/>
        <label for="Raspiness">Raspiness</label>
      </p>
      <span id="container-color">
        <p>
          <input type="checkbox" id="Color" value="Color" v-model="checked.color"
                 v-on:change="$emit('checkboxes-changed', checked)" class="check-input"/>
        <label for="Color">Color</label>
        </p>
        <svg version="1.1" id="LMH" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
             viewBox="0 0 269.8 269.8" style="enable-background:new 0 0 269.8 269.8;" xml:space="preserve"
        >
        <rect x="11.2" y="11.2" class="st0" width="247.5" height="247.5"/>
        <g>
          <g>
            <circle class="st1" cx="134.9" cy="175.8" r="83"/>
<!--            <circle class="st2" cx="94.2" cy="175.8" r="83"/>-->
          </g>
          <circle class="st3" cx="134.9" cy="94.2" r="83"/>
        </g>
        </svg>

      </span>
<!--      <span>Picked: {{ picked }}</span>-->
    </div>
  </div>
</template>

<script>
export default {
  name: "Sidebar",

  data() {
    return {
      checked: {
        stability: true,
        loudness: true,
        tonality: true,
        color: true,
        raspiness: true
      }
    }
  },
  methods: {
    printcheck(object) {
      console.log("something has changed");
      console.log(object);
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
  display: block;
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
  opacity: 0.65;
  fill: #141e66;
}

.st2 {
  opacity: 0.51;
  fill: #911F82;
}

.st3 {
  opacity: 0.65;
  fill: #e6dd32;
}
</style>