---
marp: true
paginate: true
style: |

  section::after {
    color: white;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 3rem;

  }

  .center {
    text-align: center;
  }

  .topbar {
  padding-top: 125px;
  }

    .top50 {
  padding-top: 50px;
  }

      .top100 {
  padding-top: 100px;
  }

        .top150 {
  padding-top: 150px;
  }
  img{background-color:transparent}

  header {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 1fr 1fr;
        grid-gap: 10px;
        box-sizing: border-box;
        justify-content: center;
        width: 100%;
    }

    header img {
        height: 50px;
    }

  footer {
        display: grid;
        grid-template-columns: 1fr max-content;
        #background-color: #bb2e29;
        color: white;
        align-content: right;
        font-size: 20px;
    }

  h1 {
  font-size: 70px;
  color: white;
    }  
  h2 {
  font-size: 50px;
  color: white;
    }

  h3 {
  font-size: 30px;
  color: white;
    }
    
  .slide_heaader {
    position:absolute;top:90px;left:75px;right:75px;font-size:50px;

  }

  li::marker {
  color: #397c67;
    }

   li {
  color: white;
  padding: 0px;
  font-size:30px;
  }

   p {
  color: white;
  padding: 0px;
  padding-top: 30px;
  font-size:30px;
  }

  img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }

      .container {
    display: flex;
  }
  .col {
    flex:1;
    padding-right: 20px;
    padding-left: 20px;
    padding-top: 120px;

  }
    .col_tight {
    flex:1;
    padding-right: 20px;
    padding-left: 20px;
    padding-top: 60px;

  }

  .center_img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  }

  .git-flow {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-top: 40px;
    font-size: 26px;
    color: white;
  }
  .git-step {
    padding: 18px;
    border: 2px solid white;
    border-radius: 8px;
    text-align: center;
  }
  section.git, section.code {
    justify-content: flex-start;
    padding-top: 175px;
  }
  section.git pre, section.code pre {
    font-size: 24px;
  }
  section.git p, section.code p {
    padding-top: 0;
  }
  section.code table {
    font-size: 28px;
    color: black;
  }
  section.code .small table {
    font-size: 22px;
  }

header:  ![Septima](../../ressources/logo/septima.svg "Septima")

footer: Python – struktur, OOP, Git og VS Code  





        
---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:145px;left:75px;right:75px;font-size:64px;">Python – struktur, OOP,<br>Git og VS Code</h1>
<h2 style="position:absolute;top:340px;left:75px;right:75px;font-size:45;">Dag 2</h2>
<h3 style="position:absolute;top:420px;left:75px;right:75px;font-size:30;">Underviser · dato</h3>

---
<!-- backgroundColor: #397c67 -->

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Dagens overblik</h1>

* Git-grundlag · 55 min.
* Python-struktur og refactoring · 60 min.
* OOP: class eller funktion? · 35 min.
* Tests · 40 min.
* ETL og fejlfinding i VS Code · 35 min.
* Samlet praktisk øvelse · 90 min.

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:60px;">Git-grundlag</h1>

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Hvorfor Git?</h1>

* Gem en historik over ændringer og samarbejd om koden
* Se tidligere commits med:

```bash
git log --oneline -5
```

Kommandoerne køres i terminalen inde i projektets repository.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Lokalt og fælles</h1>

<div class="git-flow">
  <div class="git-step">Din computer<br>Lokalt repository</div>
  <div>⇄</div>
  <div class="git-step">GitHub / Git-platform<br>Fælles repository</div>
</div>

Et **repository** indeholder projektets filer og historik.

```bash
git remote -v
```

Viser adresserne på projektets fælles repositories.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Hvad er et commit?</h1>

Et **commit** gemmer de valgte ændringer i projektets historik.

```bash
git add validering.py
git commit -m "Forbedr validering"
```

**Add** vælger ændringerne (stage) · **Commit** gemmer dem lokalt

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Se, hvad du har ændret</h1>

```bash
git status
git diff
git diff --staged
```

**Status** viser filernes tilstand. **Diff** viser indholdet af ændringerne – før og efter de er valgt til et commit.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Main og branches</h1>

**main** er projektets fælles udgangspunkt. En **branch** er en separat udviklingslinje til dit arbejde.

