# Opgave 1 – Fejlrapport: postnumre med mellemrum bliver afvist

**Runde 1 · Person A · Emner: debugger, tests, Git**

## Baggrund

Driften melder, at adressen *Vestergade 3, 800* mangler i resultatet, selvom den står i inputfilen. I filen står postnummeret som `" 800"` – med et mellemrum foran. Det skulle være blevet til `"0800"`.

Testene består, så fejlen er ikke dækket af en test.

## Opgave

1. Opret en branch fra en opdateret `main`, fx `fejl/postnummer-mellemrum`.
2. Find fejlen med **debuggeren** – ikke ved at tilføje `print`:
   - Sæt et breakpoint i `rens_postnummer` i `validering.py`.
   - Start `main.py` med `F5`, og følg værdien af `vaerdi` i **Variables**.
3. Skriv **først** en test, der fanger fejlen, og se den fejle med `python -m pytest`.
4. Ret fejlen, og se testen bestå.
5. Commit, publicér branchen, og opret en pull request med din makker som reviewer.

## Klar, når

- [ ] Der er en test for `rens_postnummer(" 800") == "0800"`.
- [ ] Alle tests består.
- [ ] `python main.py` skriver *Vestergade* med postnummer `0800` i resultatet.
- [ ] PR'en er godkendt og merget.
