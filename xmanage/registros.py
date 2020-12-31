#!/usr/bin/python3

import xml.etree.ElementTree as ET

archivo="../xmls/registro.xml"
tree = ET.parse(archivo)
root = tree.getroot()

def nuevo_registro(codigo,FechaStr,HoraStr,MinStr):
	#Crear registro
	entrada=ET.SubElement(root,'Entra')
	entrada.set("codigo",codigo)
	Fecha=ET.SubElement(entrada,"Fecha")
	Fecha.text=FechaStr
	Hora=ET.SubElement(entrada,"Hora")
	Hora.text=HoraStr
	Min=ET.SubElement(entrada,"Min")
	Min.text=MinStr
	#Unir al bloque principal
	#Reescribir archivo
	tree.write(archivo)

if __name__=="__main__":
	nuevo_registro("00001","31/12/20","12","04")