```bash
git switch main
git pull origin main
git switch -c validering
```

Opdatér main, og opret en branch til din ændring.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Fra branch til fælles kode</h1>

<div class="git-flow">
  <div class="git-step">main</div>
  <div>→</div>
  <div class="git-step">branch</div>
  <div>→</div>
  <div class="git-step">commit<br>og push</div>
  <div>→</div>
  <div class="git-step">pull request<br>og review</div>
  <div>→</div>
  <div class="git-step">merge<br>til main</div>
</div>

Del branchen og dens commits med det fælles repository:

```bash
git push -u origin validering
```

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Pull request og review</h1>

En **pull request (PR)** foreslår at flette din branch ind i main. En kollega kan gennemgå og kommentere ændringerne.

Opret en PR på Git-platformen – eller med GitHub CLI:

```bash
gh pr create --base main --head validering --web
```

`gh` kræver GitHub CLI og login til GitHub.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Merge efter review</h1>

Når PR'en er gennemgået og eventuelle krav er opfyldt, kan ændringerne **merges** til main på Git-platformen.

Eksempel med GitHub CLI, mens du står på din branch:

```bash
gh pr merge --merge
```

Opdatér din lokale main bagefter:

```bash
git switch main
git pull origin main
```

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Fortryd en merget PR</h1>

Fortryd med en **revert**: et nyt commit, der vender ændringerne om.

<div class="git-flow">
  <div class="git-step">PR merget<br>til main</div>
  <div>→</div>
  <div class="git-step">revert<br>på ny branch</div>
  <div>→</div>
  <div class="git-step">ny PR<br>og review</div>
  <div>→</div>
  <div class="git-step">merge<br>til main</div>
</div>

Historikken bevares. Slet eller omskriv aldrig delt historik på main.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Revert i praksis</h1>

På GitHub: **Revert**-knappen på den mergede PR opretter en ny PR. Med CLI:

```bash
git switch main
git pull origin main
git log --oneline -5
git switch -c fortryd-validering
git revert -m 1 <merge-commit>
git push -u origin fortryd-validering
```

Opret derefter en PR som normalt.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Hvad er en merge-konflikt?</h1>

En konflikt kan opstå, når Git ikke selv kan kombinere ændringer i samme fil.

På din branch kan du hente og forsøge at flette den nyeste main ind:

```bash
git fetch origin
git merge origin/main
git status
```

Hvis der opstår en konflikt, viser `git status`, hvilke filer der skal løses.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Løs en konflikt</h1>

Se på begge ændringer, aftal hvad der skal beholdes, og ret filen.

```bash
git add validering.py
git status
git commit
git push
```

Vælg alle løste filer med `git add`, kontrollér resultatet, og afslut først med commit, når alle konflikter er løst.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: git -->

<h1 class="slide_heaader">Git-flowet i praksis</h1>

1. Opdatér main, og opret en branch
2. Ændr kode, gennemgå ændringer, og commit
3. Push branchen, og opret en pull request
4. Gennemgå ændringerne, løs eventuelle konflikter, og merge

```bash
git status
```

Brug `git status` undervejs, hvis du er i tvivl om, hvor du er.

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:270px;left:75px;right:75px;font-size:60px;">Python-struktur<br>og refactoring</h1>

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Udgangspunktet: et script, der virker</h1>

```python
import csv

rows = []
with open("C:/data/adresser.csv", encoding="utf-8") as f:
    for r in csv.reader(f, delimiter=";"):
        pn = r[2].strip().zfill(4)
        if len(pn) == 4 and pn.isdigit():
            rows.append([r[0], r[1], pn])
        else:
            print("Fejl:", r)
with open("C:/data/resultat.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f, delimiter=";").writerows(rows)
```

Det virker – men hvad sker der, når det skal ændres?

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Hvad gør det svært?</h1>

* Alt ligger i **én blok** – læsning, regler og skrivning er blandet
* **Hårdkodede** stier og kolonnenumre
* Korte navne som `r`, `pn` og `f`
* Reglerne kan **ikke genbruges** i andre jobs
* Reglerne kan **ikke testes** uden at læse og skrive filer

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Én funktion – én opgave</h1>

