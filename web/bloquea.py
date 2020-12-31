from time import sleep
from sense_hat import SenseHat

def cambiar_color_fondo(color):
	O = color
	scr= [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
	return scr

rojo = [255, 0, 50]
negro = [0,0,0]
sense=SenseHat()
for i in range(3):
	scr=cambiar_color_fondo(verde)
	sense.set_pixels(scr)
	sleep(0.5)
	scr=cambiar_color_fondo(negro)
	sense.set_pixels(scr)
	sleep(0.5)
