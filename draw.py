from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
	if(x0 > x1): #swap points so that x0 is the smaller one
		tmp = x0
		x0 = x1
		x1 = tmp
		tmp = y0
		y0 = y1
		y1 = tmp
	A = y1 - y0
	B = -1 * (x1 - x0)
	slope = A / (B * -1.0)
	if(slope > 0): #octant 1
		d = 2 * A + B
		while x0 <= x1:
			plot(screen,color,x0,y0)
			if(d > 0):
				y0 += 1
				d += 2 * B
			x0 += 1
			d += 2 * A
		return
