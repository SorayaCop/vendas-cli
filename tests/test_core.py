from decimal import Decimal

from vendas_cli.core import calculate_total, top_product


def test_calculate_total() -> None:
    sales = [
        {"produto": "Notebook", "quantidade": "2", "valor": "1000"},
        {"produto": "Mouse", "quantidade": "3", "valor": "100"},
    ]

    result = calculate_total(sales)

    assert result == Decimal("2300")


def test_top_product() -> None:
    sales = [
        {"produto": "Notebook", "quantidade": "2", "valor": "1000"},
        {"produto": "Mouse", "quantidade": "5", "valor": "100"},
    ]

    result = top_product(sales)

    assert result == "Mouse"