# Lærernoter – dag 2

Noterne følger rækkefølgen i [slidesene](./slides.md). Git-afsnittet er en overordnet introduktion for begyndere; noterne støtter underviseren og behøver ikke blive gennemgået i alle detaljer.

Deltagerne har en [øvelsesvejledning](./oevelsesvejledning.md) med udførlige beskrivelser af alle øvelser og samlede løsninger bagerst. Øvelsesslides henviser til øvelsens nummer i vejledningen. Materialerne til øvelserne ligger i [ovelser/](../../ovelser/).

Under **Mulige spørgsmål** står spørgsmål, deltagerne sandsynligvis stiller, med korte svar. Svarene er udgangspunkter – tilpas dem til deltagernes egen platform og arbejdsgang.

## Slide 1 – Python: struktur, OOP, Git og VS Code

Byd velkommen til dag 2. Forklar, at dagen handler om, hvordan Python-kode kan blive lettere at forstå, ændre og dele med andre – især når den indgår i en større løsning eller et ETL-miljø.

Præsentér underviser og tidspunkt, når de er fastlagt.

## Slide 2 – Dagens overblik

Fortæl, at vi starter med Git, fordi versionsstyring giver et sikkert udgangspunkt for resten af dagens kodearbejde. Derefter ser vi på struktur, OOP og tests, inden vi kobler kode og fejlfinding til ETL-miljøet.

Tiderne er vejledende og omfatter både oplæg og øvelser. Pauser og frokost kommer oveni.

## Slide 3 – Git-grundlag

Sæt forventningen: Målet er at forstå den typiske arbejdsgang, når flere arbejder sammen om kode. Deltagerne behøver ikke kunne alle kommandoer udenad.

Afsnittet varer ca. 55 minutter: omkring 25 minutters oplæg og demonstration, efterfulgt af ca. 30 minutters guidet øvelse, hvor deltagerne selv gennemfører flowet (øvelse 1 i øvelsesvejledningen). Hold oplægget kort, så der er tid til øvelsen.

**Forberedelse:** Opret ét Git-øvelsesrepository pr. hold på Bitbucket med indholdet af `ovelser/git-ovelse/start/` på `main`, og giv begge deltagere skriveadgang. Vælg merge-strategien **Merge commit**. Afprøv på forhånd, at deltagerne kan klone og pushe fra VS Code.

Vi følger en ændring fra `main`, over en branch og et commit, til en pull request og merge. Konflikter introduceres overordnet; det er helt normalt at bede om hjælp, når de skal løses.

**Mulige spørgsmål**

- *Skal vi bruge kommandolinjen, eller kan vi bruge VS Code?* – Begge dele. VS Code bruger de samme Git-begreber bag knapperne. Vi viser kommandoerne, fordi de gør trinene tydelige og virker ens overalt.
- *Hvad hvis vi bruger en anden platform end GitHub?* – Git-delen er den samme. Navne og knapper for PR og merge kan variere, fx “merge request”, men flowet er det samme.

## Slide 4 – Hvorfor Git?

**Fortæl:** Git er et versionsstyringssystem. Det gemmer projektets udvikling i en historik, så vi kan undersøge tidligere ændringer og samarbejde om den samme kodebase. Et commit er et gemt punkt i historikken.

Historikken er nyttig, når man vil finde ud af, hvad der blev ændret, hvem der lavede et commit, eller hvad der skete før en fejl opstod. Git hjælper med at kombinere arbejde, men forhindrer ikke automatisk fejl eller konflikter.

**Kommando:** `git log --oneline -5` viser op til fem commits i en kort oversigt. Den korte identifikator og beskeden gør det muligt at skelne mellem ændringerne. Kør kommandoen i et repository med mindst ét commit.

**Mulige spørgsmål**

- *Hvorfor ikke bare gemme kopier af filerne eller bruge et fællesdrev?* – Kopier fortæller ikke, hvad der er ændret, hvorfor og af hvem, og to personer kan overskrive hinanden. Git gemmer en struktureret historik og hjælper med at kombinere ændringer.
- *Kan jeg komme tilbage til en tidligere version?* – Ja, historikken gør det muligt. Der findes flere måder afhængigt af situationen; det går vi ikke i dybden med i dag. Spørg en erfaren kollega, før du omskriver historik, der allerede er delt.
- *Er Git kun til kode?* – Git fungerer bedst med tekstfiler som kode og konfiguration. Store binære filer og data egner sig dårligt, og hemmeligheder som adgangskoder må aldrig committes.

## Slide 5 – Lokalt og fælles

**Fortæl:** Et repository består af projektets filer og Git-historik. På din computer har du en lokal kopi, hvor du kan arbejde og committe. Et fælles repository på en Git-platform gør det muligt at dele ændringer med kolleger.

Git og GitHub er ikke det samme: Git er versionsstyringsværktøjet; GitHub er én af flere platforme til at være vært for repositories og understøtte samarbejde. Andre platforme kan have lidt andre navne og arbejdsgange.

**Kommando:** `git remote -v` viser adresserne på de fjernrepositories, den lokale kopi kender. Et almindeligt navn er `origin`, men det er blot et navn og kan være anderledes.

Forklar også forskellen på **pull**, som henter og integrerer ændringer i den aktuelle branch, og **push**, som sender lokale commits til fjernrepositoryet. Kommandoerne kræver adgang til fjernrepositoryet.

**Mulige spørgsmål**

- *Hvordan får jeg en lokal kopi i første omgang?* – Med `git clone <adresse>`, som henter repositoryet og dets historik. Adressen findes på Git-platformen.
- *Hvad sker der, hvis min computer går ned, før jeg har pushet?* – Ikke-pushede commits findes kun lokalt. Push derfor jævnligt til din branch, så arbejdet også ligger på platformen.
- *Hvad er forskellen på fetch og pull?* – `fetch` henter ændringer uden at ændre dine filer. `pull` henter og fletter dem ind i den aktuelle branch.

## Slide 6 – Hvad er et commit?

**Fortæl:** Et commit er et øjebliksbillede af projektets sporede indhold på et bestemt tidspunkt, baseret på de ændringer, vi har valgt. Man kan tænke på historikken som en række gemte trin med beskrivende etiketter.

Når en fil er ændret, vælger `git add validering.py` dens aktuelle ændringer til næste commit. Det kaldes *staging*. `git commit -m "Forbedr validering"` gemmer derefter de valgte ændringer med en besked. Filnavnet er et eksempel og skal svare til en fil i projektet.

Et commit og det at gemme en fil i editoren er forskellige ting: Filen gemmes først på computeren, og commit'et gemmer de valgte ændringer i den lokale Git-historik. Commit'et deles først med andre, når det pushes.

Anbefal korte beskeder, der beskriver ændringen, eksempelvis “Forbedr validering” frem for “rettelser”. Undgå at inkludere følsomme oplysninger eller hemmeligheder i kode og commits.

**Mulige spørgsmål**

- *Hvorfor skal jeg både bruge add og commit?* – `add` lader dig vælge præcis, hvilke ændringer der hører sammen. Så kan ét commit handle om én ting, selv hvis du har ændret flere filer.
- *Hvor ofte skal jeg committe?* – Når en lille, sammenhængende ændring er færdig og virker. Hellere flere små commits med klare beskeder end ét stort.
- *Kan jeg rette en commit-besked eller fortryde et commit?* – Ja, men det afhænger af, om commit'et allerede er pushet. Før push er det ofte nemt; efter push bør man spørge, så man ikke ændrer historik, som andre bruger.
- *Hvad hvis jeg har committet en adgangskode?* – Stop og få hjælp. Fjern den ikke bare i et nyt commit; den ligger stadig i historikken. Adgangskoden skal betragtes som kompromitteret og skiftes.

## Slide 7 – Se, hvad du har ændret

Gennemgå de tre kommandoer:

- `git status` viser blandt andet den aktuelle branch og hvilke filer der er ændrede, valgt til commit eller endnu ikke spores.
- `git diff` viser ændringer i sporede filer, som endnu ikke er staged.
- `git diff --staged` viser ændringerne, der er valgt til næste commit.

Vis gerne forskellen ved at ændre en fil, se `git diff`, vælge den med `git add` og derefter se `git diff --staged`. Forklar, at helt nye, usporede filer fremgår af `git status`, men ikke vises af almindelig `git diff`, før de er tilføjet.

`git status` er et godt første sted at kigge, hvis man bliver usikker på, hvad Git forventer som næste trin.

**Mulige spørgsmål**

- *Hvordan kommer jeg ud af visningen fra `git diff` eller `git log`?* – Tryk `q`. Lange visninger åbnes i en læser i terminalen.
- *Hvordan fortryder jeg en ændring, jeg ikke har committet?* – `git status` foreslår selv kommandoerne, fx `git restore <fil>`. Vær forsigtig: Ikke-committede ændringer kan ikke hentes tilbage bagefter.
- *Kan jeg se diff i VS Code i stedet?* – Ja, Source Control-panelet viser ændringerne side om side. Det er ofte lettere at læse.

## Slide 8 – Main og branches

**Fortæl:** `main` bruges ofte som projektets fælles hovedbranch. En branch er en separat udviklingslinje, hvor man kan arbejde med en ændring uden at ændre `main` direkte. Teamet kan bruge en anden hovedbranch eller have særlige regler for, hvem der må ændre den.

Forklar eksemplet trin for trin:

1. `git switch main` skifter til den lokale `main`.
2. `git pull origin main` henter og integrerer den fælles `main` i den lokale.
3. `git switch -c validering` opretter branchen `validering` fra det aktuelle punkt og skifter til den.

Forudsæt, at repositoryet allerede findes lokalt, at `origin` og `main` findes, at man har adgang, og at der ikke er ufærdige lokale ændringer, som forhindrer skiftet. `-c` bruges kun til at oprette en ny branch; hvis branchen allerede findes, skifter man i stedet til den.

**Mulige spørgsmål**

- *Hvorfor ikke bare arbejde direkte på main?* – Så kan ændringer ikke gennemgås, før de bliver fælles, og ufærdigt arbejde kan forstyrre andre. Mange teams blokerer derfor direkte ændringer af `main`.
- *Hvad skal en branch hedde?* – Et kort navn, der beskriver ændringen, fx `validering` eller `ret-datoformat`. Følg teamets navngivning, hvis der er en.
- *Hvad sker der med mine ændringer, når jeg skifter branch?* – Committede ændringer bliver på deres branch. Ikke-committede ændringer kan forhindre skiftet eller følge med; commit dem først, hvis du er i tvivl.
- *Hvorfor hedder det nogle gange master?* – Det er et ældre standardnavn. Princippet er det samme.

## Slide 9 – Fra branch til fælles kode

Brug diagrammet som den røde tråd: Start fra `main`, lav arbejdet på en branch, commit og push, opret en PR, få ændringerne gennemgået, og merge dem til sidst.

**Kommando:** `git push -u origin validering` deler den lokale branch og dens commits på `origin`. `-u` forbinder den lokale branch med dens fjernbranch, så man normalt kan bruge `git push` næste gang, mens man står på branchen.

Push opretter ikke i sig selv en PR og ændrer ikke automatisk `main`. Deltagerne skal forstå, at commit, push og PR er forskellige trin.

**Mulige spørgsmål**

- *Skal jeg skrive `-u origin validering` hver gang?* – Nej, kun første gang. Derefter er `git push` nok, mens du står på branchen.
- *Push fejler – hvad nu?* – Læs beskeden. Ofte mangler adgang eller login, eller der ligger nyere ændringer på fjernbranchen, som skal hentes først. Brug aldrig “force push” uden at vide præcis hvorfor.
- *Kan andre se min branch, når jeg har pushet?* – Ja, alle med adgang til repositoryet kan se den. Den påvirker dog ikke `main`.

## Slide 10 – Pull request og review

