# ⚙️ Pricing Engine - Motor de Regras Configurável (Lógica de Negócio Pura)

Um motor de cálculo de preços dinâmicos desacoplado e extensível, construído em Python com foco em **Clean Architecture**, **SOLID** e desenvolvimento orientado a testes (**TDD**).

---

## 🏗️ Padrões de Projeto e Arquitetura

- **Strategy Pattern:** Permite isolar a lógica de cálculo de cada regra de desconto em classes independentes.
- **Chain of Responsibility Pattern:** Encadeia as regras em um fluxo sequencial (pipeline). O resultado de uma regra é transmitido para a próxima na corrente.
- **Auditabilidade de Cálculos:** O motor gera um histórico detalhado (*Pricing Breakdown*) explicando o motivo de cada desconto ou modificação aplicada.

---

## 📁 Estrutura do Projeto

```text
pricing_engine/
├── domain/               # Modelos de dados e contexto do pedido
├── rules/                # Regras de negócio individuais (Strategies)
├── engine/               # Orquestrador da esteira de regras (Chain)
└── tests/                # Testes unitários cobrindo cenários limite (TDD)
```

---

## 🧪 Como Rodar os Testes

1. Certifique-se de ter o Python e o `pytest` instalados:
   ```bash
   py -m pip install pytest
   ```

2. Execute a suíte de testes unitários:
   ```bash
   py -m pytest
   ```

---

## 💡 Exemplo de Uso

```python
from domain.models import Item, ContextoPedido
from engine.pricing_engine import PricingEngine

# Criando o contexto de um pedido
itens = [Item(nome="Caderno", categoria="Papelaria", preco_unitario=20.0, quantidade=10)]
contexto = ContextoPedido(
    tipo_conta="PREMIUM",
    historico_compras_qtd=15,
    horario_solicitacao="15:00",
    itens=itens,
    cupom="FIDELIDADE20"
)

# Executando o motor de regras
engine = PricingEngine()
resultado = engine.calcular(contexto)

print(f"Subtotal: R$ {resultado.subtotal}")
print(f"Valor Final: R$ {resultado.valor_final}")
print("Justificativas do cálculo:", resultado.detalhes_aplicacao)
```