# engine/pricing_engine.py

from domain.models import ContextoPedido
from rules.volume_discount import RegraDescontoVolume
from rules.loyalty_coupon import RegraCupomFidelidade


class PricingEngine:
    def __init__(self):
        # Instancia as regras
        self.regra_volume = RegraDescontoVolume()
        self.regra_cupom = RegraCupomFidelidade()

        # Define a corrente (Chain of Responsibility)
        # Regra de Volume -> Regra de Cupom
        self.regra_volume.definir_proxima(self.regra_cupom)

    def calcular(self, contexto: ContextoPedido) -> ContextoPedido:
        # Inicia o processamento no primeiro link da corrente
        return self.regra_volume.processar(contexto)