```python
def laes_raekker(sti: str) -> list[list[str]]: ...


def rens_postnummer(vaerdi: str) -> str: ...


def er_gyldigt_postnummer(vaerdi: str) -> bool: ...


def skriv_raekker(sti: str, raekker: list[list[str]]) -> None: ...
```

Navnet fortæller, hvad funktionen gør. Kan det ikke beskrives kort, gør den måske for meget.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Argumenter og returværdier</h1>

```python
# Svært at følge: funktionen ændrer en global liste
gyldige = []

def behandl(raekke):
    if er_gyldig(raekke):
        gyldige.append(raekke)


# Tydeligt: input ind, output ud
def find_gyldige(raekker: list[list[str]]) -> list[list[str]]:
    return [r for r in raekker if er_gyldig(r)]
```

Alt, funktionen bruger, kommer ind som argumenter. Resultatet returneres.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Adskil regler og sideeffekter</h1>

<div class="git-flow">
  <div class="git-step">Læs fil<br><em>sideeffekt</em></div>
  <div>→</div>
  <div class="git-step">Rens og valider<br><em>rene regler</em></div>
  <div>→</div>
  <div class="git-step">Skriv fil<br><em>sideeffekt</em></div>
</div>

* **Sideeffekter:** filer, databaser, netværk, print og logging
* Hold reglerne fri for sideeffekter – så kan de testes og genbruges
* Læg læsning og skrivning i kanten af programmet

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Navne og konstanter</h1>

```python
SEPARATOR = ";"
POSTNUMMER_KOLONNE = 2

postnummer = raekke[POSTNUMMER_KOLONNE]   # frem for: pn = r[2]
```

* Beskrivende navne – også selvom de bliver længere
* Konstanter med STORE BOGSTAVER samlet ét sted
* Type hints viser, hvad der forventes ind og ud

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Del koden op i moduler</h1>

```text
adresse_job/
├── config.py        # stier og konstanter
├── filer.py         # læs og skriv filer
├── validering.py    # regler for data
└── main.py          # binder det hele sammen
```

```python
from validering import er_gyldig, rens_raekke
```

Et **modul** er en `.py`-fil. Det, der ændres af samme grund, ligger sammen.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Projektstruktur – overordnet</h1>

```text
project/
├── README.md          # hvad er det, og hvordan køres det?
├── pyproject.toml     # projektets navn og afhængigheder
├── src/
│   └── adresse_job/   # selve koden – en package
│       ├── __init__.py
│       └── ...
└── tests/             # tests holdes adskilt fra koden
```

Principperne er vigtigere end den præcise struktur.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Refactoring i små skridt</h1>

**Refactoring** = at ændre strukturen uden at ændre, hvad koden gør.

<div class="git-flow">
  <div class="git-step">Lille ændring</div>
  <div>→</div>
  <div class="git-step">Kør koden<br>og tests</div>
  <div>→</div>
  <div class="git-step">Samme resultat?<br>Commit</div>
  <div>→</div>
  <div class="git-step">Næste<br>ændring</div>
</div>

Små skridt gør det let at finde fejlen – og at gå tilbage.

---
<!-- backgroundColor: #b8063b -->
<!-- _class: code -->

<h1 class="slide_heaader">Øvelse: refaktorér scriptet</h1>

To og to (25 min.) – med det udleverede script:

1. Opret en branch: `git switch -c refactoring`
2. Flyt stier og kolonnenumre op som konstanter
3. Udtræk funktioner til læsning, rensning, validering og skrivning
4. Har I tid: del koden op i moduler
5. Kør scriptet og commit efter hvert skridt

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Forslag til løsning: main.py</h1>

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

`main` læses nu som en opskrift. Detaljerne ligger i modulerne.

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:60px;">OOP: class eller funktion?</h1>

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Ikke alt skal være en class</h1>

* Målet er **læsbar og vedligeholdelig kode** – ikke OOP for OOP's skyld
* Funktioner er ofte den enkleste løsning
* En class giver værdi, når **data og adfærd hører sammen**

Spørgsmålet er: *Hvad gør koden lettest at forstå for den næste?*

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Funktioner er ofte nok</h1>

