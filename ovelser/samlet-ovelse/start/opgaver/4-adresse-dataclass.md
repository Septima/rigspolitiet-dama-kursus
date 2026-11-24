# Opgave 4 – Indfør en Adresse-dataclass

**Runde 2 · Person B · Emner: OOP, dataclass, struktur, Git**

## Baggrund

Koden arbejder med rækker som `list[str]` og slår felter op med kolonnenumre som `raekke[POSTNUMMER_KOLONNE]`. Det er svært at læse og let at tage fejl af. En `Adresse`-dataclass med navngivne felter gør koden tydeligere.

## Opgave

1. Skift til `main`, og hent det nyeste, så runde 1 er med. Opret derefter en branch, fx `oop/adresse`.
2. Opret `adresse.py` med:
   - en dataclass `Adresse` med felterne `vejnavn`, `husnummer` og `postnummer`
   - en funktion `fra_raekke(raekke: list[str]) -> Adresse`
   - en funktion `til_raekke(adresse: Adresse) -> list[str]`
3. Ret `validering.py`, så `rens_raekke` erstattes af `rens_adresse(adresse: Adresse) -> Adresse`, og `er_gyldig` tager en `Adresse`. Rens alle tre felter for mellemrum.
4. Ret `koer_job` i `main.py`, så rækkerne laves om til `Adresse`-objekter efter læsning og tilbage til rækker før skrivning.
5. Fjern `POSTNUMMER_KOLONNE` fra `config.py`, når den ikke længere bruges.
6. Skriv en test af `rens_adresse`. Kør `python -m pytest` og `python main.py`, og kontrollér, at resultatet er det samme som før.
7. Commit, publicér branchen, og opret en pull request med din makker som reviewer.

## Klar, når

- [ ] Koden bruger `adresse.postnummer` i stedet for kolonnenumre.
- [ ] Resultatfilen er den samme som før ændringen.
- [ ] Alle tests består, og PR'en er godkendt og merget.

## OBS

Din makker ændrer samtidig i de samme filer. Bliver din PR merget sidst, skal du hente `main` ind i din branch og løse en konflikt.
