import pygame
from damas.constantes import width, height,t_cuadrado,rojo
from damas.juego import Juego

#CONFIGURACION VENTANA----------------------------------
FPS=60
ven=pygame.display.set_mode((width,height))
#Titulo
pygame.display.set_caption("Damas Chinas")
#CONFIGURACION VENTANA----------------------------------

def get_filcol_from_mouse(pos):
    x,y=pos
    fila=y//t_cuadrado
    col=x//t_cuadrado
    return fila,col

#MAINLOOP----------------------------------
def main():
    correr=True
    #FPS a los que ira el juego, FrameRate
    clock=pygame.time.Clock()
    juego=Juego(ven)

    while correr:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                correr=False

            #MOVIMIENTO DE LAS FICHAS EN EL TABLERO
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                fila, col=get_filcol_from_mouse(pos)
                juego.selec_filcol(fila,col)

        
        juego.actualizar()

    pygame.quit()

main()