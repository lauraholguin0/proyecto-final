import pygame
from tkinter import *

ancho,altura=600,600
filas,columnas=8,8

t_cuadro=ancho//columnas

rojo=(255,105,97)
blanco=(224,176,255)
negro=(20,20,20)
gris=(128,128,128)
azul=(59,131,189)

corona=pygame.transform.scale(pygame.image.load("corona.png"), (45,25))

#PIEZAS--------------------------------
class pieces:
    relleno=15
    borde=2

    def __init__(self,fila,colu,color):
        self.fila=fila
        self.colu=colu
        self.color=color
        self.rey=False
        self.x=0
        self.y=0
        self.calc_pos()
        
    def calc_pos(self):
        self.x=t_cuadro*self.colu+t_cuadro//2
        self.y=t_cuadro*self.fila+t_cuadro//2

    def make_king(self):
        self.rey=True

    def draw(self,win):
        radio=t_cuadro//2-self.relleno
        pygame.draw.circle(win, gris, (self.x,self.y), radio+self.borde)
        pygame.draw.circle(win, self.color,(self.x,self.y), radio)
        if self.rey:
            win.blit(corona, (self.x-corona.get_width()//2, self.y-corona.get_height()//2))
    
    def move(self, fila, colu):
        self.fila=fila
        self.colu=colu
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

#TABLERO/CASILLAS----------------------------------------------------------
class Tablero:
    def __init__(self):
        self.tablero=[]
        self.rojo_I=self.blanco_I=12
        self.rojo_kings=self.blanco_kings=0
        self.crear_tablero()  

    def draw_cuadrados(self,win):
        win.fill(negro)
        for fila in range(filas):
            for colu in range(fila%2, columnas, 2):
                pygame.draw.rect(win, rojo, (fila*t_cuadro, colu*t_cuadro, t_cuadro, t_cuadro))

    def move(self, pieza, fila, colu):
        self.tablero[pieza.fila][pieza.colu], self.tablero[fila][colu]=self.tablero[fila][colu], self.tablero[pieza.fila][pieza.colu]

        if fila==filas-1 or fila==0:
            pieza.crear_rey()
            if pieza.color==blanco:
                self.blanco_kings+=1
            else:
                self.rojo_kings+=1

    def get_pieza(self,fila,colu):
        return self.tablero[fila][colu]
    
    def crear_tablero(self):
        for fila in range(filas):
            self.tablero.append([])
            for colu in range(columnas):
                if colu%2==((fila+1)%2):
                    if(fila<3):
                        self.tablero[fila].append(pieces(fila,colu,blanco))
                    elif(fila>4):
                        self.tablero[fila].append(pieces(fila,colu,rojo))
                    else:
                        self.tablero[fila].append(0)
                else:
                    self.tablero[fila].append(0)
    
    def draw(self,win):
        self.draw_cuadrados(win)
        for fila in range(filas):
            for colu in range(columnas):
                pieza=self.tablero[fila][colu]
                if pieza!=0:
                    pieza.draw(win)
    
    def eliminar(self, piezas):
        for pieza in piezas:
            self.tablero[pieza.fila][pieza.colu]
            if pieza!=0:
                if pieza.color==rojo:
                    self.rojo_I-=1
                else:
                    self.blanco_I-=1
    
    def ganador(self):
        if(self.rojo_I<=0):
            return blanco
        elif(self.blanco_I<=0):
            return rojo
        return None

    def get_movimientos_validos(self, pieza):
        movimiento={}
        izq=pieza.colu-1
        der=pieza.colu+1
        fila=pieza.fila

        if(pieza.color==rojo or pieza.rey):
            movimiento.update(self.atravezar_izq(fila-1, max(fila-3,-1),-1,pieza.color,izq)) 
            movimiento.update(self.atravezar_izq(fila-1, max(fila-3,-1),-1,pieza.color,der))

        if(pieza.color==blanco or pieza.rey):
            movimiento.update(self.atravezar_izq(fila+1, min(fila+3, filas),1, pieza.color, izq)) 
            movimiento.update(self.atravezar_izq(fila+1, min(fila+3, filas),1, pieza.color, der))

        return movimiento 

    def atravezar_izq(self, start, stop, step, color, izq, skipped=[]):
        movimientos={}
        last=[]
        for f in range(start,stop,step):
            if izq<0:
                break

            current=self.tablero[f][izq]
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    movimientos[(f,izq)]=last+skipped
                else:
                    movimientos[(f,izq)]=last
                if last:
                    if step==-1:
                        fil=max(f-3,0)
                    else:
                        fil=min(f+3, filas)
                    movimientos.update(self.atravezar_izq(f+step,fil,step,color,izq-1,skipped=last))
                    movimientos.update(self.atravezar_izq(f+step,fil,step,color,izq+1,skipped=last))
                break
            elif current.color==color:
                break
            else:
                last=[current]
            izq-=1
        return movimientos

    def atravezar_derecha(self,start,stop,step,color,der,skipped=[]):
        movimientos={}
        last=[]
        for f in range(start, stop, step):
            if der >= columnas:
                break


            current=self.tablero[f][der]
            if current ==0:
                if skipped and not last:
                    break
                elif skipped:
                    movimientos[(f,der)]=last+skipped
                else:
                    movimientos[(f,der)]=last

                if last:
                    if step==-1:
                        fil=max(f-3,0)
                    else:
                        fil=min(f+3,filas)
                    movimientos.update(self.atravezarizq(f+step, fil, step, color, der-1, skipped=last))
                    movimientos.update(self.atravezarizq(f+step, fil, step, color, der+1, skipped=last))
                break
            elif current.color==color:
                break
            else:
                last=[current]
            der+=1
        return movimientos

#MANEJO DEL JUEGO--------------------------------------------------------------
class Juego:
    def __init__(self,win):
        self._init()
        self.win=win
    
    def update(self):
        self.tablero.draw(self.win)
        self.draw_movimientos_validos(self.movimientos_validos)
        pygame.display.update()
    
    def _init(self):
        self.selected=None
        self.tablero=Tablero()
        self.turn=rojo
        self.movimientos_validos={}

    def ganador(self):
        return self.tablero.ganador()

    def reset(self):
        self._init()

    def select(self,fila,colu):
        if self.selected:
            result=self._move(fila,colu)
            if not result:
                self.selected=None
                self.select(fila,colu)
        
        pieza=self.tablero.get_pieza(fila,colu)
        if pieza!=0 and pieza.color==self.turn:
            self.selected=pieza
            self.movimientos_validos=self.tablero.get_movimientos_validos(pieza)
            return True
        return False

        
        
        
        
    def _move(self, fila,colu):
        pieza=self.tablero.get_pieza(fila,colu)
        if self.selected and pieza==0 and (fila,colu) in self.movimientos_validos:
            self.tablero.move(self.selected, fila,colu)
            skipped=self.movimientos_validos[(fila,colu)]
            if skipped:
                self.tablero.eliminar(skipped)
            self.change_turn()
        else:
            return False
        return True

    def draw_movimientos_validos(self, movimientos):
        for move in movimientos:
            fil,col=move
            pygame.draw.circle(self.win, azul, (col*t_cuadro + t_cuadro//2,fil*t_cuadro+t_cuadro//2),15)

    def change_turn(self):
        self.movimientos_validos=[]
        if self.turn==rojo:
            self.turn=blanco
        else:
            self.turn=rojo

#INDEX------------------------------------------------------
FPS=60
WIN=pygame.display.set_mode((ancho,altura))
pygame.display.set_caption("Damas-Proyecto final")
 
def get_fil_col_from_mouse(pos):
    x,y=pos
    fil=y//t_cuadro
    col=x//t_cuadro
    return fil,col

def main():
    run=True
    clock=pygame.time.Clock()
    game=Juego(WIN)

    while run:
        clock.tick(FPS)

        if(game.ganador()!= None):
            print(game.ganador())
            run=False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                fila, colu=get_fil_col_from_mouse(pos)
                game.select(fila,colu)
        game.update()
    pygame.quit()
main()
