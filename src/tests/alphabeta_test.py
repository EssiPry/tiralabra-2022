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
        self.ristinolla.paivita_mahdolliset_siirrot((1,7), self.siirrot)
        self.ristinolla.pelilauta[2][7] = '0'
        self.siirrot.remove((2,7))
        self.ristinolla.paivita_mahdolliset_siirrot((2,7), self.siirrot)
        self.ristinolla.pelilauta[3][7] = '0'
        self.siirrot.remove((3,7))
        self.ristinolla.paivita_mahdolliset_siirrot((3,7), self.siirrot)
        self.ristinolla.pelilauta[4][7] = '0'
        self.siirrot.remove((4,7))
        self.ristinolla.paivita_mahdolliset_siirrot((4,7), self.siirrot)


    def test_minimax_ab(self):
        seuraava_siirto = self.botti.minimax_ab(self.ristinolla, 2, -100, 100, True, (4,7), self.siirrot)[1]
        self.assertEqual(seuraava_siirto, (5,7))
