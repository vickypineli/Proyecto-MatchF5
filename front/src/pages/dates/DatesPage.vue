<template>
  <section class="box">
    <div class="dates">
      <h1>INSERTAR DATOS</h1>
    </div>
    <article id="container">
      <div class="selectfile">
        <label
          >ARCHIVO CODERS:
          <input
            type="file"
            id="file"
            ref="file"
            @change="onChangeFileCoders"
          />
          <!--<input @change="uploadFile" type="file" id="input_dom_element">-->
        </label>
      </div>

      <div class="selectfile">
        <label
          >ARCHIVO RECRUITERS:
          <input
            type="file"
            id="file"
            ref="file"
            @change="onChangeFileRecruiters"
          />
        </label>
      </div>
      <!-- <div class="selectfile">  
            <label>Nº REUNIONES:
              <input type="number" min="0" max="20"/>
            </label>
          </div> -->
      <button v-on:click="submitForm()">UPLOAD</button>
    </article>
  </section>
</template>

<script>
import * as fs from "fs";
var XLSX = require("xlsx");
XLSX.set_fs(fs);

/* load 'stream' for stream support */
import { Readable } from "stream";
XLSX.stream.set_readable(Readable);

export default {
  name: " Datos",
  data() {
    return {
      calculo: 0,
      coders: 0,
      recruiters: 0,
      huecos: 0,
    };
  },
  methods: {
    async onChangeFileRecruiters(event) {
      const file = event.target.files[0];
      const data = await file.arrayBuffer();
      const workbook = XLSX.read(data);
      const worksheet = workbook.Sheets["RECRUITERS"]; //Se especifica el nombre de la hoja
      //var csv = XLSX.utils.sheet_to_csv(worksheet)   //Si queremos CSV
      var json = XLSX.utils.sheet_to_json(worksheet); //Si queremos JSON
      console.log("esto es!:", json);
    },
    async onChangeFileCoders(event) {
      const file = event.target.files[0];
      const data = await file.arrayBuffer();
      const workbook = XLSX.read(data);
      const worksheet = workbook.Sheets["CODERS"]; //Se especifica el nombre de la hoja
      //var csv = XLSX.utils.sheet_to_csv(worksheet)   //Si queremos CSV
      var json = XLSX.utils.sheet_to_json(worksheet); //Si queremos JSON
      console.log("esto es!:", json);
    },
  },
};
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