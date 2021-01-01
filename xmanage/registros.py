#!/usr/bin/python3

import xml.etree.ElementTree as ET


def nuevo_registro(codigo,FechaStr,HoraStr,MinStr):
	#leer archivo
	archivo="xmls/registro.xml"
	tree = ET.parse(archivo)
	root = tree.getroot()
	#Crear registro
	entrada=ET.SubElement(root,'Entra')
	entrada.set("codigo",codigo)
	Fecha=ET.SubElement(entrada,"Fecha")
	Fecha.text=FechaStr
	Hora=ET.SubElement(entrada,"Hora")
	Hora.text=HoraStr
	Min=ET.SubElement(entrada,"Min")
	Min.text=MinStr
	#Reescribir archivo
	tree.write(archivo)