```python
def rens_postnummer(vaerdi: str) -> str:
    return vaerdi.strip().zfill(4)


def er_gyldigt_postnummer(vaerdi: str) -> bool:
    return len(vaerdi) == 4 and vaerdi.isdigit()
```

Input ind, output ud – ingen tilstand. Lette at teste og genbruge.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Hvad er en class?</h1>

```python
class CsvKilde:
    def __init__(self, sti: str, separator: str = ";"):
        self.sti = sti
        self.separator = separator

    def hent_raekker(self) -> list[list[str]]:
        with open(self.sti, encoding="utf-8") as fil:
            return [linje.rstrip("\n").split(self.separator) for linje in fil]


kilde = CsvKilde("adresser.csv")
raekker = kilde.hent_raekker()
```

**Class** = skabelon · **objekt** = en konkret instans · **self** = objektet selv

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Tegn på, at en class kan hjælpe</h1>

* De **samme argumenter** sendes rundt mellem mange funktioner
* Data og funktioner **hører tydeligt sammen**
* Der skal holdes styr på **tilstand** undervejs, fx en forbindelse eller en tæller
* Der er brug for **flere objekter** med hver sin opsætning

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Før: de samme argumenter igen og igen</h1>

```python
def hent_raekker(sti: str, separator: str, encoding: str) -> list[list[str]]: ...


def tael_raekker(sti: str, separator: str, encoding: str) -> int: ...


def valider_kolonner(
    sti: str, separator: str, encoding: str, kolonner: list[str]
) -> bool: ...
```

Hvert kald skal have den samme opsætning med – og den skal holdes ens.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Efter: opsætningen samlet ét sted</h1>

```python
class CsvKilde:
    def __init__(self, sti: str, separator: str = ";", encoding: str = "utf-8"):
        self.sti = sti
        self.separator = separator
        self.encoding = encoding

    def hent_raekker(self) -> list[list[str]]: ...
    def tael_raekker(self) -> int: ...
    def valider_kolonner(self, kolonner: list[str]) -> bool: ...


kilde = CsvKilde("adresser.csv")
```

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Dataclasses til strukturerede data</h1>

```python
from dataclasses import dataclass


@dataclass
class Adresse:
    vejnavn: str
    husnummer: str
    postnummer: str


adresse = Adresse("Søndergade", "12", "8000")
print(adresse.postnummer)
```

Navngivne felter og type hints – frem for en løs `dict`.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Composition frem for arv</h1>

```python
class Job:
    def __init__(self, kilde: CsvKilde, validator: Validator):
        self.kilde = kilde
        self.validator = validator

    def koer(self) -> list[list[str]]:
        return [r for r in self.kilde.hent_raekker() if self.validator.er_gyldig(r)]
```

Et job **har** en kilde og en validator. Delene kan udskiftes og testes hver for sig. Brug arv sparsomt.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Faresignal: en class, der burde være en funktion</h1>

```python
class PostnummerRenser:
    def __init__(self, vaerdi: str):
        self.vaerdi = vaerdi

    def rens(self) -> str:
        return self.vaerdi.strip().zfill(4)


PostnummerRenser(" 800").rens()   # Samme som: rens_postnummer(" 800")
```

Kun `__init__` og én metode? Så er det ofte bare en funktion.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Tommelfingerregel</h1>

| Situation | Vælg |
| --- | --- |
| Input ind, output ud – ingen tilstand | **Funktion** |
| Data med faste felter | **Dataclass** |
| Data og adfærd, der hører sammen | **Class** |
| Genbrug af dele | **Composition** frem for arv |

Start enkelt – lav en class, når koden beder om det.

---
<!-- backgroundColor: #b8063b -->
<!-- _class: code -->

<h1 class="slide_heaader">Øvelse: class eller funktion?</h1>

Diskutér to og to (10 min.): Hvad ville I vælge – og hvorfor?

1. Omregning af koordinater fra én projektion til en anden
2. En databaseforbindelse, som flere trin i et job bruger
3. En række med `id`, `navn` og `dato`, der sendes mellem trin
4. Fem funktioner, der alle tager `sti`, `separator` og `encoding`

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Forslag til løsning</h1>

