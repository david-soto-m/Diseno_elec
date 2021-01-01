#!/usr/bin/python3 

import xml.etree.ElementTree as ET
trabajadores_XML = ET.parse("/home/pi/Diseno_elec/xmls/trabajadores.xml")
#trabajadores_XML = ET.parse("../xmls/trabajadores.xml")
trabajadores = trabajadores_XML.getroot()

registros_XML = ET.parse("/home/pi/Diseno_elec/xmls/registro.xml")
#registros_XML = ET.parse("../xmls/registro.xml")
registros = registros_XML.getroot()

f = open("table.html", "w")
for trabajador in trabajadores:
	
	f.write("<h2>"+trabajador.text+"</h2>\n")
	f.write('<table>\n<thead>\n<tr class="header">\n<th>Hora</th>\n<th>Fecha</th>\n</tr>\n</thead>')
	i=0
	f.write("<tbody>")
	for entrada in registros.findall("./Entra[@codigo='"+trabajador.attrib["codigo"]+"']"):
		if i%2==0:
			f.write("<tr class=\"even\">\n")
		else:
			f.write("<tr class=\"odd\">\n")
		fecha=entrada.find("Fecha").text
		hora=entrada.find("Hora").text
		minu=entrada.find("Min").text
		f.write("<td>"+hora+":"+minu+"</td>\n")
		f.write("<td>"+fecha+"</td>\n")
		f.write("</tr>\n")
		i+=1
	f.write("</tbody>\n")
	f.write("</table>")
f.close()
