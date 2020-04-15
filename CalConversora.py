'''
Created on 8 abr. de 2020
@author: ASUS
'''
from builtins import int
print('========= Bienvenido a la Calculadora Universal ========')
lista_numeros=[]

def bases():
    decimal=0
    base=0
    conversion = ''
    while decimal // base != 0:
        conversion = str(decimal % base) + conversion
        decimal = decimal // base
    return str(decimal) + conversion

def sumar():
    lista_numeros=[]
    n = int(input('Introduzca la Cantidad de Numeros a Sumar:'))
    print('Introduzca los Numeros: ')
    for x in range (n):
        numeros=int(input())
        lista_numeros.append(numeros);
    suma=0
    for i in lista_numeros:    
        suma=suma+i
    print ('La SUMA de los Numeros es:',suma)

def restar():
    lista_numeros=[]
    n = int(input('Introduzca la Cantidad de Numeros a Restar:'))
    print('Introduzca los Numeros: ')
    for x in range (n):
        numeros=int(input())
        lista_numeros.append(numeros);
    resta=lista_numeros[0]
    for i in range(1,len(lista_numeros)):    
        resta-=lista_numeros[i]
    print ('La Resta de los Numeros es:',resta)
    
def multiplicar():
    lista_numeros=[]
    n1 = int(input('Introduzca la Cantidad de Numeros a Multiplicar:'))
    print('Introduzca los Numeros: ')
    for z in range (n1):
        numeros1=int(input())
        lista_numeros.append(numeros1);
    mutliplicacion=1
    for y in lista_numeros:    
        mutliplicacion=mutliplicacion*y
    print ('La Multiplicacion de los Numeros es:',mutliplicacion)
     
def dividir():
    lista_numeros=[]
    n = int(input('Introduzca la Cantidad de Numeros a Dividir:'))
    print('Introduzca los Numeros: ')
    for x in range (n):
        numeros=int(input())
        lista_numeros.append(numeros);
    div=lista_numeros[0]
    for i in range(1,len(lista_numeros)):    
        div//=lista_numeros[i]
    print ('La Division de los Numeros es:',div)   
     
def terminarprograma():
    print('Fin del Programa :)')
    global sw
    sw = False
    
def opcion_no_disponible():
    print('Opcion Noo Disponible')

sw = True
while sw:
    menu = '''
    ======Elija una Opcion :======
    1. Conversor
    2. Sumar 
    3. Restar
    4. Multiplicar
    5. Dividir
    6. Salir
    '''
    print(menu)
    user = int(input('Ingrese la opcion a realizar: '))
    if user is 1:
        numero=int(input('Introduzca Numero Decimal a Convertir:'))
        base=int(input('Introduzca la Base a Convertir:'))
        print('Su conversion es:',bases(numero,base))
    elif user is 2:
        sumar()
    elif user is 3:
        restar()
    elif user is 4:
        multiplicar()
    elif user is 5:
        dividir()
    elif user is 6:
        terminarprograma()
    else:
        opcion_no_disponible()