**Fortæl:** En pull request er en anmodning om at få ændringer fra én branch ind i en anden, ofte `main`. Platformen viser ændringerne, så en kollega kan gennemgå dem, stille spørgsmål og foreslå rettelser, før de bliver en del af den fælles kode.

En god PR beskriver kort **hvad** der er ændret og **hvorfor**. Nye commits på samme branch kan normalt føjes til den eksisterende PR ved at pushe dem.

PR'er håndteres af Git-platformen og er ikke en indbygget Git-kommando. De kan oprettes i platformens brugerflade. På GitHub åbner `gh pr create --base main --head validering --web` oprettelsen i browseren med målbranch og kildebranch angivet. Eksemplet kræver GitHub CLI, login, adgang og en branch, der er pushet. Forklar, at andre platforme har deres egne værktøjer og navne, fx merge request.

**Mulige spørgsmål**

- *Hvorfor hedder det pull request, når jeg sender noget?* – Man beder ejerne af målbranchen om at “trække” ændringerne ind. Navnet forvirrer mange, og nogle platforme kalder det derfor merge request.
- *Hvad skal en reviewer kigge efter?* – Om ændringen gør det, den skal, om koden er til at forstå, og om noget kan gå i stykker. Det handler om koden, ikke om personen.
- *Hvad gør jeg med kommentarerne?* – Ret koden på samme branch, commit og push. PR'en opdateres automatisk. Svar på kommentaren, eller forklar, hvis du er uenig.
- *Hvor stor må en PR være?* – Så lille som muligt. Små PR'er er hurtigere at gennemgå og giver bedre review.
- *Hvad hvis jeg ikke har GitHub CLI?* – Brug platformens hjemmeside. Efter push viser den ofte en knap til at oprette en PR.

## Slide 11 – Merge efter review

**Fortæl:** Når en PR er gennemgået, kan dens ændringer flettes ind i målbranchen. Det er dette, vi kalder *merge*. Hvem der må merge, og om der kræves godkendelse eller beståede checks, afhænger af teamets og platformens regler.

På GitHub kan merge ske i brugerfladen. `gh pr merge --merge` er et eksempel med GitHub CLI, når man står på branchen med PR'en. Det kræver adgang, at kravene er opfyldt, og at merge-metoden er tilladt i repositoryet. En anden platform eller opsætning kan kræve en anden arbejdsgang.

Efter merge opdaterer `git switch main` og `git pull origin main` den lokale `main`, så man har et aktuelt udgangspunkt for næste ændring. Man skal først håndtere eventuelle lokale ændringer, der forhindrer branchskift.

**Mulige spørgsmål**

- *Hvad er forskellen på merge, squash og rebase på platformen?* – Det er forskellige måder at samle historikken på. Resultatet i koden er det samme; brug den metode, teamet har valgt.
- *Hvad gør jeg med branchen bagefter?* – Den kan normalt slettes, når den er merget. Mange platforme tilbyder at gøre det automatisk.
- *Kan en merge fortrydes?* – Ja, med en revert. Det gennemgår vi på de næste to slides.

## Slide 12 – Fortryd en merget PR

**Fortæl:** Når en PR er merget til `main`, er ændringerne en del af den fælles historik, som andre måske allerede har hentet og bygger videre på. Derfor fortryder man ikke ved at slette commits, men ved at lave en **revert**: et nyt commit, der indeholder det modsatte af de oprindelige ændringer.

Resultatet er, at koden på `main` igen ser ud som før PR'en, mens historikken stadig viser både den oprindelige ændring og fortrydelsen. Det er gennemsigtigt og sikkert for alle, der arbejder på projektet.

Fortrydelsen følger samme flow som alle andre ændringer: på en ny branch, via en PR, med review og merge. Det giver en ekstra kontrol, så man ikke fortryder det forkerte i en presset situation.

Understreg reglen: **Omskriv aldrig delt historik på `main`**, fx med `git reset` efterfulgt af force push. Det kan få andres lokale kopier ud af trit og skabe forvirring eller tab af arbejde. Mange platforme blokerer det også på beskyttede branches.

**Mulige spørgsmål**

- *Hvorfor kan jeg ikke bare slette commit'et?* – Fordi andre allerede kan have hentet det. Hvis historikken på `main` ændres, passer deres kopier ikke længere, og det giver problemer. En revert ændrer ikke eksisterende historik.
- *Forsvinder min kode så?* – Nej. Den oprindelige ændring findes stadig i historikken og på den gamle branch. Den kan bruges igen senere.
- *Haster det – kan jeg springe review over?* – Det afhænger af teamets regler. Selv i en hastesituation er det en god idé, at en kollega kigger med, så man ikke fortryder for meget eller for lidt.
- *Hvad hvis det bare er en lille fejl?* – Ofte er det nemmere at rette fejlen i en ny PR end at fortryde hele ændringen. Revert er bedst, når hele ændringen skal ud.

## Slide 13 – Revert i praksis

**Fortæl:** På GitHub er den nemmeste vej **Revert**-knappen på den mergede PR. Den opretter automatisk en branch og en ny PR, der fortryder ændringerne. Den PR gennemgås og merges som normalt. Andre platforme har lignende funktioner.

Gennemgå CLI-eksemplet trin for trin:

1. `git switch main` og `git pull origin main` sørger for, at man står på en opdateret `main`.
2. `git log --oneline -5` viser de seneste commits, så man kan finde merge-commit'et for PR'en og dets korte id. Beskeden indeholder typisk "Merge pull request" og PR-nummeret.
3. `git switch -c fortryd-validering` opretter en ny branch til fortrydelsen.
4. `git revert -m 1 <merge-commit>` laver et nyt commit, der vender PR'ens ændringer om. `<merge-commit>` erstattes med id'et fra loggen. `-m 1` fortæller Git, at `main` (første forælder) er den side, der skal bevares. Git åbner normalt en editor til commit-beskeden.
5. `git push -u origin fortryd-validering` deler branchen, og derefter oprettes en PR som normalt.

Bemærk: `-m 1` bruges kun ved merge-commits. Hvis PR'en blev merget med *squash*, er den ét almindeligt commit, og så bruges `git revert <commit>` uden `-m 1`. Hvis der er kommet nyere ændringer i de samme linjer, kan en revert give en konflikt, som løses på samme måde som andre konflikter.

**Mulige spørgsmål**

- *Hvordan finder jeg det rigtige commit?* – Brug `git log --oneline` eller PR'en på platformen, som viser merge-commit'et. Er man i tvivl, så spørg, før man reverter.
- *Hvad betyder `-m 1`?* – Et merge-commit har to forældre: `main` og PR-branchen. `-m 1` siger, at vi vil tilbage til tilstanden på `main` før merge.
- *Hvad hvis jeg senere vil have ændringen ind igen?* – Så kan man reverte selve revert-commit'et, eller lave en ny PR. Bed om hjælp, da det kan være lidt drilsk.
- *Kan jeg bruge VS Code til revert?* – Revert-knappen på platformen eller kommandolinjen er det enkleste. Brug den metode, teamet er trygt ved.

## Slide 14 – Hvad er en merge-konflikt?

**Fortæl:** En konflikt opstår, når Git ikke selv kan afgøre, hvordan ændringer skal kombineres. Det kan eksempelvis ske, hvis to personer har ændret de samme linjer. Det er ikke en fejl hos personen, der får konflikten, men et signal om, at et menneske skal træffe et valg.

Eksemplet viser, hvordan man på sin egen branch kan hente den seneste `main` med `git fetch origin` og derefter forsøge at flette `origin/main` ind med `git merge origin/main`. `git status` viser resultatet og eventuelle filer med konflikter. Hvis der ikke er konflikt, gennemføres sammenfletningen uden konfliktløsning.

Forklar overordnet, at de to versioner skal sammenlignes: Nogle gange skal den ene beholdes, andre gange skal de kombineres. Konfliktløsning kan også ske i platformens eller editorens brugerflade; teamets arbejdsgang er afgørende.

**Mulige spørgsmål**

- *Har jeg gjort noget forkert, når jeg får en konflikt?* – Nej. Det er en normal del af samarbejdet, når flere ændrer i samme kode.
- *Hvordan undgår vi konflikter?* – Hent `main` ofte, hold branches og PR'er små, og tal sammen, hvis flere skal arbejde i samme fil.
- *Kan jeg afbryde, hvis det bliver uoverskueligt?* – Ja, `git merge --abort` sætter branchen tilbage til før sammenfletningen. Så kan du få hjælp og prøve igen.
- *Kan konflikter opstå i PR'en?* – Ja. Platformen viser så, at PR'en ikke kan merges, før konflikten er løst.

## Slide 15 – Løs en konflikt

Gennemgå først princippet: Åbn hver konfliktfil, forstå begge ændringer, og aftal eventuelt med en kollega, hvad den færdige kode skal gøre. Fjern konfliktmarkeringerne, når indholdet er rettet, og kontrollér, at resultatet er korrekt. Brug gerne tests, hvis der findes nogen.

`git add validering.py` markerer den pågældende fil som løst. Filnavnet er et eksempel: Alle konfliktfiler skal løses og tilføjes. `git status` viser, om der stadig er uløste konflikter. Når alle er løst, afslutter `git commit` merge-processen; Git åbner normalt en editor til commit-beskeden. `git push` deler derefter resultatet på branchen og opdaterer en eksisterende PR.

Dette eksempel forudsætter, at en lokal merge er i gang, at filen faktisk har haft en konflikt, og at branchen er knyttet til en fjernbranch. Kør ikke kommandoerne uden først at forstå og kontrollere ændringerne. Hvis man er usikker, er det bedre at spørge en kollega end at vælge en version vilkårligt.

**Mulige spørgsmål**

- *Hvordan ser en konflikt ud i filen?* – Git indsætter markeringer: `<<<<<<<` før din version, `=======` mellem versionerne og `>>>>>>>` efter den anden. Alle markeringer skal fjernes, når filen er rettet.
- *Kan VS Code hjælpe?* – Ja, VS Code viser konflikter med knapper til at beholde den ene, den anden eller begge versioner. Kontrollér altid resultatet bagefter.
- *Hvordan ved jeg, hvilken version der er rigtig?* – Det afgør Git ikke. Forstå, hvad begge ændringer skulle opnå, og spørg personen bag den anden ændring, hvis det er uklart.
- *Hvad hvis jeg har committet en forkert løsning?* – Ret filen og lav et nyt commit, eller få hjælp, før det pushes.

## Slide 16 – Git-flowet i praksis

Opsummér den samlede arbejdsgang:

1. Opdatér den lokale `main`, og opret en branch.
2. Ændr og gem en fil; kontrollér forskellen, vælg ændringerne, og opret et commit.
3. Push branchen, og opret en PR med en beskrivelse.
4. Gennemgå ændringerne, håndtér eventuelle konflikter, og merge efter teamets regler.

Understreg, at `git status` er et nyttigt orienteringspunkt undervejs. Bed deltagerne fortælle, hvor ændringen findes efter et commit, efter push og efter merge. Derefter følger den guidede Git-øvelse.

**Mulige spørgsmål**

- *Skal vi altid gøre alle trinene, også ved små ændringer?* – Det afhænger af teamets regler. Flowet giver review og en sikker `main`, så mange bruger det også til små rettelser.
- *Hvad hvis main har ændret sig, mens jeg arbejdede?* – Hent den nyeste `main` ind i din branch, løs eventuelle konflikter, og push igen, før PR'en merges.
- *Hvor finder jeg hjælp bagefter?* – `git status` foreslår ofte næste skridt, `git help <kommando>` viser dokumentation, og kolleger og platformens vejledninger er gode kilder.

## Slide 17 – Øvelse: jeres første pull request

**Fortæl:** Første halvdel af den guidede Git-øvelse (15 min.). Deltagerne arbejder to og to i holdets Git-øvelsesrepository. Indholdet er bevidst enkelt – en lille tekstfil om hver deltager – så al opmærksomhed er på Git-flowet. Den fulde beskrivelse står i øvelse 1 i øvelsesvejledningen.

