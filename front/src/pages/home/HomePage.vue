<template>
<section class="box">
    <div class="home">
      <img alt="Vue logo" src="@/assets/img/logoF5.png" />
      <h2>Digital Talent Day </h2>
      <p>Match F5</p>
    </div>
    <router-link to="/match"><button>ENTER</button></router-link>
</section>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      info: {}
    }
  },
  mounted() {},
  methods: {}
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,300&family=Poppins&display=swap');
.box {
  margin: auto;
  width: 60vw;
  background: rgb(240, 237, 237);
  padding: 1.3em;
}
.home{
  width: 60vw;
  margin: auto;
}
img{
  width: 20vw;
}

h1 {
  font-family: poppins;
}
button{
  width: 20vw;
  background:rgb(213, 205, 199);
  border-radius: 15px;
  border-color: rgb(219, 196, 177);
  margin: auto;
  color:rgb(211, 73, 22);
  font-size: 1.1em;
  font-family: 'poppins';
}

</style>
