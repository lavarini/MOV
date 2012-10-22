<?php
	define('EMBARALHAR', 'projetopaz');
	
	function verif_login(){
		if (isset( $_COOKIE['checkup'] ) && isset( $_COOKIE['email'] ) && isset( $_COOKIE['idUsuarios'] )){
			if ($_COOKIE['checkup'] == md5($_COOKIE['idUsuarios']. EMBARALHAR . $_COOKIE['email'])){
				return true;
			}
			return false;
		}
		return false;
	}