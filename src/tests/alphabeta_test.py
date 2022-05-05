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

    def test_minimax_ab_minin_vuoro(self):
        arvo = 100
        for siirto in self.siirrot:
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '0'
            siirron_arvo =  self.botti.minimax_ab(self.ristinolla, 3, -100, 100, True, siirto, self.siirrot)
            if siirron_arvo < arvo:
                arvo = siirron_arvo
                seuraava_siirto = siirto
                if arvo == -10:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(arvo, (-10))

    def test_minimax_ab_maxin_vuoro(self):
        arvo = -100
        for siirto in self.siirrot:
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = 'X'
            self.ristinolla.paivita_mahdolliset_siirrot(siirto, self.siirrot)
            self.ristinolla.tulosta_pelitilanne()
            siirron_arvo =  self.botti.minimax_ab(self.ristinolla, 1, -100, 100, False, siirto, self.siirrot)
            if siirron_arvo > arvo:
                arvo = siirron_arvo
                seuraava_siirto = siirto
                if arvo == 10:
                    break
        self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(arvo, (0))
