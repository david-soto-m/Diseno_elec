#!/usr/bin/python3
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640,480)
camera.rotation = 180
camera.capture('foto.jpg')
camera.close()

 
