import math

class ejercicio_1():
    def __init__(self,EdadJuan):
        self.EdadJuan=EdadJuan
    def obtenerEdades(self):
        edadJuan=self.EdadJuan
        edadAlber=2*(edadJuan/3)
        edadAna=4*(edadJuan/3)
        edadMama=edadAlber+edadAna+edadJuan
        print("La edad de Juan es",edadJuan)
        print("La edad de Alber es",edadAlber)
        print("La edad de Ana es",edadAna)
        print("La edad de la madre es",edadMama)

class ejercicio_2():
    def __init__(self,suma):
        self.suma=suma
    def proceso(self):
        suma=self.suma
        x=20
        suma=suma+x
        print("se suma ",x)
        y=40
        x=x+y**2
        suma=suma+x/y
        print("se suma",x/y)
        self.suma=suma
        print("El valor de su suma es",suma)
    
class ejercicio_3():
    def __init__(self,horas,precio,porcentaje):
        self.horas=horas
        self.precio=precio
        self.porcentaje=porcentaje
    def datosSalario(self):
        horas=self.horas
        precio=self.precio
        porcentaje=self.porcentaje
        salarioBruto=horas*precio
        retenidoFuente=salarioBruto*(porcentaje/100)
        salarioNeto=salarioBruto-retenidoFuente
        print("El salario bruto es",salarioBruto)
        print("El descuento por retencion en la fuente es",retenidoFuente)
        print("El salario neto resultante es ",salarioNeto)

class ejercicio_4():
    def __init__(self,radio):
        self.radio=radio
    def datosCirculo(self):
        radio=self.radio
        area=math.pi*radio**2
        longitud=2*math.pi*radio
        print("El area del circulo de radio",radio,"es",area)
        print("La longitud del circulo de radio",radio,"es",longitud)

class ejercicio_5():
    def __init__(self,numero):
        self.numero=numero
    def operaciones(self):
        numero=self.numero
        cuadrado=numero**2
        cubo=numero**3
        print("El cuadrado de",numero,"es",cuadrado)
        print("El cubo de",numero,"es",cubo)

