import unittest
from alphabeta import AlphaBeta
from ristinolla import Ristinolla

class TestAlphaBeta(unittest.TestCase):
    def setUp(self):
        self.botti = AlphaBeta()
        self.ristinolla = Ristinolla()
        self.siirrot = set()
        self.ristinolla.lisaa_reunat_lautaan()
        self.ristinolla.pelilauta[1][7] = '0'
        self.ristinolla.paivita_seuraavat_siirrot((1,7), self.siirrot)
        self.ristinolla.pelilauta[2][7] = '0'
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((2,7), self.siirrot)
        self.ristinolla.paivita_seuraavat_siirrot((2,7), self.siirrot)
        self.ristinolla.pelilauta[3][7] = '0'
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((3,7), self.siirrot)
        self.ristinolla.paivita_seuraavat_siirrot((3,7), self.siirrot)
        self.ristinolla.pelilauta[4][7] = '0'
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((4,7), self.siirrot)
        self.ristinolla.paivita_seuraavat_siirrot((4,7), self.siirrot)


    #def test_minimax_ab(self):
    #    self.ristinolla.tulosta_pelitilanne()
    #    seuraava_siirto = self.botti.minimax_ab(self.ristinolla, 3, -100, 100, True, (4,7), self.siirrot)[1]
    #    print(seuraava_siirto)
    #    self.assertEqual(seuraava_siirto, (5,7))
