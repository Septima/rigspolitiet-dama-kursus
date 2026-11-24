# Opgave 3 – Ny regel: vejnavn må ikke være tomt

**Runde 2 · Person A · Emner: struktur, tests, Git**

## Baggrund

Der er kommet rækker uden vejnavn i inputfilen, fx `;7;8000`. De bliver i dag godkendt og havner i resultatet. Fremover skal en række have et vejnavn for at være gyldig.

## Opgave

1. Skift til `main`, og hent det nyeste, så runde 1 er med. Opret derefter en branch, fx `regel/vejnavn`.
2. Tilføj en konstant `VEJNAVN_KOLONNE = 0` i `config.py`.
3. Udvid `er_gyldig` i `validering.py`, så en række kun er gyldig, hvis vejnavnet ikke er tomt eller kun består af mellemrum.
4. Skriv tests af `er_gyldig` for en gyldig række, en række uden vejnavn og en række med et vejnavn, der kun består af mellemrum.
5. Kør `python -m pytest` og `python main.py`.
6. Commit, publicér branchen, og opret en pull request med din makker som reviewer.

## Klar, når

- [ ] Rækken `;7;8000` afvises.
- [ ] Der er tests af den nye regel, og alle tests består.
- [ ] PR'en er godkendt og merget.

## OBS

Din makker ændrer samtidig i de samme filer. Bliver din PR merget sidst, skal du hente `main` ind i din branch og løse en konflikt.
