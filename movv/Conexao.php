<?php

/**
 * 
 * @author Victor Britto
 * 
 */
class Conexao {

    // Informações do banco de dados
    var $host = "localhost"; // Nome ou IP do Servidor
    var $user = "root"; // Usuário do Servidor MySQL
    var $senha = ""; // Senha do Usuário MySQL
    var $dbase = "mov"; // Nome do seu Banco de Dados
    
    // Criaremos as variáveis que Utilizaremos no script
    var $query;
    var $link;
    var $resultado;

    // Instancia o Objeto
    function MySQL() {
        
    }

    // Cria a função para efetuar conexão ao Banco MySQL.
    // Veja que abaixo, além de criarmos a conexão, geramos condições personalizadas para mensagens de erro.
    function conecta() {
        $this->link = @mysql_connect($this->host, $this->user, $this->senha);
        // Conecta ao Banco de Dados
        if (!$this->link) {
            // Se ocorrer erro exibe mensagem.
            print "Ocorreu um Erro na conexão MySQL:";
            print "<b>" . mysql_error() . "</b>";
            die();
        } elseif (!mysql_select_db($this->dbase, $this->link)) {
            // Seleciona o banco após a conexão
            // Caso ocorra um erro, exibe uma mensagem com o erro
            print "Ocorreu um Erro em selecionar o Banco:";
            print "<b>" . mysql_error() . "</b>";
            die();
        }
    }

    // Função para rodar a "query" no Banco de Dados
    function sql_query($query) {
        $this->conecta();
        $this->query = $query;

        // Conecta e executa a query no MySQL
        if ($this->resultado = mysql_query($this->query)) {
            $this->desconecta();
            return $this->resultado;
        } else {
            // Caso ocorra um erro, exibe uma mensagem com o Erro
            print "Ocorreu um erro ao executar a Query MySQL: <b>$query</b>";
            print "<br><br>";
            print "Erro no MySQL: <b>" . mysql_error() . "</b>";
            die();
            $this->desconecta();
        }
    }

    // Função para Desconectar do Banco MySQL
    function desconecta() {
        return mysql_close($this->link);
    }

}

?>
