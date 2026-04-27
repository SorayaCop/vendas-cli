import sys

from vendas_cli.cli import main


def test_cli_text_output(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["vendas-cli", "sample_vendas.csv"]
    )

    main()

    captured = capsys.readouterr()

    assert "Registros carregados" in captured.out
    assert "Produto mais vendido" in captured.out


def test_cli_json_output(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["vendas-cli", "sample_vendas.csv", "--format", "json"]
    )

    main()

    captured = capsys.readouterr()

    assert '"registros"' in captured.out