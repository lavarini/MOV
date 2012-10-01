<?php
require_once 'conexao.php';

class login {

	private $conn;
	private $timeLogin = 0;
	private $dadosUser = array ();

    public $arrCookies = array();
	
	public $EMBARALHAR = 'projetopaz';
	
	function __construct() {
		$this->conn = new Conexao();
	}
	
	public function checkLogin($email = '', $senha = '') {
		$checked = false;
		$location = '';
		
		/*
		* Checa validade da senha
		*/
		$senha = trim ( $senha );
                
        $senha = md5($senha);
		
		$dados = $this->conn->sql_query ('SELECT *
										FROM usuarios
										WHERE email = "' . $email . '"
										LIMIT 1' );
		
		// Verificando se foi encontrado algum registro

		
		while ($row = mysql_fetch_assoc($dados)) {
			$this->dadosUser = $row;
		}
		
		if (!$this->dadosUser){
			$resposta['status'] = -2;
			$resposta['msg'] = 'Usuario incorreto';
		}else{
			/**
			 * Registro encontrado
			 * Verificação da senha
			 */
			if (!($this->dadosUser['senha'] == $senha) ) {
				$resposta['status'] = -1;
				$resposta['msg'] = 'Senha incorreta';
			} else{
				$resposta['status'] = 1;
				$resposta['msg'] = 'Bem vindo '.$this->dadosUser['nome'];
				$this->doLogin();
				$resposta['cookies'] = $this->arrCookies;
			}
		}
		
		return $resposta;
	}
	
	public function doLogin() {
		$this->montaArrayCookies();
                
        foreach ($this->arrCookies as $k => $v) {
        	setcookie ($k, $v, $this->timeLogin, '/', $_SERVER['HTTP_HOST']);
		}
	}

	public function montaArrayCookies() {
    	$cookies = array();
        $cookies['email'] = $this->dadosUser['email'];
		$cookies['idUsuarios'] = $this->dadosUser['idUsuarios'];

        $cookies['checkup'] = md5($this->dadosUser['idUsuarios']. $this->EMBARALHAR . $this->dadosUser['email']);

        $this->arrCookies = $cookies;
                
	}

    public function getArrayCookies(){
    	$array = $this->arrCookies;
            if (isset ($array['checkup']))
                unset ($array['checkup']);
    	return $array;
	}
}

?>