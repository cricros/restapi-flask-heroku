# RESTAPI DESDE UNA WEBAPI


## Requirmiento
Se realiza el desarrolla de una RESTAPI la cual consume una de las siguientes webapi: 
<br>
>PokeAPI - https://pokeapi.co/ <br>
>MarvelAPI - https://developer.marvel.com/ <br>
>COVIDAPI - https://covidtracking.com/data/api <br>

Una vez generada esta RESTAPI, se deberá probar de manera local desde el navegador, algún RESTClient, y ser deployada en algún servidor, o, nube de su preferencia. 

## Tecnologías utilizadas
Para comenzar hemos de aclarar que la API seleccionada para este reto técnico fue **POKEAPI**, esto debido a su facilidad de consumo, además de que la documentación con la cual cuenta la API está bastante completa, y fácil de entender. Dandonos una idea de todas las peticiones que podemos solicitar con esta misma. 
Con respecto al resto de tecnologías que se enlistan a continuación, hemos de decir que se optó por estás, por en base a dos criterios (en el siguiente punto se dará una explicación mas a detalle sobre otros puntos que se consideraron), los cuales son los siguientes: *Facilidad de uso, y  documentación sobre la misma en internet.*  En el siguiente punto se tendrá una explicación mas a detalle
- ###### PokeAPI
- ###### Python
- ###### Flask
- ###### Postman
- ###### Heroku
- ###### Github
## Justificación
Como se menciona en el párrafo anterior. Se tomaron en cuanta diveros criterios para la elección de las tecnologías utilizadas, las cuales enlistaremos a continuación: 
- ###### Experiencia del desarrollador
En este punto, decidí tomar en cuenta mi experiencia en el desarrollo de APIS en general, y con esto, al tener experiencia previa puede bosquejar de una mejor manera las opciones con las que contaba para realizar el reto. Mucha de mi experiencia ha sido con Django y Flask, pero dado la facilidad del mismo (de la RESTAPI), opté por Flask, ya que su manejo para este tipo de APIs es mucho más fácil y con una mejor compresión con respecto al código. Además de que al haber estado como TESTER de backend, fue mucho más fácil poder decidir el RESTClient para poder probar la API, la cual fue postman. 
- ###### Documentación de cada herramienta
Otro punto importante que tomé en consideración para realizar la elección sobre que herramienta utilizaría (en especial el framework), opté porque su documentación fuera clara y extensa. 
- ###### Gratuita
Dado que por ahora es un desarrollo pequeño, opté por técnologías que fuera de uso gratuito para así evitar gastos que se pudieran considerar "innesarios". Esto va mas orientado en donde se realizó el deployeo de la RESTAPI. 

## Endpoints generados

Se generaron 4 endpoints que son complatibles con un RESTClient, las peticiones que  soportan son tanto **GET** como **POST**. 

##### Para las solicitudes GET
Las solicitudes de tipo son compatibles tanto en el localhost como en Heroku. Además, de que pueden ser realizadas desde el mismo navegador como desde Postman. 
La estructura que debes seguir, para poder dicha petición es la siguiente
>http://127.0.0.1:5000/[endpoint]/[parametrosolicitado]<br>
	ejem: http://127.0.0.1:5000/pokedex/kanto -> retorna una respuesta JSON <br>
>https://rest-api-flask-deploy.herokuapp.com/pokedex<br>
	ejem: https://rest-api-flask-deploy.herokuapp.com/pokedex/kanto -> retorna una respuesta JSON 

##### Para las solicitudes POST
Las solicitudes de tipo son compatibles tanto en el localhost como en Heroku. Sin embargo, este tipo de solicitudes es necesario realizarlas desde el RESTClient. <br>
>http://127.0.0.1:5000/[endpoint] <br>
>https://rest-api-flask-deploy.herokuapp.com/[endpoint] 

##### Lista de endpoint disponibles para su consumo
- /all - GET
- /pokedex - GET y POST
- /pokemon GET y POST
- /type GET y POST

## Instalación local
En caso de que se decida probar la RESTAPI desde un localhost, solo deberemos seguir las siguientes indicaciones:

1. Copiar el repositorio con el siguiente comando

 >git clone https://github.com/cricros/restapi-flask-heroku.git

	Nota: recuerda que el repositorio se va copiar en la ruta actual en la que te encuentras. Si requieres una ruta en especifico, primero colocate en ella y posteriormente ejecuta el comando con git.

2. Una vez con el repositorio descargado, abra su editor de codigo para posteriormente abrir la consola de python e instale las librerias necesarias ejecutando el siguiente comando dentro de la consola de python. 

 >pip install -r requirements.txt
 
3. Terminada la instalación de las librerias necesarias puede ejecutar el archivo main.py desde el editor de texto. Una vez ejecutado se genera la dirección en donde se está ejecutando nuestro localhost. 

##Deploy en Heroku

1. Para poder deployar nuestro proyecto en heroku primero debemos loguearnos, en este caso vamos a utilizar la consola de git, ya que nos permite realizar comandos bash en la misma. 

[![](qwe)](https://ibb.co/wyCyXcS)