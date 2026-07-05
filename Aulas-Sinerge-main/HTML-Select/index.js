const selectProduto = document.getElementById('produto');
const inputPreco = document.getElementById('preco');
const inputQuantidade = document.getElementById('quantidade');
const inputTotal = document.getElementById('total');

const inputValorPago = document.getElementById('valorPago');
const inputTroco = document.getElementById('troco');
const resultado = document.getElementById('resultado');
const btnCalcular = document.getElementById('btn-calcular');

function calcularTotal() {
  const preco = Number(inputPreco.value || 0);
  const quantidade = Number(inputQuantidade.value || 0);
  const total = preco * quantidade;

  inputTotal.value = Number.isFinite(total) ? total.toFixed(2) : '';
}

function pegarValores() {
  return {
    total: Number(inputTotal.value || 0),
    valorPago: Number(inputValorPago.value || 0)
  };
}

function calcularTroco() {
  const { total, valorPago } = pegarValores();

  if (!Number.isFinite(total) || !Number.isFinite(valorPago)) {
    inputTroco.value = '';
    resultado.textContent = '';
    return;
  }

  if (valorPago < total) {
    inputTroco.value = '';
    resultado.textContent = 'Dinheiro insuficiente.';
  } else {
    const troco = valorPago - total;
    inputTroco.value = troco.toFixed(2);

    if (troco === 0) resultado.textContent = 'Sem troco.';
    else resultado.textContent = 'Troco calculado com sucesso.';
  }
}

selectProduto.addEventListener('change', function () {
  inputPreco.value = selectProduto.value;
  calcularTotal();
});

inputQuantidade.addEventListener('input', function () {
  calcularTotal();
});

btnCalcular.addEventListener('click', function () {
  calcularTroco();
});

// Atualiza o troco automaticamente quando valor pago mudar
inputValorPago.addEventListener('input', function () {
  calcularTroco();
});

// Estado inicial
atualizar: {
  inputPreco.value = '';
  inputTotal.value = '';
  inputTroco.value = '';
  resultado.textContent = '';
}