1. **Funktion** – input ind, output ud
2. **Class** – forbindelsen er tilstand, som deles og skal lukkes igen
3. **Dataclass** – data med faste felter
4. **Class** – opsætningen samles ét sted

Der er ikke ét rigtigt svar – begrundelsen er det vigtigste.

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:60px;">Tests</h1>

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Hvorfor tests?</h1>

* Viser, at koden gør det, vi **forventer**
* Fanger **utilsigtede ændringer**, når koden refaktoreres
* **Dokumenterer** den forventede adfærd med eksempler
* Gør det trygt at ændre kode, som andre har skrevet

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">En test er bare en funktion</h1>

```python
# tests/test_validering.py
from validering import rens_postnummer


def test_rens_postnummer_tilfoejer_nul():
    assert rens_postnummer(" 800") == "0800"
```

* Filen og funktionen starter med `test_`
* `assert` tjekker, at resultatet er det forventede

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Kør tests med pytest</h1>

```bash
pip install pytest
python -m pytest
```

```text
..                                                    [100%]
2 passed in 0.15s
```

Kør fra projektets rodmappe. Hvert punktum er en test, der bestod.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Når en test fejler</h1>

```text
    def test_rens_postnummer_tilfoejer_nul():
>       assert rens_postnummer(" 800") == "0800"
E       AssertionError: assert '800' == '0800'

tests\test_validering.py:5: AssertionError
FAILED tests/test_validering.py::test_rens_postnummer_tilfoejer_nul
1 failed, 1 passed in 0.45s
```

Hvilken test? Hvad forventede vi? Hvad fik vi? Fejlen kan være i koden – eller i testen.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Hvad skal man teste?</h1>

```python
def test_er_gyldigt_postnummer():
    assert er_gyldigt_postnummer("8000")
    assert not er_gyldigt_postnummer("800")
    assert not er_gyldigt_postnummer("80a0")
    assert not er_gyldigt_postnummer("")
```

* Funktioner med **regler og logik**
* Det **normale** tilfælde – og **kanttilfælde** som tomme eller forkerte værdier
* Fejl, der er fundet før, så de ikke kommer igen

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Unit- og integrationstests</h1>

<div class="columns">
<div>

**Unit test**
* Tester én funktion isoleret
* Hurtig og præcis
* Lettest med rene funktioner

</div>
<div>

**Integrationstest**
* Tester flere dele sammen
* Fx læs fil → rens → skriv fil
* Langsommere, men tættere på virkeligheden

</div>
</div>

Start med unit tests af reglerne.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Tests og refactoring</h1>

<div class="git-flow">
  <div class="git-step">Tests består</div>
  <div>→</div>
  <div class="git-step">Refaktorér</div>
  <div>→</div>
  <div class="git-step">Tests består<br>stadig</div>
  <div>→</div>
  <div class="git-step">Commit</div>
</div>

Består testene både før og efter, har vi ikke ændret det, de tester.

Funktioner uden sideeffekter er de letteste at teste.

---
<!-- backgroundColor: #b8063b -->
<!-- _class: code -->

<h1 class="slide_heaader">Øvelse: skriv jeres første tests</h1>

To og to (20 min.) – i jeres refaktorerede projekt:

1. Opret `tests/test_validering.py`
2. Skriv tests for `rens_postnummer` og `er_gyldigt_postnummer`
3. Kør `python -m pytest`
4. Lav bevidst en fejl i en funktion – se testen fejle – ret den igen
5. Commit testene

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Forslag til løsning</h1>

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

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:250px;left:75px;right:75px;font-size:60px;">Afvikling i ETL<br>og fejlfinding i VS Code</h1>

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Python i et ETL-værktøj</h1>

<div class="git-flow">
  <div class="git-step">ETL-værktøj</div>
  <div>→</div>
  <div class="git-step">starter et script<br><em>eller</em><br>kalder en funktion</div>
  <div>→</div>
  <div class="git-step">vores moduler</div>
</div>

* Koden kaldes af et andet program – ikke af os
* Den skal virke, uanset **hvem** og **hvorfra** den kaldes
* Fejl skal kunne ses i værktøjets log

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Ét tydeligt entry point</h1>

```python
def main() -> None:
    ...


if __name__ == "__main__":
    main()
```

