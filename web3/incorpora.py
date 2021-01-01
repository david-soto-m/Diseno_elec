#!/usr/bin/python3

import incorporaciones as I 
from twython import Twython
import sys

#########################################################
def publica_en_twitter(nombre):
	# Twitter: @RpiMarcelo
	APP_KEY = "wvbENKZWzWGbBnV1O93z9BaKW"
	APP_SECRET = "qK76rTuHGwTkWukZvt1ce6zVwpI0yoKxDz1qQBgSXpGaHKiHac"
	OAUTH_TOKEN = "1334992616853794817-CmrY3VgiifqRItNQAMFhQCEEFYROY5"
	OAUTH_TOKEN_SECRET = "VSIDNE824r14dpNQ5Hsa8lQfdP1xH9BhCOxc6AwQpxiyd"
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	Texto = nombre + " se ha incorporado a nuestra empresa. ¡Bienvenido!"
	# Publicación del tweet
	twitter.update_status(status=Texto)
#########################################################
# Lectura de la informacion de publicacion del trabajador

print(sys.argv)
#codigo = sys.argv[1]
#nombre = sys.argv[2]
#publicar = sys.argv[3]=="0"

#respuesta = I.comprueba_valido(codigo)

#if respuesta:
	#I.nuevo_registro(codigo,nombre)
	
	#if publicar=="Si":
		#publica_en_twitter(nombre)
#else:
	#print("Invalido")
