#ESTA CLASE ES EL CONTROLADOR DEL TABLERO
import pygame
from damas.tablero import Tablero
from .constantes import cafe_claro,blanco,azul,t_cuadrado

class Juego:
    def __init__(self,ven):
        self._init()
        self.ven=ven

    def actualizar(self): 
        self.tablero.dibujar(self.ven)
        self.dibujar_movimientos_validos(self.movimientos_validos)
        pygame.display.update()
    
    def _init(self):
        self.selected=None
        self.tablero=Tablero()
        self.turn=cafe_claro
        self.movimientos_validos={}
    
    def ganador(self):
        return self.tablero.ganador()


    def reset(self):
        self._init()

    def selec_filcol(self,fila,col): #TRATA DE MOVER LA FICHA A LA COLUMNA Y A LA FILA 
        if self.selected:
            resultado=self._mover(fila,col)
            if not resultado:
                self.selected=None
                self.selec_filcol(fila,col)

        pieza=self.tablero.get_pieza(fila,col)
        if(pieza!=0 and pieza.color==self.turn):
            self.selected=pieza
            self.movimientos_validos=self.tablero.get_movimientos_validos(pieza)
            return True
        
        return False


    def _mover(self,fila,col):
        pieza=self.tablero.get_pieza(fila,col)
        if self.selected and pieza==0 and (fila,col) in self.movimientos_validos:
            self.tablero.mover(self.selected, fila, col) #MOVER LA FICHA A LA FILA Y COLUMNA SELECCIONADA
            skipped=self.movimientos_validos[(fila,col)]
            if skipped:
                self.tablero.borrar(skipped)
            self.cambio_turno()
        else:
            return False


        return True

    def dibujar_movimientos_validos(self,movimientos):
        for movi in movimientos:
            fil,col=movi            
            pygame.draw.circle(self.ven,azul,(col*t_cuadrado+t_cuadrado//2,fil*t_cuadrado+t_cuadrado//2), 15)

    def cambio_turno(self):
        self.movimientos_validos={}
        if self.turn==cafe_claro:
            self.turn=blanco
        else:
            self.turn=cafe_claro
