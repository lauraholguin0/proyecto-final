from tkinter import *
import tkinter as tk
from tkinter import ttk

raiz=Tk()


raiz.title("Juego de Damas Chinas")
# self.raiz.iconbitmap("imagenes/damas.ico")
raiz.config(bg="#663300")

#pantalla completa
ancho_ventana=raiz.winfo_screenwidth()
alto_ventana=raiz.winfo_screenheight()
#centrar en cualquier tamaño de ventana
x_ventana=raiz.winfo_screenwidth()//2-ancho_ventana//2
y_ventana=raiz.winfo_screenheight()//2-alto_ventana//2

lado_cuadrado=(ancho_ventana/16)
posicion=str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(x_ventana)+"+"+str(y_ventana)
raiz.geometry(posicion)
interfaz2=Frame()
interfaz2.pack(side="left")
interfaz2.config(width="684.8",height="50",bg="green")
interfaz=tk.Canvas()
interfaz.pack(fill="y",expand=True)
interfaz.config(width=(ancho_ventana/2),height=(alto_ventana/2),bg="#663300",cursor="circle")
for i in range(8):
    for l in range(8): 
        if(i+l)%2==0:
            interfaz.create_rectangle(i*lado_cuadrado,l*lado_cuadrado,(i+1)*lado_cuadrado,(l+1)*lado_cuadrado,fill="dark red")
        else:
            interfaz.create_rectangle(i*lado_cuadrado,l*lado_cuadrado,(i+1)*lado_cuadrado,(l+1)*lado_cuadrado,fill="black")
# #contador de fichas


ttk.Label(interfaz2, text="Hello World!").pack(side="left")
ttk.Button(interfaz2, text="Quit", command=raiz.destroy).pack(side="left")

#fichas


raiz.mainloop()
