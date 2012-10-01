<?php
require_once 'conexao.php';

class usuario {

	private $dadosUser = array ();
	
	function __construct() {
		$this->conn = new Conexao();
	}
	
	public function cadastro($nome,$email,$senha) {
		
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
		
		if ($this->dadosUser){
			$resposta['status'] = -1;
			$resposta['msg'] = 'Email ja existente no sistema';
		}else{
			$dados = $this->conn->sql_query ('INSERT INTO usuarios
										(email, nome, senha)
										values("'.$email.'","'.$nome.'","'.$senha.'")');
			$resposta['status'] = 1;
			$resposta['msg'] = 'Cadastro efetuado com sucesso';
		}
		
		return $resposta;
	}
}

?>