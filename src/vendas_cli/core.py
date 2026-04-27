from __future__ import annotations

from datetime import date
from decimal import Decimal


def calculate_total(sales: list[dict]) -> Decimal:
    total = Decimal("0")

    for item in sales:
        quantity = Decimal(item["quantidade"])
        price = Decimal(item["valor"])
        total += quantity * price

    return total


def sales_by_product(sales: list[dict]) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}

    for item in sales:
        product = item["produto"]
        quantity = Decimal(item["quantidade"])
        price = Decimal(item["valor"])

        totals[product] = totals.get(product, Decimal("0")) + (quantity * price)

    return totals


def top_product(sales: list[dict]) -> str:
    ranking: dict[str, Decimal] = {}

    for item in sales:
        product = item["produto"]
        quantity = Decimal(item["quantidade"])

        ranking[product] = ranking.get(product, Decimal("0")) + quantity

    return max(ranking, key=ranking.get)


def filter_by_date(
    sales: list[dict],
    start: date | None = None,
    end: date | None = None,
) -> list[dict]:
    filtered_sales: list[dict] = []

    for item in sales:
        sale_date = date.fromisoformat(item["data"])

        if start and sale_date < start:
            continue

        if end and sale_date > end:
            continue

        filtered_sales.append(item)

    return filtered_sales