#!/usr/bin/python3

import xml.etree.ElementTree as ET


	
def es_trabajador(cadena):
	tree = ET.parse("xmls/trabajadores.xml")
	root = tree.getroot()
	elemento=root.find("./Trabajador[@codigo='"+cadena+"']")
	if elemento is None:
		return(False,"")
	else:
		return(True,elemento.text)
