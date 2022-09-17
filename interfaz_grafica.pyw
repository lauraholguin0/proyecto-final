from tkinter import *
from tkinter import ttk

#raiz o ventana
raiz=Tk()
raiz.title("Juego de Damas Chinas")
raiz.resizable(1,1)
raiz.iconbitmap("imagenes/damas.ico")
raiz.config(bg="green")

#pantalla completa
ancho_ventana=raiz.winfo_screenwidth()
alto_ventana=raiz.winfo_screenheight()
#centrar en cualquier tamaño de ventana
x_ventana=raiz.winfo_screenwidth()//2-ancho_ventana//2
y_ventana=raiz.winfo_screenheight()//2-alto_ventana// 2

posicion=str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(x_ventana)+"+"+str(y_ventana)
raiz.geometry(posicion)

#frame
frame=Frame()
frame.pack(fill="y", expand="true")
frame.pack()
frame.config(width="700",height="600",bg="#000",bd="35",cursor="circle")
#widgets botones
frm = ttk.Frame(frame, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=raiz.destroy).grid(column=1, row=0)



#ejecuta la ventana(bucle infinito)
raiz.mainloop()

