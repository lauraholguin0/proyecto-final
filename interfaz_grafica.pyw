import tkinter as tk
class app():
    def __init__(self, lado_cuadrado):
        self.lado_cuadrado=lado_cuadrado

        self.raiz=tk.Tk()
        self.raiz.title("Juego de Damas Chinas")
        self.raiz.iconbitmap("imagenes/damas.ico")
        self.raiz.config(bg="green")
        
        #pantalla completa
        ancho_ventana=self.raiz.winfo_screenwidth()
        alto_ventana=self.raiz.winfo_screenheight()
        #centrar en cualquier tamaño de ventana
        x_ventana=self.raiz.winfo_screenwidth()//2-ancho_ventana//2
        y_ventana=self.raiz.winfo_screenheight()//2-alto_ventana//2
        
        posicion=str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(x_ventana)+"+"+str(y_ventana)
        self.raiz.geometry(posicion)
        self.interfaz2=tk.Canvas()
        self.interfaz=tk.Canvas()
        self.interfaz2.pack()
        self.interfaz2.config(width="684.8",height="50",bg="green")
        self.interfaz.pack(fill="y",expand=True)
        self.interfaz.config(width=(ancho_ventana/2),height=(alto_ventana/2),bg="#000",cursor="circle")

    def __call__(self):
        self.raiz.mainloop()

    def tablero(self):
        for i in range(8):
            for l in range(8): 
                if(i+l)%2==0:
                    self.interfaz.create_rectangle(i*self.lado_cuadrado,l*self.lado_cuadrado,(i+1)*self.lado_cuadrado,(l+1)*self.lado_cuadrado,fill="dark red")
                else:
                    self.interfaz.create_rectangle(i*self.lado_cuadrado,l*self.lado_cuadrado,(i+1)*self.lado_cuadrado,(l+1)*self.lado_cuadrado,fill="grey")
inicio1=app(85.6)
inicio1.tablero()
inicio1()
