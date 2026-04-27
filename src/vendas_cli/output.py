from __future__ import annotations

import json
from decimal import Decimal


def render_text(
    total_records: int,
    total_amount: Decimal,
    best_seller: str
) -> None:
    print(f"Registros carregados: {total_records}")
    print(f"Faturamento total: R$ {total_amount}")
    print(f"Produto mais vendido: {best_seller}")


def render_json(
    total_records: int,
    total_amount: Decimal,
    best_seller: str
) -> None:
    data = {
        "registros": total_records,
        "faturamento_total": str(total_amount),
        "produto_mais_vendido": best_seller,
    }

    print(json.dumps(data, indent=2, ensure_ascii=False))