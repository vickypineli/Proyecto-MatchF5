<template>
  <section class="box">
    <div class="data">
      <h1>INSERTAR DATOS</h1>
    </div>
    <article id="container">
      <div class="selectfile">
        <label
          >SUBIR ARCHIVO:
          <input type="file" @change="onChangeFile" />
        </label>
      </div>

      <button @click="sendData">UPLOAD</button>
    </article>
  </section>
  <p v-show="checkSpreadsheetName===true">Verificar el nombre de las hojas sea en mayúsculas</p>
</template>

<script>
import * as fs from "fs"
var XLSX = require("xlsx")
XLSX.set_fs(fs)

/* load 'stream' for stream support */
import { Readable } from "stream"
XLSX.stream.set_readable(Readable)

export default {
  name: "MatchPage",
  data() {
    return {
      calculo: 0,
      coders: 0,
      recruiters: 0,
      huecos: 0,
      jsonCoders:'',
      jsonRecruiters:'',
      checkSpreadsheetName:''
    }
  },
  methods: {
    async onChangeFile(event) {
      const file = event.target.files[0]
      const data = await file.arrayBuffer()
      const workbook = XLSX.read(data)
      const worksheetCoders = workbook.Sheets["CODERS"]
      const worksheetRecruiters = workbook.Sheets["RECRUITERS"]
  
      this.jsonCoders = XLSX.utils.sheet_to_json(worksheetCoders)
      this.jsonRecruiters = XLSX.utils.sheet_to_json(worksheetRecruiters)
      console.log("Coders", this.jsonCoders)
      console.log("Recruiters", this.jsonRecruiters)
    },

    checkDataIfIsComplete(){
      if (this.jsonRecruiters.length === 0 || this.jsonCoders.length === 0){
          this.checkSpreadsheetName=true
          return false
        }
      else {return true}
      },
      
    sendData(){
      if (this.checkDataIfIsComplete()===true){
          const settings={
            method:"POST",
            body:{CODERS:this.jsonCoders,RECRUITERS:this.jsonRecruiters},
            headers:{"Content-Type":"application/json"}
          }
          // let response = await fetch("http://localhost:5000/api/match", settings)
          console.log("Response", settings)
      }
    }
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,300&family=Poppins&display=swap");
.box {
  margin: auto;
  width: 80vw;
  background: rgb(240, 237, 237);
  padding: 1.1em;
}
#container {
  width: 70vw;
  margin: auto;
  display: flex;
  flex-direction: column;
}
.selectfile {
  display: flex;
  flex-direction: column;
}
input {
  width: 60vw;
  margin: 10px;
  padding: 20px;
  background: rgb(215, 211, 211);
  color: #2c3e50;
}
label {
  margin: 10px;
  font-size: 1.5em;
  color: rgb(215, 66, 12);
  font-family: "Bebas Neue", cursive;
  text-align: left;
}
button {
  width: 30vw;
  background: orangered;
  border-radius: 15px;
  border-color: rgb(237, 142, 74);
  margin: auto;
  color: white;
  font-size: 1.2em;
  font-family: "poppins";
}
</style>