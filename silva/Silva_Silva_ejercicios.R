#1 Crear la matriz 4 × 5
a<-matrix(1:20,4,5,byrow = T)

#2 Extraer los elementos A[4, 3], A[3, 4], A[2, 5] utilizando una
#matriz de  ??indices.
indices<-matrix(c(4,3,3,4,2,5),2,3,byrow = F)
#A[4, 3]
a[indices[1],indices[2]]
#A[3, 4]
a[indices[1,2],indices[2,2]]
#A[2, 5]
a[indices[1,3],indices[2,3]]
#3 Reemplazar dichos elementos con 0.
a[4,3]<-0
a[3,4]<-0
a[2,5]<-0
#4 Crear la matriz identidad 5 × 5

#5. Convertir la matriz A anterior en una matriz cuadrada B
#a~nadiendo al final una fila de unos 
b<-rbind(a,rep(1,5))
#6 Calcular la inversa de la matriz B con la funci??on
solve(b)
#7 Multiplicar B por su inversa
inv<-solve(b)
b*inv

#-------------------EJERCICIOS DATAFRAMES--------------------------------
#Con el data frame iris (viene cargado en R).
#1 ¿Como est??a estructurado el data frame? (utilizarfunciones str() y dim()).
str(iris)
#Es un objeto del tipo dataframe que consta de 150 filas, 5 variables 
#$ Sepal.Length,$ Sepal.Width,$ Petal.Length,$ Petal.Width,$ Species
dim(iris)
#El objeto consta de 150 filas y 5 columnas

#2 ¿De qu ??e tipo es cada una de las variables del dataframe
class(iris$Sepal.Length)
#la variable sepal.length tiene un valor de tipo numeric
class(iris$Sepal.Width)
#la variable Sepal.Width tiene un valor de tipo numeric
class(iris$Petal.Length)
#la variable Petal.Length tiene un valor de tipo numeric
class(iris$Petal.Width)
#la variable Petal.Width tiene un valor de tipo numeric
class(iris$Species)
#la variable Species tiene un valor de tipo factor

#3. Utilizar la funci??on summary() para obtener un resumen
#los estad ??isticos de las variables
summary(iris)
#Entrega el resumen estadistico del dataframe retornando el valor minimo,1st quartil,
#mediana, la media, 3rd quartil, y el valor maximo.

#4. Comprobar con las funciones mean(), range(), que se
#obtienen los mismos valores.
attach(iris)
mean(Sepal.Length)
mean(Sepal.Width)
mean(Petal.Length)
mean(Petal.Width)
mean(Petal.Width)
range(Sepal.Length)
range(Sepal.Width)
range(Petal.Width)
range(Petal.Length)
range(Species)
detach(iris)
#los valores que arroja la funcion mean() son los mismos que summary, en la variable
#species arroja el valor NA por no ser un argumento numerico.
#para el caso de range arroja los valores igual que usando summary, en la variable 
#species genera un error ya que no son datos numericos.

#5. Cambia los valores de las variables Sepal.Length
#Sepal.Width de las 5 primeras observaciones por NA.
iris$Sepal.Length[1:5]<-NA  
iris$Sepal.Width[1:5]<-NA

#6. ¿Qu ??e pasa si usamos ahora las funciones mean(),
#con las variables Sepal.Length y Sepal.Width? ¿Tiene el
#mismo problema la funci ??on summary?
mean(iris$Sepal.Length)
mean(iris$Sepal.Width)
#El resultado que arroja la funcion para estos dos casos es NA , la funcion summary
#no presenta el mismo problema.

#7. Ver la documentaci ??on de mean(), range(), etc.
#par ??ametro habr ??ia que cambiar para arreglar el problema
#anterior?.
mean(iris$Sepal.Length,trim = 0,na.rm = TRUE)
range(iris$Sepal.Length,trim = 0,na.rm = TRUE)
#el parametro que se debe cambiar para solucionar el problema es na.rm=TRUE
#por defecto se encuentra en FALSE, este parametro indica si se quieren omitir
#los valores NA

#8. Visto lo anterior, ¿por qu ??e es importante codificar
#missing values como NA y no como 0, por ejemplo?

#por que asi podemos identificar los missing values, si se codifican como 0 no 
#sabremos cuales eran los valores missing. al trabajar con NA podemos 
#modificar los parametros na.rm de las funciones paratrabajar sin inconveniente.

#9. Eliminar los valores NA usando na.omit().
na.omit(iris)

#10. Calcular la media de la variable Petal.Length para cada
#uno de las distintas especies (Species). Pista: usar la
#funci ??on tapply
tapply(iris$Petal.Length,iris$Species,FUN = mean)
