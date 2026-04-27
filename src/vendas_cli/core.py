from __future__ import annotations

from decimal import Decimal


def calculate_total(sales: list[dict]) -> Decimal:
    total = Decimal("0")

    for item in sales:
        quantity = Decimal(item["quantidade"])
        price = Decimal(item["valor"])
        total += quantity * price

    return total


def top_product(sales: list[dict]) -> str:
    ranking: dict[str, Decimal] = {}

    for item in sales:
        product = item["produto"]
        quantity = Decimal(item["quantidade"])

        ranking[product] = ranking.get(product, Decimal("0")) + quantity

    return max(ranking, key=ranking.get)