* Kode på modulniveau køres, så snart modulet **importeres**
* `if __name__ == "__main__"` kører kun, når filen **startes direkte**
* Så kan modulet både køres og importeres uden overraskelser

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Undgå antagelser om afviklingen</h1>

```python
from pathlib import Path

DATA_MAPPE = Path(__file__).parent / "data"
INPUT_STI = DATA_MAPPE / "adresser.csv"
```

* **Arbejdsmappen** kan være en anden – brug ikke bare `"adresser.csv"`
* **Python-miljøet** kan være et andet – samme version og pakker?
* Der er **ingen bruger** til at se `print` eller svare på `input()`

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Hvad er offentligt i et modul?</h1>

```python
def koer_job(input_sti: str, output_sti: str) -> int:
    """Kaldes af ETL-værktøjet. Returnerer antal skrevne rækker."""
    ...


def _fjern_tomme(raekker: list[list[str]]) -> list[list[str]]:
    ...
```

* Uden `_` = beregnet til at blive brugt udefra
* Med `_` = intern hjælpefunktion, som kan ændres frit
* Hold den offentlige del **lille og stabil** – jobs afhænger af den

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Logging frem for print</h1>

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Læste %d rækker", len(raekker))
logger.warning("Ugyldigt postnummer: %s", raekke)
```

* Niveauer: `debug`, `info`, `warning`, `error`
* Værktøjets log kan opsamle og filtrere beskederne
* Opsætningen af logging sker ét sted – i entry pointet

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Fejl skal være synlige</h1>

```python
try:
    raekker = laes_raekker(sti)
except FileNotFoundError:
    logger.error("Inputfil findes ikke: %s", sti)
    raise
```

* Fang kun de fejl, du kan håndtere – og log dem
* Undgå `except:` med `pass`, som skjuler alle fejl
* Et job, der fejler tydeligt, er bedre end forkerte data i stilhed

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">VS Code: det rigtige Python-miljø</h1>

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pytest
```

* Ét **virtuelt miljø** pr. projekt med de pakker, projektet bruger
* Vælg miljøet i VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter**
* Brug samme Python-version som ETL-værktøjet, hvis muligt

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Debuggeren i VS Code</h1>

<!-- TODO: Indsæt skærmbillede af VS Code under debugging -->

| Handling | Genvej |
| --- | --- |
| Sæt et breakpoint | Klik i margenen eller `F9` |
| Start debugging | `F5` |
| Næste linje | `F10` |
| Gå ind i funktionen | `F11` |
| Fortsæt | `F5` |

Panelerne **Variables** og **Call Stack** viser værdier og vejen til linjen.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Debug koden, som værktøjet kører den</h1>

```json
{
  "name": "Kør som ETL-job",
  "type": "debugpy",
  "request": "launch",
  "program": "${workspaceFolder}/main.py",
  "cwd": "C:/etl/arbejdsmappe",
  "env": { "MILJOE": "test" }
}
```

Tilføjes under `configurations` i `.vscode/launch.json`. Arbejdsmappe og miljøvariabler sættes som i ETL-værktøjet.

---
<!-- backgroundColor: #b8063b -->
<!-- _class: code -->

<h1 class="slide_heaader">Øvelse: find fejlen med debuggeren</h1>

To og to (15 min.) – med det udleverede script, som giver et forkert resultat:

1. Sæt et breakpoint, og start med `F5`
2. Gå linje for linje, og følg værdierne i **Variables**
3. Find og ret fejlen
4. Skriv en test, der havde fanget den, og kør `python -m pytest`
5. Commit rettelsen og testen

---
<!-- backgroundColor: #397c67 -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:60px;">Samlet praktisk øvelse</h1>

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Adresse-jobbet i produktion</h1>

I er et team på to, der vedligeholder adresse-jobbet. Opgaverne kommer som opgavesedler.

| Tid | Person A | Person B |
| --- | --- | --- |
| 0–10 min. | Kom i gang | Kom i gang |
| 10–40 min. | Opgave 1: fejl i postnumre | Opgave 2: gør jobbet ETL-klar |
| 40–70 min. | Opgave 3: ny regel for vejnavn | Opgave 4: Adresse-dataclass |
| 70–90 min. | Overraskelse og opsamling | |

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Kom i gang</h1>

