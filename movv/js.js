$(document).ready(function() {
	$('#login').click(function(){
		$('div.login').show();
		return false;
	});
	
	$('#logar').click(function(){
		login();
	});
	
	$('#cadastrar').click(function(){
		cadastro();
	})
	
	function login(){
	
		$.ajax({
            url: '/ajax/login.php',
            dataType: 'json',
            type: 'POST',
            data: {
				'email': $('#email').val(),
				'senha': $('#senha').val()
			},
            success: function (data) {
				document.cookie = ['idUsuarios=',data.cookies.idUsuarios].join('');
				document.cookie = ['email=',data.cookies.email].join('');
				document.cookie = ['checkup=',data.cookies.checkup].join('');
            },
            error: function (data) {
                console.log(data);
            }
        });
	};
	
	function cadastro(){
	
		$.ajax({
            url: '/ajax/cadastro.php',
            dataType: 'json',
            type: 'POST',
            data: {
				'email': $('#cadastro_email').val(),
				'senha': $('#cadastro_senha').val(),
				'nome': $('#cadastro_nome').val()
			},
            success: function (data) {
				if(data.status === 1){
					alert(data.msg);
				}else{
					alert(data.msg);
				}
            },
            error: function (data) {
                console.log(data);
            }
        });
	};
	
});