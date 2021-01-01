


# ESTO TIENE QUE ESTAR MAL, porque "incoporaciones.py" están
# en la carpeta xmanage, pero este archivo está en web3
import xmanage.incorporaciones as I

from twython import Twython



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
fichero = open("nombre.txt", "r")
nombre = fichero.readline()
fichero.close

fichero = open("codigo.txt", "r")
codigo = fichero.readline()
fichero.close

fichero = open("publicar.txt", "r")
publicar = fichero.readline()
fichero.close

respuesta = I.comprueba_valido()

if respuesta:
    I.nuevo_registro(codigo,nombre)

    if publicar=="Si":
        publica_en_twitter(nombre)



        
