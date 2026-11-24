import csv
from pathlib import Path

from config import SEPARATOR


def laes_raekker(sti: Path) -> list[list[str]]:
    with open(sti, encoding="utf-8", newline="") as fil:
        return list(csv.reader(fil, delimiter=SEPARATOR))


def skriv_raekker(sti: Path, raekker: list[list[str]]) -> None:
    with open(sti, "w", encoding="utf-8", newline="") as fil:
        csv.writer(fil, delimiter=SEPARATOR).writerows(raekker)