1. Klon holdets repository: `Ctrl+Shift+P` → **Git: Clone** → adressen fra Bitbucket
2. Opret miljøet og kør projektet i terminalen:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python main.py
```

3. Vælg `.venv` med **Python: Select Interpreter**, og aftal, hvem der er A og B

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Arbejdsgangen for hver opgave</h1>

<div class="small">

| Trin | I VS Code | I terminalen |
| --- | --- | --- |
| Hent nyeste main | Skift til `main` → **Sync Changes** | `git switch main` · `git pull` |
| Opret branch | Branch-navnet nederst → **Create new branch** | `git switch -c navn` |
| Commit | **Source Control** → `+` → besked → **Commit** | `git add` · `git commit` |
| Del branchen | **Publish Branch** | `git push -u origin navn` |
| Pull request | Opret på Bitbucket mod `main` med makkeren som reviewer | |

</div>

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Review i Bitbucket</h1>

* Gør ændringen det, opgavesedlen beder om?
* Er koden til at forstå – navne, struktur, ansvar?
* Er der tests, og består de?
* Kommentér **konkret og venligt** – det handler om koden, ikke personen
* Godkend med **Approve**, og merge med **Merge commit**

---
<!-- backgroundColor: #b8063b -->
<!-- _class: code -->

<h1 class="slide_heaader">Runde 1 · 30 min.</h1>

<div class="columns">
<div>

**Person A – opgave 1**
Fejlrapport: postnumre med mellemrum bliver afvist

*Debugger · tests først*

</div>
<div>

**Person B – opgave 2**
Gør jobbet klar til ETL-værktøjet

*Entry point · logging · fejl*

</div>
</div>

Opgavesedlerne ligger i `opgaver/`. Opret PR, og review hinandens ændringer.

---
<!-- backgroundColor: #b8063b -->
<!-- _class: code -->

<h1 class="slide_heaader">Runde 2 · 30 min.</h1>

<div class="columns">
<div>

**Person A – opgave 3**
Ny regel: vejnavn må ikke være tomt

*Struktur · tests*

</div>
<div>

**Person B – opgave 4**
Indfør en `Adresse`-dataclass

*OOP · struktur*

</div>
</div>

Start fra en **opdateret main**. I ændrer i de samme filer – den, der merger sidst, får en konflikt.

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Konflikt? Sådan gør I</h1>

1. Hent den nyeste main ind i jeres branch:

```bash
git fetch origin
git merge origin/main
```

2. Åbn hver fil med konflikt → **Resolve in Merge Editor**
3. Kombinér ændringerne – ofte er **ingen af siderne rigtig alene**
4. Kør `python -m pytest` – **før** I afslutter
5. **Complete Merge** → **Commit** → **Sync Changes**

---
<!-- backgroundColor: #b8063b -->
<!-- _class: code -->

<h1 class="slide_heaader">Ups! · 10 min.</h1>

Leverandøren meddeler, at adressefilerne fremover bliver **kommaseparerede**.

1. Person A ændrer `SEPARATOR` til `","` – PR, review og merge
2. Hent main, og kør `python main.py`. Hvad sker der?
3. Person B fortryder ændringen med en **revert** – se opgaveseddel 5

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Opsamling på øvelsen</h1>

```bash
git log --oneline --graph
```

* Hvad var svært ved konflikten – og hvordan løste I den?
* Hvad fangede jeres review?
* Hvad fangede testene – og hvad fangede de **ikke**?
* Hvad ville I gøre anderledes i jeres egen kode?

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:60px;">Opsamling og spørgsmål</h1>

---
<!-- backgroundColor: #2e495c -->
<!-- _class: code -->

<h1 class="slide_heaader">Dagens vigtigste pointer</h1>

* Arbejd på en **branch**, og få ændringer ind via en **pull request**
* **Små funktioner** med ét ansvar – adskil regler og sideeffekter
* **Funktion** først – **class**, når data og adfærd hører sammen
* **Tests** gør det trygt at ændre koden
* Ét tydeligt **entry point**, **logging** og **synlige fejl**

Spørgsmål?