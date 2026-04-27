from __future__ import annotations

import csv
from pathlib import Path


def load_sales(file_path: str) -> list[dict]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    with path.open(mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)