Demonstrér første gang på storskærm: klon med **Git: Clone**, opret en branch via branch-navnet nederst til venstre, commit i **Source Control**, **Publish Branch** og opret en PR på Bitbucket. Lad derefter deltagerne gøre det selv.

Hver deltager opretter sin egen fil i `deltagere/`, så de to PR'er ikke rører de samme linjer og kan merges uden konflikt. Begge skal både oprette en PR og reviewe makkerens.

Typiske udfordringer: login til Bitbucket, ændringer lavet direkte på `main` fordi branchen ikke blev oprettet, og PR'er med forkert målbranch.

**Mulige spørgsmål**

- *Hvorfor skal vi oprette en mappe, der ikke findes?* – Git holder kun styr på filer. Mappen oprettes, når den første fil lægges i den.
- *Hvad skriver man i PR-beskrivelsen?* – Kort, hvad der er ændret og hvorfor. Her: "Tilføjer min præsentation."
- *Kan jeg godkende min egen PR?* – Bitbucket tillader det ikke i alle opsætninger, og det er pointen med review, at en anden kigger med.

## Slide 18 – Øvelse: jeres første konflikt

**Fortæl:** Anden halvdel af Git-øvelsen (15 min.). Begge ændrer den samme linje i `holdet.md` på hver sin branch, så den PR, der merges sidst, får en konflikt. Fortæl gerne på forhånd, at konflikten er meningen.

Konflikten løses lokalt: **Git: Fetch**, **Git: Merge** → `origin/main`, og derefter **Resolve in Merge Editor**. Gennemgå merge editoren på storskærm for det første hold, der får konflikten: de to versioner øverst og resultatet nederst. Opfordr til at kombinere forslagene, så ingen ændring forsvinder ubevidst. Afslut med **Complete Merge**, **Commit** og **Sync Changes**.

Konfliktmarkeringerne i filen (`<<<<<<<`, `=======`, `>>>>>>>`) er vist i løsningen til øvelse 1 i øvelsesvejledningen.

Afslut øvelsen med en kort runde: Hvad skete der i Bitbucket, da PR'en fik konflikt? Hvordan så det ud i VS Code? Deltagerne skal møde en mere realistisk konflikt i kode i den samlede øvelse sidst på dagen.

**Mulige spørgsmål**

- *Hvorfor løser vi ikke konflikten direkte i Bitbucket?* – Det kan nogle platforme, men lokalt kan man køre koden og testene, før konfliktløsningen committes. Det er vigtigt, når konflikten er i kode.
- *Hvad hvis vi begge har skrevet det samme?* – Så kan Git ofte selv se, at ændringerne er ens, og der opstår ingen konflikt.
- *Vi klikkede forkert i merge editoren – hvad nu?* – Ret resultatet direkte i filen, eller afbryd med `git merge --abort` og start forfra.

## Slide 19 – Python-struktur og refactoring

Sektionsslide. Afsnittet varer ca. 60 minutter: ca. 25 minutters oplæg, 25 minutters refactoring-øvelse og 10 minutters fælles gennemgang. Hold oplægget kort, så der er tid til øvelsen.

Introducér overgangen: Nu hvor vi ved, hvordan vi samarbejder sikkert om kode med Git, ser vi på, hvordan selve koden gøres lettere at forstå og ændre. Vi tager udgangspunkt i ét lille script, som går igen resten af dagen i tests og ETL-afsnittet.

**Forberedelse:** Udlever `ovelser/refactoring/start/` med `adresse_script.py` og `data/adresser.csv` (øvelse 2 i øvelsesvejledningen). Scriptet er det samme som på næste slide. Testdata indeholder en række med et postnummer, der skal have et nul foran, og én ugyldig række. Løsningen ligger i `ovelser/refactoring/loesning/` og giver præcis samme resultatfil som scriptet.

## Slide 20 – Udgangspunktet: et script, der virker

**Fortæl:** Scriptet læser en CSV-fil med adresser, retter postnumre op ved at fjerne mellemrum og tilføje et nul foran, sorterer ugyldige rækker fra og skriver resultatet til en ny fil. Det virker – og det er sådan, meget kode starter.

Gennemgå koden linje for linje, så alle forstår, hvad den gør, før vi ændrer den. Bed deltagerne forestille sig, at de skal ændre den: fx at postnummeret nu står i en anden kolonne, eller at reglen skal bruges i et andet job.

Undgå at gøre grin med koden. Pointen er, at det er helt naturligt at starte sådan, men at koden bliver sværere at vedligeholde, når den vokser.

**Mulige spørgsmål**

- *Hvad er der galt med koden, når den virker?* – Intet, så længe den ikke skal ændres. Problemerne opstår, når den skal ændres, genbruges eller fejlsøges.
- *Hvorfor `newline=""`?* – Det anbefales af `csv`-modulet ved skrivning, så der ikke opstår ekstra tomme linjer på Windows.

## Slide 21 – Hvad gør det svært?

**Fortæl:** Lad gerne deltagerne komme med bud, før punkterne vises.

- **Én blok:** Man skal læse hele scriptet for at forstå én del af det. En ændring ét sted kan påvirke noget andet.
- **Hårdkodede værdier:** Stierne og `r[2]` står midt i koden. Skal de ændres, skal man finde alle steder.
- **Korte navne:** `r`, `pn` og `f` sparer tastetryk, men koster tid for den næste læser.
- **Ingen genbrug:** Reglen for postnumre kan ikke bruges i et andet job uden at kopiere koden.
- **Ingen tests:** Man kan kun afprøve reglerne ved at køre hele scriptet med rigtige filer.

**Mulige spørgsmål**

- *Er korte navne ikke okay i små løkker?* – I meget korte løkker kan `i` eller `r` være fint. Men når variablen bruges over flere linjer eller har en særlig betydning, som et postnummer, er et beskrivende navn bedre.
- *Hvornår er et script stort nok til at blive delt op?* – Når det bliver svært at overskue, eller når dele skal genbruges eller testes. Det handler mere om ansvar end om antal linjer.

## Slide 22 – Én funktion – én opgave

**Fortæl:** Første skridt er at dele scriptet op i funktioner, hvor hver funktion har én opgave: læse, rense, validere eller skrive. `...` betyder, at indholdet er udeladt på sliden.

Fordele: Hver funktion kan forstås for sig. Navnet beskriver, hvad den gør, så koden, der kalder den, bliver selvforklarende. Funktionerne kan testes og genbruges hver for sig.

Test for, om en funktion gør for meget: Kan man beskrive, hvad den gør, uden at bruge ordet "og"? Hvis ikke, kan den måske deles.

**Mulige spørgsmål**

- *Bliver der ikke alt for mange små funktioner?* – Det kan ske, men det er sjældent problemet i praksis. Små funktioner med gode navne er lettere at læse end én lang. Del, når det gør koden tydeligere.
- *Hvor lang må en funktion være?* – Der er ingen fast grænse. Hvis den ikke kan overskues på én skærm, eller den har flere opgaver, er det et tegn på, at den kan deles.

## Slide 23 – Argumenter og returværdier

**Fortæl:** Den første version ændrer en global liste. For at forstå, hvad den gør, skal man kende listen og vide, hvem der ellers ændrer den. Den er også svær at teste, fordi resultatet afhænger af, hvad der ligger i listen i forvejen.

Den anden version får alt, den skal bruge, som argument og returnerer resultatet. Den kan forstås, testes og genbruges uden at kende resten af programmet.

Kobl til begrebet *scope*: Variabler, der oprettes i en funktion, findes kun i funktionen. Det er en fordel, fordi det begrænser, hvad funktionen kan påvirke.

**Mulige spørgsmål**

- *Er globale variabler altid forkerte?* – Konstanter, som ikke ændres, er fine på modulniveau. Det er globale variabler, der ændres undervejs, der giver problemer.
- *Hvad er en list comprehension?* – `[r for r in raekker if er_gyldig(r)]` er en kort måde at lave en ny liste på. Den svarer til en `for`-løkke med `if` og `append`.

## Slide 24 – Adskil regler og sideeffekter

**Fortæl:** En *sideeffekt* er alt, hvad en funktion gør ud over at returnere en værdi: læse eller skrive filer, tale med en database, printe eller logge. Sideeffekter er nødvendige, men gør koden sværere at teste og genbruge.

Idéen er at holde reglerne, fx rensning og validering, fri for sideeffekter, og samle læsning og skrivning i kanten af programmet. Så kan reglerne testes med simple værdier og bruges i andre jobs, uanset hvor data kommer fra.

Brug diagrammet: Data læses ind, reglerne arbejder på data i hukommelsen, og resultatet skrives ud.

**Mulige spørgsmål**

- *Er logging også en sideeffekt?* – Ja, men den er sjældent et problem for test. Det vigtige er, at reglerne ikke afhænger af filer eller databaser.
- *Hvad hvis data er for store til at ligge i hukommelsen?* – Så kan man læse og behandle data i bidder, fx række for række. Princippet om at adskille regler fra I/O er det samme.

## Slide 25 – Navne og konstanter

**Fortæl:** Værdier, der har en betydning, får et navn. `POSTNUMMER_KOLONNE = 2` forklarer, hvad tallet 2 betyder, og der er kun ét sted at ændre det. STORE BOGSTAVER er Pythons konvention for konstanter – værdier, der ikke ændres, mens programmet kører.

Beskrivende navne gør koden læsbar uden kommentarer: `postnummer = raekke[POSTNUMMER_KOLONNE]` forklarer sig selv, mens `pn = r[2]` kræver, at man kender filens opbygning.

Type hints, fx `-> str`, viser, hvad en funktion forventer og returnerer. De gør koden lettere at læse og giver hjælp i editoren.

**Mulige spørgsmål**

- *Skal vi bruge danske eller engelske navne?* – Det vigtigste er at være konsekvent og følge teamets praksis. Undgå at blande sprog i samme navn. Æ, ø og å virker i Python-navne, men mange undgår dem for at være på den sikre side.
- *Hvad er konventionen for navne i Python?* – `snake_case` til funktioner og variabler, `PascalCase` til classes og `STORE_BOGSTAVER` til konstanter. Det står i stilguiden PEP 8.

## Slide 26 – Del koden op i moduler

**Fortæl:** Et modul er blot en `.py`-fil. Når koden vokser, kan funktionerne deles i moduler efter ansvar: `config.py` til stier og konstanter, `filer.py` til læsning og skrivning, `validering.py` til reglerne og `main.py` til at binde det hele sammen.

`from validering import er_gyldig, rens_raekke` henter de to funktioner fra modulet `validering`. Importen virker, når modulerne ligger i samme mappe som det script, der startes, eller er installeret som en package.

Princippet for opdelingen: Det, der ændres af samme grund, ligger sammen. Ændres reglerne for postnumre, ændres kun `validering.py`.

**Mulige spørgsmål**

- *Hvornår skal jeg lave et nyt modul?* – Når en gruppe funktioner har et klart fælles ansvar, og filen er ved at blive svær at overskue.
- *Hvorfor får jeg `ModuleNotFoundError`?* – Python finder moduler ud fra mappen med det script, der startes, og installerede pakker. Kontrollér, hvilken mappe der køres fra, og at filnavnet er stavet rigtigt.
- *Hvad er `__pycache__`-mappen?* – Python gemmer en kompileret udgave af modulerne for at starte hurtigere. Den kan slettes og bør ikke i Git.

## Slide 27 – Projektstruktur – overordnet

**Fortæl:** Når et projekt bliver større, er det almindeligt at bruge en struktur som denne:

- `README.md` forklarer, hvad projektet gør, og hvordan det køres.
- `pyproject.toml` beskriver projektet, fx navn og afhængigheder.
- `src/adresse_job/` indeholder koden som en *package* – en mappe med moduler og en `__init__.py`-fil.
- `tests/` holder testene adskilt fra koden.

