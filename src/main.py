from ristinolla import Ristinolla
from alphabeta import AlphaBeta
from pelilooppi import Pelilooppi


def main():
    ristinolla = Ristinolla()
    ristinolla.lisaa_reunat_lautaan()
    botti = AlphaBeta()
    peli = Pelilooppi(ristinolla, botti)
    peli.aloita_peli()


if __name__ == "__main__":
    main()
