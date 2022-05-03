<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/logo.png" />
    <h1>{{ info.app_name }}</h1>
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
h1 {
  font-style: italic;
}
</style>
