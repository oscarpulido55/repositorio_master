#@author:Oscar Daniel Pulido Parra
#@date:29/oct/2016

#-------------------------------------------------------------#
#------------------Ejercicio matrices ------------------------#
#-------------------------------------------------------------#

#1. Crear la matriz 4 × 5 Pista: ver el parametro byrow de la funcion matrix().
  A<-matrix(1:20, nrow=4, ncol=5, byrow = T)

#Extraer los elementos A[4, 3], A[3, 4], A[2, 5] utilizando una matriz de ı́ndices
  A[matrix(c(4:2,3:5),nrow=3,ncol=2)]

#3. Reemplazar dichos elementos con 0.
  A[matrix(c(4:2,3:5),nrow=3,ncol=2)]<-0

#4. Crear la matriz identidad 5 × 5
  I<-matrix(0,nrow=5,ncol=5)
  diag(I)<-1

#5. Convertir la matriz A anterior en una matriz cuadrada B aniadiendo al final una fila de unos (funcion rbind()):
  B<-rbind(A, 1)

#6. Calcular la inversa de la matriz B con la funcion solve().
  solve(B)

#7. Multiplicar B por su inversa B^1 .
  B%*%solve(B)

#8. Comprobar si el resultado es exactamente la matriz identidad I.
#RTA: No

#9. En caso contrario, calcular el “error” o “precision” de la operacion, definido como:
  precision<- 1/(length(B))*abs(sum(B%*%solve(B)-I))

  
#-------------------------------------------------------------#
#-----------------Ejercicio data frames-----------------------#
#-------------------------------------------------------------#

#1. ¿Como esta estructurado el data frame? (utilizar las funciones str() y dim()).
  str(iris)
  dim(iris)
  #RTA: El data frame tiene 150 objetos, en 5 columnas o variables, 

#2. ¿De que tipo es cada una de las variables del data frame?.
  class(iris$Sepal.Length) # "numeric"
  class(iris$Sepal.Width) # "numeric"
  class(iris$Petal.Length) # "numeric"
  class(iris$Petal.Width) # "numeric"
  class(iris$Species) # "factor"
  #RTA 4 de las variables son de tipo; "numeric" y la quinta es de tipo; "factor".

#3. Utilizar la funcion summary() para obtener un resumen de los estadı́sticos de las variables.
  summary(iris)
  #RTA: Usando la funcion summary() en un data fame; por cada columna se calcula el valor minimo, 
  #el valor maximo, la media y la mediana, asi como el primer y tercer cuartil de la muestra 

#4. Comprobar con las funciones mean(), range(), que se obtienen los mismos valores.
  mean(iris$Sepal.Length) # Media de la columna Sepal.Length del dataframe irirs
  range(iris$Sepal.Length) # Rango o valor Maximo y minimo de los valores en la columna Sepal.Length del dataframe irirs
  mean(iris$Sepal.Width) # Media de la columna Sepal.Width  del dataframe irirs
  range(iris$Sepal.Width) # Rango o valor Maximo y minimo de los valores en la columna Sepal.Width del dataframe irirs
  mean(iris$Petal.Length) # Media de la columna Petal.Length  del dataframe irirs
  range(iris$Petal.Length)# Rango o valor Maximo y minimo de los valores en la columna Petal.Length del dataframe irirs
  mean(iris$Petal.Width) # Media de la columna Petal.Width del dataframe irirs
  range(iris$Petal.Width) # Rango o valor Maximo y minimo de los valores en la columna Petal.Width
  mean(iris$Species) # Produce advertencia por que solamente son soportados valores numericos o logicos en la funcion "mean()", retorna NA
  range(iris$Species) # Produce error por que solamente son soportados valores numericos o cadenas de caracteres en la funcion "range()"

#5. Cambia los valores de las variables Sepal.Length Sepal.Width de las 5 primeras observaciones por NA.
  iris$Sepal.Length[1:5]<-NA  
  iris$Sepal.Width[1:5]<-NA

#6.¿Que pasa si usamos ahora las funciones mean(), range() con las variables Sepal.Length y Sepal.Width? 
  mean(iris$Sepal.Length)
  #[1] NA
  range(iris$Sepal.Length)
  #[1] NA NA
  mean(iris$Sepal.Width)
  #[1] NA
  range(iris$Sepal.Width)
  #[1] NA NA
  #RTA:Las funciones "range()" y "mean()" dan como resultado NA al tener valores NA dentro de la muestra.

#¿Tiene el mismo problema la funcion summary()?
  summary(iris)
  summary(iris$Sepal.Width)
  #RTA: No, la funcion sumary obtiene resultado sin tener en cuenta los valores nulos para el calculo.

#7. Ver la documentacion de mean(), range(), etc. ¿Que parametro habrı́a que cambiar para arreglar el problema anterior?.
  mean(iris$Sepal.Length,na.rm = T)
  range(iris$Sepal.Length,na.rm = T)
  #RTA: El parametro "na.rm" en las funciones mean(), range(), permite omitir los valores NA antes de hacer el calculo, por omision se encuentra FALSE

#8. Visto lo anterior, ¿por que es importante codificar los missing values como NA y no como 0, por ejemplo?
  #RTA: Seria importante usar NA en cambio de 0 para valores faltantes en un conjunto de datos para hacer calculos 
        #unicamente con los datos existentes, evitando asi contaminar la muestra y obtener resultados falseados.
        #Por otra parte al usar 0 no se podrian identificar los valores faltantes al confundirse con el resto de los datos numericos.

#9. Eliminar los valores NA usando na.omit().
  na.omit(iris)
  na.omit(irir$Sepal.Length)

#10. Calcular la media de la variable Petal.Length para cada uno de las distintas especies (Species). 
  #Pista: usar la funcion tapply().
  tapply(iris$Petal.Length,iris$Species,FUN = mean)