Gå ikke i detaljer med `pyproject.toml` eller installation af packages. Pointen er principperne: Kode, tests og dokumentation har hver deres plads, og en ny udvikler kan hurtigt finde rundt.

**Mulige spørgsmål**

- *Skal vi bruge præcis denne struktur?* – Nej. Følg det, teamet eller ETL-værktøjet forventer. Det vigtige er, at strukturen er ensartet og logisk.
- *Hvad gør `__init__.py`?* – Den markerer mappen som en package. Den kan være tom.
- *Hvorfor `src/`-mappen?* – Den sikrer, at koden testes, som den bliver installeret, og ikke tilfældigt fra den aktuelle mappe. For små projekter er en flad struktur også fin.

## Slide 28 – Refactoring i små skridt

**Fortæl:** Refactoring betyder at forbedre strukturen uden at ændre, hvad koden gør. Resultatet skal være det samme før og efter.

Arbejd i små skridt: Lav én ændring, kør koden og eventuelle tests, kontrollér, at resultatet er det samme, og commit. Så er det let at finde fejlen, hvis noget går galt, og let at gå tilbage til sidste fungerende version.

Kobl til Git: Hvert commit er et sikkert punkt. Små commits med klare beskeder gør det også lettere for en reviewer at følge ændringerne i en PR.

**Mulige spørgsmål**

- *Hvordan ved jeg, at resultatet er det samme?* – Sammenlign outputfilen før og efter, og brug tests. Det ser vi på i næste afsnit.
- *Må jeg rette fejl, mens jeg refaktorerer?* – Hold det adskilt. Ret fejlen i et separat commit, så det er tydeligt, hvad der ændrer adfærd, og hvad der kun ændrer struktur.
- *Kan VS Code hjælpe?* – Ja, fx med **Rename Symbol** (`F2`), som omdøber en variabel eller funktion alle steder.

## Slide 29 – Øvelse: refaktorér scriptet

**Fortæl:** Deltagerne arbejder to og to i 25 minutter med `adresse_script.py`. De opretter først en branch, så `main` forbliver uændret.

Forventningen er ikke, at alle når alle trin. Trin 2 og 3 er det vigtigste. Opdeling i moduler er en bonus.

Gå rundt og hjælp. Typiske udfordringer: Funktioner, der stadig bruger globale variabler, importfejl ved opdeling i moduler og glemte commits. Mind deltagerne om at køre scriptet og sammenligne outputfilen efter hvert skridt.

Rød baggrund markerer, at deltagerne løser opgaven selv.

**Mulige spørgsmål**

- *Skal vi bruge præcis de samme navne som på slides?* – Nej, men gode, beskrivende navne. Det gør det dog lettere at følge løsningsforslaget bagefter.
- *Vi har ødelagt noget – hvad nu?* – Brug `git status` og `git diff` til at se ændringerne. `git restore <fil>` går tilbage til sidste commit for filen.
- *Skal vi lave en PR?* – Ikke nødvendigvis nu. Branch og commits er nok. PR'er øves i den samlede øvelse.

## Slide 30 – Forslag til løsning: main.py

**Fortæl:** Vis `main.py` og bed et par grupper fortælle, hvordan de løste opgaven, før løsningsforslaget gennemgås.

`main` læses nu som en opskrift: læs rækker, rens dem, find de gyldige og skriv dem. Detaljerne ligger i modulerne. `if __name__ == "__main__":` sørger for, at `main()` kun køres, når filen startes direkte. Det uddybes i ETL-afsnittet.

Det fulde løsningsforslag, som kan vises eller udleveres:

```python
# config.py
from pathlib import Path

DATA_MAPPE = Path(__file__).parent / "data"
INPUT_STI = DATA_MAPPE / "adresser.csv"
OUTPUT_STI = DATA_MAPPE / "resultat.csv"
SEPARATOR = ";"
POSTNUMMER_KOLONNE = 2
```

```python
# filer.py
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

```python
# validering.py
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

Bemærk forskellene fra det oprindelige script: Stierne findes ud fra placeringen af `config.py` i stedet for en fast sti, og ugyldige rækker bliver ikke længere printet. Logging af dem tilføjes i ETL-afsnittet.

**Mulige spørgsmål**

- *Vi har lavet det anderledes – er det forkert?* – Ikke hvis resultatet er det samme, og koden er lettere at forstå. Der er mange gode løsninger.
- *Hvorfor ikke en class her?* – Funktionerne har ingen tilstand, så funktioner er det enkleste valg. Det kobler til OOP-afsnittet, der kommer nu.

## Slide 31 – OOP: class eller funktion?

Sektionsslide. Afsnittet varer ca. 35 minutter: ca. 20 minutters oplæg med eksempler, 10 minutters diskussionsøvelse og 5 minutters fælles gennemgang.

Sæt forventningen: Deltagerne har erfaring med Python, men har måske ikke selv skrevet classes. Målet er ikke at lære al OOP-teori, men at kunne **vurdere, hvornår en class gør koden bedre** – og hvornår en funktion er det enkleste og bedste valg. Eksemplerne ligner den type kode, der bruges i ETL-jobs: læsning af filer, rensning og validering af data.

## Slide 32 – Ikke alt skal være en class

**Fortæl:** Python er ikke et sprog, hvor alt skal pakkes ind i classes. Meget god Python-kode består primært af funktioner og moduler. Classes er et værktøj, man tager frem, når det giver en konkret fordel.

Bed deltagerne tænke over, hvem der skal læse koden næste gang – en kollega, eller dem selv om et halvt år. Den rigtige løsning er den, der gør koden lettest at forstå og ændre.

Kobl gerne til det forrige afsnit om struktur: En class er en måde at gruppere ting, der hører sammen. Moduler og funktioner er andre måder.

**Mulige spørgsmål**

- *Er OOP ikke "den rigtige måde" at programmere på?* – Nej, det er én måde blandt flere. Python understøtter både funktioner og classes, og god kode kombinerer dem efter behov.
- *Bruger biblioteker, vi kender, classes?* – Ja, fx er en `DataFrame` i pandas eller et lag i PyQGIS objekter. Man bruger ofte classes uden selv at skrive dem.

## Slide 33 – Funktioner er ofte nok

**Fortæl:** De to funktioner tager en værdi ind og returnerer et resultat. De husker ikke noget mellem kaldene og ændrer ikke noget uden for sig selv. Det kaldes ofte en *ren funktion*.

`rens_postnummer` fjerner mellemrum med `strip()` og fylder op med nuller foran med `zfill(4)`, så `" 800"` bliver `"0800"`. `er_gyldigt_postnummer` tjekker, at værdien er fire cifre.

Fordelene: Funktionerne er lette at forstå, teste og genbruge i forskellige jobs, fordi de ikke afhænger af andet end deres input. Det er et godt udgangspunkt, og der er ingen grund til at pakke dem ind i en class.

**Mulige spørgsmål**

- *Hvad betyder `-> str` og `: str`?* – Det er type hints. De fortæller, hvilke typer funktionen forventer og returnerer. Python håndhæver dem ikke, men editoren og andre udviklere har gavn af dem.
- *Hvor skal sådanne funktioner ligge?* – Samlet i et modul med et sigende navn, fx `validering.py`, så de kan importeres, hvor der er brug for dem.

## Slide 34 – Hvad er en class?

**Fortæl:** En class er en skabelon, der samler **data** (attributter) og **adfærd** (metoder). Ud fra skabelonen laver man konkrete *objekter*, også kaldet instanser.

Gennemgå eksemplet:

- `class CsvKilde:` definerer skabelonen.
- `__init__` køres automatisk, når et objekt oprettes. Her gemmes stien og separatoren på objektet.
- `self` er det aktuelle objekt. `self.sti = sti` betyder "gem stien på netop dette objekt".
- `hent_raekker` er en metode. Den bruger objektets egne data via `self`, så de ikke skal sendes med igen.
- `kilde = CsvKilde("adresser.csv")` opretter et objekt, og `kilde.hent_raekker()` kalder metoden på det.

Man kan oprette flere objekter med forskellig opsætning, fx én kilde med semikolon og én med komma.

Eksemplet er bevidst enkelt. I praksis vil man ofte bruge modulet `csv`, som håndterer citationstegn og andre særtilfælde korrekt.

**Mulige spørgsmål**

- *Hvorfor skal `self` stå som første parameter?* – Python sender automatisk objektet med som første argument, når en metode kaldes. Navnet `self` er en konvention, som alle bruger.
- *Hvad er forskellen på en funktion og en metode?* – En metode er en funktion, der hører til en class og arbejder på et objekt via `self`.
- *Hvad betyder de dobbelte understreger i `__init__`?* – Det er Pythons særlige metoder, som Python selv kalder i bestemte situationer. `__init__` kaldes, når objektet oprettes.

## Slide 35 – Tegn på, at en class kan hjælpe

**Fortæl:** Gennemgå de fire tegn med konkrete eksempler fra ETL-verdenen:

- **Samme argumenter:** Hvis mange funktioner alle tager `sti`, `separator` og `encoding`, hører de data sammen og kan samles.
- **Data og funktioner hører sammen:** Fx en kilde, der både har en opsætning og ved, hvordan den læses.
- **Tilstand:** Fx en databaseforbindelse, der åbnes, bruges flere gange og skal lukkes, eller en tæller over afviste rækker under et job.
- **Flere objekter:** Fx flere kilder med hver sin opsætning i samme job.

Understreg, at ét tegn ikke automatisk betyder, at man skal skrive en class. Det er en vurdering.

**Mulige spørgsmål**

- *Hvad er "tilstand"?* – Data, der huskes og kan ændre sig over tid, mens programmet kører, fx om en forbindelse er åben, eller hvor mange rækker der er behandlet.
- *Kunne man ikke bare bruge globale variabler til tilstand?* – Det virker i små scripts, men gør koden svær at teste og genbruge, fordi alle funktioner kan ændre dem. En class gør det tydeligt, hvem der ejer tilstanden.

## Slide 36 – Før: de samme argumenter igen og igen

**Fortæl:** Her har vi tre funktioner, der alle skal have de samme tre oplysninger om filen. `...` betyder blot, at indholdet er udeladt på sliden.

Problemerne: Hvert kald bliver langt, og opsætningen skal gentages hver gang. Hvis man fx tilføjer en ny indstilling, skal alle funktioner og alle kald ændres. Der er også risiko for, at to kald ved en fejl bruger forskellig opsætning til den samme fil.

Spørg deltagerne, om de kender mønsteret fra deres egen kode.

**Mulige spørgsmål**

- *Kunne man ikke bare samle argumenterne i en `dict`?* – Jo, og det er et skridt i den rigtige retning. Men en `dict` giver ingen hjælp fra editoren ved stavefejl i nøgler. En dataclass eller en class er tydeligere.
- *Er det forkert at have funktioner med mange argumenter?* – Ikke forkert, men mange gentagne argumenter er et tegn på, at noget hører sammen og kunne samles.

## Slide 37 – Efter: opsætningen samlet ét sted

**Fortæl:** Opsætningen gives nu én gang, når objektet oprettes. Metoderne henter oplysningerne fra `self`, så kaldene bliver korte, og opsætningen er altid den samme for den samme kilde.

Fordelene: Én indstilling ændres ét sted. Det er tydeligt, hvilke funktioner der hører til kilden. Separator og encoding har standardværdier, så de kun skal angives, når de afviger.

Bemærk også, at `valider_kolonner` stadig tager `kolonner` som argument, fordi det er noget, der varierer fra kald til kald – ikke en del af kildens opsætning.

**Mulige spørgsmål**

- *Hvordan ved jeg, hvad der skal være attribut, og hvad der skal være argument?* – Det, der beskriver objektet og er det samme hver gang, bliver attribut. Det, der ændrer sig fra kald til kald, bliver argument.
- *Bliver koden ikke længere?* – Selve definitionen kan blive lidt længere, men den kode, der bruger kilden, bliver kortere og mere overskuelig.

