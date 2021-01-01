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
	<h1>Tabla de registros de empleados</h1>
	<?php
		$a=exec("sudo python3 lee_registros.py");
		echo $a;
	?>
<html/> 
