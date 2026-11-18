# Jeu de la vie — Groupe 4

Simulation du jeu de la vie de Conway en Python. Le programme génère une grille aléatoire ou lit une grille sur l'entrée standard, puis calcule son évolution avec des conditions aux limites fixes ou périodiques.

## Installation

Le programme utilise uniquement **Python 3** et sa bibliothèque standard. Les vidéos nécessitent **ffmpeg** et **Gource**.

### Ubuntu / Debian (ou WSL sous Windows)

```bash
sudo apt update
sudo apt install python3 git ffmpeg gource
```

### macOS

```bash
brew install python3 ffmpeg gource
```

### Windows

Installer WSL depuis un PowerShell ouvert en administrateur, puis suivre la procédure Ubuntu dans le terminal WSL :

```powershell
wsl --install
```

### Récupérer le projet

```bash
git clone https://github.com/AAAAAAAAAAAAAAAAARGH/git-evaluation-jeu-de-la-vie_groupe-4.git
cd git-evaluation-jeu-de-la-vie_groupe-4
```

## Exécution

Toutes les commandes se lancent depuis la racine du dépôt.

### Sans option (grille aléatoire, 21 images)

```bash
$ python3 main.py
Generation of 21 images in directory outputs
```

### Grille de 50 cellules, graine 4200, 201 images

```bash
$ python3 main.py -n 50 -m 200 -s 4200
Generation of 201 images in directory outputs
```

### Lire une grille sur l'entrée standard (bords fixes)

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -t text
iteration: 1
0 1 0
0 0 1
0 1 0
```

### Même grille avec bords périodiques

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text
iteration: 1
0 0 0
0 0 0
0 0 0
```

### Format d'une grille en entrée

La première ligne contient la taille N, suivie de N lignes de N cellules (0 ou 1) séparées par des espaces :

```text
3
1 0 1
0 0 1
1 0 1
```

## Arguments

| Option courte | Option longue | Description | Valeur par défaut |
|---|---|---|---|
| `-n N` | `--nb_cells N` | nombre de cellules par côté pour une grille aléatoire (entier > 0) | `10` |
| `-m N` | `--max_iterations N` | numéro de la dernière itération à calculer (entier ≥ 0) | `20` |
| `-s N` | `--seed N` | graine du générateur aléatoire (entier quelconque) | `42` |
| `-o DOSSIER` | `--output_directory DOSSIER` | dossier dans lequel écrire les images | `outputs` |
| `-t TYPE` | `--output_type TYPE` | type de sortie : `image` ou `text` | `image` |
| `-p` | `--periodic` | active les conditions aux limites périodiques | désactivée |
| `-h` | `--help` | affiche l'aide du programme | — |

Avec `-m N`, le programme calcule N + 1 générations (de 0 à N). En sortie `image`, il écrit un fichier `grid_XXXX.png` par génération. En sortie `text`, il affiche uniquement la dernière génération.

## Vidéos

_À compléter (Yann)_

## Intégration continue

![Tests](https://github.com/AAAAAAAAAAAAAAAAARGH/git-evaluation-jeu-de-la-vie_groupe-4/actions/workflows/tests.yml/badge.svg)

À chaque push et à chaque Pull Request, GitHub Actions lance automatiquement `sh check_script_options.sh` et `sh check_tests.sh` sur Ubuntu avec Python 3 (workflow `.github/workflows/tests.yml`). Si l'un des scripts échoue, le workflow est marqué en échec.

Exécution réussie des deux scripts : [voir sur GitHub Actions](https://github.com/AAAAAAAAAAAAAAAAARGH/git-evaluation-jeu-de-la-vie_groupe-4/actions/runs/43838971050)

## Auteurs

| Nom | Prénom | Numéro étudiant |
|---|---|---|
| CADIL | Yann | 45002501 |
| GRONDIN | Morgan | 45004032 |
| HOAREAU | Hugo | 45006141 |
| OKPEICHA | Kolawole Amour Dieudonne | 45005731 |
| RAYBAUD | Marc | 45002016 |

## Liens utiles

_À compléter (Morgan)_