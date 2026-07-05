const selectProduto = document.getElementById('produto');
const inputPreco = document.getElementById('preco');
const inputQuantidade = document.getElementById('quantidade');
const inputTotal = document.getElementById('total');

function calcularTotal() {
  const preco = Number(inputPreco.value || 0);
  const quantidade = Number(inputQuantidade.value || 0);
  const total = preco * quantidade;

  inputTotal.value = Number.isFinite(total) ? total.toFixed(2) : '';
}

selectProduto.addEventListener('change', function () {
  inputPreco.value = selectProduto.value;
  calcularTotal();
});

inputQuantidade.addEventListener('input', function () {
  calcularTotal();
});

const checkboxesInfo = document.querySelectorAll('.info-adicional');

function pegarInformacoesAdicionais() {
  const informacoes = [];

  checkboxesInfo.forEach(function (checkbox) {
    if (checkbox.checked) {
      informacoes.push(checkbox.value);
    }
  });

  return informacoes;
}

function atualizarInformacoes() {
  const informacoes = pegarInformacoesAdicionais();
  const resultado = document.getElementById('resultado-info');
  resultado.textContent = informacoes.join(', ');
}

checkboxesInfo.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    atualizarInformacoes();
  });
});

function pegarFormaPagamento() {
  const pagamentoSelecionado = document.querySelector('input[name="pagamento"]:checked');
  if (pagamentoSelecionado) return pagamentoSelecionado.value;
  return '';
}

function atualizarFormaPagamento() {
  const pagamento = pegarFormaPagamento();
  const resultado = document.getElementById('resultado-pagamento');

  if (pagamento === '') {
    resultado.textContent = '';
  } else {
    resultado.textContent = 'Forma de pagamento: ' + pagamento;
  }
}

const radiosPagamento = document.querySelectorAll('input[name="pagamento"]');

radiosPagamento.forEach(function (radio) {
  radio.addEventListener('change', function () {
    atualizarFormaPagamento();
  });
});

// Desafio 3 (resumo)
const btnResumo = document.getElementById('btn-resumo');
btnResumo.addEventListener('click', function () {
  const produtoNome = selectProduto.options[selectProduto.selectedIndex]?.text || '';

  console.log('Produto:', produtoNome);
  console.log('Preço:', inputPreco.value);
  console.log('Quantidade:', inputQuantidade.value);
  console.log('Total:', inputTotal.value);
  console.log('Informações:', pegarInformacoesAdicionais());
  console.log('Pagamento:', pegarFormaPagamento());
});

// Estado inicial
atualizarInformacoes();
atualizarFormaPagamento();

