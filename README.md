# video-detection-sipecam

## Descripción

Script para detectar videos con animales.

## Preparación

Se espera que el archivo del modelo esté en un directorio `model` dentro de este repositorio.

## Pasos

1. `main.py`: Corre el modelo megadetector sobre el directorio de los videos. Se ejecuta dentro del contenedor con el comando `python main.py`.

## Variables de ambiente

- DATA_DIRECTORY: Directorio donde están alojados los videos.
- FRAMES_DIRECTORY: Directorio temporal donde se obtienen los frames de los videos.
- MEGADETECTOR_MODEL: Directorio del modelo.
- WITH_ANIMAL_DIRECTORY: Directorio donde se copian los videos que se detectan con animales.
- WITHOUT_ANIMAL_DIRECTORY: Directorio donde se copian los videos que no se detectan con animales.

## Dockerfile

Para correr estos scripts en el contenedor de docker, se deben seguir los siguientes pasos:

Countruir la imagen con lo necesario para correr los scripts usando el siguiente comando

```shell
    docker build -t megadetector-video:1.0 .
```

Verificar que se construyó correctamente la imagen con el comando

``` shell
  docker images
```

Ejecutar el contenedor especificando el path a las imagenes, el path al archivo de salidas y el path del modelo con el siguiente comando

``` shell
  docker run -it -v /path/to/data/:/data/ -v /home/promero/video-detection-sipecam/with_animal/:/with_animal/ -v /home/promero/video-detection-sipecam/model.pt:/model/model.pt megadetector-video:1.0 bash
```

docker run -it -v /LUSTRE_IMAGENES/:/data/ -v /path/to/with_animal/:/with_animal/ -v /path/to/model.pt:/model/model.pt megadetector-video:1.0 bash

Seguir los pasos.