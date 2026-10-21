# rules/loyalty_coupon.py

from rules.base import RegraPricing
from domain.models import ContextoPedido


class RegraCupomFidelidade(RegraPricing):
    def aplicar_regra(self, contexto: ContextoPedido) -> None:
        if contexto.tipo_conta == "PREMIUM" and contexto.cupom == "FIDELIDADE20":
            desconto = 20.0
            contexto.valor_final = max(0.0, contexto.valor_final - desconto)
            contexto.detalhes_aplicacao.append(
                f"Cupom Fidelidade: -R$ {desconto:.2f} aplicado para conta PREMIUM."
            )