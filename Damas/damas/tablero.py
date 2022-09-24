import pygame
from .pieza import Pieza
from .constantes import cafe_oscuro,filas, cafe_claro,rojo, t_cuadrado,colu, blanco

class Tablero:
    def __init__(self):
        self.tablero=[] 
        self.cafe_claro_izq=self.blanco_izq=12
        self.rey_cafe_claro=self.rey_blanco=0
        self.crear_Tablero()

    def dibujar_cuadrados(self,ven):
        ven.fill(cafe_oscuro)
        for fila in range(filas):
            for col in range(fila%2,colu ,2 ):
                pygame.draw.rect(ven, cafe_claro, (fila*t_cuadrado,col*t_cuadrado, t_cuadrado, t_cuadrado))

    def mover(self, pieza, fila, col):
        self.tablero[pieza.fila][pieza.col], self.tablero[fila][col] = self.tablero[fila][col], self.tablero[pieza.fila][pieza.col]
        pieza.mover(fila, col)

        if fila == filas - 1 or fila == 0:
            pieza.crear_rey()
            if pieza.color == blanco:
                self.rey_blanco += 1
            else:
                self.rey_cafe_claro += 1 

    def get_pieza(self,fila,col):
        return self.tablero[fila][col]

    
    def crear_Tablero(self):
        for fila in range(filas):
            self.tablero.append([])
            for col in range(colu):
                if col%2==((fila+1)%2):
                    if(fila<3):
                        self.tablero[fila].append(Pieza(fila,col,blanco))
                    elif(fila>4):
                        self.tablero[fila].append(Pieza(fila,col,rojo))
                    else:
                        self.tablero[fila].append(0)
                else:
                    self.tablero[fila].append(0) 
    
    def dibujar(self,ven):
        self.dibujar_cuadrados(ven) 
        for fila in range(filas):
            for col in range(colu):
                pieza=self.tablero[fila][col]
                if pieza!=0:
                    pieza.dibujar(ven)

    def borrar(self,piezas):
        for pieza in piezas:
            self.tablero[pieza.fila][pieza.col]=0
            if pieza!=0:
                if pieza.color==cafe_claro:
                    self.cafe_claro_izq-=1
                else:
                    self.blanco_izq-=1

    def ganador(self):
        if self.cafe_claro_izq<=0:
            return blanco
        elif(self.blanco_izq<=0):
            return cafe_claro
        return None 

    def get_movimientos_validos(self, pieza):
        movimientos = {}
        izquierda = pieza.col - 1
        derecha = pieza.col + 1
        fila = pieza.fila

        if pieza.color == cafe_claro or pieza.rey:
            movimientos.update(self._diagonal_izq(fila -1, max(fila-3, -1), -1, pieza.color, izquierda))
            movimientos.update(self._diagonal_der(fila -1, max(fila-3, -1), -1, pieza.color, derecha))
        if pieza.color == blanco or pieza.rey:
            movimientos.update(self._diagonal_izq(fila +1, min(fila+3, filas), 1, pieza.color, izquierda))
            movimientos.update(self._diagonal_der(fila +1, min(fila+3, filas), 1, pieza.color, derecha))
    
        return movimientos 
    
    def _diagonal_izq(self, iniciar, parar, paso,color,izquierda,skipped=[]):
        movimientos={}
        final=[]
        for i in range(iniciar,parar,paso):
            if(izquierda<0):
                break
            ahora=self.tablero[i][izquierda]    
            if ahora==0: #SI ES VERDADERO, ENCONTRARA UN CUADRO VACIO 
                if skipped and not final:
                    break
                elif skipped:
                    movimientos[(i,izquierda)]=final+skipped
                else:
                    movimientos[(i,izquierda)]=final    

                if final:
                    if paso== -1:   
                        fila=max(i-3,0)
                    else:
                        fila=min(i+3,filas)
                    movimientos.update(self._diagonal_izq(i+paso, fila, paso, color, izquierda-1,skipped=final))
                    movimientos.update(self._diagonal_der(i+paso, fila, paso, color, izquierda+1,skipped=final))
                break
            elif( ahora.color==color):
                break
            else:
                final=[ahora]

            izquierda-=1

        return  movimientos

    def _diagonal_der(self, iniciar, parar, paso,color,derecha,skipped=[]):
        movimientos={}
        final=[]
        for i in range(iniciar,parar,paso):
            if(derecha>=colu):
                break
            ahora=self.tablero[i][derecha]
            if ahora==0: #SI ES VERDADERO, ENCONTRARA UN CUADRO VACIO 
                if skipped and not final:
                    break
                elif skipped:
                    movimientos[(i,derecha)]=final+skipped
                else:
                    movimientos[(i,derecha)]=final

                if final:
                    if paso==-1:
                        fila=max(i-3,0)
                    else:
                        fila=min(i+3,filas)

                    movimientos.update(self._diagonal_izq(i+paso, fila, paso, color, derecha-1,skipped=final))
                    movimientos.update(self._diagonal_der(i+paso, fila, paso, color, derecha+1,skipped=final))
                break
            elif( ahora.color==color):
                break
            else:
                final=[ahora]

            derecha+=1
        return movimientos
