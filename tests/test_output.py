from decimal import Decimal

from vendas_cli.output import render_text, render_json


def test_render_text(capsys) -> None:
    render_text(4, Decimal("1000"), "Notebook")

    captured = capsys.readouterr()

    assert "Registros carregados" in captured.out
    assert "Notebook" in captured.out


def test_render_json(capsys) -> None:
    render_json(4, Decimal("1000"), "Notebook")

    captured = capsys.readouterr()

    assert '"registros": 4' in captured.out
    assert '"produto_mais_vendido": "Notebook"' in captured.out