## Slide 38 – Dataclasses til strukturerede data

**Fortæl:** En dataclass er en enkel måde at lave en class, der primært holder data. `@dataclass` genererer automatisk `__init__` og en læsbar tekstvisning ud fra felterne, så man ikke skal skrive det selv.

Fordele frem for en `dict`: Felterne har navne og type hints, editoren kan foreslå felter og fange stavefejl, og det er tydeligt, hvilke felter en adresse har. `adresse.postnummer` er lettere at læse end `adresse["postnummer"]`.

Dataclasses er velegnede til fx rækker, poster eller opsætning, der sendes mellem trin i et job.

**Mulige spørgsmål**

- *Kan en dataclass have metoder?* – Ja. Den er en almindelig class med ekstra hjælp. Små metoder, der hører til dataene, er fint.
- *Kontrollerer Python typerne?* – Nej, type hints håndhæves ikke under kørsel. De er dokumentation og hjælp til editoren og værktøjer.
- *Kan man forhindre, at felterne ændres?* – Ja, med `@dataclass(frozen=True)`. Det er nyttigt, når data ikke bør ændres undervejs.

## Slide 39 – Composition frem for arv

**Fortæl:** *Composition* betyder, at et objekt er bygget af andre objekter. Et `Job` **har** en kilde og en validator og bruger dem. `Validator` er her en anden class, som vi forestiller os har en metode `er_gyldig`; den er udeladt på sliden.

Fordelene: Delene kan udskiftes, fx en anden kilde eller en strengere validator, uden at ændre `Job`. Hver del kan testes for sig.

*Arv* betyder, at en class bygger videre på en anden og **er en** variant af den. Arv kan være nyttigt, men dybe arvehierarkier bliver hurtigt svære at overskue, fordi adfærden er spredt over flere classes. Derfor er rådet: Brug composition som udgangspunkt, og arv sparsomt.

**Mulige spørgsmål**

- *Hvornår er arv så en god idé?* – Når der er et tydeligt "er en"-forhold, og underklassen kun tilføjer eller tilpasser lidt. Det ses ofte, når et bibliotek eller framework lægger op til det.
- *Hvad er forskellen på "har en" og "er en"?* – Et job *har en* kilde (composition). En CSV-kilde *er en* slags kilde (arv). Hvis "har en" passer, er composition som regel det bedste valg.

## Slide 40 – Faresignal: en class, der burde være en funktion

**Fortæl:** Denne class gør præcis det samme som `rens_postnummer` fra tidligere, men kræver at man først opretter et objekt og derefter kalder en metode. Der er ingen tilstand, der skal huskes, og ingen fordel ved at have et objekt.

Tommelfingerregel: Hvis en class kun har `__init__` og én metode, er den ofte bare en funktion i forklædning.

Nævn også andre faresignaler: dybe arvehierarkier, classes med vage navne som `Manager`, `Helper` eller `Utils`, der samler alt muligt uden en klar opgave, og classes lavet "for en sikkerheds skyld", fordi man måske får brug for dem senere.

**Mulige spørgsmål**

- *Men hvad nu hvis jeg senere får brug for en class?* – Så kan man lave om. Det er lettere at gå fra en simpel funktion til en class end at fjerne unødvendig kompleksitet. Byg til det behov, der er nu.
- *Er det forkert at have en `utils.py`?* – Ikke nødvendigvis, men den har det med at vokse sig stor og uoverskuelig. Moduler med sigende navne er bedre.

## Slide 41 – Tommelfingerregel

**Fortæl:** Opsummér afsnittet med tabellen:

- Input ind, output ud uden tilstand → **funktion**.
- Data med faste felter → **dataclass**.
- Data og adfærd, der hører sammen → **class**.
- Når dele skal genbruges og kombineres → **composition** frem for arv.

Afslut med "Start enkelt": Begynd med funktioner, og lav en class, når koden viser et behov, fx gentagne argumenter eller tilstand.

**Mulige spørgsmål**

- *Hvad med static methods og class methods?* – Det er metoder, der ikke bruger et konkret objekt. De har deres brug, men de springes over i dag for at holde fokus på grundvalget.
- *Hvad med properties?* – Properties gør det muligt at beregne en værdi, når en attribut læses. Det er nyttigt, men ikke nødvendigt for at komme i gang.

## Slide 42 – Øvelse: class eller funktion?

**Fortæl:** Deltagerne diskuterer to og to i 10 minutter. De skal vælge funktion, class eller dataclass til hvert scenarie og kunne begrunde valget. Der skal ikke skrives kode.

Gå rundt og lyt. Spørg ind til begrundelserne, fx: Er der tilstand? Hører data og adfærd sammen? Hvor mange steder bruges det?

Rød baggrund markerer, at deltagerne løser opgaven selv.

**Mulige spørgsmål**

- *Skal vi skrive koden?* – Nej, det er en diskussionsøvelse. Fokus er på valget og begrundelsen.
- *Må vi vælge noget, der ikke står på listen?* – Ja, fx en kombination. Det vigtige er, at I kan forklare hvorfor.

## Slide 43 – Forslag til løsning

**Fortæl:** Gennemgå forslagene og bed nogle par om deres begrundelser først.

1. **Funktion:** Omregningen tager koordinater ind og returnerer nye. Der er ingen tilstand. Hvis omregningen kræver en opsætning, der er dyr at lave, kan et objekt dog være relevant – fx bruger mange biblioteker et transformationsobjekt.
2. **Class:** En forbindelse er tilstand. Den skal åbnes, deles mellem trinene og lukkes igen. Det er et klassisk eksempel på data og adfærd, der hører sammen.
3. **Dataclass:** Rækken er data med faste felter og ingen eller lidt adfærd.
4. **Class:** De gentagne argumenter peger på en kilde med en fast opsætning, som på "Før/efter"-slidesene. En dataclass med opsætningen og almindelige funktioner er også et godt svar.

Understreg, at der ikke er ét rigtigt svar. Det vigtigste er at kunne begrunde valget ud fra læsbarhed og vedligehold.

**Mulige spørgsmål**

- *Vi valgte noget andet – er det forkert?* – Ikke nødvendigvis. Hvis begrundelsen holder, og koden bliver lettere at forstå, er det et fint valg.
- *Hvordan håndterer man lukning af forbindelsen?* – Ofte med en `with`-blok, så forbindelsen lukkes automatisk, også ved fejl. Det kommer vi ikke i dybden med i dag.

## Slide 44 – Tests

Sektionsslide. Afsnittet varer ca. 40 minutter: ca. 15 minutters oplæg, 20 minutters øvelse og 5 minutters gennemgang.

Introducér tests som en hjælp til det, vi lige har gjort: Når vi refaktorerer, vil vi være sikre på, at koden stadig gør det samme. Tests kontrollerer det automatisk. Hold niveauet overordnet: Målet er at kunne læse, skrive og køre simple tests – ikke at kende alle testteknikker.

**Forberedelse:** pytest skal kunne installeres i deltagernes Python-miljø. Er der ikke internetadgang, skal det være installeret på forhånd.

## Slide 45 – Hvorfor tests?

**Fortæl:** En test er kode, der kalder vores kode med et kendt input og kontrollerer, at resultatet er det forventede.

- **Forventet adfærd:** Testen viser, at funktionen gør det, vi tror.
- **Utilsigtede ændringer:** Ændrer vi noget, der får en test til at fejle, opdager vi det med det samme – ikke når et job har leveret forkerte data.
- **Dokumentation:** Testene viser med konkrete eksempler, hvordan en funktion skal bruges, og hvad den returnerer.
- **Tryghed:** Med tests er det mindre risikabelt at ændre kode, man ikke selv har skrevet.

**Mulige spørgsmål**

- *Tager det ikke lang tid at skrive tests?* – Lidt, men det sparer tid senere, fordi fejl findes tidligt. Start med de vigtigste regler.
- *Kan tests bevise, at koden er fejlfri?* – Nej. De viser kun, at de afprøvede tilfælde virker. Derfor er det vigtigt at vælge gode eksempler.

## Slide 46 – En test er bare en funktion

**Fortæl:** Med pytest er en test en almindelig funktion, hvis navn starter med `test_`, i en fil, hvis navn starter med `test_`. pytest finder og kører dem automatisk.

`assert` kontrollerer, at udtrykket er sandt. Hvis `rens_postnummer(" 800")` ikke returnerer `"0800"`, fejler testen.

Testens navn bør beskrive, hvad der testes, så man kan forstå fejlen ud fra navnet alene.

**Mulige spørgsmål**

- *Hvad er forskellen på pytest og `unittest`?* – `unittest` er indbygget i Python, men kræver mere kode. pytest er mere udbredt og enklere at komme i gang med. pytest kan også køre `unittest`-tests.
- *Må testnavnet være så langt?* – Ja. Det kaldes aldrig fra anden kode, så tydelighed er vigtigere end korthed.

## Slide 47 – Kør tests med pytest

**Fortæl:** pytest installeres én gang i projektets miljø med `pip install pytest`. `python -m pytest` køres fra projektets rodmappe og finder selv alle tests.

Vi bruger `python -m pytest` i stedet for blot `pytest`, fordi det kører pytest med det aktive Python-miljø og gør projektets rodmappe tilgængelig for imports. Så kan testene importere `validering` uden ekstra opsætning.

Outputtet viser et punktum for hver test, der bestod, og en opsummering til sidst. `-v` giver en linje pr. test.

VS Code har også et **Testing**-panel, hvor tests kan køres og debugges med et klik, når pytest er valgt som testværktøj.

**Mulige spørgsmål**

- *Hvorfor får jeg `ModuleNotFoundError: No module named 'validering'`?* – Kør fra projektets rodmappe med `python -m pytest`. Blot `pytest` finder ikke altid projektets moduler.
- *Hvorfor findes `pytest` ikke?* – Den er ikke installeret i det aktive miljø. Kontrollér miljøet, og kør `pip install pytest`.
- *Kan jeg køre én bestemt test?* – Ja, fx `python -m pytest tests/test_validering.py` eller med `-k` og en del af testnavnet.

## Slide 48 – Når en test fejler

**Fortæl:** Outputtet er reelt pytest-output fra en version af `rens_postnummer`, hvor `zfill(4)` er fjernet. Gennemgå, hvordan det læses:

- Linjen med `>` viser det `assert`, der fejlede.
- Linjen med `E` viser værdierne: Funktionen returnerede `'800'`, men testen forventede `'0800'`.
- Fil og linjenummer viser, hvor testen ligger.
- Opsummeringen viser, hvor mange tests der fejlede og bestod.

Understreg, at en fejlende test ikke altid betyder, at koden er forkert. Testen kan også være forkert, eller kravene kan have ændret sig. Man skal forstå fejlen, før man retter.

pytest viser også en linje-for-linje-sammenligning af de to værdier. Den er udeladt på sliden.

**Mulige spørgsmål**

- *Hvad gør jeg, hvis testen er forkert?* – Ret testen, men vær sikker på, hvad det rigtige resultat er. Spørg gerne en kollega.
- *Må jeg slette en test, der fejler?* – Kun hvis den tester noget, der ikke længere gælder. Ellers skjuler man en fejl.

## Slide 49 – Hvad skal man teste?

**Fortæl:** Fokusér på funktioner med regler og logik, som rensning og validering. Det er her, fejl typisk opstår, og hvor tests giver mest værdi.

Test både det normale tilfælde og *kanttilfælde*: tomme værdier, for korte eller for lange værdier og værdier i forkert format. Eksemplet tester et gyldigt postnummer, ét med for få cifre, ét med et bogstav og en tom værdi.

Når man finder en fejl, er det en god vane at skrive en test, der fanger den, før den rettes. Så kommer den ikke igen.

**Mulige spørgsmål**

