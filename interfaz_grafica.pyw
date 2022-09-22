from tkinter import *
import tkinter as tk
from tkinter import ttk
import pygame

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
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
PADDING = 15
OUTLINE = 2

def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

def make_king(self):
        self.king = True
    
def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

def __repr__(self):
        return str(self.color)

raiz.mainloop()
