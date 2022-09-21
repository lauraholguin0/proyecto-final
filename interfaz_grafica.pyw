import tkinter as tk
raiz=tk.Tk()


raiz.title("Juego de Damas Chinas")
# self.raiz.iconbitmap("imagenes/damas.ico")
raiz.config(bg="green")

#pantalla completa
ancho_ventana=raiz.winfo_screenwidth()
alto_ventana=raiz.winfo_screenheight()
#centrar en cualquier tamaño de ventana
x_ventana=raiz.winfo_screenwidth()//2-ancho_ventana//2
y_ventana=raiz.winfo_screenheight()//2-alto_ventana//2

lado_cuadrado=(ancho_ventana/16)
posicion=str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(x_ventana)+"+"+str(y_ventana)
raiz.geometry(posicion)
interfaz2=tk.Canvas()
interfaz=tk.Canvas()
interfaz2.pack()
interfaz2.config(width="684.8",height="50",bg="green")
interfaz.pack(fill="y",expand=True)
interfaz.config(width=(ancho_ventana/2),height=(alto_ventana/2),bg="#000",cursor="circle")
for i in range(8):
    for l in range(8): 
        if(i+l)%2==0:
            interfaz.create_rectangle(i*lado_cuadrado,l*lado_cuadrado,(i+1)*lado_cuadrado,(l+1)*lado_cuadrado,fill="dark red")
        else:
            interfaz.create_rectangle(i*lado_cuadrado,l*lado_cuadrado,(i+1)*lado_cuadrado,(l+1)*lado_cuadrado,fill="grey")

raiz.mainloop()
