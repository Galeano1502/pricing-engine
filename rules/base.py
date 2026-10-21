from abc import ABC, abstractmethod
from typing import Optional
from domain.models import ContextoPedido


class RegraPricing(ABC):
    def __init__(self):
        self._proxima_regra: Optional['RegraPricing'] = None

    def definir_proxima(self, regra: 'RegraPricing') -> 'RegraPricing':
        self._proxima_regra = regra
        return regra

    def processar(self, contexto: ContextoPedido) -> ContextoPedido:
        self.aplicar_regra(contexto)
        if self._proxima_regra:
            return self._proxima_regra.processar(contexto)
        return contexto

    @abstractmethod
    def aplicar_regra(self, contexto: ContextoPedido) -> None:
        pass