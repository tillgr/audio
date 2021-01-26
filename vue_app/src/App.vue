<template>
  <div id="app">
  <Navbar ></Navbar>
    <div class="container" id="mainContainer">
      <Sidebar ></Sidebar>
      <MainView ref="mainView"></MainView>
    </div>
<!--    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  </div>
</template>

<script>
/*import HelloWorld from './components/HelloWorld.vue'*/
import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";
import MainView from "@/components/MainView";

export default {
  name: 'App',
  components: {
    Sidebar,
    Navbar,
    MainView
  },
  created() {
    window.addEventListener("resize", this.resizeContainer);
  },
  destroyed() {
    window.removeEventListener("resize", this.resizeContainer);
  },
  methods: {
    resizeContainer() {
      let headerHeight = document.getElementById("header").clientHeight;
      let container = document.getElementById("mainContainer");

      console.log(`container height on resize: ${container.style.height}`);
      console.log(`header height on resize: ${headerHeight}`);

      container.style.height = `${window.innerHeight - headerHeight}px`;
      this.$refs.mainView.redrawGlyphGraph();
    }
  }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  /*margin-top: 60px;*/
}

body{
  margin: 0;
}

.container{
  display: flex;
  width: 100%;
  height: 100vh;
  flex-direction: row;
}
</style>
