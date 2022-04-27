import unittest
from alphabeta import AlphaBeta
from ristinolla import Ristinolla

class TestAlphaBeta(unittest.TestCase):
    def setUp(self):
        self.botti = AlphaBeta()
        self.ristinolla = Ristinolla()
        self.ristinolla.lisaa_reunat_lautaan()
        self.ristinolla.lisaa_merkki((1,7), False)
        self.ristinolla.paivita_seuraavat_siirrot((1,7))
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((1,7))
        #self.ristinolla.vaihda_vuoro()
        self.ristinolla.lisaa_merkki((1,8),True)
        self.ristinolla.paivita_seuraavat_siirrot((1,8))
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((1,8))
        #self.ristinolla.vaihda_vuoro()
        self.ristinolla.lisaa_merkki((2,7), False)
        self.ristinolla.paivita_seuraavat_siirrot((2,7))
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((2,7))
        #self.ristinolla.vaihda_vuoro()
        self.ristinolla.lisaa_merkki((3,6), True)
        self.ristinolla.paivita_seuraavat_siirrot((3,6))
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((3,6))
        #self.ristinolla.vaihda_vuoro()
        self.ristinolla.lisaa_merkki((3,7), False)
        self.ristinolla.paivita_seuraavat_siirrot((3,7))
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((3,7))
        self.ristinolla.lisaa_merkki((4,7), False)
        self.ristinolla.paivita_seuraavat_siirrot((4,7))
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((4,7))
        #self.ristinolla.vaihda_vuoro()

    def test_minimax_ab(self):
        self.ristinolla.tulosta_pelitilanne()
        seuraava_siirto = self.botti.minimax_ab(self.ristinolla, 3, -100, 100, True)[1]
        print(seuraava_siirto)
        print(self.ristinolla.maksin_vuoro)
        self.assertTrue(self.ristinolla.maksin_vuoro)
        self.assertEqual(seuraava_siirto, (5,7))
