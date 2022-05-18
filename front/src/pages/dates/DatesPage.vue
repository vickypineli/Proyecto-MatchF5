<template>  
  <div class="dates">
    <h1> DATOS</h1>
  </div>
  <section id="container">
    <div>
        <label for="">Archivo Recruiters</label>
        <input type="number" v-model="recruiters"/>
    </div>
    <div>
    <label for="">Archivo Coders</label>
    <input type="number" v-model="coders"/>
    </div>
    <div>
    <label for="">Nº de reuniones de la jornada</label>
    <input type="number" v-model="huecos"/>
    </div>
</section>

</template>

<script>
export default {
  name: " Datos",
    data(){
      return {
        calculo: 0,
        coders: 0,
        recruiters: 0,
        huecos: 0,
      }
    },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,300&family=Poppins&display=swap');
#container {
  width: 30vh;
  margin: auto;
  display: flex;
  flex-direction: column;
  padding: 50px;
  background: rgb(233, 225, 225);
}
#result{
  color: crimson;
}
</style>
