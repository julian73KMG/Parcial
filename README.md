Las salidas en terminal de acuerdo al codigo son los siguientes

-- Salida Postiva o Predeterminada


![image](https://github.com/user-attachments/assets/e98ff4a4-194d-4f54-97aa-daf7a21fe06e)

>> True (elementoRepetido con 'rata')


>> calle (hayVocal en la lista x)


>> ['carro', 'raton']  (Elementos diferentes con las listas w y x)


>> 3.0  (Promedio de la variable u)


>> (3, 4)  (Mediana de la variable v)


-- Salida Negativa o Variable


![image](https://github.com/user-attachments/assets/784d5cca-97f3-48d1-8191-650cd3095792)


>> False (elementoRepetido con 'pato')


>> No hay dos o más vocales (hayVocal en la lista y)


>> []  (Elementos diferentes con las listas w y w1, son la misma lista)


>> Vacío  (Promedio de la variable vacio, es un arreglo sin numeros, por tanto no hay promedio)


>> 3  (Mediana de la variable v1)



-- Errores hallados y corregidos (changes) --

Inicialmente insuficiencia de variables para probar y codigo sin comentar

En 'elementoRepetido' se inicalizaba el segundo recorrido en el mismo lugar, por tanto siempre daba True, además el 'else' hacía que hubiera una única ejecucion

En 'hayVocales' la condicion se daba inicialmente y por tanto nunca se imprimiría la palabra, adicionalmente, el recorrido no requiere de un rango necesariamente, también se puede ejecutar el conteo en unas pocas líneas.

En 'difElementos' estaba como 'tuple' en vez de 'list' con el cual es más sencillo recorrer y agregar, sin embargo con tuplas se puede ejecutar igual, sin embargo, el 'else' en el condicional está sobrando

En 'promedio' y 'mediana' se puede incluir facilmente un caso de uso con las listas vacías


