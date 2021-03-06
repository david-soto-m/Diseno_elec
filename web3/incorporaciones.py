#!/usr/bin/python3
import xml.etree.ElementTree as ET

def comprueba_valido(codigo):
	respuesta = True
	if len(codigo)!=5:
		respuesta=False
	else:
		try:
			a = int(codigo)
		except:
			respuesta = False
	if respuesta==True:
		tree = ET.parse("/home/pi/Diseno_elec/xmls/trabajadores.xml")
		#tree = ET.parse("../xmls/trabajadores.xml")
		root = tree.getroot()
		elemento=root.find("./Trabajador[@codigo='"+codigo+"']")
		if elemento is not None:
			respuesta = False
	return respuesta

def nuevo_registro(codigo,nombre):
	#leer archivo
	archivo="/home/pi/Diseno_elec/xmls/trabajadores.xml"
	#archivo="../xmls/trabajadores.xml"
	tree = ET.parse(archivo)
	root = tree.getroot()
	#Crear registro
	entrada=ET.SubElement(root,'Trabajador')
	entrada.set("codigo",codigo)
	entrada.text = nombre
	#Reescribir archivo
	tree.write(archivo)
