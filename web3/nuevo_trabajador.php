<html>
<head>
  <meta charset="utf-8" />
  <title>Incorporación de trabajadores</title>
  <style type="text/css">
      code{white-space: pre-wrap;}
      span.smallcaps{font-variant: small-caps;}
      span.underline{text-decoration: underline;}
      div.column{display: inline-block; vertical-align: top; width: 50%;}
  </style>
  <link rel="stylesheet" href="../web_resources/web.css"/>
</head>
<body>
	<h1>Introduzca los datos del nuevo trabajador</h1>
	</br>
	<?php 
		 if($_GET["a"]=="1"){
		 echo("ERROR:Código ya usado");
		 }
	?>
	<form action="nuevo_trabajador_recibido.php" method="get">
    Nombre completo:<input type="text" name="nombre" value="">
    </br>
    Código de acceso:<input type="text" name="codigo" value="">
    </br>
		<input type="submit" name="Estado" autofocus=true value="Registrar"/>
    </br>
    <input type="submit" name="Estado" autofocus=true value="Registrar y publicar en twitter"/>
	</form>
	<a href="../index.html">Directorio</a></br>
</body>
</html>
