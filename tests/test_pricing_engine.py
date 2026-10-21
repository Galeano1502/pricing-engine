# tests/test_pricing_engine.py

from domain.models import Item, ContextoPedido
from engine.pricing_engine import PricingEngine


def test_deve_aplicar_desconto_de_volume_e_cupom_fidelidade_cumulativamente():
    # 10 cadernos a R$ 20.0 = Subtotal R$ 200.0
    itens = [Item(nome="Caderno", categoria="Papelaria", preco_unitario=20.0, quantidade=10)]
    contexto = ContextoPedido(
        tipo_conta="PREMIUM",
        historico_compras_qtd=15,
        horario_solicitacao="15:00",
        itens=itens,
        cupom="FIDELIDADE20"
    )

    engine = PricingEngine()
    resultado = engine.calcular(contexto)

    # Subtotal: R$ 200.0
    # Desconto Volume (10%): -R$ 20.0 -> R$ 180.0
    # Cupom Fidelidade: -R$ 20.0 -> R$ 160.0
    assert resultado.subtotal == 200.0
    assert resultado.valor_final == 160.0
    assert len(resultado.detalhes_aplicacao) == 2