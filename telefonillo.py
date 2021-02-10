# Espera la pulsacion del boton central del senseHat
# Se le debe indicar si:
#       trabajador -> joystick dcha
#           Mete codigo (eligiendo numeros con el joystick)
#           Bienvenido / no registrado
#               Busqueda > Funcion:(bool,str)= es_Trabajador(Codigo)
#                   Está registrado: Escritura registro de entradas a la empresa-> Funcion: Añade un registro al xml->reg_entrada(Codigo,hora)
#                   No está registrado: foto para guardar intruso, y enviarla por correo
#       repartidor -> joystick izq
#           Notificacion por email a recepcion (solo notificacion, sin foto)



# Estados:
#   estado 0: esperando que alguien llegue al telefonillo
#   estado 1: esperando que nos indique si es trabajador o repartidor
#   estado 2: es trabajador, y debe meter los numeros con el joystick
#   estado 3: es repartidor



#
#
#


import xmanage.trabajadores as T
import xmanage.registros as R

from time import sleep
from time import localtime

from sense_hat import SenseHat
from picamera import PiCamera

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os

sense=SenseHat()
sense.clear()

naranja = [255, 146, 0]
azul = [0, 30, 255]
blanco = [255, 255, 255]
verde = [0, 255, 50]
rojo = [255, 0, 0]
negro = [0,0,0]
gris = [125, 125, 125]


PANTALLA = []

def cambiar_color_fondo(color):
    global PANTALLA
    O = color
    PANTALLA = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]


codigo_trabajador = []
cont_codigo = 0
num_mostrado = 0

respuesta = False
nombre = []

estado = 0
estado_ant = 0





################################################################################
def convertir_vector_decimal(vector, n_digitos):
    codigo = 0
    multiplicador = 1
    for i in range(n_digitos-1, -1, -1):
        codigo = codigo + vector[i]*multiplicador
        multiplicador = multiplicador*10

    return codigo


def convertir_vector_cadena(vector, n_digitos):
    cadena = ""
    for i in range(0, n_digitos):
        cadena = cadena + str(vector[i])

    return cadena


################################################################################
def sacar_foto_intruso():
    camera = PiCamera()

    camera.resolution = (640,480)
    camera.rotation = 180               # Rotamos la imagen de la camara
    camera.start_preview(fullscreen=False, window=(30,30,320,240))

    sleep(2)

    # Comprobamos el numero de la foto de intruso que toca
    DIR = "./fotos_intrusos"
    cont_instrusos = len(os.listdir(DIR))

    # Capturamos la imagen y la guardamos en el fichero indicado
    nombre_archivo = "foto_intruso_" + str(cont_instrusos)
    nombre_completo = DIR + "/" + nombre_archivo + '.jpg'
    camera.capture(nombre_completo)

    # Cierre de la ventana de previsualizacion
    camera.stop_preview()

    # Enviamos la foto por correo a la administracion
    enviar_foto_intruso(cont_instrusos, nombre_completo)

    # Cerramos la camara para que pueda ser usada por la Repeccion
    camera.close()


################################################################################

