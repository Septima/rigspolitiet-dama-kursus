# Dag 1


# Dag 2

# Python – struktur, OOP, Git og VS Code

## Forslag til tidsfordeling

Ca. 5 timer og 15 minutter fagligt indhold og øvelser. Pauser og frokost kommer oveni.

| Tid | Emne og arbejdsform |
| --- | --- |
| 55 min. | Git: samarbejdsflowet med branch, commit, PR, merge og konflikter – oplæg og guidet øvelse |
| 60 min. | Python-struktur og refactoring af eksisterende kode |
| 35 min. | OOP: hvornår giver en class værdi frem for en funktion? |
| 40 min. | Tests: skriv eller kør en enkel test før og efter en ændring |
| 35 min. | Afvikling i ETL-miljøet og fejlfinding i VS Code |
| 90 min. | Samlet praktisk øvelse: teamarbejde i Bitbucket med branches, PR, review, konflikt og revert |

## Formål

Kurset henvender sig til deltagere, som allerede har erfaring med Python og ønsker at blive bedre til at skrive struktureret, genbrugelig og vedligeholdelig kode.

Kurset tager udgangspunkt i den virkelighed, hvor Python-kode indgår i et ETL-værktøj og afvikles som en del af en større løsning. Fokus er derfor ikke på selve ETL-processerne, men på **hvordan man skriver og organiserer Python-kode, så den er nem at forstå, vedligeholde, genbruge og afvikle i et større system**.

Kurset kombinerer korte faglige oplæg med praktiske øvelser, kodeeksempler, refactoring og fælles diskussion af konkrete problemstillinger.

---

# 1. Git – fra lokal versionsstyring til samarbejde

Git introduceres tidligt, så deltagerne kan bruge versionsstyring gennem resten af kurset. Deltagerne er nybegyndere i Git, så fokus er på at forstå samarbejdsflowet overordnet – ikke på avancerede kommandoer.

Afsnittet består af et kort oplæg (ca. 25 min.) og en guidet øvelse (ca. 30 min.), hvor deltagerne selv opretter en branch, committer, opretter en PR, merger og løser en enkel konflikt. Git bruges derefter løbende i resten af dagens øvelser.

### Grundlæggende Git

- Repository
- Working tree
- Staging
- Commits
- `git status`
- `git add`
- `git commit`
- `git log`
- `git diff`

### Branches og samarbejde

- Branches
- Feature branches
- Merge
- Merge conflicts
- Konflikthåndtering
- Pull requests / code review
- God commit-praksis
- Hvordan man bruger Git til at arbejde sikkert med ændringer

Fokus er på at kunne bruge Git i det daglige udviklingsarbejde frem for at lære alle Gits funktioner.

---

# 2. Python – fra script til struktureret kode

Vi tager udgangspunkt i Python-kode, som fungerer, men som over tid kan blive vanskelig at vedligeholde.

Afsnittet holdes på ca. 60 minutter: kort oplæg om funktioner, læsbarhed og modulopdeling efterfulgt af en refactoring-øvelse. Projektstruktur gennemgås overordnet, og en del af refactoringen fortsætter i den samlede øvelse sidst på dagen.

### Emner

- God strukturering af Python-kode
- Funktioner og ansvar
- Argumenter, return values og scope
- Type hints
- Navngivning og læsbarhed
- Separation of concerns
- Side effects og state
- Genbrugelig kode
- Refactoring af eksisterende kode

### Moduler og packages

- Python modules
- Packages
- Imports og namespaces
- `__init__.py`
- Hvordan man opdeler et større Python-script i logiske moduler
- Hvordan man vurderer, hvad der bør ligge sammen, og hvad der bør adskilles

### Projektstruktur

Introduktion til en hensigtsmæssig struktur for et Python-projekt, eksempelvis:

```text
project/
├── README.md
├── pyproject.toml
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       ├── processing.py
│       ├── validation.py
│       └── config.py
└── tests/
```

Der fokuseres på principperne bag strukturen frem for en bestemt projektstruktur.

---

# 3. Classes og objektorienteret programmering

Formålet er ikke at gøre al Python-kode objektorienteret, men at give deltagerne en forståelse for **hvornår classes og OOP giver værdi, og hvordan de bruges hensigtsmæssigt**.

### Emner

- Hvad er en class?
- Objects, attributes og methods
- `__init__`
- `self`
- Properties
- Class methods og static methods
- Dataclasses
- State og ansvar
- Hvornår er en class relevant?
- Hvornår er en funktion en bedre løsning?

### OOP-principper

- Encapsulation
- Single Responsibility
- Composition
- Inheritance
- Composition vs. inheritance
- Loose coupling
- Genbrug og fleksibilitet
- Undgåelse af unødvendig kompleksitet og overengineering

Der arbejdes med konkrete eksempler, hvor deltagerne vurderer forskellige måder at strukturere den samme funktionalitet på.

