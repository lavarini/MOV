<?php
require_once '../classes/login.php';


$login = new login();
$r = $login->checkLogin($_POST['email'], $_POST['senha']);
	
echo json_encode($r);
?>