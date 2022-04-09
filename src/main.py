from ristinolla import Ristinolla
from alphabeta import Alphabeta

def main():
    ristinolla = Ristinolla()
    ristinolla.lisaa_reunat_lautaan()
    botti = Alphabeta()
    ristinolla.maksin_vuoro = False
    ristinolla.lisaa_merkki((1,3))
    ristinolla.vaihda_vuoro()
    ristinolla.tulosta_pelitilanne()
    while True:
        seuraava_siirto = botti.minimax_ab(ristinolla, 3, -100, 100)[1]
        ristinolla.lisaa_merkki(seuraava_siirto)
        ristinolla.tulosta_pelitilanne()
        if ristinolla.tarkista_voitto() == 'X' or ristinolla.tarkista_voitto == '0' or ristinolla.tarkista_voitto == 'tasapeli':
            break
        ristinolla.vaihda_vuoro()
    print('Peli loppui. Tittidii.')

if __name__ == "__main__":
    main()
