# tests/test_volume_discount.py

from domain.models import Item, ContextoPedido
from rules.volume_discount import RegraDescontoVolume


def test_deve_aplicar_10_por_cento_de_desconto_quando_quantidade_de_itens_for_10_ou_mais():
    # Arrange
    itens = [
        Item(nome="Caderno", categoria="Papelaria", preco_unitario=20.0, quantidade=10)
    ]
    contexto = ContextoPedido(
        tipo_conta="PADRAO",
        historico_compras_qtd=2,
        horario_solicitacao="14:00",
        itens=itens
    )
    regra = RegraDescontoVolume()

    # Act
    contexto_processado = regra.processar(contexto)

    # Assert
    assert contexto_processado.subtotal == 200.0
    assert contexto_processado.valor_final == 180.0
    assert len(contexto_processado.detalhes_aplicacao) == 1
    assert "Desconto por Volume (10%)" in contexto_processado.detalhes_aplicacao[0]


def test_nao_deve_aplicar_desconto_quando_quantidade_de_itens_for_menor_que_10():
    # Arrange
    itens = [
        Item(nome="Caneta", categoria="Papelaria", preco_unitario=5.0, quantidade=5)
    ]
    contexto = ContextoPedido(
        tipo_conta="PADRAO",
        historico_compras_qtd=1,
        horario_solicitacao="10:00",
        itens=itens
    )
    regra = RegraDescontoVolume()

    # Act
    contexto_processado = regra.processar(contexto)

    # Assert
    assert contexto_processado.subtotal == 25.0
    assert contexto_processado.valor_final == 25.0
    assert len(contexto_processado.detalhes_aplicacao) == 0