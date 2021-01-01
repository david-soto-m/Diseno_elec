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
	<body>
	<?php
	if ($_GET["Estado"]=="Si"){
		echo "Dejando Pasar";
		exec("sudo python3 abre.py");
		}
	if ($_GET["Estado"]=="No"){
		echo "Bloqueando";
		exec("sudo python3 bloquea.py");
		}
	echo "<br/>";
        ?>
	<a href="../index.html">Directorio</a></br>
	</head>
</html>
