# tests/test_loyalty_coupon.py

from domain.models import Item, ContextoPedido
from rules.loyalty_coupon import RegraCupomFidelidade


def test_deve_aplicar_desconto_de_20_reais_para_conta_premium_com_cupom_fidelidade():
    itens = [Item(nome="Mochila", categoria="Acessórios", preco_unitario=150.0, quantidade=1)]
    contexto = ContextoPedido(
        tipo_conta="PREMIUM",
        historico_compras_qtd=10,
        horario_solicitacao="11:00",
        itens=itens,
        cupom="FIDELIDADE20"
    )
    regra = RegraCupomFidelidade()

    contexto_processado = regra.processar(contexto)

    assert contexto_processado.valor_final == 130.0
    assert len(contexto_processado.detalhes_aplicacao) == 1
    assert "Cupom Fidelidade" in contexto_processado.detalhes_aplicacao[0]


