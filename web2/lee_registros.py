#!/usr/bin/python3 

import xml.etree.ElementTree as ET

trabajadores_XML = ET.parse("/home/pi/Diseno_elec/xmls/trabajadores.xml")
trabajadores = trabajadores_XML.getroot()

registros_XML = ET.parse("/home/pi/Diseno_elec/xmls/registro.xml")
registros = registros_XML.getroot()


for trabajador in trabajadores:
	print("<h2>",trabajador.text,"</h2>")
	print('<table>\n<thead>\ntr class="header">\n<th>Hora</th>\n<th>Fecha</th>\n</tr>\n</thead>')
	i=0
	print("<tbody>")
	for entrada in registros.findall("./Entra[@codigo='"+trabajador.attrib["codigo"]+"']"):
		if i%2==0:
			print("<tr class=\"even\">")
		else:
			print("<tr class=\"odd\">")
		fecha=entrada.find("Fecha").text
		hora=entrada.find("Hora").text
		minu=entrada.find("Min").text
		print("<td>",hora,":",minu,"</td>")
		print("<td>",fecha,"</td>")
		print("</tr>")
		i+=1
	print("</tbody>")
