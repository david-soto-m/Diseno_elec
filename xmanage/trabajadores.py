#!/usr/bin/python3

import xml.etree.ElementTree as ET


tree = ET.parse("../xmls/trabajadores.xml")
root = tree.getroot()
	
def es_trabajador(cadena):
	elemento=root.find("./Trabajador[@codigo='"+cadena+"']")
	if elemento is None:
		return(False,"")
	else:
		return(True,elemento.text)

if __name__=="__main__":
	print(es_trabajador("00001"))
