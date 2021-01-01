<html>
 <head>
   <meta charset="utf-8" />
   <title>Apertura de Puerta</title>
   <style type="text/css">
     code{white-space: pre-wrap;}
     span.smallcaps{font-variant: small-caps;}
     span.underline{text-decoration: underline;}
     div.column{display: inline-block; vertical-align: top; width: 50%;}
   </style>
   <link rel="stylesheet" href="../web_resources/web.css"/>
 </head>
	<?php
	$codigo=$_GET['codigo'];
	$nombre=$_GET['nombre'];
	$a=strcmp($_GET["Estado"],"Registrar y publicar en twitter");
	$instucc="sudo python3 incorpora.py"." ".$codigo."-*-".$nombre."-*-".$a;
	$a=exec($instucc);
	if($a=="Invalido"){
		header('Location: nuevo_trabajador.php?a=1'); 
	}
	echo $a;
	?>

<a href="nuevo_trabajador.php"> Volver </a>
</html>
