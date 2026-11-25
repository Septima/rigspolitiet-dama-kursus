# Øvelsesvejledning – dag 2

**Python – struktur, OOP, Git og VS Code**

Denne vejledning hører til dagens slides. Den beskriver hver øvelse mere udførligt, end der er plads til på slides: hvorfor vi laver øvelsen, hvad I skal gøre, og hvad I kan gøre, hvis I går i stå. Løsningsforslag til alle øvelser står samlet bagerst.

Prøv selv først. Løsningerne er der til at sammenligne med bagefter, eller hvis I sidder helt fast. Der er ofte flere gode løsninger. Det vigtigste er, at I kan forklare jeres valg.

## Indhold

- [Før I starter](#før-i-starter)
- [Øvelse 1 – Git: jeres første pull request og konflikt](#øvelse-1--git-jeres-første-pull-request-og-konflikt) · 30 min.
- [Øvelse 2 – Refaktorér scriptet](#øvelse-2--refaktorér-scriptet) · 25 min.
- [Øvelse 3 – Class eller funktion?](#øvelse-3--class-eller-funktion) · 10 min.
- [Øvelse 4 – Skriv jeres første tests](#øvelse-4--skriv-jeres-første-tests) · 20 min.
- [Øvelse 5 – Find fejlen med debuggeren](#øvelse-5--find-fejlen-med-debuggeren) · 15 min.
- [Øvelse 6 – Samlet øvelse: Adresse-jobbet i produktion](#øvelse-6--samlet-øvelse-adresse-jobbet-i-produktion) · 90 min.
- [Opslag: Git, VS Code og pytest](#opslag-git-vs-code-og-pytest)
- [Løsninger](#løsninger)

---

## Før I starter

### Arbejdsform

Alle øvelser laves **to og to**. Skift gerne til at sidde ved tastaturet, så I begge prøver det hele. Snak højt om, hvad I gør og hvorfor – det er en stor del af læringen.

### Det skal være installeret

- **Python** 3.10 eller nyere
- **Git**
- **VS Code** med udvidelsen **Python** fra Microsoft
- Adgang til **Bitbucket**, hvor underviseren har oprettet repositories til jeres hold

Kontrollér i en terminal (**Terminal → New Terminal** i VS Code):

```bash
python --version
git --version
```

### Første gang med Git på maskinen

Git skal vide, hvem I er, så jeres commits får det rigtige navn:

```bash
git config --global user.name "Dit Navn"
git config --global user.email "din@mail.dk"
```

### Et virtuelt miljø pr. projekt

Et *virtuelt miljø* er en separat Python-installation til ét projekt med dets egne pakker. I opretter et miljø i hvert projekt, I arbejder i:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pytest
```

Vælg derefter miljøet i VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** → `.venv`. Så bruger editoren, testene og debuggeren det samme miljø.

> **Tip:** Fejler aktiveringen i PowerShell, kan I springe den over. Når miljøet er valgt i VS Code, bruger nye terminaler det automatisk.

### Materialer

Underviseren udleverer projekterne til øvelserne – enten som Bitbucket-repositories eller som mapper:

| Øvelse | Materiale |
| --- | --- |
| 1 | Holdets Git-øvelsesrepository på Bitbucket |
| 2 | `refactoring/start/` med `adresse_script.py` og `data/adresser.csv` |
| 3 | Ingen – det er en diskussionsøvelse |
| 4 | Jeres refaktorerede projekt fra øvelse 2 (eller `refactoring/loesning/`) |
| 5 | `debugging/start/` |
| 6 | Holdets repository med adresse-jobbet på Bitbucket |

---

## Øvelse 1 – Git: jeres første pull request og konflikt

**30 minutter · to og to · hører til afsnittet "Git-grundlag"**

### Formål

I skal prøve hele samarbejdsflowet fra Git-afsnittet i praksis, mens indholdet er så enkelt, at I kan koncentrere jer om Git: branch, commit, publicering, pull request, review, merge – og en konflikt.

### Baggrund

Når flere arbejder i samme kode, ændrer ingen direkte i `main`. Hver ændring laves på en *branch*, som er en separat udviklingslinje. Når ændringen er klar, oprettes en *pull request* (PR) på Bitbucket. Det er et forslag om at få branchen flettet ind i `main`. En kollega gennemgår ændringerne – det kaldes *review* – og når de er godkendt, *merges* de ind i `main`.

En *konflikt* opstår, når to personer har ændret de samme linjer, og Git ikke selv kan afgøre, hvad resultatet skal være. Det er helt normalt og ikke en fejl hos nogen. Et menneske skal blot tage stilling til, hvad den rigtige version er.

I bruger VS Codes indbyggede Git-klient til at tale med Bitbucket. PR'er oprettes og merges på Bitbucket i browseren.

### Del 1 – Jeres første pull request (15 min.)

1. **Klon repositoryet.** Find holdets Git-øvelsesrepository på Bitbucket, og kopiér adressen via knappen **Clone**. I VS Code: `Ctrl+Shift+P` → **Git: Clone** → indsæt adressen → vælg en mappe → **Open**.
2. **Opret hver jeres branch.** Klik på branch-navnet `main` nederst til venstre i VS Code → **Create new branch...** → skriv fx `anna/praesentation`.
3. **Lav en ændring.** Opret filen `deltagere/<dit navn>.md`, og skriv et par linjer om dig selv – fx hvad du arbejder med, og hvad du bruger Python til.
4. **Commit.** Åbn **Source Control** (`Ctrl+Shift+G`). Den nye fil står under *Changes*. Klik `+` ud for filen for at vælge den til commit (*staging*), skriv en kort besked som "Tilføj præsentation af Anna", og klik **Commit**.
5. **Publicér branchen.** Klik **Publish Branch**. Nu ligger branchen også på Bitbucket.
6. **Opret en pull request.** Gå til repositoryet på Bitbucket → **Pull requests** → **Create pull request**. Vælg jeres branch som kilde og `main` som mål. Skriv en kort beskrivelse, og tilføj makkeren som *reviewer*.
7. **Review og merge.** Åbn makkerens PR, og se ændringerne under **Diff**. Skriv evt. en kommentar, klik **Approve**, og derefter **Merge** med strategien **Merge commit**.
8. **Hent den nye main.** Skift til `main` nederst til venstre, og klik **Sync Changes**. Nu har I begge præsentationer lokalt.

### Del 2 – Jeres første konflikt (15 min.)

1. Stå på en opdateret `main`, og opret hver jeres nye branch, fx `anna/holdnavn`.
2. Åbn `holdet.md`. Ret **begge** linjen `Holdets navn: (skriv jeres forslag her)` til jeres eget forslag til et holdnavn – uden at aftale det med hinanden.
3. Commit, publicér, og opret hver jeres PR mod `main`.
4. Merge **den ene** PR. Se nu på den anden: Bitbucket viser, at den har en konflikt og ikke kan merges.
5. Den, hvis PR har konflikten, løser den lokalt på sin branch:
   - `Ctrl+Shift+P` → **Git: Fetch**.
   - `Ctrl+Shift+P` → **Git: Merge** → vælg `origin/main`.
   - `holdet.md` står nu under **Merge Changes** i Source Control. Åbn filen, og klik **Resolve in Merge Editor**.
   - Vælg, hvad linjen skal indeholde. Prøv fx at kombinere de to forslag, så ingen af dem forsvinder.
   - Klik **Complete Merge**, derefter **Commit** og **Sync Changes**.
6. PR'en er nu opdateret og uden konflikt. Makkeren godkender, og den merges.

### Hvis I går i stå

- **Klon eller publicering fejler med en adgangsfejl:** Kontrollér, at I er logget ind på Bitbucket, og at I har skriveadgang. Spørg underviseren – login er den hyppigste årsag til problemer.
- **Ændringerne endte på `main`:** I har glemt at oprette en branch. Spørg underviseren, før I publicerer.
- **I fortryder midt i konflikten:** `Ctrl+Shift+P` → **Git: Abort Merge** (eller `git merge --abort` i terminalen) sætter branchen tilbage til før merge.

### I er færdige, når

- [ ] Begge præsentationer ligger i `deltagere/` på `main` på Bitbucket.
- [ ] Linjen med holdnavnet på `main` er resultatet af jeres konfliktløsning.
- [ ] Der er fire mergede pull requests.

---

## Øvelse 2 – Refaktorér scriptet

**25 minutter · to og to · hører til afsnittet "Python-struktur og refactoring"**

### Formål

I skal omskrive et script, der virker, så det bliver lettere at forstå, ændre, teste og genbruge – uden at ændre, hvad det gør. Det kaldes *refactoring*.

### Baggrund

`adresse_script.py` læser adresser fra `data/adresser.csv`, renser postnumre ved at fjerne mellemrum og fylde op med nuller foran, sorterer ugyldige rækker fra og skriver resultatet til `data/resultat.csv`. Det er det samme script, som står på sliden "Udgangspunktet: et script, der virker".

Scriptet fungerer, men alt ligger i én blok: læsning, regler og skrivning er blandet sammen. Stier og kolonnenumre står midt i koden, og variabelnavne som `r`, `pn` og `f` siger ikke meget. Reglen for postnumre kan hverken genbruges i et andet job eller testes uden at læse og skrive filer.

Når I refaktorerer, arbejder I i **små skridt**: Lav én ændring, kør scriptet, kontrollér at resultatet er det samme, og commit. Går noget galt, er det let at se, hvad der skete, og at gå tilbage.

### Sådan gør I

1. **Læg projektet i Git, og opret en branch.** Åbn mappen i VS Code. Er den ikke allerede et Git-repository, så kør `git init` og commit filerne på `main` først. Opret derefter en branch:

   ```bash
   git switch -c refactoring
   ```

2. **Kør scriptet, og gem resultatet.** Kør `python adresse_script.py`, og se på `data/resultat.csv`. Det er facit – resultatet skal være det samme efter hvert skridt. Scriptet skriver `Fejl: ['Torvet', '1', '80a0']`, fordi den række har et ugyldigt postnummer.
3. **Flyt værdier op som konstanter.** Giv stier, separator og kolonnenummeret for postnummeret navne øverst i filen, fx `SEPARATOR = ";"` og `POSTNUMMER_KOLONNE = 2`. Kør scriptet, og commit.
4. **Udtræk funktioner.** Lav små funktioner med ét ansvar hver: én til at læse rækker, én til at rense et postnummer, én til at afgøre, om et postnummer er gyldigt, og én til at skrive rækker. Funktionerne skal få det, de bruger, som argumenter og returnere resultatet – ikke ændre globale variabler. Kør scriptet, og commit efter hver funktion.
5. **Saml forløbet i `main()`.** Lad en funktion `main()` kalde de andre i rækkefølge, og kald den nederst i filen under `if __name__ == "__main__":`. Kør scriptet, og commit.
6. **Har I tid: del koden op i moduler.** Flyt konstanter til `config.py`, læsning og skrivning til `filer.py`, regler til `validering.py`, og lad `main.py` binde det sammen med imports. Kør `python main.py`, og commit.

### Gode råd

- Giv funktioner navne, der siger, hvad de gør – fx `rens_postnummer` frem for `behandl`.
- Brug type hints, fx `def rens_postnummer(vaerdi: str) -> str:`.
- **VS Code kan hjælpe:** Markér en variabel, og tryk `F2` (**Rename Symbol**) for at omdøbe den alle steder.
- Det er helt i orden, hvis I ikke når trin 6. Trin 3–5 er det vigtigste.

### Hvis I går i stå

- **`ModuleNotFoundError` efter opdeling i moduler:** Kør `python main.py` fra projektmappen, og kontrollér stavningen af filnavne og imports.
- **I har ødelagt noget:** `git status` og `git diff` viser, hvad der er ændret. `git restore <fil>` henter filen tilbage fra sidste commit.

### I er færdige, når

- [ ] Koden er delt op i små funktioner med beskrivende navne.
- [ ] Stier og kolonnenumre står som konstanter ét sted.
- [ ] Resultatfilen er den samme som før.
- [ ] Hvert skridt er committet på branchen `refactoring`.

---

## Øvelse 3 – Class eller funktion?

**10 minutter · diskussion to og to · hører til afsnittet "OOP: class eller funktion?"**

### Formål

I skal øve jer i at vurdere, hvornår en class gør koden bedre, og hvornår en funktion eller en dataclass er det enkleste valg. Der skal ikke skrives kode.

### Baggrund

En **funktion** er det enkleste valg, når kode tager noget ind og returnerer et resultat uden at skulle huske noget. En **dataclass** passer til data med faste, navngivne felter. En **class** giver værdi, når data og adfærd hører sammen, når der er *tilstand* – noget der skal huskes og kan ændre sig undervejs – eller når de samme argumenter sendes rundt mellem mange funktioner.

### Sådan gør I

Diskutér hvert scenarie, og bliv enige om, hvad I ville vælge. Skriv begrundelsen ned i en enkelt sætning.

1. Omregning af koordinater fra én projektion til en anden
2. En databaseforbindelse, som flere trin i et job bruger
3. En række med `id`, `navn` og `dato`, der sendes mellem trin
4. Fem funktioner, der alle tager `sti`, `separator` og `encoding`

Spørgsmål, der kan hjælpe:

- Skal noget huskes mellem kaldene?
- Hører data og adfærd tydeligt sammen?
- Er det mest data, mest adfærd – eller begge dele?
- Hvad ville gøre koden lettest at forstå for den næste, der skal læse den?

### I er færdige, når

- [ ] I har et valg og en begrundelse for alle fire scenarier.

---

## Øvelse 4 – Skriv jeres første tests

**20 minutter · to og to · hører til afsnittet "Tests"**

### Formål

I skal skrive og køre simple tests med pytest og se, hvordan en test fanger en fejl.

### Baggrund

En test er kode, der kalder jeres kode med et kendt input og kontrollerer, at resultatet er det forventede. Med pytest er en test en almindelig funktion, hvis navn starter med `test_`, i en fil, hvis navn også starter med `test_`. `assert` kontrollerer, at et udtryk er sandt – ellers fejler testen.

Tests er særligt nyttige sammen med refactoring: Består testene både før og efter en ændring, har I ikke ændret den adfærd, de tester.

### Sådan gør I

I arbejder i jeres refaktorerede projekt fra øvelse 2. Nåede I ikke at udtrække funktionerne, så brug `refactoring/loesning/`.

1. **Installér pytest** i projektets miljø, hvis det ikke er gjort:

   ```bash
   pip install pytest
   ```

2. **Opret testfilen** `tests/test_validering.py`.
3. **Skriv tests** for `rens_postnummer` og `er_gyldigt_postnummer`. Tænk over både det normale tilfælde og *kanttilfælde*:
   - Et postnummer, der skal have et nul foran, fx `" 800"`.
   - Et gyldigt postnummer, fx `"8000"`.
   - Ugyldige værdier: for få cifre, et bogstav, en tom tekst.
4. **Kør testene** fra projektmappen:

   ```bash
   python -m pytest
   ```

   Hvert punktum i outputtet er en test, der bestod.
5. **Se en test fejle.** Lav bevidst en fejl, fx ved at fjerne `.zfill(4)` i `rens_postnummer`. Kør testene igen, og læs outputtet: Hvilken test fejlede, hvad forventede den, og hvad fik den? Ret fejlen igen, og se testene bestå.
6. **Commit testene.**

### Gode råd

- Brug `python -m pytest` frem for blot `pytest`. Så bruges det aktive miljø, og testene kan importere jeres moduler.
- Giv testene navne, der beskriver, hvad de tester. Så forstår man fejlen alene ud fra navnet.
- VS Code har et **Testing**-panel (kolbeikonet), hvor tests kan køres med et klik. Første gang skal I vælge **pytest** og mappen `tests`.

### Hvis I går i stå

- **`ModuleNotFoundError: No module named 'validering'`:** Kør fra projektmappen med `python -m pytest`.
- **pytest finder ingen tests:** Kontrollér, at både filen og funktionerne starter med `test_`.
- **`No module named pytest`:** pytest er ikke installeret i det miljø, I bruger. Kontrollér det valgte miljø, og kør `pip install pytest`.

### I er færdige, når

- [ ] Der er tests af begge funktioner, også af kanttilfælde.
- [ ] Alle tests består.
- [ ] I har set en test fejle og forstået outputtet.
- [ ] Testene er committet.

---

## Øvelse 5 – Find fejlen med debuggeren

**15 minutter · to og to · hører til afsnittet "Afvikling i ETL og fejlfinding i VS Code"**

### Formål

I skal bruge debuggeren i VS Code til at finde en fejl, der giver et forkert resultat uden at give en fejlmeddelelse, og derefter sikre jer med en test, at den ikke kommer igen.

### Baggrund

En *debugger* stopper programmet på en bestemt linje – et *breakpoint* – så I kan se værdierne af variablerne og følge koden linje for linje. Det er ofte hurtigere og mere præcist end at sprede `print` ud i koden.

Projektet i `debugging/start/` ligner løsningen fra øvelse 2, men en kollega har lavet en ændring. Jobbet kører uden fejl, men resultatet er forkert: Åbn `data/resultat.csv` efter en kørsel, og sammenlign med inputfilen. Alle fire rækker kommer med – også *Torvet* med det ugyldige postnummer `80a0` – og husnumrene ser mærkelige ud.

| Handling | Genvej |
| --- | --- |
| Sæt eller fjern et breakpoint | Klik i margenen til venstre for linjenummeret, eller `F9` |
| Start debugging | `F5` |
| Kør næste linje | `F10` |
| Gå ind i funktionen på linjen | `F11` |
| Fortsæt til næste breakpoint | `F5` |

### Sådan gør I

1. Åbn `debugging/start/` i VS Code, og vælg Python-miljøet.
2. Kør `python main.py`, og se på resultatet i `data/resultat.csv`.
3. Åbn `validering.py`, og sæt et breakpoint på den første linje inde i `rens_raekke`.
4. Åbn `main.py`, og start med `F5`. Vælg **Python Debugger** og **Python File**, hvis VS Code spørger.
5. Når programmet stopper, så se i **Variables**-panelet til venstre. Hvad indeholder `raekke`? Brug `F10` til at gå linje for linje. Hvilken værdi bliver behandlet som postnummer?
6. Find årsagen, og ret den.
7. Skriv en test, der ville have fanget fejlen, og kør `python -m pytest`. Kontrollér, at testen fejler, hvis I sætter fejlen ind igen.
8. Commit rettelsen og testen.

### Gode råd

- I **Debug Console** nederst kan I skrive udtryk, mens programmet står stille, fx `raekke[2]`.
- Panelet **Call Stack** viser, hvilke funktioner der har kaldt hinanden for at nå den aktuelle linje.
- Fandt I fejlen ved at læse koden? Fint – men prøv alligevel debuggeren, så I kender den, når koden er større.

### I er færdige, når

- [ ] Resultatet indeholder tre rækker med korrekte husnumre og postnumre.
- [ ] Der er en test, der fejler med fejlen og består uden.

---

## Øvelse 6 – Samlet øvelse: Adresse-jobbet i produktion

**90 minutter · to og to · hører til afsnittet "Samlet praktisk øvelse"**

### Formål

Øvelsen samler hele dagen. I arbejder som et lille team, der vedligeholder et rigtigt job: Hver af jer løser opgaver på jeres egen branch, opretter pull requests og reviewer hinandens ændringer – præcis som i en almindelig arbejdsdag.

### Baggrund

Holdet har overtaget *adresse-jobbet*. Det ligner løsningen fra øvelse 2, men er lagt i et fælles Bitbucket-repository og køres af et ETL-værktøj. Driften og leverandøren af adressefilen sender opgaver, som I løser én ad gangen. Opgaverne står nedenfor og også som opgavesedler i mappen `opgaver/` i repositoryet.

Én af jer er **person A**, den anden **person B**. I hver runde løser I hver jeres opgave samtidig.

| Tid | Person A | Person B |
| --- | --- | --- |
| 0–10 min. | Kom i gang | Kom i gang |
| 10–40 min. | Opgave 1: fejl i postnumre | Opgave 2: gør jobbet ETL-klart |
| 40–70 min. | Opgave 3: ny regel for vejnavn | Opgave 4: `Adresse`-dataclass |
| 70–80 min. | Opgave 5: udleveres af underviseren | Opgave 5 |
| 80–90 min. | Fælles opsamling | |

### Kom i gang

1. Klon holdets repository: `Ctrl+Shift+P` → **Git: Clone** → adressen fra Bitbucket.
2. Opret miljøet, og kør tests og jobbet:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python -m pytest
   python main.py
   ```

3. Vælg `.venv` med **Python: Select Interpreter**.
4. Se på `data/adresser.csv` og `data/resultat.csv`. Jobbet skriver tre af fem rækker. Læg mærke til, hvilke rækker der mangler, og hvilke der er med – det får I brug for.
5. Aftal, hvem der er person A og B.

### Arbejdsgangen for hver opgave

Hver opgave følger det samme flow som i øvelse 1:

| Trin | I VS Code | I terminalen |
| --- | --- | --- |
| Hent nyeste main | Skift til `main` → **Sync Changes** | `git switch main` · `git pull` |
| Opret branch | Branch-navnet nederst → **Create new branch** | `git switch -c navn` |
| Commit | **Source Control** → `+` → besked → **Commit** | `git add` · `git commit` |
| Del branchen | **Publish Branch** | `git push -u origin navn` |
| Pull request | Opret på Bitbucket mod `main` med makkeren som reviewer | |

**Start altid en ny opgave fra en opdateret `main`.** Ellers bygger I videre på en gammel version.

### Sådan reviewer I

Review handler om at hjælpe hinanden – ikke om at finde fejl hos personen. Når I reviewer makkerens PR, så spørg:

- Gør ændringen det, opgaven beder om? Tjek punkterne under "Klar, når".
- Er koden til at forstå – navne, struktur, ansvar?
- Er der tests, og består de? Er I i tvivl, så hent branchen og kør `python -m pytest`.

Kommentér konkret og venligt. Godkend med **Approve**, og merge med **Merge commit**.

### Runde 1

#### Opgave 1 – Fejlrapport: postnumre med mellemrum bliver afvist (person A)

*Emner: debugger, tests, Git*

Driften melder, at adressen *Vestergade 3* mangler i resultatet, selvom den står i inputfilen. I filen står postnummeret som `" 800"` – med et mellemrum foran. Det skulle være blevet til `"0800"`. Testene består, så fejlen er ikke dækket af en test.

1. Opret en branch fra en opdateret `main`, fx `fejl/postnummer-mellemrum`.
2. Find fejlen med **debuggeren** – ikke ved at tilføje `print`. Sæt et breakpoint i `rens_postnummer` i `validering.py`, start `main.py` med `F5`, og følg værdien af `vaerdi` i **Variables**. Breakpointet rammes én gang pr. række, så tryk `F5` for at fortsætte, indtil `vaerdi` er `' 800'`.
3. Skriv **først** en test, der fanger fejlen, og se den fejle med `python -m pytest`. Så ved I, at testen faktisk tester fejlen.
4. Ret fejlen, og se testen bestå.
5. Commit, publicér, og opret en PR med person B som reviewer.

**Klar, når:**

- [ ] Der er en test for `rens_postnummer(" 800") == "0800"`.
- [ ] Alle tests består.
- [ ] `python main.py` skriver *Vestergade* med postnummer `0800` i resultatet.
- [ ] PR'en er godkendt og merget.

#### Opgave 2 – Gør jobbet klar til ETL-værktøjet (person B)

*Emner: entry point, logging, fejlhåndtering, Git*

ETL-værktøjet skal kunne kalde jobbet som en funktion med sine egne stier. I dag står stierne fast i `main`, og jobbet skriver med `print`, som ingen ser i værktøjets log. Afviste rækker forsvinder også uden spor. Alle ændringer sker i `main.py`.

1. Opret en branch fra en opdateret `main`, fx `etl/koer-job`.
2. Lav en funktion `koer_job(input_sti, output_sti) -> int`, som udfører jobbet med de givne stier og returnerer antallet af skrevne rækker.
3. Brug `logging` i stedet for `print`:
   - Opret en logger øverst i filen: `logger = logging.getLogger(__name__)`.
   - Log antallet af skrevne og læste rækker på niveau `info`.
   - Log hver afvist række på niveau `warning`. Det kræver, at I gennemløber rækkerne med en løkke i stedet for en list comprehension.
4. Hvis inputfilen ikke findes, skal fejlen logges på niveau `error` og sendes videre med `raise`. Fang kun `FileNotFoundError`.
5. Lad `main()` sætte logging op med `logging.basicConfig(level=logging.INFO)` og kalde `koer_job(INPUT_STI, OUTPUT_STI)`.
6. Kør `python main.py`. Prøv også midlertidigt med en sti, der ikke findes, og se fejlen.
7. Commit, publicér, og opret en PR med person A som reviewer.

**Klar, når:**

- [ ] `koer_job` kan kaldes med andre stier end dem i `config.py`.
- [ ] Afviste rækker står som advarsler i outputtet.
- [ ] En manglende inputfil giver en tydelig fejl – ikke en tom resultatfil.
- [ ] Alle tests består, og PR'en er godkendt og merget.

**Bonus:** Skriv en test af `koer_job` med pytests indbyggede `tmp_path`, som giver en midlertidig mappe. Opret en lille inputfil i mappen, kald `koer_job`, og kontrollér resultatet.

#### Når runde 1 er færdig

Begge skifter til `main` og henter det nyeste. Kør `python -m pytest` og `python main.py`. Nu skal jobbet skrive fire af fem rækker og logge *Torvet* som afvist.

### Runde 2

I denne runde ændrer I begge i de samme filer. **Den, der merger sidst, får en konflikt.** Det er meningen – det er den, I skal lære at løse.

#### Opgave 3 – Ny regel: vejnavn må ikke være tomt (person A)

*Emner: struktur, tests, Git*

Der er kommet rækker uden vejnavn i inputfilen, fx `;7;8000`. De bliver i dag godkendt og havner i resultatet. Fremover skal en række have et vejnavn for at være gyldig.

1. Skift til `main`, hent det nyeste, og opret en branch, fx `regel/vejnavn`.
2. Tilføj en konstant `VEJNAVN_KOLONNE = 0` i `config.py`.
3. Udvid `er_gyldig` i `validering.py`, så en række kun er gyldig, hvis vejnavnet ikke er tomt eller kun består af mellemrum.
4. Skriv tests af `er_gyldig` for en gyldig række, en række uden vejnavn og en række med et vejnavn, der kun består af mellemrum.
5. Kør `python -m pytest` og `python main.py`.
6. Commit, publicér, og opret en PR med person B som reviewer.

**Klar, når:**

- [ ] Rækken `;7;8000` afvises.
- [ ] Der er tests af den nye regel, og alle tests består.
- [ ] PR'en er godkendt og merget.

#### Opgave 4 – Indfør en Adresse-dataclass (person B)

*Emner: OOP, dataclass, struktur, Git*

Koden arbejder med rækker som `list[str]` og slår felter op med kolonnenumre som `raekke[POSTNUMMER_KOLONNE]`. Det er svært at læse og let at tage fejl af. En `Adresse`-dataclass med navngivne felter gør koden tydeligere.

1. Skift til `main`, hent det nyeste, og opret en branch, fx `oop/adresse`.
2. Opret `adresse.py` med:
   - en dataclass `Adresse` med felterne `vejnavn`, `husnummer` og `postnummer`
   - en funktion `fra_raekke(raekke: list[str]) -> Adresse`
   - en funktion `til_raekke(adresse: Adresse) -> list[str]`
3. Ret `validering.py`, så `rens_raekke` erstattes af `rens_adresse(adresse: Adresse) -> Adresse`, og `er_gyldig` tager en `Adresse`. Rens alle tre felter for mellemrum.
4. Ret `koer_job` i `main.py`, så rækkerne laves om til `Adresse`-objekter efter læsning og tilbage til rækker før skrivning.
5. Fjern `POSTNUMMER_KOLONNE` fra `config.py`, når den ikke længere bruges.
6. Skriv en test af `rens_adresse`. Kør `python -m pytest` og `python main.py`, og kontrollér, at resultatet er det samme som før ændringen.
7. Commit, publicér, og opret en PR med person A som reviewer.

**Klar, når:**

- [ ] Koden bruger `adresse.postnummer` i stedet for kolonnenumre.
- [ ] Resultatfilen er den samme som før ændringen.
- [ ] Alle tests består, og PR'en er godkendt og merget.

#### Konflikt? Sådan gør I

Når den første PR er merget, viser Bitbucket, at den anden har en konflikt. Den, der ejer den anden PR, løser den lokalt på sin branch:

1. Hent den nyeste `main` ind i jeres branch:

   ```bash
   git fetch origin
   git merge origin/main
   ```

   Eller i VS Code: **Git: Fetch** og derefter **Git: Merge** → `origin/main`.

2. Filer med konflikt står under **Merge Changes** i Source Control. Åbn hver fil, og klik **Resolve in Merge Editor**.
3. **Kombinér ændringerne.** Her er hverken jeres egen eller makkerens version rigtig alene: Den endelige kode skal både have dataclassen og den nye regel for vejnavn. Læs begge sider, og skriv den version, der indeholder begge ændringer.
4. Kør `python -m pytest`, **før** I afslutter. Testene afslører, om de to ændringer passer sammen.
5. Klik **Complete Merge**, derefter **Commit** og **Sync Changes**. PR'en opdateres og kan merges.

Bliver det uoverskueligt, kan I starte forfra med `git merge --abort`.

#### Når runde 2 er færdig

Hent `main`. Nu skal der være fem tests, der består, og jobbet skal skrive tre af fem rækker og afvise både *Torvet* og rækken uden vejnavn.

### Opgave 5 – Udleveres af underviseren

Ca. 10 minutter før tid får I en sidste opgave fra underviseren. Læs ikke løsningen bagest, før I har prøvet den.

### Opsamling

Kør `git log --oneline --graph` i terminalen på `main`, eller se historikken under **Commits** på Bitbucket. Grafen viser jeres branches, merges, konfliktløsningen og resten af dagens arbejde. Tal sammen om:

- Hvad var svært ved konflikten – og hvordan løste I den?
- Hvad fangede jeres review?
- Hvad fangede testene – og hvad fangede de **ikke**?
- Hvad ville I gøre anderledes i jeres egen kode?

---

## Opslag: Git, VS Code og pytest

### Git i terminalen

| Kommando | Hvad den gør |
| --- | --- |
| `git status` | Viser aktuel branch og ændrede filer – brug den, når I er i tvivl |
| `git diff` | Viser ændringer, der endnu ikke er valgt til commit |
| `git add <fil>` | Vælger ændringer til næste commit |
| `git commit -m "besked"` | Gemmer de valgte ændringer i historikken |
| `git switch main` | Skifter til `main` |
| `git switch -c <navn>` | Opretter en ny branch og skifter til den |
| `git pull` | Henter og fletter ændringer ind i den aktuelle branch |
| `git push -u origin <navn>` | Deler en ny branch på Bitbucket |
| `git fetch origin` | Henter ændringer uden at ændre jeres filer |
| `git merge origin/main` | Fletter den nyeste `main` ind i den aktuelle branch |
| `git merge --abort` | Afbryder en merge med konflikter |
| `git log --oneline --graph` | Viser historikken som en graf |
| `git restore <fil>` | Kasserer ikke-committede ændringer i en fil |
| `git revert <commit>` | Laver et nyt commit, der vender et tidligere om |

Lange visninger, fx fra `git log`, lukkes med `q`.

### VS Code

| Handling | Sådan |
| --- | --- |
| Kommandopalet | `Ctrl+Shift+P` |
| Source Control | `Ctrl+Shift+G` |
| Ny terminal | **Terminal → New Terminal** |
| Vælg Python-miljø | **Python: Select Interpreter** |
| Omdøb overalt | `F2` |
| Breakpoint / start debug | `F9` / `F5` |
| Næste linje / ind i funktion | `F10` / `F11` |

### pytest

| Kommando | Hvad den gør |
| --- | --- |
| `python -m pytest` | Kører alle tests |
| `python -m pytest -v` | Viser én linje pr. test |
| `python -m pytest tests/test_validering.py` | Kører testene i én fil |
| `python -m pytest -k postnummer` | Kører tests, hvis navn indeholder "postnummer" |

---

## Løsninger

Løsningerne er forslag. Er jeres løsning anderledes, men giver samme resultat og er let at forstå, er den lige så god.

### Løsning til øvelse 1

**Del 1:** Efter de to pull requests indeholder `main` mappen `deltagere/` med en fil for hver af jer. Historikken på `main` har to merge-commits – et for hver PR. Fordi I ændrede i hver jeres fil, kunne Git flette ændringerne uden konflikt.

**Del 2:** Begge ændrede den samme linje i `holdet.md`. Da den anden PR skulle flettes, kunne Git ikke vide, hvilket forslag der var det rigtige. Under konflikten ser filen sådan ud:

```text
# Holdet

<<<<<<< HEAD
Holdets navn: Datadetektiverne
=======
Holdets navn: Postnummerpatruljen
>>>>>>> origin/main

## Deltagere
```

- Mellem `<<<<<<< HEAD` og `=======` står jeres egen version.
- Mellem `=======` og `>>>>>>> origin/main` står versionen fra `main`.

Merge editoren i VS Code viser de to versioner side om side med resultatet nedenunder. En løsning, der beholder begge forslag:

```text
# Holdet

Holdets navn: Datadetektiverne / Postnummerpatruljen

## Deltagere
```

Alle konfliktmarkeringerne er væk, og filen er committet som afslutning på merge. Det var lige så korrekt at aftale ét af navnene – det vigtige er, at I traf beslutningen bevidst.

### Løsning til øvelse 2

Den refaktorerede kode er delt i fire moduler. Resultatfilen er den samme som fra det oprindelige script.

`config.py`:

```python
from pathlib import Path

DATA_MAPPE = Path(__file__).parent / "data"
INPUT_STI = DATA_MAPPE / "adresser.csv"
OUTPUT_STI = DATA_MAPPE / "resultat.csv"
SEPARATOR = ";"
POSTNUMMER_KOLONNE = 2
```

`filer.py`:

```python
import csv
from pathlib import Path

from config import SEPARATOR


def laes_raekker(sti: Path) -> list[list[str]]:
    with open(sti, encoding="utf-8", newline="") as fil:
        return list(csv.reader(fil, delimiter=SEPARATOR))


def skriv_raekker(sti: Path, raekker: list[list[str]]) -> None:
    with open(sti, "w", encoding="utf-8", newline="") as fil:
        csv.writer(fil, delimiter=SEPARATOR).writerows(raekker)
```

`validering.py`:

```python
from config import POSTNUMMER_KOLONNE


def rens_postnummer(vaerdi: str) -> str:
    return vaerdi.strip().zfill(4)


def er_gyldigt_postnummer(vaerdi: str) -> bool:
    return len(vaerdi) == 4 and vaerdi.isdigit()


def rens_raekke(raekke: list[str]) -> list[str]:
    renset = [felt.strip() for felt in raekke]
    renset[POSTNUMMER_KOLONNE] = rens_postnummer(renset[POSTNUMMER_KOLONNE])
    return renset


def er_gyldig(raekke: list[str]) -> bool:
    return er_gyldigt_postnummer(raekke[POSTNUMMER_KOLONNE])
```

`main.py`:

```python
from config import INPUT_STI, OUTPUT_STI
from filer import laes_raekker, skriv_raekker
from validering import er_gyldig, rens_raekke


def main() -> None:
    raekker = [rens_raekke(r) for r in laes_raekker(INPUT_STI)]
    gyldige = [r for r in raekker if er_gyldig(r)]
    skriv_raekker(OUTPUT_STI, gyldige)


if __name__ == "__main__":
    main()
```

Læg mærke til:

- `main` læses nu som en opskrift. Detaljerne ligger i modulerne.
- Reglerne i `validering.py` læser og skriver ikke filer, så de kan testes med simple værdier.
- Stierne findes ud fra placeringen af `config.py`, så jobbet virker, uanset hvilken mappe det startes fra.
- Det oprindelige script printede de ugyldige rækker. Det er udeladt her – i ETL-afsnittet og øvelse 6 logges de i stedet.

### Løsning til øvelse 3

1. **Funktion.** Omregningen tager koordinater ind og returnerer nye. Der er ingen tilstand at huske. Kræver omregningen en opsætning, der er dyr at lave, kan et objekt dog være relevant – mange GIS-biblioteker bruger fx et transformationsobjekt.
2. **Class.** Forbindelsen er tilstand: Den åbnes, deles mellem trinene og skal lukkes igen. Data og adfærd hører tydeligt sammen.
3. **Dataclass.** Rækken er data med faste, navngivne felter og ingen eller lidt adfærd.
4. **Class.** De gentagne argumenter er et tegn på, at de hører sammen. En class kan samle opsætningen ét sted, så den kun gives, når objektet oprettes. En dataclass med opsætningen sammen med almindelige funktioner er også et godt svar.

Der er ikke ét rigtigt svar. Holder jeres begrundelse, og gør valget koden lettere at forstå, er det et godt valg.

### Løsning til øvelse 4

`tests/test_validering.py`:

```python
from validering import er_gyldigt_postnummer, rens_postnummer


def test_rens_postnummer_tilfoejer_nul():
    assert rens_postnummer(" 800") == "0800"


def test_er_gyldigt_postnummer():
    assert er_gyldigt_postnummer("8000")
    assert not er_gyldigt_postnummer("800")
    assert not er_gyldigt_postnummer("80a0")
    assert not er_gyldigt_postnummer("")
```

`python -m pytest` giver `2 passed`. Fjernes `.zfill(4)` i `rens_postnummer`, fejler den første test med:

```text
E       AssertionError: assert '800' == '0800'
```

Det betyder: Funktionen returnerede `'800'`, men testen forventede `'0800'`.

Gode ekstra tests er et postnummer, der allerede er korrekt (`"8000"` skal forblive `"8000"`), og en værdi med mellemrum på begge sider (`" 8000 "`).

### Løsning til øvelse 5

**Fejlen:** I `config.py` er `POSTNUMMER_KOLONNE` ændret fra `2` til `1`. Derfor behandles husnummeret som postnummer: `"12"` bliver til `"0012"` og godkendes, mens det rigtige postnummer ikke bliver renset eller valideret.

**Sådan findes den:** Med et breakpoint i `rens_raekke` viser **Variables**, at `raekke` er `['Søndergade', '12', ' 800']`, og at `POSTNUMMER_KOLONNE` er `1`. Med `F10` ses det, at det er `'12'` – ikke `' 800'` – der sendes til `rens_postnummer`.

**Rettelsen** i `config.py`:

```python
POSTNUMMER_KOLONNE = 2
```

**En test, der fanger fejlen.** Tilføj den til `tests/test_validering.py`, og udvid importen med `rens_raekke`:

```python
from validering import rens_raekke


def test_rens_raekke_renser_postnummeret():
    assert rens_raekke(["Søndergade", "12", " 800"]) == ["Søndergade", "12", "0800"]
```

Med fejlen returnerer `rens_raekke` `['Søndergade', '0012', '800']`, og testen fejler. Med rettelsen består den.

Bemærk, at testene fra øvelse 4 ikke fangede fejlen: De tester `rens_postnummer` og `er_gyldigt_postnummer`, som begge virker fint. Fejlen ligger i, *hvilken værdi* der sendes til dem. Derfor er det også værd at teste de funktioner, der binder reglerne sammen.

### Løsning til øvelse 6

#### Opgave 1

Fejlen ligger i `rens_postnummer`, som kalder `zfill(4)` **før** `strip()`. `" 800"` er allerede fire tegn langt, så `zfill` gør ingenting, og `strip` fjerner derefter mellemrummet. Resultatet `"800"` har kun tre cifre og afvises.

Rettelsen bytter om på rækkefølgen:

```python
def rens_postnummer(vaerdi: str) -> str:
    return vaerdi.strip().zfill(4)
```

Testen, der skrives først:

```python
def test_rens_postnummer_fjerner_mellemrum():
    assert rens_postnummer(" 800") == "0800"
```

Den eksisterende test brugte `"800"` uden mellemrum og fangede derfor ikke fejlen. Valget af testdata er vigtigt.

#### Opgave 2

`main.py` efter opgave 2:

```python
import logging
from pathlib import Path

from config import INPUT_STI, OUTPUT_STI
from filer import laes_raekker, skriv_raekker
from validering import er_gyldig, rens_raekke

logger = logging.getLogger(__name__)


def koer_job(input_sti: Path, output_sti: Path) -> int:
    try:
        raekker = laes_raekker(input_sti)
    except FileNotFoundError:
        logger.error("Inputfil findes ikke: %s", input_sti)
        raise

    gyldige = []
    for raekke in raekker:
        renset = rens_raekke(raekke)
        if er_gyldig(renset):
            gyldige.append(renset)
        else:
            logger.warning("Afvist række: %s", raekke)

    skriv_raekker(output_sti, gyldige)
    logger.info("Skrev %d af %d rækker", len(gyldige), len(raekker))
    return len(gyldige)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    koer_job(INPUT_STI, OUTPUT_STI)


if __name__ == "__main__":
    main()
```

Output fra `python main.py` efter runde 1:

```text
WARNING:__main__:Afvist række: ['Torvet', '1', '80a0']
INFO:__main__:Skrev 4 af 5 rækker
```

Bonustesten i fx `tests/test_main.py`:

```python
import pytest

from main import koer_job


def test_koer_job_skriver_gyldige_raekker(tmp_path):
    input_sti = tmp_path / "input.csv"
    output_sti = tmp_path / "output.csv"
    input_sti.write_text("Søndergade;12; 800\nTorvet;1;80a0\n", encoding="utf-8")

    antal = koer_job(input_sti, output_sti)

    assert antal == 1
    assert output_sti.read_text(encoding="utf-8") == "Søndergade;12;0800\n"


def test_koer_job_fejler_ved_manglende_fil(tmp_path):
    with pytest.raises(FileNotFoundError):
        koer_job(tmp_path / "findes-ikke.csv", tmp_path / "output.csv")
```

`pytest.raises` kontrollerer, at koden giver den forventede fejl.

#### Opgave 3

Før konflikten – på branchen `regel/vejnavn`:

`config.py` får en ny linje:

```python
VEJNAVN_KOLONNE = 0
```

`er_gyldig` i `validering.py`:

```python
from config import POSTNUMMER_KOLONNE, VEJNAVN_KOLONNE


def er_gyldig(raekke: list[str]) -> bool:
    har_vejnavn = raekke[VEJNAVN_KOLONNE].strip() != ""
    return har_vejnavn and er_gyldigt_postnummer(raekke[POSTNUMMER_KOLONNE])
```

Testen:

```python
def test_er_gyldig_kraever_vejnavn():
    assert er_gyldig(["Søndergade", "12", "8000"])
    assert not er_gyldig(["", "7", "8000"])
    assert not er_gyldig(["   ", "7", "8000"])
```

#### Opgave 4

Før konflikten – på branchen `oop/adresse`:

`adresse.py`:

```python
from dataclasses import dataclass


@dataclass
class Adresse:
    vejnavn: str
    husnummer: str
    postnummer: str


def fra_raekke(raekke: list[str]) -> Adresse:
    vejnavn, husnummer, postnummer = raekke
    return Adresse(vejnavn, husnummer, postnummer)


def til_raekke(adresse: Adresse) -> list[str]:
    return [adresse.vejnavn, adresse.husnummer, adresse.postnummer]
```

`fra_raekke` pakker rækkens tre felter ud i hver sin variabel. Har rækken ikke præcis tre felter, giver det en `ValueError`.

I `main.py` ændres løkken i `koer_job`, så hver række laves om til en `Adresse`, og de gyldige laves tilbage til rækker før skrivning:

```python
    for raekke in raekker:
        adresse = rens_adresse(fra_raekke(raekke))
        if er_gyldig(adresse):
            gyldige.append(adresse)
        else:
            logger.warning("Afvist række: %s", raekke)

    skriv_raekker(output_sti, [til_raekke(a) for a in gyldige])
```

Testen:

```python
def test_rens_adresse_fjerner_mellemrum():
    adresse = Adresse(" Vestergade ", "3 ", " 800")
    assert rens_adresse(adresse) == Adresse("Vestergade", "3", "0800")
```

Dataclassen sammenligner objekter felt for felt, så `==` virker uden ekstra kode.

#### Konflikten i runde 2

Uanset hvem der merger først, opstår der konflikt i `config.py`, `validering.py` og `tests/test_validering.py`. Fx ser `er_gyldig` sådan ud under konflikten, hvis opgave 3 blev merget først:

```text
<<<<<<< HEAD
def er_gyldig(adresse: Adresse) -> bool:
    return er_gyldigt_postnummer(adresse.postnummer)
=======
def er_gyldig(raekke: list[str]) -> bool:
    har_vejnavn = raekke[VEJNAVN_KOLONNE].strip() != ""
    return har_vejnavn and er_gyldigt_postnummer(raekke[POSTNUMMER_KOLONNE])
>>>>>>> origin/main
```

Vælger man blindt den ene side, mister man enten dataclassen eller den nye regel. Vælger man begge, er der to funktioner med samme navn, og koden fejler. Den rigtige løsning kombinerer dem:

- `config.py`: Hverken `POSTNUMMER_KOLONNE` eller `VEJNAVN_KOLONNE` – `Adresse` har navngivne felter.
- `validering.py`: Dataclass-versionen udvidet med reglen for vejnavn.
- `tests/test_validering.py`: Alle tests fra begge sider. Testen af vejnavn skrives om fra lister til `Adresse`-objekter.

`config.py` efter konfliktløsningen:

```python
from pathlib import Path

DATA_MAPPE = Path(__file__).parent / "data"
INPUT_STI = DATA_MAPPE / "adresser.csv"
OUTPUT_STI = DATA_MAPPE / "resultat.csv"
SEPARATOR = ";"
```

`validering.py` efter konfliktløsningen:

```python
from adresse import Adresse


def rens_postnummer(vaerdi: str) -> str:
    return vaerdi.strip().zfill(4)


def er_gyldigt_postnummer(vaerdi: str) -> bool:
    return len(vaerdi) == 4 and vaerdi.isdigit()


def rens_adresse(adresse: Adresse) -> Adresse:
    return Adresse(
        vejnavn=adresse.vejnavn.strip(),
        husnummer=adresse.husnummer.strip(),
        postnummer=rens_postnummer(adresse.postnummer),
    )


def er_gyldig(adresse: Adresse) -> bool:
    har_vejnavn = adresse.vejnavn.strip() != ""
    return har_vejnavn and er_gyldigt_postnummer(adresse.postnummer)
```

`tests/test_validering.py` efter konfliktløsningen:

```python
from adresse import Adresse
from validering import er_gyldig, er_gyldigt_postnummer, rens_adresse, rens_postnummer


def test_rens_postnummer_tilfoejer_nul():
    assert rens_postnummer("800") == "0800"


def test_er_gyldigt_postnummer():
    assert er_gyldigt_postnummer("8000")
    assert not er_gyldigt_postnummer("800")
    assert not er_gyldigt_postnummer("80a0")
    assert not er_gyldigt_postnummer("")


def test_rens_postnummer_fjerner_mellemrum():
    assert rens_postnummer(" 800") == "0800"


def test_er_gyldig_kraever_vejnavn():
    assert er_gyldig(Adresse("Søndergade", "12", "8000"))
    assert not er_gyldig(Adresse("", "7", "8000"))
    assert not er_gyldig(Adresse("   ", "7", "8000"))


def test_rens_adresse_fjerner_mellemrum():
    adresse = Adresse(" Vestergade ", "3 ", " 800")
    assert rens_adresse(adresse) == Adresse("Vestergade", "3", "0800")
```

`main.py` er ikke i konflikt – den kommer kun fra opgave 4. Efter runde 2 giver `python -m pytest` `5 passed`, og `python main.py` giver:

```text
WARNING:__main__:Afvist række: ['Torvet', '1', '80a0']
WARNING:__main__:Afvist række: ['', '7', '8000']
INFO:__main__:Skrev 3 af 5 rækker
```

#### Opgave 5 – læs først, når I har prøvet opgaven

Opgaven var at ændre `SEPARATOR` til `","`, fordi leverandøren skifter til kommaseparerede filer. Efter merge fejler jobbet på dagens semikolonseparerede fil:

```text
ValueError: not enough values to unpack (expected 3, got 1)
```

Med komma som separator læses hver linje som ét felt, og `fra_raekke` kan ikke pakke det ud i tre. **Testene består stadig**, fordi ingen af dem læser en fil. Bonustesten fra opgave 2 ville have fanget fejlen.

Ændringen fortrydes med en revert, som laver et nyt commit, der vender ændringerne om – uden at slette eller omskrive historikken på `main`:

```bash
git switch main
git pull
git log --oneline -5
git switch -c fortryd/komma
git revert -m 1 <id på merge-commit'et>
git push -u origin fortryd/komma
```

- `git log --oneline -5` viser de seneste commits. Merge-commit'et har en besked som *Merged in config/komma (pull request #5)*. Det korte id står forrest på linjen.
- `-m 1` fortæller Git, at `main` er den side af merge-commit'et, der skal bevares.

Fortrydelsen oprettes som en PR, reviewes og merges som alle andre ændringer. Derefter skriver jobbet igen tre af fem rækker, og historikken viser både ændringen og fortrydelsen.
