# Git-guide: Dit eget repo med øvelserne

Denne guide er til dig, der vil have din kode på flere computere (fx en stationær derhjemme og en bærbar på skolen).

Når du er færdig, har du to "remotes" (forbindelser til GitHub):

| Navn | Hvad er det? | Hvad bruger du det til? |
|---|---|---|
| `upstream` | Undervisernes repo (`atal-eaaa/teknologi_data_integration`) | Hente nye øvelser hver uge |
| `origin` | **Dit eget** repo på GitHub | Gemme din egen kode, så du kan hente den på andre computere |

> Du kan kun **hente** fra `upstream`. Du kan **hente og gemme** i `origin`.

---

## Del 1: Opsætning (én gang)

### Trin 1: Lav en GitHub-konto

Gå til [github.com](https://github.com) og opret en konto, hvis du ikke har en.

### Trin 2: Opret et nyt, tomt repo på GitHub

1. Klik på **+** øverst til højre → **New repository**.
2. **Repository name:** `teknologi_data_integration`
3. Vælg **Private** (så andre ikke kan se din kode).
4. **Sæt IKKE flueben** i "Add a README file", ".gitignore" eller "license". Repoet skal være helt tomt.
5. Klik **Create repository**.
6. Kopier adressen på siden. Den ligner: `https://github.com/DIT-BRUGERNAVN/teknologi_data_integration.git`

### Trin 3: Åbn en terminal i din øvelsesmappe

Åbn mappen `teknologi_data_integration` (den du klonede i starten af kurset) i VS Code, og vælg **Terminal → New Terminal**.

Tjek at du er det rigtige sted:

```bash
git remote -v
```

Du skal se `https://github.com/atal-eaaa/teknologi_data_integration.git`.

### Trin 4: Fortæl git hvem du er

Brug dit navn og den e-mail, du har brugt på GitHub:

```bash
git config --global user.name "Dit Navn"
git config --global user.email "din@email.dk"
git config --global pull.rebase false
```

(Den sidste linje sørger for, at `git pull` altid fletter ændringer sammen på samme måde.)

### Trin 5: Omdøb undervisernes repo til `upstream`

```bash
git remote rename origin upstream
```

### Trin 6: Tilføj dit eget repo som `origin`

Indsæt den adresse, du kopierede i trin 2:

```bash
git remote add origin https://github.com/DIT-BRUGERNAVN/teknologi_data_integration.git
```

Tjek resultatet:

```bash
git remote -v
```

Du skal nu se både `origin` (dit repo) og `upstream` (undervisernes repo).

### Trin 7: Gem (commit) din egen kode

```bash
git add .
git commit -m "Min kode indtil nu"
```

### Trin 8: Send det hele op til dit eget repo

```bash
git push -u origin main
```

Første gang åbner der et vindue, hvor du logger ind på GitHub. Genindlæs dit repo på GitHub bagefter, så kan du se dine filer.

**Opsætningen er færdig!**

---

## Del 2: Hver uge – hent nye øvelser

Gem først din egen kode, hent så de nye øvelser, og send det hele op til dit eget repo:

```bash
git add .
git commit -m "Min kode fra ugen"
git pull --no-edit upstream main
git push
```

> **Bemærk:** Du skal nu skrive `git pull upstream main` for at hente nye øvelser. Et almindeligt `git pull` henter kun fra dit eget repo.

---

## Del 3: Gem dit arbejde

Når du er færdig med at arbejde:

```bash
git add .
git commit -m "Kort beskrivelse af hvad du har lavet"
git push
```

---

## Del 4: Brug en anden computer

### Første gang på den nye computer

Klon **dit eget** repo (ikke undervisernes), og tilføj undervisernes repo som `upstream`:

```bash
git clone https://github.com/DIT-BRUGERNAVN/teknologi_data_integration.git
cd teknologi_data_integration
git remote add upstream https://github.com/atal-eaaa/teknologi_data_integration.git
```

Husk også trin 4 (`git config ...`) på den nye computer.

### Når du skifter computer

- **Når du starter:** `git pull` (henter din egen seneste kode)
- **Når du stopper:** `git add .`, `git commit -m "..."`, `git push`

Hvis du glemmer at pushe på den ene computer, har du ikke din nyeste kode på den anden.

---

## Hvis noget går galt

| Fejlbesked | Hvad betyder det? | Løsning |
|---|---|---|
| `Updates were rejected because the remote contains work that you do not have locally` | Der ligger nyere kode i dit repo (fx fra din anden computer) | Kør `git pull` og derefter `git push` igen |
| `Please commit your changes or stash them before you merge` | Du har ændringer, der ikke er gemt | Kør `git add .` og `git commit -m "..."` først, og prøv igen |
| `CONFLICT (content): Merge conflict in ...` | Samme fil er ændret to steder | Åbn filen i VS Code, vælg hvilken version du vil beholde, og kør `git add .` og `git commit -m "Løst konflikt"` |
| `fatal: 'upstream' does not appear to be a git repository` | `upstream` er ikke sat op på denne computer | Kør `git remote add upstream https://github.com/atal-eaaa/teknologi_data_integration.git` |
| Der åbner en mærkelig teksteditor i terminalen | Git vil have en besked til en sammenfletning | Skriv `:wq` og tryk Enter |

**Tip:** Ret ikke i filerne i roden af repoet (`README.md`, `Pipfile`, `Pipfile.lock`, `check_git.py`, `check_python_installation.py`) eller i mappen `vejledninger_read_only`. Hvis underviserne opdaterer dem, giver det konflikter.
