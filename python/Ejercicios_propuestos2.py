#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:07:21 2016
EJERCICIOS PROPUESTOS PYTHON 2
@author: oscar
"""
import sys
import random 
"""
1.Modificar una lista de números reales que representan las calificaciones de los
alumnos de una clase, para sustituir los valores numéricos por sus 
calificaciones alfanuméricas (Suspenso, Aprobado, etc.)

9,0 - 10,0 = Sobresaliente (SB) - Equivalencia Europea: A
7,0 - 8,9 = Notable (NT) - Equivalencia Europea: B
5,0 - 6,9 = Aprobado (AP) - Equivalencia Europea: C
4,9 - 0,0 = Suspenso (SS) - Equivalencia Europea: Fail
"""
num_califications = [5.0,8.5,7.0,4.5,8.9,10.0]
desc_califications = []
for num in num_califications:
    if 0.0>=num<=4.9:
        desc_califications.append("Suspenso (SS)")
    elif 5.0>=num<=6.9:
        desc_califications.append("Aprobado (AP)")
    elif 7.0>=num<=8.9:
        desc_califications.append("Notable (NT)")
    elif 9.0>=num<=10.0:
        desc_califications.append("Sobresaliente (SB)")
    else:
        desc_califications.append(None)
print desc_califications

"""
2. Implementar una función que pone en mayúsculas todas las primeras letras
de las palabras de una frase.
"""
def get_capital(text):
    cap=text.title()
    return cap
    
print get_capital("hsdofbdfdso dofhsdof dsf oidshf")
    
"""
3. Implemente una función que indique si una palabra contiene las cinco
vocales: por ejemplo “murciélago”. Modifique posteriormente la función para 
que detecte sólo aquellas palabras que contienen una única vez cada vocal.
"""
def is_pentavocalica(text):
    if "A" in text.upper() and "E" in text.upper() and "I" in text.upper() and "O" in text.upper() and "U" in text.upper():
        return True
    else:
        return False

print is_pentavocalica("murcielago")
def is_pentavocalica2(text):
    counta=0
    counte=0
    counti=0
    counto=0
    countu=0
    for char in text:
        if char.upper() == 'A':
            counta += 1
        if char.upper() == 'E':
            counte += 1
        if char.upper() == 'I':
            counti += 1
        if char.upper() == 'O':
            counto += 1
        if char.upper() == 'U':
            countu += 1
    if counta+counte+counti+counto+countu==5:
        return True
    else:
        return False
print is_pentavocalica2("murcielagito")

"""
4. Escribir una función que sume dos listas de igual longitud y retorne otra lista
que contenga la suma de las originales elemento a elemento.
"""
def sum_list(num_list1,num_list2):
    res_list=[]
    i=0
    if len(num_list1)==len(num_list2):
        for num in num_list1:
            res_list.append(num+num_list2[i])
            i+=1
    return res_list
print sum_list([1,2,3,2],[5,6,7,8])
"""
5. Modifique el ejercicio anterior permitiendo que las listas sean desiguales. En
este caso, los elementos sobrantes de la lista más larga se añadirán al final 
de la lista resultante.
"""
def sum_list2(num_list1,num_list2):
    res_list=[]
    big_list=[]
    small_list=[]
    i=0
    if len(num_list1)>len(num_list2):
        big_list=num_list1
        small_list=num_list2
    else:
         big_list=num_list2
         small_list=num_list1
    for num in big_list:
        if i>=len(small_list):
            num2=0
        else:
            num2=small_list[i]
        res_list.append(num+num2)
        i+=1
    return res_list
print sum_list2([1,1,1],[2,2,2,2,4,5])

"""
6.Crear una lista de enteros, inicializarlos según valores aleatorios en el rango
1..20 y computar la media de los valores, el valor más alto y el más bajo (todo 
ello utilizando listas). Utilizar las funciones para generación de números 

