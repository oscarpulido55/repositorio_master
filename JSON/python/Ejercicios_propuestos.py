#1. Funcion que retorne el mayor de dos numeros o 0 si son iguales
def get_greater(numa,numb):
    """float, float -> float
       OBJ: Retorne el mayor de dos numeros o 0 si son iguales
    """
    result=0
    if numa==numb:
        result=0
    elif numa>numb:
        result=numa
    else:
        result=numb
    return result

print get_greater(4,8)
#prueba cod anterior
#a=float(input('Primer Numero: '))
#b=float(input('Segundo Numero: '))
#c=get_greater(a,b)
#if c==0:
#    print('Los Numeros son iguales')
#else:
#    print('El numero mayor es: ', c)

    
#2. Funcion que determine si una persona es mayor de edad o no 
#(pista:el retorno debe ser un valor booleano)
def is_adult(age):
    result=False
    if age>18:
        result=True
    return result   
print is_adult(21)

def is_adult2(year,month,day):
    from datetime import  datetime 
    today_minus_18years=datetime(datetime.now().year-18, datetime.now().month, datetime.now().day)
    birth_date = datetime(year, month, day)
    print birth_date,  today_minus_18years
    if birth_date > today_minus_18years:
        return False
    else:
        return True
print is_adult2(1998,10,18)


#3. Programar una funcion que determine si una empresa es
#microempresa o no (retorno booleano True o False). Se dice que es
#microempresa si tiene menos de 50 empleados, factura menos de 30
#milones de euros y tiene un balance igual o inferior a los 5 millones de
#euros
def is_small_bussines(num_emp,fac,bal):
    es_micro=num_emp<50 and fac<30 and bal<5
    result='su empresa no es microempresa'
    if es_micro:
        result='su empresa es microempresa'
    return result

print is_small_bussines(40,20,4)

#4.Calcular el impuesto que debe pagar un contribuyente a partir de sus
#ingresos anuales y el numero de hijos. El impuesto a pagar es un tercio
#del ingreso imponible, siendo este ultimo igual a los ingresos totales
#menos una deduccion personal de 600 y otra deduccion de 60 por
#hijo
def get_tax(anual_in,num_child):
    if num_child==0:
        disp=anual_in-600
    else:
        disp=anual_in-600-(60*num_child)
    return disp/3
print get_tax(30000,2)

#5.Hacer los calculos que permiten saber si una empresa de 20
#empleados, 18 millones de euros de facturacion y 5 millones de euros
#de balance es una micro empresa y almacenar el valor en una variable
#logica (booleana)
if is_small_bussines(20,18,5)=='su empresa es microempresa':
    bool_var=True
else:
    bool_var=True
print bool_var

#6.La temperatura expresada en grados centigrados TC, se puede
#convertir a grados Fahrenheit (TF) mediante la siguiente formula: TF =
#9*TC/5 + 32. Programa una funcion para hacer esta transformacion que
#reciba como argumento la temperatura en grados centigrados y retorne
#su equivalente en Farenheit.
def get_fahrenheit_val(cent_val):
    return ((9*cent_val)/5) + 32

print get_fahrenheit_val(30)

#7.Escribir una funcion Python que a partir de una cierta cantidad en
#euros y del tipo de cambio del dia, retorne el equivalente en libras
#teniendo en cuenta que la casa de cambio retiene una comision del 2 opr cien
#sobre el total de la operacion.
def get_sterling(eur_in,exchange):
    return (eur_in*exchange)+(eur_in*0.02)
print get_sterling(50,1.1091)

#8.Procedimiento que pinte una linea de asteriscos en pantalla
def print_starts():
    print '******************************************'
print_starts()

#9.Programe un modulo en Python que reutilizando la funcion anterior
#muestre nuestros datos en pantalla con formato banner tal y como se
#representa abajo:
#******************************
#Autor: Lucas Sanchez
#Email: lucassanchez@campusciff.net
#******************************
def get_autor(name,email):
    print_starts()
    print 'Autor:' +name
    print 'Email:' +email
    print_starts()
print get_autor('Daniel Pulido','oscarpulido@campusciff.net')

#10. Programa modularizado que, utilizando funciones, calcule el
#perimetro y el area de un circulo cuyo radio es proporcionado por el
#usuario
def get_circle_data(radius):
    pi=3.1416
    print get_perimeter(radius,pi)
    print get_area(radius,pi)

def get_perimeter(radius,pi):
    return 2.0*pi*radius
def get_area(radius,pi):
    return pi*(radius**2)
    
get_circle_data(3)

#11. Escribamos un programa para solicitar al usuario el numero de
#horas y el precio por hora con vistas a calcular su salario bruto. Las
#horas que sobrepasen 40 se consideraran extra y pagadas a 1,5 veces
#el precio de la hora regular.
def get_salary(hours,price_per_hour):
    if hours<=40:
        result=hours*price_per_hour
    elif hours>40:
        ext=(hours-40)*(price_per_hour*1.5)
        result=40*price_per_hour+ext
    else:
        result=0.0
    return result

print get_salary(45,100)

#12. Programar una funcion que determine si un numero es par o impar.
#La funcion debe retornar verdadero o falso haciendo uso de valores
#booleanos.
def is_even_number(num):
    if (num%2)==0:
        return True
    else:
        return False

print is_even_number(56541)

#13. Programar una funcion que determine si una letra es vocal o no.
def is_vocal(char):
    #if char.upper()=='A' or char.upper()=='E' or char.upper()=='I' or char.upper()=='O' or char.upper()=='U':
    if char.upper() in['A','E','I','O','U']:  
        return True
    else:
        return False
print is_vocal('A')

#14. Programar un modulo en Python que a partir de un numero entero
#entre 1 y 7 que recibe como argumento muestre en pantalla el dia de la
#semana que corresponda, y un mensaje de error si el numero no esta
#entre 1 y 7.
def get_day(num):
    switcher = {
    1: "sunday",
    2: "monday",
    3: "tuesday",
    4: "wednesday",
    5: "thursday",
    6: "friday",
    7: "saturday",}
    return switcher.get(num, "nothing")
print get_day(5)