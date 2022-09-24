from turtle import width
import pygame

width,height=600,600 #TAMAÑO PANTALLA

filas,colu=8,8 #NUMERO FILAS COLUMNAS
t_cuadrado=width//colu

#COLORES
negro=(0,0,0)
rojo=(255,0,0)
azul=(0,0,255)
blanco=(255,255,255)
gris=(128,128,128)

corona=pygame.transform.scale(pygame.image.load('damas/crown.png'),(44,25)) #IMAGEN DEL REY 
