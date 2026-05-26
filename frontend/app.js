const API_URL = 'http://127.0.0.1:7000';


const formCadastro = document.getElementById('form-cadastro');
const formCancelar = document.getElementById('form-cancelar');
const btnChamar = document.getElementById('btn-chamar');
const listaFila = document.getElementById('lista-fila');
const totalFila = document.getElementById('total-fila');
const listaHistorico = document.getElementById('lista-historico');
const alertaChamado = document.getElementById('alerta-chamado');


async function atualizarInterface() {
    await carregarFila();
    await carregarHistorico();
}


async function carregarFila() {
    try {
        const res = await fetch(`${API_URL}/fila`);
        const dados = await res.json();
        
        listaFila.innerHTML = '';
        totalFila.textContent = dados.total;

        if (dados.fila.length === 0) {
            listaFila.innerHTML = '<p class="vazio">Fila vazia. Nenhum cliente aguardando.</p>';
            return;
        }

        dados.fila.forEach((cliente, index) => {
            const item = document.createElement('div');
            item.className = `fila-item ${cliente.tipo.toLowerCase()}`;
            
            item.innerHTML = `
                <span class="posicao">${index + 1}º</span>
                <div class="detalhes">
                    <strong>${cliente.nome}</strong>
                    <small>Chegada: ${cliente.horario_chegada}</small>
                </div>
                <span class="badge">${cliente.tipo}</span>
            `;
            listaFila.appendChild(item);
        });
    } catch (err) {
        console.error("Erro ao carregar fila:", err);
    }
}


async function carregarHistorico() {
    try {
        const res = await fetch(`${API_URL}/historico`);
        const dados = await res.json();
        
        listaHistorico.innerHTML = '';

        if (dados.historico.length === 0) {
            listaHistorico.innerHTML = '<p class="vazio">Nenhum atendimento realizado hoje.</p>';
            return;
        }

        dados.historico.forEach(atend => {
            const item = document.createElement('div');
            item.className = 'historico-item';
            item.innerHTML = `
                <strong>${atend.nome}</strong>
                <small>${atend.tipo} • ${atend.horario_atendimento}</small>
            `;
            listaHistorico.appendChild(item);
        });
    } catch (err) {
        console.error("Erro ao carregar histórico:", err);
    }
}


formCadastro.addEventListener('submit', async (e) => {
    e.preventDefault();
    const nome = document.getElementById('nome').value;
    const tipo = document.getElementById('tipo').value;

    try {
        const res = await fetch(`${API_URL}/clientes`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ nome, tipo })
        });
        if(res.ok) {
            formCadastro.reset();
            atualizarInterface();
        }
    } catch (err) { alert("Falha na conexão com o servidor."); }
});


btnChamar.addEventListener('click', async () => {
    try {
        const res = await fetch(`${API_URL}/fila/chamar`, { method: 'POST' });
        const dados = await res.json();

        if (res.ok) {
            alertaChamado.className = "alerta sucesso";
            alertaChamado.innerHTML = `📢 <strong>Chamando:</strong> ${dados.cliente.nome} (${dados.cliente.tipo})`;
            atualizarInterface();
        } else {
            alertaChamado.className = "alerta erro";
            alertaChamado.textContent = dados.detail;
        }
    } catch (err) { console.error(err); }
});


formCancelar.addEventListener('submit', async (e) => {
    e.preventDefault();
    const nome = document.getElementById('nome-cancelar').value;

    try {
        const res = await fetch(`${API_URL}/fila/cancelar`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ nome })
        });
        const dados = await res.json();

        if (res.ok) {
            alert(dados.mensagem);
            formCancelar.reset();
            atualizarInterface();
        } else {
            alert(dados.detail);
        }
    } catch (err) { console.error(err); }
});


atualizarInterface();