from __future__ import annotations

import argparse
import logging

from vendas_cli.parser import load_sales
from vendas_cli.core import calculate_total, top_product
from vendas_cli.output import render_text, render_json


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

    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Formato de saída"
    )

    args = parser.parse_args()

    logging.info("Lendo arquivo CSV...")

    sales = load_sales(args.arquivo)
    total = calculate_total(sales)
    best_seller = top_product(sales)

    if args.format == "json":
        render_json(
            total_records=len(sales),
            total_amount=total,
            best_seller=best_seller
        )
    else:
        render_text(
            total_records=len(sales),
            total_amount=total,
            best_seller=best_seller
        )


if __name__ == "__main__":
    main()