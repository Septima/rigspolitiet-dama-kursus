# Opgave 2 – Gør jobbet klar til ETL-værktøjet

**Runde 1 · Person B · Emner: entry point, logging, fejlhåndtering, Git**

## Baggrund

ETL-værktøjet skal kunne kalde jobbet som en funktion med sine egne stier. I dag står stierne fast i `main`, og jobbet skriver med `print`, som ingen ser i værktøjets log. Afviste rækker forsvinder også uden spor.

## Opgave

Alle ændringer sker i `main.py`.

1. Opret en branch fra en opdateret `main`, fx `etl/koer-job`.
2. Lav en funktion `koer_job(input_sti, output_sti) -> int`, som udfører jobbet med de givne stier og returnerer antallet af skrevne rækker.
3. Brug `logging` i stedet for `print`:
   - Log antallet af skrevne og læste rækker på niveau `info`.
   - Log hver afvist række på niveau `warning`.
4. Hvis inputfilen ikke findes, skal fejlen logges på niveau `error` og sendes videre med `raise`.
5. Lad `main()` sætte logging op med `logging.basicConfig(level=logging.INFO)` og kalde `koer_job(INPUT_STI, OUTPUT_STI)`.
6. Kør `python main.py`, og prøv også med en forkert sti.
7. Commit, publicér branchen, og opret en pull request med din makker som reviewer.

## Klar, når

- [ ] `koer_job` kan kaldes med andre stier end dem i `config.py`.
- [ ] Afviste rækker står som advarsler i outputtet.
- [ ] En manglende inputfil giver en tydelig fejl – ikke en tom resultatfil.
- [ ] Alle tests består, og PR'en er godkendt og merget.

## Bonus

Skriv en test af `koer_job` med pytests `tmp_path`, som opretter en lille inputfil og kontrollerer resultatet.
