import tkinter as tk
from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("340x320")

#Valida si la pantilla contiene numeros para saber si se puede poner operadores o no
def validar_1():
    if(len(pantalla.get())>0):
        return True
    return False

#Validaciones extras para la correcta ejecicion de la operaciones
def validar_2(insert):
    cadena = pantalla.get()
    if(cadena=="¡Numeros antes!" or cadena.count("=")>0):
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "¡Numeros antes!")
    else:
        if(validar_1()==False):
            pantalla.insert(0, "¡Numeros antes!")
        else:
            pantalla.insert(tk.END,insert)

#Inserta los operadores
def insert_operador(insert):
    cadena = pantalla.get()
    if(cadena[-1]!="."):
        if(cadena.count("+")==0 and cadena.count("-")==0 and cadena.count("*")==0 and cadena.count("/")==0):
            validar_2(insert)
            
#Inserta los operandos
def insert_operandos(insert):
    cadena = pantalla.get()
    if(cadena=="¡Numeros antes!" or cadena.count("=")>0):
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END,insert)
    else:
        pantalla.insert(tk.END,insert)

#Realiza la operacion solicitada por el usuario
def igual():
    cadena = pantalla.get()
    if(cadena.count("+")==1):
        indice = cadena.find("+")
        pantalla.delete(0, tk.END)
        pantalla.insert(0,("="+str(float(cadena[:indice])+float(cadena[(indice+1):len(cadena)]))))
    elif(cadena.count("-")==1):
        indice = cadena.find("-")
        pantalla.delete(0, tk.END)
        pantalla.insert(0,("="+str(float(cadena[:indice])-float(cadena[(indice+1):len(cadena)]))))
    elif(cadena.count("*")==1):
        indice = cadena.find("*")
        pantalla.delete(0, tk.END)
        pantalla.insert(0,("="+str(float(cadena[:indice])*float(cadena[(indice+1):len(cadena)]))))
    elif(cadena.count("/")==1):
        indice = cadena.find("/")
        pantalla.delete(0, tk.END)
        pantalla.insert(0,("="+str(float(cadena[:indice])/float(cadena[(indice+1):len(cadena)]))))

#Los metodos que llaman los botones operandos en caso de ser presionados
def sumar():insert_operador("+")
def restar():insert_operador("-")
def multiplicar():insert_operador("*")
def dividir():insert_operador("/")

#los metodos que llaman los botones numericos en caso de ser presionados
def uno():insert_operandos("1")
def dos():insert_operandos("2")
def tres():insert_operandos("3")
def cuatro():insert_operandos("4")
def cinco():insert_operandos("5")
def seis():insert_operandos("6")
def siete():insert_operandos("7")
def ocho():insert_operandos("8")
def nueve():insert_operandos("9")
def cero():insert_operandos("0")
def punto():insert_operandos(".")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=100, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", command=uno, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", command=dos, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", command=tres, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", command=cuatro, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", command=cinco, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", command=seis, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", command=siete, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", command=ocho, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", command=nueve, width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", command=igual, width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", command=punto, width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", command=sumar ,width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", command=restar, width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", command=multiplicar, width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, command=dividir, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)


root.mainloop()