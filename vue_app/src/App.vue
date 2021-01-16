<template>
  <span id="app">
  <Navbar></Navbar>

<!--    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <Sidebar></Sidebar>
  </span>
</template>

<script>
/*import HelloWorld from './components/HelloWorld.vue'*/
import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";

export default {
  name: 'App',
  components: {
    Sidebar,
    Navbar
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
  /*margin-top: 60px;*/
}
body{
  margin: 0;
}
</style>
