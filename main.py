#!/usr/bin/python3
import xmanage.registros as R
import xmanage.trabajadores as T
def main():
    R.nuevo_registro("00001","1/1/21","12","04")
    print(T.es_trabajador("00001"))
    print(T.es_trabajador("00002"))

if __name__=="__main__":
    main()
# No conocia esta forma de hacer lo que has hecho
# Con lo que yo he aprendido simplemente hubiera puesto: main()
# Lo de __main__, ¿qué es una especie de main predefinido de python??
# Sip, sirve para que puedas hacer cosas distintas dependiendo de si importas al paquete o lo llamas directamente para ejecución

