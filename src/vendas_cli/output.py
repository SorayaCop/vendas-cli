from __future__ import annotations

from decimal import Decimal


def render_text(total_records: int, total_amount: Decimal) -> None:
    print(f"Registros carregados: {total_records}")
    print(f"Faturamento total: R$ {total_amount}")