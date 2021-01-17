<template>
  <span id="app">
  <Navbar></Navbar>
    <div class="container">
      <Sidebar></Sidebar>
      <MainView></MainView>
    </div>
<!--    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  </span>
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
.container{
  display: flex;
  width: 100%;
  flex-direction: row;
}
</style>
