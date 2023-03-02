from clases_actividad1 import *


def ejercicio1():
    edadJuan=input("Digite la edad de Juan\n")
    edades=ejercicio_1(int(edadJuan))
    edades.obtenerEdades()
def ejercicio2():
    sum=input("Digite el valor al que le quiere hacer los calculos\n")
    valor=ejercicio_2(int(sum))
    valor.proceso()
def ejercicio3():
    horas=input("Digite la cantidad de horas que gana a la semana\n")
    precio=input("Digite cuanto gana por hora trabajada\n")
    porcentaje=input("Digite el porcentaje (%) de retencion en la fuente\n")
    valor=ejercicio_3(int(horas),int(precio),float(porcentaje))
    valor.datosSalario()
def ejercicio4():
    radio=input("Digite el radio del circulo\n")
    valor=ejercicio_4(int(radio))
    valor.datosCirculo()
def ejercicio5():
    numero=input("Digite el numero deal cual aplicarle el cuadrado y el cubo\n")
    valor=ejercicio_5(int(numero))
    valor.operaciones()

print("Este es la primera actividad del semestre, elige el numeral de uno de los 5 ejercicios para ejecutar")

while True:
    print("---------------------------------------------")
    print("1-Edades familia")
    print("2-Sumar valores a un numero")
    print("3-Salario Trabajador")
    print("4-Radio y longitud circulo")
    print("5-Cubo y cuadrado de un numero")
    print("Para acabar presione 0")
    print("----------------------------------------------")
    ejercicio=input("El ejercicio que desde probar es :  ")
    if ejercicio=="1":
        ejercicio1()
        continue
    if ejercicio=="2":
        ejercicio2()
        continue
    if ejercicio=="3":
        ejercicio3()
        continue
    if ejercicio=="4":
        ejercicio4()
        continue 
    if ejercicio=="5":
        ejercicio5()
        continue
    if ejercicio=="0":
        break
    else:
        print("Digite un valor valido")
 




    


input
