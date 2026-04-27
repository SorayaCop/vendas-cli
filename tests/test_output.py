from decimal import Decimal

from vendas_cli.output import render_text, render_json


def test_render_text(capsys) -> None:
    product_totals = {"Notebook": Decimal("1000")}

    render_text(4, Decimal("1000"), "Notebook", product_totals)

    captured = capsys.readouterr()

    assert "Registros carregados" in captured.out
    assert "Notebook" in captured.out
    assert "Total por produto" in captured.out


def test_render_json(capsys) -> None:
    product_totals = {"Notebook": Decimal("1000")}

    render_json(4, Decimal("1000"), "Notebook", product_totals)

    captured = capsys.readouterr()

    assert '"registros": 4' in captured.out
    assert '"produto_mais_vendido": "Notebook"' in captured.out
    assert '"total_por_produto"' in captured.out