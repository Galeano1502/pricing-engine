from rules.base import RegraPricing
from domain.models import ContextoPedido


class RegraDescontoVolume(RegraPricing):
    def aplicar_regra(self, contexto: ContextoPedido) -> None:
        qtd_total = sum(item.quantidade for item in contexto.itens)
        if qtd_total >= 10:
            desconto = contexto.valor_final * 0.10
            contexto.valor_final -= desconto
            contexto.detalhes_aplicacao.append(
                f"Desconto por Volume (10%): -R$ {desconto:.2f} por comprar {qtd_total} itens."
            )