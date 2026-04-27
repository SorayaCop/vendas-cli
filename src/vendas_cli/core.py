from __future__ import annotations

from decimal import Decimal


def calculate_total(sales: list[dict]) -> Decimal:
    total = Decimal("0")

    for item in sales:
        quantity = Decimal(item["quantidade"])
        price = Decimal(item["valor"])
        total += quantity * price

    return total