# guros
Repositorio de projecto para reto de programación de Fullstack Developer, por Erick Martínez

URL de invocación:
https://ytt9g96iog.execute-api.us-west-1.amazonaws.com/dev/

##Instrucciones
**hasMutation**
Método:POST 
Ruta: /mutation
JSON: {  "dna":["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]}
Respuestas:
-Validation Failed:400
-Mutation found!:200
-No mutation found:403

**Mutation count**
Método:GET 
Ruta: /stats
Respuesta: {"count_mutations": 40,"count_no_mutation": 100,"ratio": 0.4}
