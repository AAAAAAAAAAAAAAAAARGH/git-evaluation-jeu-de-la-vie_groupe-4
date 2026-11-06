import argparse
import random
import sys

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
    # À compléter par Marc
    pass


def random_grid(nb_cells, seed):
    """Renvoie une grille carrée aléatoire de 0 et de 1 (nb_cells x nb_cells).

    Utiliser random.Random(seed) pour que la grille soit toujours la même
    pour une même graine.
    """
    # À compléter par Hugo
    pass


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
    # À compléter par Amour (bords fixes) et Hugo (bords périodiques)
    pass


def next_generation(grid, periodic):
    """Renvoie une NOUVELLE grille correspondant à la génération suivante.

    La grille reçue ne doit pas être modifiée.
    """
    # À compléter par Amour
    pass


def write_text(grid, iteration):
    """Affiche sur STDOUT "iteration: N" puis les lignes de la grille."""
    # À compléter par Yann
    pass


def write_image(grid, iteration, output_directory):
    """Écrit la grille dans output_directory/grid_XXXX.png avec write_grid.

    Créer le dossier s'il n'existe pas.
    """
    # À compléter par Yann
    pass


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