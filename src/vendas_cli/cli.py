from __future__ import annotations

import argparse
import logging
from datetime import date

from vendas_cli.parser import load_sales
from vendas_cli.core import (
    calculate_total,
    filter_by_date,
    sales_by_product,
    top_product,
)
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

    parser.add_argument("arquivo", help="Caminho do arquivo CSV")

    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Formato de saída"
    )

    parser.add_argument("--start", help="Data inicial no formato YYYY-MM-DD")
    parser.add_argument("--end", help="Data final no formato YYYY-MM-DD")

    args = parser.parse_args()

    logging.info("Lendo arquivo CSV...")

    sales = load_sales(args.arquivo)

    start_date = date.fromisoformat(args.start) if args.start else None
    end_date = date.fromisoformat(args.end) if args.end else None

    filtered_sales = filter_by_date(
        sales,
        start=start_date,
        end=end_date
    )

    total = calculate_total(filtered_sales)
    best_seller = top_product(filtered_sales)
    product_totals = sales_by_product(filtered_sales)

    if args.format == "json":
        render_json(
            len(filtered_sales),
            total,
            best_seller,
            product_totals
        )
    else:
        render_text(
            len(filtered_sales),
            total,
            best_seller,
            product_totals
        )


if __name__ == "__main__":
    main()