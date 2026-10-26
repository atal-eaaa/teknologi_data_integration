# Typiske git-fejl

Til undervisere, der hjælper studerende med kun én remote (`origin` = undervisernes repo), som kun bruger `git clone` og `git pull`. Fejlbeskederne står på engelsk, fordi det er dem, de studerende ser.

**Første skridt ved ethvert problem:** bed den studerende køre `git status`. Den viser, hvilken mappe og branch de står i, og hvilke filer de har ændret, og den foreslår ofte selv løsningen.

| # | Det ser den studerende | Hvad er der sket? | Sådan løser du det |
|---|---|---|---|
| 1 | `fatal: not a git repository (or any of the parent directories)` | Terminalen står i den forkerte mappe. | Åbn repo-mappen i VS Code (File → Open Folder), eller `cd` ind i den. Mappenavne med mellemrum skal i anførselstegn: `cd "Lektion 6"`. |
| 2 | `error: Your local changes to the following files would be overwritten by merge:` efterfulgt af en liste med filer | Den studerende har rettet i en fil, som underviserne også har ændret. Det sker også, når en notebook er kørt og gemt, fordi outputtet gemmes i `.ipynb`-filen. | `git stash`, derefter `git pull`, derefter `git stash pop`. Hvis `stash pop` melder en konflikt, se række 6. |
| 3 | `error: The following untracked working tree files would be overwritten by merge:` | Den studerende har lavet en fil med samme navn som en, underviserne lige har tilføjet, fx sin egen `Lektion 6/opgave.py`. | Omdøb eller flyt den studerendes fil, og kør `git pull` igen. |
| 4 | `fatal: destination path '...' already exists and is not an empty directory` | De har kørt `git clone` en gang til. | De skal ikke klone igen. `cd` ind i den eksisterende mappe og kør `git pull`. |
| 5 | `Already up to date.`, men de nye øvelser mangler | Som regel har de to kopier af repoet og puller i den forkerte. Ellers er undervisernes PR ikke merget endnu. | Tjek med `git remote -v`, og se mappestien i VS Code. Tjek på GitHub, at PR'en er merget. |
| 6 | `CONFLICT (content): Merge conflict in <fil>` | De samme linjer er ændret både lokalt og i undervisernes repo. | Åbn filen i VS Code og vælg **Accept Current / Incoming / Both**. Gem, og kør så `git add .` og `git commit -m "Løst konflikt"`. For at opgive og gå tilbage: `git merge --abort`. |
| 7 | `fatal: Need to specify how to reconcile divergent branches` | Den studerende har kørt `git commit` lokalt (tit efter at have googlet), og der er også nye commits i undervisernes repo. | Kør `git config --global pull.rebase false` én gang, og derefter `git pull` igen. |
| 8 | En mærkelig editor åbner i terminalen med teksten `Merge branch 'main' of ...` | Det er Vim. Git vil have en besked til merge-committet (kommer efter række 7). | Skriv `:wq` og tryk Enter. |
| 9 | `Author identity unknown *** Please tell me who you are` | Git skal kende navn og e-mail for at lave et commit eller en merge. | `git config --global user.name "Navn"` og `git config --global user.email "mail@eaaa.dk"`, og gentag så kommandoen. |
| 10 | `git : The term 'git' is not recognized...` eller `'git' is not recognized as an internal or external command` | Git er ikke installeret, eller VS Code var åben, da Git blev installeret. | Installer Git, og **genstart VS Code** helt. `check_git.py` i repoet kan bekræfte, at det virker. |
| 11 | `remote: Permission to atal-eaaa/... denied` eller `403` efter `git push` | Studerende kan ikke pushe til undervisernes repo. Det er meningen. | Intet at løse. En studerende, der vil gemme sin kode online, skal følge `git_guide.md`. |
| 12 | En slettet fil kommer ikke tilbage efter `git pull` | Git ser sletningen som den studerendes egen ændring og beholder den. | `git restore "Lektion 6/filnavn.py"`, eller `git restore .` for at gendanne alle slettede og ændrede filer. **Advarsel:** det sletter også deres egne rettelser. |
| 13 | `fatal: unable to access 'https://github.com/...': Could not resolve host` | Ingen internetforbindelse, eller netværket blokerer GitHub. | Tjek wifi og prøv igen. |
| 14 | **Når intet andet virker** | Repoet er kommet i en tilstand, der er svær at rede ud. | 1. Omdøb den studerendes mappe, fx til `teknologi_data_integration_gammel`.<br>2. Kør `git clone` igen for at få en frisk kopi.<br>3. Kopier den studerendes egne filer tilbage fra den gamle mappe.<br>Det virker altid, og intet går tabt. |

## Tips

- De fleste af disse fejl kommer fra **række 2 og 3**, og begge starter, når underviserne ændrer en eksisterende fil eller tilføjer en, hvis navn en studerende allerede har brugt. Reglen om "aldrig at rette i tidligere mapper" forebygger de fleste af dem.
- Gits beskeder foreslår som regel selv, hvad man skal gøre. Det er en god idé at læse linjerne, der starter med `hint:`, sammen med den studerende.
