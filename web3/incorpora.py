#!/usr/bin/python3

#import incorporaciones as I 
#from twython import Twython
import sys

#################################################
#def publica_en_twitter(nombre):
	#Twitter: @RpiMarcelo
	#APP_KEY = "wvbENKZWzWGbBnV1O93z9BaKW"
	#APP_SECRET = "qK76rTuHGwTkWukZvt1ce6zVwpI0yoKxDz1qQBgSXpGaHKiHac"
	#OAUTH_TOKEN = "1334992616853794817-CmrY3VgiifqRItNQAMFhQCEEFYROY5"
	#OAUTH_TOKEN_SECRET = "VSIDNE824r14dpNQ5Hsa8lQfdP1xH9BhCOxc6AwQpxiyd"
	#twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	#Texto = nombre + " se ha incorporado a nuestra empresa. ¡Bienvenido!"
	#Publicación del tweet
	#twitter.update_status(status=Texto)
#########################################################
# Lectura de la informacion de publicacion del trabajador

reparto=" ".join(sys.argv[1:]).split("-*-")
codigo = reparto[0]
nombre = reparto[1]
publicar = reparto[2] =="0"
print(codigo,nombre,publicar)
#respuesta = I.comprueba_valido(codigo)

#if respuesta:
	#I.nuevo_registro(codigo,nombre)
	
	#if publicar=="Si":
		#publica_en_twitter(nombre)
#else:
	#print("Invalido")
