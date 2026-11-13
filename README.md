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

À compléter (Amour)

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

À compléter (Yann)

## Intégration continue

À compléter (Hugo)

## Auteurs

À compléter (Morgan)

## Liens utiles

À compléter (Morgan)