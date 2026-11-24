# Opgave 5 – Ups! Leverandøren skifter separator

**Udleveres af underviseren ca. 10 minutter før tid · Hele holdet · Emner: revert, Git**

## Del 1 – Ændringen

Leverandøren af adressefilen meddeler, at filerne fremover bliver kommaseparerede.

1. Person A: Opret en branch fra en opdateret `main`, fx `config/komma`.
2. Ret `SEPARATOR` i `config.py` til `","`.
3. Commit, publicér, og opret en pull request. Person B godkender, og PR'en merges.

## Del 2 – Ups

Lige efter merge kører driften jobbet på dagens fil – og det går galt. Leverandøren skifter først næste måned.

1. Hent `main`, og kør `python main.py`. Hvad sker der?
2. Person B: Fortryd ændringen med en **revert** – uden at slette eller omskrive historikken på `main`. Brug terminalen i VS Code:

   ```bash
   git switch main
   git pull
   git log --oneline -5
   git switch -c fortryd/komma
   git revert -m 1 <id på merge-commit'et>
   git push -u origin fortryd/komma
   ```

   Har jeres Bitbucket en **Revert**-knap på den mergede pull request, kan I bruge den i stedet.
3. Opret en pull request for fortrydelsen. Person A godkender, og den merges.
4. Hent `main`, og kør `python main.py` og `python -m pytest` igen.

## Klar, når

- [ ] Jobbet virker igen på dagens fil.
- [ ] Historikken på `main` viser både ændringen og fortrydelsen.
