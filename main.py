from multiprocessing import current_process
import pygame

ANCHO,ALTURA=600,600
FILAS,COLUMNAS=8,8

TAMANO_CUADRO=ANCHO//COLUMNAS

ROJO=(255,105,97)
BLANCO=(224,176,255)
NEGRO=(20,20,20)
GRIS=(128,128,128)
AZUL=(59,131,189)

CORONA=pygame.transform.scale(pygame.image.load("corona.png"), (45,25))

#PIEZAS--------------------------------
class PIEZAS:
    RELLENO=15
    BORDE=2

    def __init__(self,fil,col,color):
        self.fil=fil
        self.col=col
        self.color=color
        self.king=False
        self.x=0
        self.y=0
        self.calc_pos()
        
    def calc_pos(self):
        self.x=TAMANO_CUADRO*self.col+TAMANO_CUADRO//2
        self.y=TAMANO_CUADRO*self.fil+TAMANO_CUADRO//2

    def make_king(self):
        self.king=True

    def draw(self,win):
        radio=TAMANO_CUADRO//2-self.RELLENO
        pygame.draw.circle(win, GRIS, (self.x,self.y), radio+self.BORDE)
        pygame.draw.circle(win, self.color,(self.x,self.y), radio)
        if self.king:
            win.blit(CORONA, (self.x-CORONA.get_width()//2, self.y-CORONA.get_height()//2))
    
    def move(self, fil, col):
        self.fil=fil
        self.col=col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

#TABLERO/CASILLAS----------------------------------------------------------
class Tablero:
    def __init__(self):
        self.tablero=[]
        self.ROJO_left=self.BLANCO_left=12
        self.ROJO_kings=self.BLANCO_kings=0
        self.crear_tablero()  

    def draw_cuadrados(self,win):
        win.fill(NEGRO)
        for fil in range(FILAS):
            for col in range(fil%2, COLUMNAS, 2):
                pygame.draw.rect(win, ROJO, (fil*TAMANO_CUADRO, col*TAMANO_CUADRO, TAMANO_CUADRO, TAMANO_CUADRO))

    def move(self, pieza, fil, col):
        self.tablero[pieza.fil][pieza.col], self.tablero[fil][col]=self.tablero[fil][col], self.tablero[pieza.fil][pieza.col]

        if fil==FILAS-1 or fil==0:
            pieza.make_king()
            if pieza.color==BLANCO:
                self.BLANCO_kings+=1
            else:
                self.ROJO_kings+=1

    def get_pieza(self,fil,col):
        return self.tablero[fil][col]
    
    def crear_tablero(self):
        for fil in range(FILAS):
            self.tablero.append([])
            for col in range(COLUMNAS):
                if col%2==((fil+1)%2):
                    if(fil<3):
                        self.tablero[fil].append(PIEZAS(fil,col,BLANCO))
                    elif(fil>4):
                        self.tablero[fil].append(PIEZAS(fil,col,ROJO))
                    else:
                        self.tablero[fil].appned(0)
                else:
                    self.tablero[fil].append(0)
    
    def draw(self,win):
        self.draw_cuadrados(win)
        for fil in range(FILAS):
            for col in range(COLUMNAS):
                pieza=self.tablero[fil][col]
                if pieza!=0:
                    pieza.draw(win)
    
    def eliminar(self, piezas):
        for pieza in piezas:
            self.tablero[pieza.fil][pieza.col]
            if pieza!=0:
                if pieza.color==ROJO:
                    self.ROJO_left-=1
                else:
                    self.BLANCO_left-=1
    
    def ganador(self):
        if(self.ROJO_left<=0):
            return BLANCO
        elif(self.BLANCO_left<=0):
            return ROJO
        return None

    def movimientos_validos(self, pieza):
        movimiento={}
        izq=pieza.col-1
        der=pieza.col+1
        fil=pieza.fil

        if(pieza.color==ROJO or pieza.king):
            movimiento.update(self.atravezar_izq(fil-1, max(fil-3,-1),-1,pieza.color,izq)) 
            movimiento.update(self.atravezar_izq(fil-1, max(fil-3,-1),-1,pieza.color,der))

        if(pieza.color==BLANCO or pieza.king):
            movimiento.update(self.atravezar_izq(fil+1, min(fil+3, FILAS),1, pieza.color, izq)) 
            movimiento.update(self.atravezar_izq(fil+1, min(fil+3, FILAS),1, pieza.color, der))

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
                        fil=min(f+3, FILAS)
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
            if der >= COLUMNAS:
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
                        fil=min(f+3,FILAS)
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
        self.__init__()
        self.win=win
    
    def update(self):
        self.tablero.draw(self.win)
        self.draw_movimientos_validos(self.movimientos_validos)
        pygame.display.update()
    
    def _init(self):
        self.selected=None
        self.tablero=Tablero()
        self.turn=ROJO
        self.movimientos_validos={}

    def ganador(self):
        return self.tablero.ganador()

    def reset(self):
        self._init()

    def select(self,fil,col):
        if self.selected:
            result=self._move(fil,col)
            if not result:
                self.selected=None
                self.select(fil,col)
        
        pieza=self.tablero.get_pieza(fil,col)
        if pieza!=0 and pieza.color==self.turn:
            self.selected=pieza
            self.movimientos_validos=self.tablero.get_movimientos_validos(pieza)
            return True
        return False

        
        
        
        
    def _move(self, fil,col):
        pieza=self.tablero.get_pieza(fil,col)
        if self.selected and pieza==0 and (fil,col) in self.movimientos_validos:
            self.tablero.move(self.selected, fil,col)
            skipped=self.movimientos_validos[(fil,col)]
            if skipped:
                self.tablero.eliminar(skipped)
            self.change_turn()
        else:
            return False
        return True

    def draw_movimientos_validos(self, movimientos):
        for move in movimientos:
            fil,col=move
            pygame.draw.circle(self.win, AZUL, (col*TAMANO_CUADRO + TAMANO_CUADRO//2,fil*TAMANO_CUADRO+TAMANO_CUADRO//2,15))

    def change_turn(self):
        self.movimientos_validos=[]
        if self.turn==ROJO:
            self.turn=BLANCO
        else:
            self.turn=ROJO

#INDEX------------------------------------------------------
FPS=60
WIN=pygame.display.set_mode((ANCHO,ALTURA))
pygame.display.set_caption("Damas-Proyecto final")
 
def get_fil_col_from_mouse(pos):
    x,y=pos
    fil=y//TAMANO_CUADRO
    col=x//TAMANO_CUADRO
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
                fil, col=get_fil_col_from_mouse(pos)
                game.select(fil,col)
        game.update()
    pygame.quit()
main()
