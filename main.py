from display import *
from draw import *

screen = new_screen()
color = [ 255, 0 , 0 ]

draw_line(10,10,50,50,screen,color)
draw_line(10,10,50,250,screen,color)
draw_line(10,50,50,10,screen,color)
draw_line(10,250,50,10,screen,color)
draw_line(10,10,50,10,screen,color)
draw_line(30,10,30,250,screen,color)
display(screen)
save_extension(screen, 'img.png')
