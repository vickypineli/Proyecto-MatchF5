# Aplicación semilla (backend)

## Puesta en marcha

(Esta aplicación supone que el comando `python` ejecuta al menos la versión `3.8`. En caso de que no fuera así, hay que tenerlo en cuenta en todos los comandos que uticen `python` y modificarlos en consecuencia).

1. Instalar los paquetes necesarios

    `python -m pip install --user -r requirements.txt`

2. Ejecutar los tests

    `python -m pytest`

3. Generar los datos iniciales

    `python scripts/initial_data.py`

4. Ejecutar la aplicación

    `python app.py`
