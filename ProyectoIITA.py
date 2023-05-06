import tkinter
from random import randint #genera un número entero entre a y b, ambos incluidos. a debe ser inferior o igual a b.

ventana=tkinter.Tk()
ventana.geometry("800x300")
def rango():
    salida.delete(0,10000000) #Debe borrar toda la vieja contraseña generada
    largo=int(entrada.get()) #Establece que tan larga sera la contraseña y la funcion get toma todo lo escrito adentro
    contraseña=""
    for x in range(largo):
        contraseña+= str(randint(0, 9))
    salida.insert(0, contraseña)


pregunta=tkinter.Label(ventana,text="¿Cuantos numeros, letras o simbolos deseas que tenga?", font="Helvetica 20")
pregunta.pack(pady=10)

entrada=tkinter.Entry(ventana, font="Helvetica 20")
entrada.pack(pady=30, padx=30)
salida= tkinter.Entry(ventana, font="Helvetica 20")
salida.pack()

boton1=tkinter.Button(ventana, text="Generar contraseña", command=rango)
boton1.pack(padx=20, pady=20)

ventana.mainloop()