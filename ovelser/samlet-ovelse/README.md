# Samlet praktisk øvelse – underviservejledning

Øvelsen "Adresse-jobbet i produktion" samler dagens emner i ét forløb på 90 minutter for hold á to personer. Slides og lærernoter findes i [slides/dag2](../../slides/dag2/).

| Mappe/fil | Indhold |
| --- | --- |
| [start/](./start/) | Startprojektet, som hvert hold får i et Bitbucket-repository. Indeholder en plantet fejl og opgavesedler 1–4 i `opgaver/`. |
| [5-ups-separator.md](./5-ups-separator.md) | Opgave 5, som underviseren udleverer ca. 10 minutter før tid. Ligger bevidst uden for startprojektet. |
| [loesning/](./loesning/) | Sluttilstanden efter opgave 1–4 inklusive løst konflikt. Efter opgave 5 er koden den samme igen. |

## Forberedelse

1. **Opret ét repository pr. hold** i Bitbucket, fx `adresse-job-hold-1`, med indholdet af `start/` som første commit på `main`:

   ```bash
   cd start
   git init -b main
   git add .
   git commit -m "Startprojekt"
   git remote add origin <adresse på holdets repository>
   git push -u origin main
   ```

2. **Giv begge deltagere skriveadgang** til holdets repository.
3. **Vælg merge-strategien "Merge commit"** i repositoryets indstillinger, så revert i opgave 5 virker med `git revert -m 1`. Bruges *squash*, skal `-m 1` udelades.
4. Overvej at kræve **mindst én godkendelse** før merge til `main` (branch permissions / merge checks).
5. **Afprøv adgangen inden kurset:** Kan deltagerne klone og pushe fra VS Code på kursusmaskinerne? Kræves der app-password, API-token eller SSO-login, skal det være på plads på forhånd – det er den hyppigste årsag til, at øvelsen går i stå.
6. Kontrollér, at Python, Git og VS Code med Python-udvidelsen er installeret, og at `pip install pytest` virker. Har maskinerne ikke internetadgang, skal pytest installeres på forhånd.

## Forløbet

| Tid | Person A | Person B |
| --- | --- | --- |
| 0–10 min. | Klon, opret miljø, kør tests og jobbet | Samme |
| 10–40 min. | Opgave 1: fejl i postnumre (debugger, tests) | Opgave 2: gør jobbet ETL-klar (entry point, logging, fejl) |
| 40–70 min. | Opgave 3: ny regel for vejnavn (tests) | Opgave 4: `Adresse`-dataclass (OOP) |
| 70–80 min. | Opgave 5: ups – ændring og revert | Opgave 5 |
| 80–90 min. | Fælles opsamling | |

Opgave 1 og 2 rører ikke de samme filer og giver ingen konflikt. Opgave 3 og 4 ændrer begge `config.py`, `validering.py` og `tests/test_validering.py`. Den, der merger sidst, får en konflikt i alle tre filer.

## Forventede resultater

| Tidspunkt | `python main.py` | `python -m pytest` |
| --- | --- | --- |
| Start | 3 af 5 rækker – *Vestergade* mangler fejlagtigt, rækken uden vejnavn kommer med | 2 tests består |
| Efter runde 1 | 4 af 5 rækker – kun *Torvet* (`80a0`) afvises og logges | 3 tests består (flere med bonus) |
| Efter runde 2 | 3 af 5 rækker – *Torvet* og rækken uden vejnavn afvises | 5 tests består |
| Efter opgave 5, del 1 | `ValueError: not enough values to unpack` | 5 tests består – testene dækker ikke filindlæsningen |
| Efter revert | 3 af 5 rækker igen | 5 tests består |

Hele forløbet er afprøvet med Git, herunder konflikten i runde 2 og revert i opgave 5.
