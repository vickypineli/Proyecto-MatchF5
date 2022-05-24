# Aplicación MatchF5(front)

## Configuración del proyecto

```
npm install

```

## Instalación librería xlsx

```
npm install xlsx

```

### Ejecutar servidor de desarrollo

```
npm run serve
```

### Generar archivos de distribución

```
npm run build
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/)

### JSON esperado por el enpoint POST a api/prematch

El json es un diccionario con dos claves (coders y recruiters) las cuales
contienen una lista de diccionarios con los coder y recruiters respectivamente.

{"coders": [{coder},{coder},{coder}, ...], "recruiters": [{recruiter},{recruiter},{recruiter}, ...]}

cada diccionario de coder tendrá el siguiente aspecto:

{
"NOMBRE": el nombre del coder,
"APELLIDOS": uno o mas apellidos del coder,
"TELEFONO": el telefono de contacto del coder,
"MAIL": el e-mail de contacto del coder,
"PROMOCION": el identificador de la promoción del coder (ej.: BIO para Bilbao),
"L-BILBAO": "x",
"L-BARCELONA: "",
"S-PYTHON": "x",
"S-JAVASCRIPT": ""
}
donde los datos de clave L- son localizaciones de las cuales las que contienen "x" son
aquellas seleccionadas como lugares de trabajo deseados y los datos de clave S- son skills
de los cuales el coder posee aquellos que contienen "x"

además cada diccionario de recruiter tendra el siguiente aspecto:

{
"EMPRESA": el nombre de la empresa a la que el recruiter representa,
"NOMBRE DEL RECRUITER": el nombre del recruiter que asiste a la reunión,
"EMAIL": el e-mail de contacto,
"CARGO": el cargo del recruiter dentro de la empresa que representa,
"L-BILBAO": "x",
"L-BARCELONA: "",
"S-PYTHON": "x",
"S-JAVASCRIPT": "",
"10:10": "x",
"10:20": "x",
"13:00": "x",
"13:30": "x"
}

donde los datos de clave L- son localizaciones de las cuales las que contienen "x" son
aquellas seleccionadas como localizaciones en los que necesita contratar el recruiter
y los datos de clave S- son skills de los cuales aquellos que contienen "x" son los que
el recruiter necesita. Finalmente el diccionario contiene una serie de claves que son
horas en formato de 24h y aquellas marcadas con "x" son aquellas a las que el recruiter
puede asistir.