def enviar_foto_intruso(contador_intruso, nombre_foto):
    direccion_fuente = "smartfonillorpi@gmail.com"
    direccion_destino = "smartfonillorpi@gmail.com"
    password = "Smartfonillo1234"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(direccion_fuente, password)

    msg = MIMEMultipart()
    msg['From'] = direccion_fuente
    msg['To'] = direccion_destino
    msg['Subject'] = "Foto del intruso número " + str(contador_intruso)


    instante = localtime()
    ano = instante.tm_year
    mes = instante.tm_mon
    dia = instante.tm_mday
    hora = instante.tm_hour
    min = instante.tm_min
    str_hora = str(dia)+"/"+str(mes)+"/"+str(ano)+" a las "+str(hora)+":"+str(min)

    cuerpo_mensaje = "Un nuevo intruso ha intentado acceder al complejo\n" + str_hora
    msg.attach(MIMEText(cuerpo_mensaje, 'plain'))


    archivo = nombre_foto
    adjunto = open(archivo, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((adjunto).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % archivo)
    msg.attach(part)

    texto = msg.as_string()

    try:
        print("Enviando email con foto del intruso")
        server.sendmail(direccion_fuente, direccion_destino, texto)
    except:
        print("Error al enviar el email")
        server.quit()

    server.quit()



################################################################################

def enviar_notificacion_repartidor():
    direccion_fuente = "smartfonillorpi@gmail.com"
    direccion_destino = "smartfonillorpi@gmail.com"
    password = "Smartfonillo1234"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(direccion_fuente, password)

    msg = MIMEMultipart()
    msg['From'] = direccion_fuente
    msg['To'] = direccion_destino
    msg['Subject'] = "Notificación de repartidor esperando"

    instante = localtime()
    ano = instante.tm_year
    mes = instante.tm_mon
    dia = instante.tm_mday
    hora = instante.tm_hour
    min = instante.tm_min
    str_hora = str(dia)+"/"+str(mes)+"/"+str(ano)+" a las "+str(hora)+":"+str(min)

    cuerpo_mensaje = "Hay un repartidor esperando en la puerta\n" + str_hora
    msg.attach(MIMEText(cuerpo_mensaje, 'plain'))

    texto = msg.as_string()

    try:
        print("Enviando email de notificación de repartidor")
        server.sendmail(direccion_fuente, direccion_destino, texto)
    except:
        print("Error al enviar el email")
        server.quit()

    server.quit()


    
    
################################################################################


if __name__=="__main__":
    cambiar_color_fondo(gris)
    sense.set_pixels(PANTALLA)
    sleep(1)
    sense.clear()

    bucle=True
    while bucle:
        if estado_ant != estado:
            print("-Estado: " + str(estado))
            estado_ant = estado

        # estado 0: espera inicial
        if estado == 0:
            codigo_trabajador = []
            cont_codigo = 0

            events = sense.stick.get_events()
            for event in events:
                # Llega alguien al telefonillo
                if event.direction  == "middle":
                    estado = 1
                if event.direction  == "up"and event.action != "released":
                    bucle = False



        # estado 1: esperando que nos indique si es trabajador o repartidor
        if estado == 1:
            # Muestra interrogacion
            sense.show_letter("?", text_colour=naranja)

            #Espera a que se pulse dcha o izqda
            events = sense.stick.get_events()

            for event in events:
                # Trabajador
                if event.direction  == "right"and event.action != "released":
                    estado = 2

                # Repartidor
                if event.direction  == "left"and event.action != "released":
                    estado = 3



        # estado 2: es trabajador, y debe meter los numeros con el joystick
        if estado == 2:
            sense.show_letter(str(num_mostrado), text_colour=azul)
            events = sense.stick.get_events()
            for event in events:
                if event.direction  == "down" and event.action != "released":
                    num_mostrado = num_mostrado - 1
                    if num_mostrado==-1:
                        num_mostrado = 9
                if event.direction  == "up" and event.action != "released":
                    num_mostrado = num_mostrado + 1
                    if num_mostrado==10:
                        num_mostrado = 0

                if event.direction  == "middle" and event.action != "released":
                    #codigo_trabajador[cont_codigo] = num_mostrado
                    codigo_trabajador.append(num_mostrado)
                    cont_codigo +=1
                    print(codigo_trabajador)
                    cambiar_color_fondo(azul)
                    sense.set_pixels(PANTALLA)
                    sleep(0.5)  
                    cambiar_color_fondo(negro)
                    sense.set_pixels(PANTALLA)

                # Cuando el trabajador termina de meter el código:
                if event.direction  == "right"and event.action != "released":
                    num_mostrado = 0

                    #codigo_decimal = convertir_vector_decimal(codigo_trabajador, cont_codigo)
                    codigo_cadena = convertir_vector_cadena(codigo_trabajador, cont_codigo)
                    print("Cadena del código: " + codigo_cadena)
                    # Llamada a la funcion de comprobacion de si es trabajador:
                    (respuesta, nombre) = T.es_trabajador(codigo_cadena)

                    if respuesta:
                        print("Bienvenido ", nombre)
                        cambiar_color_fondo(verde)
                        sense.set_pixels(PANTALLA)
                        sleep(1)
                        sense.show_message(nombre,scroll_speed=0.2, back_colour=negro, text_colour=verde)
                        cambiar_color_fondo(negro)
                        sense.set_pixels(PANTALLA)
                        # Instante de entrada al edificio
                        instante = localtime()
                        ano = instante.tm_year
                        mes = instante.tm_mon
                        dia = instante.tm_mday
                        hora = instante.tm_hour
                        min = instante.tm_min
                        FechaStr = str(dia)+"/"+str(mes)+"/"+str(ano)
                        HoraStr = str(hora)
                        MinStr = str(min)

                        # Llamada a la funcion de guardado en el registro de la informacion del trabajador
                        R.nuevo_registro(codigo_cadena, FechaStr, HoraStr, MinStr)

                    else:
                        # Encendemos la pantalla del senseHat en rojo
                        cambiar_color_fondo(rojo)
                        sense.set_pixels(PANTALLA)
                        
                        # Tomamos una foto al intruso
                        print("Tomando foto al intruso")
                        sacar_foto_intruso()
                        cambiar_color_fondo(negro)
                        sense.set_pixels(PANTALLA)

                    # Volvemos al estado inicial
                    estado = 0

        if estado == 3:
            # Encendemos la pantalla del senseHat en naranja parpadeando
            cambiar_color_fondo(naranja)
            sense.set_pixels(PANTALLA)
            sleep(0.8)

            # Encendemos la pantalla del senseHat en negro parpadeando
            cambiar_color_fondo(negro)
            sense.set_pixels(PANTALLA)
            sleep(0.8)

            # Encendemos la pantalla del senseHat en naranja parpadeando
            cambiar_color_fondo(naranja)
            sense.set_pixels(PANTALLA)
            sleep(0.5)
            cambiar_color_fondo(negro)
            sense.set_pixels(PANTALLA)

            enviar_notificacion_repartidor()

            estado = 0




    cambiar_color_fondo(gris)
    sense.set_pixels(PANTALLA)
    sleep(1)
    sense.clear()
    
# Fin del main

