# Adresse-jobbet

Et lille Python-job, der læser adresser fra `data/adresser.csv`, renser postnumre, sorterer ugyldige rækker fra og skriver resultatet til `data/resultat.csv`.

Jobbet køres af et ETL-værktøj, men kan også køres direkte.

## Struktur

| Fil | Ansvar |
| --- | --- |
| `config.py` | Stier og konstanter |
| `filer.py` | Læsning og skrivning af CSV-filer |
| `validering.py` | Regler for rensning og validering |
| `main.py` | Entry point, der binder det hele sammen |
| `tests/` | Tests af reglerne |
| `opgaver/` | Opgavesedler til øvelsen |

## Kom i gang

Åbn mappen i VS Code, og kør i terminalen (**Terminal → New Terminal**):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python main.py
```

Vælg derefter miljøet i VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** → `.venv`.

## Arbejdsgang

Al ændring sker på en branch og kommer ind i `main` via en pull request i Bitbucket:

1. Skift til `main`, og hent det nyeste (**Sync Changes** eller `git pull`).
2. Opret en branch (klik på branch-navnet nederst til venstre → **Create new branch...**).
3. Ret koden, og kør `python -m pytest`.
4. Commit i **Source Control** (`Ctrl+Shift+G`), og publicér branchen (**Publish Branch**).
5. Opret en pull request i Bitbucket mod `main`, og tilføj din makker som reviewer.
6. Når PR'en er godkendt, merges den i Bitbucket.