aleatorios de Python (https://docs.python.org/dev/library/random.html)
"""
int_list=[random.randrange(20), random.randrange(20),random.randrange(20),random.randrange(20),random.randrange(20),random.randrange(20),random.randrange(20),random.randrange(20),random.randrange(20)]
def get_average(plist):
    if len(plist)>0:
        return reduce(lambda x,y:x+y,plist)/len(plist)
    return 0
def get_biggest(plist):
    maxn=0
    for num in plist:
        if num>maxn:
            maxn=num
    return maxn
def get_smallest(plist):
    minn=sys.maxint
    for num in plist:
        if num<minn:
            minn=num
    return minn
print get_average(int_list)
print get_biggest(int_list)
print get_smallest(int_list)

"""
7. Implementar una función que compruebe si una palabra es un palíndromo.
"""
def is_palindrome(word):
   if word.upper()==word[::-1].upper():
       return True
   else:
       return False
       
print is_palindrome("Rotomotor")

"""
8. Crear una función que compruebe si dos cadenas de caracteres son iguales
recorriendo con un índice ambas cadenas (no puede utilizar cad1==cad2).
"""
def are_equals(cad1,cad2):
    same=False
    if len(cad1)==len(cad2):
        i=0
        for char in cad1:
           if char == cad2[i]:
               same=True
           else:
               same = False
               break
           i+=1
    return same
print are_equals("asdf","asdf")

"""
9. Distribuir 20 datos enteros leídos por teclado en dos listas de tal manera que
se vayan generando dos secuencias ordenadas, una creciente y otra
decreciente.
"""
list_asc=[]
list_desc=[]
for num in range(1,21):
    #a=input('Ingrese Numero: ')
    list_asc.append(a)
list_asc=sorted(list_asc)
list_desc=sorted(list_asc, reverse = True)
print list_asc
print list_desc

"""
10. Escriba un programa que “codifique” una frase modificando todas las vocales
según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el 
símbolo #. Por ejemplo, la frase: “Un perro del hortelano”, deberá 
devolverse: “#n p3rr0 d3l h0rt3l4n0”.
"""
sentence="Un perro del hortelano"
sentence=sentence.upper().replace("A","4").replace("E","3").replace("I","1").replace("O","0").replace("U","#")
print sentence.capitalize()
"""
11.Crear un diccionario en python con parejas numero de tfno, nombre que
represente una agenda telefónica. Posteriormente simular un manos libres, 
pidiendo al usuario “A quién desea llamar” y mostrando en pantalla el 
mensaje “Llamada al número XXX en curso” donde XXX seria el número 
telefónico de la persona elegida.
"""
contacts = {"oscar": 3112513, "daniel": 31548}
#name=input('A quién desea llamar: ')
print contacts[name]
"""
12. Escribir una función que reciba un tweet y retorne los hashtags en una lista
"""
def get_hashtags(tweet):
    words=tweet.split()
    tweets=[]
    for word in words:
        if word.startswith("#"):
            tweets.append(word)
    return tweets
print get_hashtags("#hola esto es #una prueba #facil")

"""
13. Escriba un programa que lea un archivo de texto y lo mete en una lista
donde cada línea es una sublista
"""            
def read_file(path_file):
    f=open(path_file,'rw')
    lines=[]
    for line in f:
        linelist=[]
        for word in line.split():
            linelist.append(word)
        lines.append(linelist)
    f.close()
    return lines
print read_file("/home/oscar/ejemplo.txt")

"""
14.Realizar un programa que lea palabras hasta que se introduzca “fin”,
mostrando una estadística de las longitudes de las palabras, es decir, el 
número total de palabras de longitud 1 que se hayan introducido, el total de 
longitud 2, etc. La máxima longitud de las palabras deberá ser de 25 
caracteres. Una posible salida de este programa sería: 
Palabras longitud 1: 0 
Palabras longitud 2: 10 
... 
Palabras longitud 25: 1 
"""
def get_input_statistics():
    word_list=[]
    inword=input('ingrese una palabra: ')
    word_list.append(inword)
    if inword!="fin":
        while inword!="fin":
            inword=input('ingrese otra palabra: ')
            word_list.append(inword)
    print word_list
    for i in range(1,25):
        count=0
        for w in word_list:
            if len(w)==i:
               count+=1
        if count!=0:
            print "Palabras longitud "+str(i)+":"+str(count)
        
print get_input_statistics()       