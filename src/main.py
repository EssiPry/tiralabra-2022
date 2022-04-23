from ristinolla import Ristinolla
from alphabeta import Alphabeta
from pelilooppi import Pelilooppi


def main():
    ristinolla = Ristinolla()
    botti = Alphabeta()
    peli = Pelilooppi(ristinolla, botti)
    peli.aloita_peli()


if __name__ == "__main__":
    main()
