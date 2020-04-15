'''
@author: Alvarez
'''
import tkinter as tk
lista_numeros=[]
root = tk.Tk()
numero1=tk.IntVar()
numero2=tk.IntVar()
mensaje=tk.IntVar()
mensaje1=tk.StringVar()

print('========= Bienvenido a la Calculadora Universal ========')
def sumar():
    num1=numero1.get()
    num2=numero2.get()
    suma=num1+num2
    print ('La SUMA de los Numeros es:',suma)
    mensaje1.set('La Suma de los Numeros es :')
    mensaje.set(suma)
     
def restar():
    num1=numero1.get()
    num2=numero2.get()
    resta=num1-num2
    print ('La RESTA de los Numeros es:',resta)
    mensaje1.set('La Resta de los Numeros es :')
    mensaje.set(resta)
def multiplicar():
    num1=numero1.get()
    num2=numero2.get()
    multiplicacion=num1*num2
    print ('La MULTIPLICACION de los Numeros es:',multiplicacion)
    mensaje1.set('La Multiplicacion de los Numeros es :')
    mensaje.set(multiplicacion)
def dividir():
    num1=numero1.get()
    num2=numero2.get()
    division=num1/num2
    print ('La DIVISION de los Numeros es:',division)
    mensaje1.set('La Division de los Numeros es :')
    mensaje.set(division)
def terminarprograma():
    print('Fin del Programa :)')
    global sw
    sw = False
    
def opcion_no_disponible():
    print('Opcion Noo Disponible')

root.geometry('800x500')
root.title('calculator')
root.configure(bg='#455A64')
tk.Label(root,text='Bienvenido a la Calculadora Universal',bg='#455A64',fg='white',font=('Times',20)).place(x=170,y=20)
tk.Label(root,text='""""""ELIJA UNA OPCION A REALIZAR""""""',bg='#455A64',fg='white',font=('Times',14)).place(x=170,y=140)
#Numero 1
tk.Label(root,text='Introduzca un Numero :',bg='#455A64',fg='white',font=('Times',14)).place(x=150,y=60)
tk.Entry(root,justify='center',textvariable=numero1).place(x=370,y=65)
#Numero 2
tk.Label(root,text='Introduzca otro Numero :',bg='#455A64',fg='white',font=('Arial',14)).place(x=150,y=90)
tk.Entry(root,justify='center',textvariable=numero2).place(x=370,y=95)
#Sumar
tk.Label(root,text='Quiere que los numeros:',bg='#455A64',fg='white',font=('',14)).place(x=100,y=195)
tk.Button(root,text='SUMEN',bd=0,command=sumar).place(x=345,y=200)
#Restar
tk.Label(root,text='Quiere que los numeros:',bg='#455A64',fg='white',font=('',14)).place(x=100,y=235)
tk.Button(root,text='RESTEN',bd=0,command=restar).place(x=345,y=240)
#Multiplicar
tk.Label(root,text='Quiere que los numeros:',bg='#455A64',fg='white',font=('',14)).place(x=100,y=275)
tk.Button(root,text='MULTIPLIQUEN',bd=0,command=multiplicar).place(x=329,y=280)
#Dividir
tk.Label(root,text='Quiere que los numeros:',bg='#455A64',fg='white',font=('',14)).place(x=100,y=315)
tk.Button(root,text='DIVIDAN',bd=0,command=dividir).place(x=345,y=320)

#Salir
tk.Label(root, textvariable=mensaje1,bg='#455A64',fg='white',font=('',18)).place(x=200,y=380)
tk.Label(root, textvariable=mensaje,bg='#455A64',fg='white',font=('',18)).place(x=340,y=410)
tk.Button(root,text='Salir',bd=0,command=root.destroy).place(x=350,y=450)
root.mainloop()