- *Skal alt testes?* – Nej. Start med de vigtigste regler. Simpel kode, der kun læser eller skriver filer, er mindre vigtig at unit-teste.
- *Skal hvert tilfælde have sin egen test?* – Det giver mere præcise fejlbeskeder, men flere `assert` i én test er fint at starte med. pytest kan også køre den samme test med flere værdier via `@pytest.mark.parametrize`.
- *Hvordan tester jeg noget, der læser filer?* – pytest har en indbygget `tmp_path`, som giver en midlertidig mappe. Det er et emne til senere.

## Slide 50 – Unit- og integrationstests

**Fortæl:** En *unit test* tester én funktion isoleret. Den er hurtig, og når den fejler, er det tydeligt, hvor fejlen er. Rene funktioner uden sideeffekter er lettest at unit-teste – derfor er adskillelsen af regler og sideeffekter fra refactoring-afsnittet så nyttig.

En *integrationstest* tester flere dele sammen, fx at hele jobbet kan læse en testfil, rense data og skrive et korrekt resultat. Den er tættere på virkeligheden, men langsommere og sværere at fejlsøge.

Anbefal at starte med unit tests af reglerne og eventuelt én integrationstest af hele forløbet.

**Mulige spørgsmål**

- *Hvilken type er vigtigst?* – Begge har værdi. Mange unit tests og få integrationstests er en god tommelfingerregel.
- *Kan man teste mod den rigtige database?* – Det er muligt, men det gør testene langsomme og afhængige af data. Brug små testdata, hvor det er muligt.

## Slide 51 – Tests og refactoring

**Fortæl:** Tests og refactoring hænger tæt sammen. Kør testene før refactoring for at sikre, at de består. Refaktorér, og kør dem igen. Består de stadig, har ændringen ikke ændret den adfærd, testene dækker. Så kan der committes.

Gør opmærksom på begrænsningen: Testene beskytter kun det, de tester. Derfor er gode tests af de vigtigste regler afgørende.

**Mulige spørgsmål**

- *Hvad hvis der ikke er tests til den kode, jeg skal ændre?* – Skriv nogle få tests af den nuværende adfærd først. Så har du et sikkerhedsnet.
- *Skal tests køres automatisk?* – Det er en god idé, fx når der oprettes en PR. Mange Git-platforme kan sættes op til det. Det ligger uden for dagens emne.

## Slide 52 – Øvelse: skriv jeres første tests

**Fortæl:** Deltagerne arbejder to og to i 20 minutter i deres refaktorerede projekt. Har en gruppe ikke nået at udtrække funktionerne, kan de bruge løsningsforslaget fra refactoring-afsnittet.

Trin 4 er vigtigt: Ved at lave en bevidst fejl ser deltagerne, at testen faktisk fanger den, og de øver sig i at læse pytest-output.

Typiske udfordringer: Importfejl, fordi pytest køres fra en forkert mappe eller uden `python -m`; testfiler eller funktioner, der ikke starter med `test_`, og derfor ikke findes; og pytest, der ikke er installeret i det aktive miljø.

**Mulige spørgsmål**

- *pytest finder ingen tests – hvorfor?* – Kontrollér, at både fil og funktion starter med `test_`, og at der køres fra projektets rodmappe.
- *Skal tests i Git?* – Ja, testene er en del af koden og skal deles med teamet.

## Slide 53 – Forslag til løsning

**Fortæl:** Gennemgå løsningen og bed et par grupper vise ekstra tests, de har skrevet. Diskutér, hvilke kanttilfælde der er dækket, og hvilke der mangler, fx `None` eller et postnummer med mellemrum i midten.

Løsningen er kørt med pytest og består.

**Mulige spørgsmål**

- *Hvorfor tester `rens_postnummer` kun ét tilfælde?* – Det er et minimum. Gode tilføjelser er en værdi, der allerede er korrekt, og en værdi med mellemrum på begge sider.
- *Hvad sker der med `None`?* – `rens_postnummer(None)` giver en fejl, fordi `None` ikke har `strip()`. Om det skal håndteres, afhænger af, hvad data kan indeholde. En test kan dokumentere beslutningen.

## Slide 54 – Afvikling i ETL og fejlfinding i VS Code

Sektionsslide. Afsnittet varer ca. 35 minutter: ca. 20 minutters oplæg og demonstration og 15 minutters øvelse.

Introducér afsnittet: Deltagernes Python-kode køres ikke kun af dem selv, men af et ETL-værktøj. Det stiller krav til, hvordan koden startes, hvordan den finder filer, og hvordan fejl bliver synlige. Fokus er på Python-koden – ikke på selve ETL-værktøjet.

Afstem på forhånd, hvordan deltagernes ETL-værktøj kalder Python: Starter det et script, importerer det et modul og kalder en funktion, eller kører det kode indlejret i værktøjet? Tilpas eksemplerne derefter.

**Forberedelse:** Udlever `ovelser/debugging/start/` til øvelsen (øvelse 5 i øvelsesvejledningen). Det er refactoring-løsningen med en bevidst fejl, der giver et forkert resultat uden at fejle.

## Slide 55 – Python i et ETL-værktøj

**Fortæl:** I et ETL-miljø er det værktøjet, der starter koden – typisk ved at køre et script eller ved at importere et modul og kalde en funktion. Koden kører ofte på en server, under en anden bruger og fra en anden mappe end på udviklerens egen maskine.

Derfor skal koden være robust over for, hvem og hvorfra den kaldes, og fejl skal være synlige i værktøjets log, fordi der ikke sidder en bruger og kigger på skærmen.

**Mulige spørgsmål**

- *Hvordan finder jeg ud af, hvordan vores værktøj kalder koden?* – Se værktøjets dokumentation eller konfigurationen af jobbet, eller spørg den, der har sat det op.
- *Hvad hvis koden er skrevet direkte i værktøjet?* – Så gælder de samme principper. Det kan dog være en fordel at flytte koden ud i moduler, så den kan versionsstyres og testes.

## Slide 56 – Ét tydeligt entry point

**Fortæl:** Et *entry point* er det sted, hvor afviklingen starter. Det er en god praksis at samle det i en `main`-funktion.

Når Python importerer et modul, køres al kode på modulniveau. Står der fx kode, der læser filer, direkte i modulet, køres den allerede ved import – også når værktøjet eller en test blot vil bruge en funktion fra modulet.

`__name__` er `"__main__"`, når filen startes direkte, fx med `python main.py`, og ellers modulets navn. `if __name__ == "__main__":` sørger derfor for, at `main()` kun køres, når filen startes direkte. Så kan modulet både køres som script og importeres.

**Mulige spørgsmål**

- *Hvad skal stå i `main`?* – Det overordnede forløb: opsætning, kald af de vigtigste funktioner og eventuelt logging af resultatet.
- *Hvad hvis værktøjet kalder en funktion i stedet for at køre filen?* – Så er funktionen entry pointet. Den skal kunne kaldes direkte og må ikke afhænge af, at `main` er kørt først.

## Slide 57 – Undgå antagelser om afviklingen

**Fortæl:** Kode, der virker på udviklerens maskine, kan fejle i ETL-værktøjet, fordi forudsætningerne er anderledes:

- **Arbejdsmappen:** En relativ sti som `"adresser.csv"` slås op i den aktuelle arbejdsmappe, som værktøjet bestemmer. `Path(__file__).parent` er mappen, hvor modulet ligger, så stien virker, uanset hvorfra koden startes. Alternativt kan stier komme fra konfiguration eller argumenter.
- **Python-miljøet:** Værktøjet kan bruge en anden Python-version eller mangle pakker. Aftal, hvilket miljø der bruges.
- **Ingen bruger:** `print` bliver måske ikke vist, og `input()` vil hænge eller fejle.

**Mulige spørgsmål**

- *Hvad er `__file__`?* – Stien til den fil, koden står i. Python sætter den automatisk, når et modul indlæses.
- *Hvorfor `pathlib` frem for tekststrenge?* – `Path` håndterer stier på tværs af styresystemer og gør det let at sammensætte stier med `/`.
- *Hvor skal stier til produktion stå?* – I konfiguration, fx en fil eller miljøvariabler, så de kan ændres uden at ændre koden.

## Slide 58 – Hvad er offentligt i et modul?

**Fortæl:** Python har ingen egentlig "privat", men der er en stærk konvention: Navne, der starter med `_`, er interne og kan ændres uden varsel. Navne uden `_` er beregnet til at blive brugt udefra.

Når ETL-jobs kalder funktioner i et modul, bliver de funktioner en slags kontrakt. Ændres navnet eller argumenterne, holder jobbene op med at virke. Derfor bør den offentlige del være lille og stabil, mens hjælpefunktioner gerne må ændres.

Docstringen under `koer_job` beskriver, hvad funktionen gør, og hvad den returnerer. Det er særligt vigtigt for funktioner, som andre kalder.

**Mulige spørgsmål**

- *Kan man forhindre, at nogen kalder en funktion med `_`?* – Nej, det er en konvention, ikke en spærring. Men den signalerer tydeligt, at funktionen ikke er beregnet til brug udefra.
- *Hvad hvis jeg er nødt til at ændre en offentlig funktion?* – Find ud af, hvilke jobs der bruger den, og ændr dem samtidig. Eller lav en ny funktion, og udfas den gamle.

## Slide 59 – Logging frem for print

**Fortæl:** `print` skriver til konsollen, som ingen nødvendigvis ser i et ETL-miljø. `logging` er Pythons indbyggede system til log-beskeder. Beskederne har niveauer, så man kan vælge, hvor meget der skal vises, og værktøjet kan ofte opsamle dem.

`logging.getLogger(__name__)` giver en logger med modulets navn, så man kan se, hvor beskeden kommer fra. `%d` og `%s` er pladsholdere, som udfyldes med værdierne efter teksten.

Opsætningen, fx med `logging.basicConfig(level=logging.INFO)`, sker ét sted i entry pointet – ikke i hvert modul. Er det værktøjet, der kalder en funktion, kan værktøjet selv stå for opsætningen.

Niveauerne kort: `debug` til detaljer under fejlfinding, `info` til normale hændelser, `warning` til noget uventet, som jobbet kan fortsætte efter, og `error` til fejl.

**Mulige spørgsmål**

- *Hvorfor vises mine info-beskeder ikke?* – Standardniveauet er `warning`. Sæt niveauet til `INFO` i opsætningen.
- *Hvorfor ikke f-strings i log-beskeder?* – Det virker også. Pladsholderne er den traditionelle form og udfyldes kun, hvis beskeden faktisk logges.
- *Kan jeg logge til en fil?* – Ja, med `logging.basicConfig(filename="job.log")`. Men ofte er det bedre at lade værktøjet håndtere loggen.

## Slide 60 – Fejl skal være synlige

**Fortæl:** Når der opstår en fejl, er det vigtigste, at den bliver synlig. Eksemplet fanger kun `FileNotFoundError`, logger en forklarende besked og sender fejlen videre med `raise`, så jobbet stadig fejler, og værktøjet kan registrere det.

Det farligste mønster er `except:` efterfulgt af `pass`. Det skjuler alle fejl, også dem man ikke havde forudset, og jobbet ser ud til at gå godt, selvom data er forkerte eller mangler.

Pointe: Et job, der stopper med en tydelig fejl, er bedre end et, der stille leverer forkerte data.

**Mulige spørgsmål**

- *Hvornår skal jeg fange en fejl?* – Når du kan gøre noget fornuftigt ved den, fx springe en enkelt ugyldig række over og logge den. Kan du ikke håndtere den, så lad den gå videre.
- *Hvad gør `raise` uden noget efter?* – Den sender den samme fejl videre, efter at vi har logget den.
- *Hvordan ser værktøjet, at jobbet fejlede?* – Typisk via en exit-kode, der ikke er 0, eller via en exception, når værktøjet kalder en funktion. En ufanget fejl sørger for det.

## Slide 61 – VS Code: det rigtige Python-miljø

**Fortæl:** Et *virtuelt miljø* er en separat Python-installation til et projekt med dets egne pakker. Så påvirker projekterne ikke hinanden, og man kan matche de pakker, ETL-miljøet har.

