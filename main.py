import argparse
import random
import sys
import os

from lib import write_grid


def error(message):
    """Affiche un message sur STDERR et arrête le programme avec le code 1."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def parse_args():
    """Lit les options de la ligne de commande et renvoie le résultat d'argparse.

    Options : -n/--nb_cells, -m/--max_iterations, -s/--seed,
    -o/--output_directory, -t/--output_type, -p/--periodic (et -h/--help).
    Vérifier que nb_cells > 0 et max_iterations >= 0.
    """
    parser = argparse.ArgumentParser(description="Jeu de la vie de Conway")

    parser.add_argument("-n", "--nb_cells", type=int, default=10,
                        help="nombre de cellules par côté pour une grille aléatoire (défaut : 10)")
    parser.add_argument("-m", "--max_iterations", type=int, default=20,
                        help="numéro de la dernière itération à calculer (défaut : 20)")
    parser.add_argument("-s", "--seed", type=int, default=42,
                        help="graine du générateur aléatoire (défaut : 42)")
    parser.add_argument("-o", "--output_directory", default="outputs",
                        help="dossier dans lequel écrire les images (défaut : outputs)")
    parser.add_argument("-t", "--output_type", choices=["image", "text"], default="image",
                        help="type de sortie : image ou text (défaut : image)")
    parser.add_argument("-p", "--periodic", action="store_true",
                        help="active les conditions aux limites périodiques")

    args = parser.parse_args()

    if args.nb_cells <= 0:
        parser.error("--nb_cells doit être un entier strictement positif")
    if args.max_iterations < 0:
        parser.error("--max_iterations doit être un entier positif ou nul")

    return args


def random_grid(nb_cells, seed):
    """Renvoie une grille carrée aléatoire de 0 et de 1 (nb_cells x nb_cells).

    Utiliser random.Random(seed) pour que la grille soit toujours la même
    pour une même graine.
    """
    rng = random.Random(seed)
    grid = []
    for i in range(nb_cells):
        line = []
        for j in range(nb_cells):
            line.append(rng.choice([0, 1]))
        grid.append(line)
    return grid


def read_grid(text):
    """Transforme le texte lu sur STDIN en grille (liste de listes d'entiers).

    Première ligne : la taille N. Puis N lignes de N cellules (0 ou 1)
    séparées par des espaces. En cas de problème, appeler error(...).
    """
    # À compléter par Morgan
    pass


def count_neighbors(grid, row, col, periodic):
    """Renvoie le nombre de voisines vivantes de la cellule (row, col).

    Bords fixes : ce qui est hors de la grille est mort.
    Bords périodiques : on revient de l'autre côté (modulo la taille).
    """
    size = len(grid)
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r = row + dr
            c = col + dc
            if periodic:
                # on revient de l'autre côté de la grille
                r = r % size
                c = c % size
                count = count + grid[r][c]
            elif r >= 0 and r < size and c >= 0 and c < size:
                count = count + grid[r][c]
    return count


def next_generation(grid, periodic):
    """Renvoie une NOUVELLE grille correspondant à la génération suivante.

    La grille reçue ne doit pas être modifiée.
    """
    # À compléter par Amour
    pass


def write_text(grid, iteration):
    """Affiche sur STDOUT "iteration: N" puis les lignes de la grille."""
    print(f"iteration: {iteration}")
    for line in grid:
        values = []
        for cell in line:
            values.append(str(cell))
        print(" ".join(values))


def write_image(grid, iteration, output_directory):
    """Écrit la grille dans output_directory/grid_XXXX.png avec write_grid.

    Créer le dossier s'il n'existe pas.
    """
    os.makedirs(output_directory, exist_ok=True)
    filename = f"{output_directory}/grid_{iteration:04d}.png"

    # write_grid demande une image d'au moins 2 * taille + 1 pixels
    size = 540
    if 2 * len(grid) + 1 > size:
        size = 2 * len(grid) + 1

    write_grid(grid, filename, size)


def main():
    args = parse_args()

    # Grille initiale : lue sur STDIN si on reçoit quelque chose, sinon aléatoire
    if sys.stdin.isatty():
        grid = random_grid(args.nb_cells, args.seed)
    else:
        grid = read_grid(sys.stdin.read())

    if args.output_type == "image":
        write_image(grid, 0, args.output_directory)
        for iteration in range(1, args.max_iterations + 1):
            grid = next_generation(grid, args.periodic)
            write_image(grid, iteration, args.output_directory)
        nb_images = args.max_iterations + 1
        print(f"Generation of {nb_images} images in directory {args.output_directory}")
    else:
        for iteration in range(1, args.max_iterations + 1):
            grid = next_generation(grid, args.periodic)
        write_text(grid, args.max_iterations)


if __name__ == "__main__":
    main()