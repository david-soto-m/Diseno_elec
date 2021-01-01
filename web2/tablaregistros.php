<html>
	<head>
		<meta charset="utf-8" />
		<title>Registros del Smartfonillo</title>
		<style type="text/css">
			code{white-space: pre-wrap;}
			span.smallcaps{font-variant: small-caps;}
			span.underline{text-decoration: underline;}
			div.column{display: inline-block; vertical-align: top; width: 50%;}
		</style>
		<link rel="stylesheet" href="../web_resources/web.css"/>
	</head>
	<body>
	<h1>Tabla de registros de empleados</h1>
	<a href="../index.html">Directorio</a></br>
	<?php
		exec("sudo python3 lee_registros.py");
		$a="table.html";
		$file = fopen($a, "r") or die("Unable to open file!");
		echo fread($file,filesize($a));
		fclose($file);
	?>
	</body>
<html/> 