- `python -m venv .venv` opretter miljøet i mappen `.venv`.
- `.venv\Scripts\activate` aktiverer det i terminalen på Windows.
- `pip install pytest` installerer pakken i miljøet.

I VS Code vælges miljøet med **Python: Select Interpreter**. Så bruger editoren, testpanelet og debuggeren det samme miljø. Det aktive miljø vises nederst i statuslinjen.

Brug om muligt samme Python-version som ETL-værktøjet, så man ikke bruger funktioner, som ikke findes der.

**Mulige spørgsmål**

- *Skal `.venv` i Git?* – Nej. Tilføj den til `.gitignore`, og gem i stedet listen over pakker, fx i `requirements.txt` eller `pyproject.toml`.
- *Aktiveringen fejler i PowerShell – hvorfor?* – PowerShell kan blokere scripts. Brug kommandoprompten, eller få hjælp til at ændre indstillingen efter organisationens regler.
- *Hvordan ser jeg, hvilken Python der bruges?* – `python --version` og `python -c "import sys; print(sys.executable)"` i terminalen, eller statuslinjen i VS Code.

## Slide 62 – Debuggeren i VS Code

**Fortæl:** En debugger stopper programmet på en bestemt linje, så man kan se værdierne af variablerne og følge koden linje for linje. Det er ofte hurtigere end at sprede `print` ud i koden.

Demonstrér live med refactoring-løsningen:

1. Sæt et breakpoint i `rens_raekke` ved at klikke i margenen til venstre for linjenummeret.
2. Start med `F5`, og vælg **Python Debugger** og den aktuelle fil, hvis VS Code spørger.
3. Når programmet stopper, vis **Variables**-panelet med værdien af `raekke`.
4. Brug `F10` til at gå til næste linje og `F11` til at gå ind i `rens_postnummer`.
5. Vis **Call Stack**, som viser, hvilke funktioner der har kaldt hinanden.
6. Fortsæt med `F5`.

Nævn også **Debug Console**, hvor man kan evaluere udtryk, mens programmet er stoppet, og at tests kan debugges direkte fra Testing-panelet.

Sliden mangler et skærmbillede af VS Code under debugging. Tag det fra demonstrationsprojektet, gem det lokalt i repoet, og indsæt det.

**Mulige spørgsmål**

- *Hvad er forskellen på `F10` og `F11`?* – `F10` kører hele linjen, også funktionskald. `F11` går ind i den funktion, der kaldes på linjen.
- *Kan breakpoints have betingelser?* – Ja, højreklik på breakpointet og vælg en betingelse, fx at stoppe, når postnummeret er tomt.
- *Debuggeren stopper ikke – hvorfor?* – Kontrollér, at det er den rigtige fil, der startes, at linjen faktisk køres, og at den rigtige interpreter er valgt.

## Slide 63 – Debug koden, som værktøjet kører den

**Fortæl:** Fejl, der kun opstår i ETL-værktøjet, skyldes ofte forskelle i afviklingen, fx arbejdsmappe eller miljøvariabler. En *launch configuration* i `.vscode/launch.json` gør det muligt at starte debuggeren under de samme forhold.

- `program` er filen, der startes.
- `cwd` er arbejdsmappen – sæt den til den, værktøjet bruger.
- `env` sætter miljøvariabler, som værktøjet sætter.
- `"type": "debugpy"` bruger VS Codes Python-debugger.

Stien og miljøvariablen er eksempler og skal tilpasses. Filen kan oprettes via **Run and Debug** → **create a launch.json file**.

Hvis værktøjet importerer et modul og kalder en funktion, kan man i stedet skrive en lille testfil eller et script, der kalder funktionen med de samme argumenter, og debugge det.

**Mulige spørgsmål**

- *Skal `launch.json` i Git?* – Det kan være nyttigt at dele den med teamet, men den må ikke indeholde adgangskoder eller andre hemmeligheder.
- *Kan man debugge direkte på serveren?* – Det er muligt, men mere avanceret. Prøv først at genskabe forholdene lokalt, og brug loggen fra værktøjet.

## Slide 64 – Øvelse: find fejlen med debuggeren

**Fortæl:** Deltagerne arbejder to og to i 15 minutter med `ovelser/debugging/start/`, som giver et forkert resultat uden at fejle. De skal finde fejlen med debuggeren – ikke ved at læse koden igennem eller tilføje `print`.

Trin 4 kobler til testafsnittet: Når fejlen er fundet, skrives en test, der havde fanget den. Så kommer den ikke igen.

Gennemgå til sidst kort, hvordan fejlen blev fundet: Hvor blev breakpointet sat? Hvilken variabel afslørede fejlen?

Fejlen i `ovelser/debugging/start/` er, at `POSTNUMMER_KOLONNE` i `config.py` er sat til `1`. Husnummeret behandles derfor som postnummer: Alle fire rækker kommer med, husnumrene får nuller foran (`0012`), og postnumrene renses ikke. Et breakpoint i `rens_raekke` viser hurtigt, at det er `'12'` og ikke `' 800'`, der sendes til `rens_postnummer`. Testen `rens_raekke(["Søndergade", "12", " 800"]) == ["Søndergade", "12", "0800"]` fanger fejlen. Bemærk, at testene fra test-øvelsen ikke fanger den, fordi `rens_postnummer` og `er_gyldigt_postnummer` virker fint – en god pointe om at teste de funktioner, der binder reglerne sammen.

**Mulige spørgsmål**

- *Hvor skal vi sætte breakpointet?* – Start, hvor resultatet bliver forkert, fx i rensning eller validering, og gå baglæns, hvis det ikke afslører noget.
- *Vi fandt fejlen ved at læse koden – er det snyd?* – Nej, men prøv alligevel debuggeren, så I kender den, når koden er større.

## Slide 65 – Samlet praktisk øvelse

Sektionsslide. Øvelsen varer 90 minutter og samler hele dagen i ét forløb. Deltagerne arbejder to og to i et fælles Bitbucket-repository som et lille team, der vedligeholder adresse-jobbet. Hver person løser opgaver på sin egen branch, opretter pull requests og reviewer makkerens ændringer.

**Forberedelse** (se [underviservejledningen](../../ovelser/samlet-ovelse/README.md)):

- Opret ét Bitbucket-repository pr. hold med indholdet af `ovelser/samlet-ovelse/start/` på `main`, og giv begge deltagere skriveadgang.
- Vælg merge-strategien **Merge commit**, så revert i opgave 5 virker som beskrevet.
- Afprøv, at deltagerne kan klone og pushe fra VS Code på kursusmaskinerne. Login til Bitbucket er den hyppigste årsag til, at øvelsen går i stå.
- Print eller udlever opgave 5 (`ovelser/samlet-ovelse/5-ups-separator.md`) – den ligger bevidst ikke i startprojektet.

Deltagerne bruger VS Codes indbyggede Git-klient til at tale med Bitbucket. Pull requests oprettes, reviewes og merges i Bitbucket i browseren. Revert kræver terminalen, da VS Code ikke har en indbygget kommando til at reverte et merge-commit.

## Slide 66 – Adresse-jobbet i produktion

**Fortæl:** Præsentér scenariet: Holdet har overtaget adresse-jobbet fra refactoring-afsnittet. Driften og leverandøren sender opgaver, som løses én ad gangen. Opgavesedlerne ligger i `opgaver/` i repositoryet.

Gennemgå tidsplanen. Runde 1 er bygget, så de to opgaver ikke rører de samme filer. Runde 2 er bygget, så de to opgaver *gør* – det giver en konflikt, som er en planlagt del af øvelsen. De sidste 20 minutter rummer en overraskelse og en fælles opsamling.

Sammenhæng med dagens emner:

| Opgave | Emner |
| --- | --- |
| 1 – fejl i postnumre | Debugger, tests først, Git-flow |
| 2 – ETL-klar | Entry point, logging, synlige fejl |
| 3 – regel for vejnavn | Struktur, tests |
| 4 – Adresse-dataclass | OOP, dataclass, struktur |
| 5 – ups | Revert |
| Alle | Branch, commit, PR, review, merge, konflikt |

**Mulige spørgsmål**

- *Hvad hvis vi ikke når det hele?* – Det er helt fint. Runde 1 og 2 er det vigtigste. Opgave 5 kan også vises som demonstration.
- *Må vi hjælpe hinanden?* – Ja, gerne. Men skriv selv koden på jeres egen opgave, og brug reviewet til at forstå makkerens.

## Slide 67 – Kom i gang

**Fortæl:** Deltagerne kloner holdets repository i VS Code med **Git: Clone** og indsætter adressen fra Bitbucket (knappen **Clone** på repositoryets side). VS Code spørger, hvor det skal gemmes, og om det skal åbnes.

Derefter opretter de et virtuelt miljø, installerer pytest og kører tests og jobbet. Forventet resultat: 2 tests består, og jobbet skriver "Skrev 3 af 5 rækker".

Bed dem lægge mærke til resultatfilen `data/resultat.csv`: *Vestergade* mangler, og rækken uden vejnavn er med. Det er udgangspunktet for opgave 1 og 3. Bed dem også aftale, hvem der er person A og B.

**Mulige spørgsmål**

- *Klon fejler med en fejl om adgang eller login.* – Kontrollér, at de er logget ind på Bitbucket, og at de bruger den rigtige adresse. Ved HTTPS kræver Bitbucket typisk en app-password eller et API-token i stedet for den almindelige adgangskode – afhængigt af organisationens opsætning.
- *Aktiveringen af `.venv` fejler i PowerShell.* – Brug kommandoprompten i VS Code-terminalen, eller spring aktiveringen over og vælg interpreteren i VS Code. Så bruger nye terminaler miljøet automatisk.
- *Skal `.venv` committes?* – Nej, den står i `.gitignore`.

## Slide 68 – Arbejdsgangen for hver opgave

**Fortæl:** Gennemgå flowet, som gentages for hver opgave. Vis det gerne live i VS Code:

- **Hent nyeste main:** Skift til `main` via branch-navnet nederst til venstre, og klik **Sync Changes** (eller pilene ved branch-navnet). Det henter og sender ændringer.
- **Opret branch:** Klik på branch-navnet → **Create new branch...** → skriv navnet. Branchen oprettes fra den branch, man står på – derfor skal man stå på en opdateret `main`.
- **Commit:** I **Source Control** (`Ctrl+Shift+G`) vises ændrede filer. `+` stager en fil, man skriver en besked og klikker **Commit**.
- **Del branchen:** Første gang vises **Publish Branch**. Senere bruges **Sync Changes**.
- **Pull request:** Efter publicering viser Bitbucket ofte et link til at oprette en PR. Vælg `main` som mål, og tilføj makkeren som reviewer.

Terminalkolonnen viser de samme trin med kommandoer, som deltagerne kender fra Git-afsnittet.

**Mulige spørgsmål**

- *VS Code spørger, om den skal stage alle ændringer automatisk.* – Det er en bekvemmelighed. Det er bedre at se, hvad der committes, så svar nej, indtil man er tryg.
- *Hvad er forskellen på Sync og Push?* – **Sync Changes** både henter (pull) og sender (push). Push sender kun.
- *Kan PR'en oprettes fra VS Code?* – Med Atlassians udvidelse *Jira and Bitbucket* kan det lade sig gøre, men i øvelsen bruger vi Bitbucket i browseren.

## Slide 69 – Review i Bitbucket

**Fortæl:** Review er en central del af øvelsen. Reviewer læser ændringerne i PR'ens **Diff** og kan kommentere på enkelte linjer. Gennemgå punkterne kort.

Reviewet behøver ikke at være langt, men det skal være reelt: Læs koden, og kontrollér den mod opgavesedlens "Klar, når". Opfordr reviewer til at hente branchen og køre testene, hvis der er tvivl.

Når reviewer er tilfreds, klikkes **Approve**, og PR'en merges med strategien **Merge commit**. Er der kommentarer, retter forfatteren på samme branch, committer og synkroniserer – PR'en opdateres automatisk.

