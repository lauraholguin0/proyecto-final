from .constantes import rojo,blanco,t_cuadrado, gris, corona
import pygame

class Pieza:

    padding=15
    borde=2


    def __init__(self,fila,col,color):
        self.fila=fila
        self.col=col
        self.color=color
        self.rey=False        
        self.x=0
        self.y=0
        self.calc_pos()

    def calc_pos(self): #POSICION DE LAS FICHAS 
        self.x=t_cuadrado*self.col+t_cuadrado//2
        self.y=t_cuadrado*self.fila+t_cuadrado//2

    def crear_rey(self): #VOLVER UNA FICHA REYco
        self.king=True
    
    def dibujar(self, ven): #TAMAÑO DE LAS FICHAS
        radio=t_cuadrado//2-self.padding
        pygame.draw.circle(ven, gris,(self.x,self.y),radio+self.borde)
        pygame.draw.circle(ven, self.color,(self.x,self.y),radio)
        if self.rey:
            ven.blit(corona, (self.x-corona.get_width()//2, self.y-corona.get_height()//2))

    def mover(self,fila,col):
             self.fila=fila
             self.col=col
             self.calc_pos()

    def __repr__(self):
        #PARA EL DEBBUGING
        return str(self.color)

        

