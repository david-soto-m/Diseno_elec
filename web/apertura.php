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
	<h1>¿Tiene esta persona permiso para entrar?</h1>
	<?php
		$a=exec("sudo python3 FotoPython.py")
	?>
	<img src="foto.jpg" alt="Foto" />
	</br>
	<form action="apertura_recibido.php" method="get">
		<input type="submit" name="Estado" value="Si"/>
		<input type="submit" name="Estado" autofocus=true value="No"/>
	</form>
	<a href="../index.html">Directorio</a></br>
</body>
</html>
