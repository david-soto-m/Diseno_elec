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
   if ($_GET["Estado"]=="Registrar y publicar en twitter"){
     	echo "Registrando y publicando trabajador";
     	$fp=fopen("codigo_trabajador.txt","w");
     	fputs($fp,$codigo);
     	fclose($fp);

      $fp=fopen("nombre_trabajador.txt","w");
      fputs($fp,$nombre);
      fclose($fp);

      $fp=fopen("publicar.txt","w");
      fputs($fp,"Si");
      fclose($fp);


     	exec("sudo python incorpora.py");
     }
   if ($_GET["Estado"]=="Registrar"){
     echo "Registrando trabajador";
     $fp=fopen("codigo.txt","w");
     fputs($fp,$codigo);
     fclose($fp);

     $fp=fopen("nombre.txt","w");
     fputs($fp,$nombre);
     fclose($fp);

     $fp=fopen("publicar.txt","w");
     fputs($fp,"No");
     fclose($fp);


     exec("sudo python incorpora.py");
       ?>

<a href="nuevo_trabajador.html"> Volver </a>
</html>
