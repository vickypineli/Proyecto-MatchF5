<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/F5logo.png" />
    <h2>Digital Talent Day </h2>
    <p>Match F5</p>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      info: {}
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/info')
      this.info = await response.json()
    }
  }


}
</script>

<style scoped>

.home{
  width: 60vw;
  margin: auto;
  padding: 50px;
}
img{
  width: 10vw;
}

h1 {
  font-style: italic;
}

</style>
