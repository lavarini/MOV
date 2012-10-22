<ul class="hmenu">
    
    <li>
        <a href="index.php">Home</a>
    </li>	
    
    <li>
        <a href="cadastro.php" >Cadastro</a>
    
        <ul>
            <li>
                <a href="#">Nascimento</a>
            </li>
            <li>
                <a href="#">Paciente</a>
            </li>
            <li>
                <a href="#">Doa&ccedil;&atilde;o</a>
            </li>
            <li id="cadastro_usuario">
                <a href="#">Usuario</a>
            </li>
        </ul>
        
    </li>
	
	<?php
	require_once './config.php';
	if(verif_login){
		$html = '<li id="logged"><span>Bem vindo '.$_COOKIE['nome'].'!</span></li>';
		echo $html;
	}else{
		$html = '<li id="login"><a href="#">Login</a></li>';
		echo $html;
	}
	?>
    
</ul>