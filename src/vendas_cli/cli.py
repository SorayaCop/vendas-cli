from __future__ import annotations

import argparse
import logging

from vendas_cli.parser import load_sales
from vendas_cli.core import calculate_total
from vendas_cli.output import render_text


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="vendas-cli",
        description="Processador de vendas CSV"
    )

    parser.add_argument(
        "arquivo",
        help="Caminho do arquivo CSV"
    )

    args = parser.parse_args()

    logging.info("Lendo arquivo CSV...")

    sales = load_sales(args.arquivo)
    total = calculate_total(sales)

    render_text(
        total_records=len(sales),
        total_amount=total
    )


if __name__ == "__main__":
    main()