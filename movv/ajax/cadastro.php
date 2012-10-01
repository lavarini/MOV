<?php
require_once '../classes/usuario.php';


$usuario = new usuario();
$r = $usuario->cadastro($_POST['nome'], $_POST['email'], $_POST['senha']);
	
echo json_encode($r);
?>