**Mulige spørgsmål**

- *Hvem merger – forfatteren eller reviewer?* – Aftal det i holdet. Mange teams lader forfatteren merge efter godkendelse.
- *Hvad hvis vi er uenige?* – Diskutér det i PR'en eller ansigt til ansigt. Opgavesedlen er afgørende for, hvad der skal laves.
- *Hvad betyder merge-strategierne?* – **Merge commit** bevarer branchens commits og laver et merge-commit. **Squash** samler alle commits i ét. Vi bruger merge commit, så revert i opgave 5 virker som beskrevet.

## Slide 70 – Runde 1 · 30 min.

**Fortæl:** Person A tager opgave 1, person B opgave 2. Hver følger opgavesedlen. Når begge PR'er er merget, henter begge `main`.

**Opgave 1 – forventet løsning:** Fejlen er, at `rens_postnummer` kalder `zfill(4)` *før* `strip()`. `" 800"` er allerede fire tegn langt, så `zfill` gør ingenting, og `strip` fjerner derefter mellemrummet – resultatet `"800"` afvises. Rettelsen er `vaerdi.strip().zfill(4)`. Testen `assert rens_postnummer(" 800") == "0800"` skal skrives først og fejle. Den eksisterende test bruger `"800"` uden mellemrum og fangede derfor ikke fejlen – en god pointe om valg af testdata.

I debuggeren kan man sætte et breakpoint i `rens_postnummer` og se, at `vaerdi` er `' 800'`. Med `F10` gennem linjen eller i **Debug Console** ses, at `vaerdi.zfill(4)` stadig er `' 800'`. Breakpointet rammes én gang pr. række – brug **Continue** (`F5`), indtil `vaerdi` er `' 800'`, eller et betinget breakpoint.

**Opgave 2 – forventet løsning:** `koer_job` læser med `try`/`except FileNotFoundError`, logger fejlen og bruger `raise`. En løkke renser hver række, tilføjer gyldige og logger afviste med `logger.warning`. Til sidst skrives resultatet, antallet logges, og antallet returneres. `main()` sætter logging op og kalder `koer_job(INPUT_STI, OUTPUT_STI)`. Den fulde version findes i `loesning/main.py` (der dog også indeholder opgave 4).

Forventet resultat efter runde 1: 3 tests består, og jobbet skriver 4 af 5 rækker og logger *Torvet* (`80a0`) som afvist.

Gå rundt og hjælp. Typiske udfordringer: Branch oprettet fra en forældet `main`, glemt **Publish Branch**, forkert målbranch i PR'en og debuggeren, der starter den forkerte fil.

**Mulige spørgsmål**

- *Hvorfor skal testen skrives før rettelsen?* – Så man ser, at testen faktisk fanger fejlen. En test, der aldrig har fejlet, kan teste det forkerte.
- *Skal `koer_job` have type hints som `Path` eller `str`?* – Begge virker, fordi `open` accepterer begge. `Path` passer til `config.py`.
- *Hvordan tester jeg den manglende fil?* – Kald `koer_job` med en sti, der ikke findes, fx fra en lille testfil eller Debug Console. Bonusopgaven viser, hvordan det kan blive en test.

## Slide 71 – Runde 2 · 30 min.

**Fortæl:** Begge starter fra en opdateret `main`, så runde 1 er med. Person A tager opgave 3, person B opgave 4. Fortæl åbent, at de vil få en konflikt – det er meningen.

**Opgave 3 – forventet løsning:** `VEJNAVN_KOLONNE = 0` i `config.py`. `er_gyldig` tjekker `raekke[VEJNAVN_KOLONNE].strip() != ""` sammen med postnummeret. Tests af en gyldig række, en tom og en med kun mellemrum.

**Opgave 4 – forventet løsning:** Se `loesning/adresse.py`. `rens_adresse` returnerer en ny `Adresse` med rensede felter. `koer_job` bruger `fra_raekke` efter læsning og `til_raekke` før skrivning. `POSTNUMMER_KOLONNE` fjernes fra `config.py`. Resultatet skal være uændret: 4 af 5 rækker.

Hold øje med, hvem der merger først. Den, der merger sidst, skal løse konflikten – se næste slide.

**Mulige spørgsmål**

- *Kan vi undgå konflikten ved at vente på hinanden?* – Ja, og det er en god strategi i praksis. Her er konflikten med vilje, så I prøver at løse en.
- *Skal `fra_raekke` håndtere rækker med for få felter?* – Ikke i opgaven. Men det er et godt spørgsmål – og det viser sig i opgave 5.

## Slide 72 – Konflikt? Sådan gør I

**Fortæl:** Den, der merger sidst, ser i Bitbucket, at PR'en har konflikter og ikke kan merges. Konflikten løses lokalt på branchen:

1. `git fetch origin` og `git merge origin/main` henter og fletter den nyeste `main` ind. (I VS Code: **Git: Fetch** og derefter **Git: Merge** i kommandopaletten → vælg `origin/main`.)
2. Filer med konflikt står under **Merge Changes** i Source Control. Åbn hver fil, og klik **Resolve in Merge Editor**.
3. Kombinér ændringerne, og klik **Complete Merge**.
4. Kør testene, før der committes.
5. Commit og synkronisér. PR'en opdateres og kan merges.

Brug ikke `git pull origin main` her. Med nyere Git kræver det ekstra opsætning, når branches er gået i hver sin retning.

**Konflikten i detaljer** (afprøvet). Hvis opgave 3 merges først, får person B konflikter i tre filer:

- `config.py`: B har fjernet `POSTNUMMER_KOLONNE`, A har tilføjet `VEJNAVN_KOLONNE`. Løsning: Ingen af konstanterne – `Adresse` har navngivne felter.
- `validering.py`: Importen og `er_gyldig` er i konflikt. Løsning: B's version med `Adresse`, *udvidet* med A's regel: `adresse.vejnavn.strip() != ""`.
- `tests/test_validering.py`: Begge har ændret importen og tilføjet en test. Løsning: Begge tests skal med, og importen skal indeholde både `er_gyldig` og `rens_adresse`. A's test skal omskrives fra lister til `Adresse(...)`.

Pointen: **Hverken "Accept Current" eller "Accept Incoming" er korrekt.** Vælger man blindt den ene side, mister man enten regel eller dataclass. Vælger man "Accept Both", fejler koden. Testene afslører, om løsningen holder. Det er derfor, de skal køres før commit.

Hvis opgave 4 merges først, får person A de samme konflikter med omvendte roller. Løsningen er den samme. Den løste version findes i `loesning/`.

Forventet resultat efter runde 2: 5 tests består, og jobbet skriver 3 af 5 rækker og afviser *Torvet* og rækken uden vejnavn.

**Mulige spørgsmål**

- *Kan vi ikke bare vælge vores egen version?* – Så forsvinder makkerens ændring. Det er den hyppigste fejl ved konflikter.
- *Hvorfor skal A's test ændres, når den ikke var i konflikt med vores?* – Fordi `er_gyldig` nu tager en `Adresse`. Teksten kunne flettes, men koden passer ikke sammen. Testene fanger netop den slags.
- *Vi har lavet noget forkert midt i konflikten – hvad nu?* – `git merge --abort` sætter branchen tilbage til før merge. Så kan I starte forfra.

## Slide 73 – Ups! · 10 min.

**Fortæl:** Udlever opgaveseddel 5 eller vis sliden. Lad holdet gennemføre ændringen hurtigt: branch, ret `SEPARATOR` til `","`, PR, godkendelse og merge.

Når de kører jobbet på `main`, fejler det med `ValueError: not enough values to unpack (expected 3, got 1)`. Med komma som separator læses hver linje som ét felt, og `fra_raekke` kan ikke pakke den ud i tre. Bemærk: **Testene består stadig**, fordi de ikke dækker filindlæsningen. Det er en vigtig pointe til opsamlingen.

Meddel derefter: "Leverandøren skifter først næste måned – fortryd ændringen nu." Person B reverter i terminalen som beskrevet på opgavesedlen: opdatér `main`, find merge-commit'et med `git log --oneline -5`, opret en branch, `git revert -m 1 <id>`, push og opret en PR. Merge-commit'et har beskeden *Merged in config/komma (pull request #...)*. Har Bitbucket en **Revert**-knap på den mergede PR, kan den bruges i stedet.

Efter merge af fortrydelsen virker jobbet igen: 3 af 5 rækker.

**Mulige spørgsmål**

- *Hvorfor ikke bare ændre separatoren tilbage i en ny PR?* – Det giver samme kode og er også en løsning. Revert gør det tydeligt i historikken, at ændringen blev fortrudt, og virker også, når ændringen er større end én linje.
- *Git åbner en editor ved revert – hvad gør jeg?* – Git beder om en commit-besked. Gem og luk filen for at bruge standardbeskeden. Brug `--no-edit` for at springe editoren over.
- *Hvorfor fangede testene ikke fejlen?* – De tester kun reglerne, ikke læsning af filer. En integrationstest af `koer_job` med en rigtig fil – som i bonusopgaven – ville have fanget den.

## Slide 74 – Opsamling på øvelsen

**Fortæl:** Vis `git log --oneline --graph` på et af holdenes `main` – på storskærm eller i Bitbucket under **Commits**. Grafen viser branches, merge-commits, konfliktløsningen og revert'en. Brug den til at fortælle historien om, hvad holdet har lavet.

Tag derefter en kort runde med spørgsmålene. Gode pointer at få frem:

- Konflikten krævede forståelse af begge ændringer – ikke blot et valg af side.
- Reviewet er en chance for at lære af hinandens kode – ikke kun for at finde fejl.
- Testene fangede fejlen i opgave 1 og en dårlig konfliktløsning, men ikke separatoren i opgave 5. Tests beskytter kun det, de tester.
- Små branches og hyppige merges giver færre og mindre konflikter.

**Mulige spørgsmål**

- *Er det normalt med så mange merge-commits?* – Ja, med merge-strategien merge commit. Andre teams bruger squash for en lineær historik. Begge dele er fine – det vigtige er at være enige.
- *Hvordan kommer vi i gang med det her i vores egne projekter?* – Start med branches og pull requests for alle ændringer, og tilføj tests til de vigtigste regler, efterhånden som I alligevel ændrer koden.

## Slide 75 – Opsamling og spørgsmål

Sektionsslide. Brug ca. 5–10 minutter. Sig tak for dagen, og forklar, at vi samler op på de vigtigste pointer, før der er tid til spørgsmål.

## Slide 76 – Dagens vigtigste pointer

**Fortæl:** Gennemgå pointerne og kobl hver af dem til det, deltagerne har prøvet i løbet af dagen:

- **Git:** Arbejd på en branch, og få ændringer ind i `main` via en pull request med review.
- **Struktur:** Små funktioner med ét ansvar. Hold reglerne fri for sideeffekter, så de kan testes og genbruges.
- **OOP:** Start med funktioner. Brug en class, når data og adfærd hører sammen, og en dataclass til data med faste felter.
- **Tests:** Tests gør det trygt at ændre kode og fanger fejl, før de når produktion.
- **ETL:** Et tydeligt entry point, logging i stedet for print, og fejl, der er synlige frem for skjulte.

Spørg deltagerne, hvad de vil tage med tilbage til deres egen kode. Afslut med spørgsmål.

**Mulige spørgsmål**

- *Hvor starter vi med vores eksisterende kode?* – Vælg ét job, der ofte ændres. Læg det i Git, skriv nogle få tests af de vigtigste regler, og refaktorér i små skridt.
- *Hvor kan vi lære mere?* – Python-dokumentationen på docs.python.org, pytest-dokumentationen og VS Codes dokumentation om Python. Pro Git-bogen er gratis online og god til Git.
- *Skal alt eksisterende kode laves om?* – Nej. Forbedr koden, når I alligevel skal ændre i den.