---

# 4. Python Best Practice

Fokus på de valg, der gør kode lettere for andre udviklere at forstå og arbejde videre med.

### Emner

- Læsbarhed og tydelig kode
- Naming conventions
- Type hints
- Docstrings
- Exceptions og fejlhåndtering
- Logging
- Configuration
- Constants
- Mutable vs. immutable data
- Scope og global state
- Små, fokuserede funktioner
- Genbrug uden unødig abstraktion

Der arbejdes løbende med eksempler på både god og problematisk kode, så deltagerne træner evnen til at **læse, diskutere og forbedre eksisterende kode**.

---

# 5. Tests – grundlæggende forståelse

En kort introduktion til, hvorfor tests er nyttige, og hvordan de kan støtte arbejdet med eksisterende kode og refactoring. Fokus er på at kunne læse og forstå simple tests – ikke på en dyb gennemgang af testmetoder eller testværktøjer.

### Emner

- Hvad en test kan hjælpe med at afklare
- At teste funktioners forventede input og output
- Enkle unit tests og forskellen på unit- og integrationstests
- At køre eksisterende tests før og efter en ændring
- Hvordan tests kan hjælpe med at opdage utilsigtede ændringer

---

# 6. Python i et ETL-miljø

Kurset tager højde for, at Python-koden ikke nødvendigvis afvikles som et selvstændigt program, men bliver kaldt og håndteret af et ETL-værktøj.

### Emner

- Hvordan Python-koden bliver afviklet af et eksternt værktøj
- Entry points og execution flow
- Hvad skal være offentligt tilgængeligt i et Python-modul?
- Hvordan undgår man kode, der kun virker i én bestemt afviklingssituation?
- Imports og afhængigheder
- Strukturering af kode, så den kan genbruges på tværs af ETL-jobs
- Debugging af kode, der afvikles fra et eksternt program

Fokus er på **Python-kodens struktur og afvikling**, ikke på at lære selve ETL-værktøjet.

---

# 7. VS Code som udviklingsmiljø

VS Code bruges som det primære værktøj til udvikling og afvikling af Python-koden.

### Emner

- Python interpreter og environments
- Projektstruktur
- Terminal
- Navigation i større kodebaser
- Search og symbol navigation
- Refactoring
- Debugger
- Breakpoints
- Variables og call stack
- Git integration
- Diff og ændringshistorik
- Formatter/linter
- Kørsel og fejlsøgning af Python-kode

VS Code introduceres primært gennem konkrete udviklingsopgaver frem for som en gennemgang af alle funktioner.

---

# 8. Praktisk arbejdsform

Kurset er ikke bygget op omkring traditionelle præsentationer.

Undervisningen vil primært bestå af:

- Korte faglige introduktioner
- Konkrete Python-eksempler
- Praktiske opgaver
- Refactoring af eksisterende kode
- Fælles code reviews
- Diskussion af forskellige løsningsmuligheder
- Fejlfinding og debugging
- Git-øvelser
- Arbejde direkte i VS Code

Dagen afsluttes med en samlet øvelse på 90 minutter, "Adresse-jobbet i produktion". Deltagerne arbejder to og to i et fælles Bitbucket-repository via VS Code. De løser opgavesedler på hver sin branch, opretter pull requests, reviewer hinandens ændringer, løser en planlagt merge-konflikt og fortryder en merget ændring med revert. Opgaverne dækker debugger og tests, ETL-klar kode med logging, en ny valideringsregel og en dataclass. Materialet ligger i [ovelser/samlet-ovelse](ovelser/samlet-ovelse/README.md).

---

# Kursets overordnede progression

Kurset introducerer Git fra starten og bevæger sig fra den enkelte Python-fil til den samlede udviklingsproces:

**Git – versionsstyring fra starten**

↓

**Python-kode**

↓

**Funktioner og ansvar**

↓

**Moduler og packages**

↓

**Classes og OOP**

↓

**Projektstruktur og best practice**

↓

**Tests og refactoring**

↓

**Afvikling i ETL-miljøet**

↓

**VS Code og debugging**

↓

**Samarbejde og code review**

---

# Udbytte

Efter kurset skal deltagerne kunne:

- Strukturere Python-kode i funktioner, moduler og packages
- Vurdere hvornår en class er hensigtsmæssig
- Anvende grundlæggende OOP-principper
- Skrive mere læsbar og vedligeholdelig Python
- Refaktorere eksisterende kode
- Forstå formålet med simple tests og bruge dem i forbindelse med ændringer
- Forstå og arbejde med en større Python-projektstruktur
- Skrive Python-kode, der passer ind i et eksternt ETL-miljø
- Bruge Git til versionsstyring og almindeligt udviklingsarbejde
- Arbejde med branches og håndtere merge conflicts
- Bruge VS Code til udvikling, debugging og Git
- Forholde sig konstruktivt til andres kode gennem code review