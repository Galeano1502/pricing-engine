from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Item:
    nome: str
    categoria: str
    preco_unitario: float
    quantidade: int


@dataclass
class ContextoPedido:
    tipo_conta: str
    historico_compras_qtd: int
    horario_solicitacao: str
    itens: List[Item]
    cupom: Optional[str] = None

    subtotal: float = 0.0
    valor_final: float = 0.0
    prioridade_fila: int = 1
    detalhes_aplicacao: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.subtotal = sum(item.preco_unitario * item.quantidade for item in self.itens)
        self.valor_final = self.subtotal