const API_URL = "http://localhost:5000";

// para otimizar o tempo

function mostrarMensagem(mensagem) {
	// pegar o elemento do HTML (onde vamos mostrar a msg)
	const divMsg = document.querySelector("#mensagem");

	divMsg.textContent = mensagem;

	// mostrar a div
	divMsg.style.display = "block";

	// vc quer que a div fique para sempre na tela?
	setTimeout(() => {
		divMsg.style.display = "none";
	}, 5000);
}

async function cadastrarUsuario(event) {
	event.preventDefault();

	const nome = document.querySelector("#nome").value;

	const email = document.querySelector("#email").value;

	const senha = document.querySelector("#senha").value;

	const dados = { nome, email, senha };

	try {
		const response = await fetch(`${API_URL}/usuarios`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(dados),
		});
		// Esperando o resultado da promessa
		const resultado = await response.json();

		if (response.ok) {
			// aqui entraria mostrar na div
			mostrarMensagem("Usuario cadastrado com sucesso");
			document.querySelector("#formCadastro").reset();
		} else {
			// aqui entraria mostrar erro na div
			mostrarMensagem("Erro ao cadastrar usuario");
		}
	} catch (erro) {
		// mostrar erro de servidor na div
		mostrarMensagem("Erro ao conectar com o servidor" + erro.message);
	}
}

async function listarUsuarios() {
	// primeira coisa: pegar a tabela
	const tabela = document.querySelector("#tabela-usuarios");

	// segunda coisa: esconder a tabela
	tabela.style.display = "none";

	try {
		
	} catch (erro) {
		
	}finally{
		
	}
}
