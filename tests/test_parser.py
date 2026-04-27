from vendas_cli.parser import load_sales


def test_load_sales() -> None:
    result = load_sales("sample_vendas.csv")

    assert len(result) > 0
    assert result[0]["produto"]