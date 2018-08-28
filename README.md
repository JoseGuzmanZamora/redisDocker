# RedisDocker
Laboratorio Redis para curso Programación 3

El laboratorio de utilización de redis a través de docker consta de la creación de una instancia de redis y llevar a cabo una conexión exitosa desde otra aplicación en Docker. En esta ocasión se realizó una pequeña base de datos de imágenes de personajes de Disney. Los datos posteriormente se consultan desde un script de Python que manda a desplegar la imagen en un archivo html. 

### Proceso Central
Como primer punto es necesario tener instalado Docker (respecto al sistema operativo en función). Posteriormente se descarga y se instancia la imagen oficial de Redis, disponible en https://hub.docker.com/_/redis/.
Antes de ingresar los comandos para el instanciamiento, debe asegurarse de crear un volumen para mantener los datos de manera persistente: 

```
$ docker volume create redis
```
La creación del volumen se puede verificar utilizando
```
$ docker volume ls 
```
y 
```
$ docker volume inspect redis
```
Después de asegurarse de haber creado el volumen, se introduce el siguiente comando para instanciar la imagen oficial de redis, es importante ponerle atención al nombre que se le da y los puertos que se habilitan.
```
$ docker run --name disneyCharacters -p 6379:6379 -v redis:/data -d redis redis-server --appendonly yes
```
Con los comandos puestos hasta el momento, ya está disponible el contenedor de redis para poder empezar a realizar cambios en la base de datos. Para empezar a hacer dichos cambios primero hay que revisar que el contenedor esté activo y saludable.
Para entrar al contenedor de redis ejecute lo siguiente:
```
$ docker exec -it disneyCharacters sh 
$ #redis-cli
```
Con esto ya puede entrar al ambiente de redis y comenzar a insertar valores o realizar queries. En este caso específico se insertaron 20 valores de prueba con sus respectivas imágenes
 1) "pluto"
 2) "aliens"
 3) "hudson"
 4) "cindirella"
 5) "pocahontas"
 6) "rapunzel"
 7) "belle"
 8) "elsa"
 9) "donald"
10) "minnie"
11) "buzz"
12) "goofy"
13) "woody"
14) "anna"
15) "aurora"
16) "mickey"
17) "daisy"
18) "ariel"
19) "christopher"
20) "mcqueen"

Después de haber insertado los datos necesarios, el siguiente paso es instanciar la imagen de la aplicación de python local, con el detalle de hacer el link con el contenedor de Redis. 
```
$ docker run -p 5000:5000 --link disneyCharacters:redis -d busquedadisney
```
Es importante tomar en cuenta habilitar el puerto para correr el programa y por supuesto, ponerle atención a los nombres utilizados para cada imagen y contenedor. Debe de esperar unos segundos y cuando el contenedor esté listo aparece lo siguiente en consola:
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
Esto se puede correr desde cualquier navegador asegurándose que la dirección esté correcta basado en la utilización de una máquina virtual o de una computadora común. 

## Imágenes de ejemplo
![alt text](https://github.com/JoseGuzmanZamora/redisDocker/blob/master/images/mickey.jpg)
![alt text](https://github.com/JoseGuzmanZamora/redisDocker/blob/master/images/woody.jpg)
![alt text](https://github.com/JoseGuzmanZamora/redisDocker/blob/master/images/rapunzel.jpg)
