const productsGrid = document.getElementById('products-grid');
const selectedProductInput = document.getElementById('selected-product');
const selectedPriceInput = document.getElementById('selected-price');
const valorPagoInput = document.getElementById('valorPago');
const trocoInput = document.getElementById('troco');
const btnComprar = document.getElementById('btnComprar');
const btnLimpar = document.getElementById('btnLimpar');
const mensagem = document.getElementById('mensagem');
const trocoNotas = document.getElementById('troco-notas');

let produtoSelecionado = null; // { id, price, name }

const notasMoedas = [10, 5, 2, 1];

function formatBRL(value) {
  if (!Number.isFinite(value)) return '';
  return 'R$ ' + value.toFixed(2).replace('.', ',');
}

function setMessage(text, type) {
  mensagem.textContent = text;
  mensagem.classList.remove('ok', 'err');
  if (type) mensagem.classList.add(type);
}

function limparTroco() {
  trocoInput.value = '';
  trocoNotas.innerHTML = '';
}

function calcularTrocoBreakdown(troco) {
  // troco vem em número (ex: 4.00). Vamos tratar como inteiro de centavos.
  const totalCentavos = Math.round(Number(troco) * 100);

  // notasMoedas em reais (inteiro). Vamos converter pra centavos.
  const valoresCentavos = notasMoedas.map(v => Math.round(v * 100));

  let restante = totalCentavos;
  const itens = [];

  for (let i = 0; i < valoresCentavos.length; i++) {
    const valor = valoresCentavos[i];
    const qtd = Math.floor(restante / valor);
    restante = restante % valor;

    if (qtd > 0) {
      const valorReal = valoresCentavos[i] / 100;
      itens.push({ qtd, valorReal });
    }
  }

  return itens;
}

function atualizarSelecionado(card) {
  // remove seleção anterior
  [...productsGrid.querySelectorAll('.product-card')].forEach(c => c.classList.remove('selected'));

  card.classList.add('selected');

  const name = card.querySelector('.product-name')?.textContent.trim() || '';
  const price = Number(card.dataset.price);
  const id = card.dataset.id;

  produtoSelecionado = { id, price, name };
  selectedProductInput.value = name;
  selectedPriceInput.value = formatBRL(price);

  setMessage('Produto selecionado. Insira o valor e clique em Comprar.', null);
  limparTroco();
}

productsGrid.addEventListener('click', function (e) {
  const card = e.target.closest('.product-card');
  if (!card) return;
  atualizarSelecionado(card);
});

btnComprar.addEventListener('click', function () {
  if (!produtoSelecionado) {
    setMessage('Escolha um produto primeiro.', 'err');
    return;
  }

  const valorPago = Number(valorPagoInput.value || 0);
  const preco = produtoSelecionado.price;

  if (!Number.isFinite(valorPago) || valorPago <= 0) {
    setMessage('Digite um valor pago válido.', 'err');
    return;
  }

  if (valorPago < preco) {
    const falta = preco - valorPago;
    limparTroco();
    setMessage('Dinheiro insuficiente. Faltam ' + formatBRL(falta) + ' para comprar este produto.', 'err');
    return;
  }

  const troco = valorPago - preco;
  trocoInput.value = formatBRL(troco);

  if (troco === 0) {
    setMessage(
      `Compra realizada com sucesso!\nVocê escolheu: ${produtoSelecionado.name}\nPreço: ${formatBRL(preco)}\nValor pago: ${formatBRL(valorPago)}\nNão há troco.`,
      'ok'
    );
    trocoNotas.innerHTML = '';
    return;
  }

  const itens = calcularTrocoBreakdown(troco);

  setMessage(
    `Você escolheu: ${produtoSelecionado.name}\nPreço: ${formatBRL(preco)}\nValor pago: ${formatBRL(valorPago)}\nCompra realizada com sucesso.\nTroco: ${formatBRL(troco)}`,
    'ok'
  );

  const listHtml = itens.length
    ? '<ul>' + itens.map(i => `<li>${i.qtd}x de ${formatBRL(i.valorReal)}</li>`).join('') + '</ul>'
    : '';

  trocoNotas.innerHTML = '<h3>Troco (notas e moedas)</h3>' + listHtml;
});

btnLimpar.addEventListener('click', function () {
  produtoSelecionado = null;
  selectedProductInput.value = '';
  selectedPriceInput.value = '';
  valorPagoInput.value = '';
  limparTroco();
  setMessage('', null);

  [...productsGrid.querySelectorAll('.product-card')].forEach(c => c.classList.remove('selected'));
});

