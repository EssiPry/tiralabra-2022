import unittest
from ristinolla import Ristinolla


class TestRistinolla(unittest.TestCase):
    def setUp(self):
        self.ristinolla = Ristinolla()
        self.ristinolla.lisaa_reunat_lautaan()
        self.ristinolla.maksin_vuoro = True
        self.ristinolla.maksin_siirto = (2, 7)
        self.ristinolla.minin_siirto = (1, 10)

    def test_lisaa_merkki(self):
        self.ristinolla.lisaa_merkki((2, 3))
        self.assertEqual(self.ristinolla.pelilauta[2][3], 'X')
        self.ristinolla.vaihda_vuoro()
        self.ristinolla.lisaa_merkki((0, 11))
        self.assertEqual(self.ristinolla.pelilauta[0][11], '#')
        self.ristinolla.lisaa_merkki((1, 10))
        self.assertEqual(self.ristinolla.pelilauta[1][10], '0')

    def test_vaihda_vuoro(self):
        self.ristinolla.vaihda_vuoro()
        self.assertFalse(self.ristinolla.maksin_vuoro)
        self.ristinolla.vaihda_vuoro()
        self.assertTrue(self.ristinolla.maksin_vuoro)


    def test_tarkista_voitto_vaaka(self):
        self.ristinolla.pelilauta[2][3] = 'X'
        self.ristinolla.pelilauta[2][4] = 'X'
        self.ristinolla.pelilauta[2][5] = 'X'
        self.ristinolla.pelilauta[2][6] = 'X'
        self.ristinolla.pelilauta[2][7] = 'X'
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'X')
        self.ristinolla.pelilauta[2][6] = '0'
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'kesken')

    def test_tarkista_voitto_pysty(self):
        self.ristinolla.pelilauta[1][7] = 'X'
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.pelilauta[3][7] = 'X'
        self.ristinolla.pelilauta[4][7] = 'X'
        self.ristinolla.pelilauta[5][7] = 'X'
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'X')
        self.ristinolla.pelilauta[1][7] = '0'
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'kesken')

    def test_seuraavat_siirrot(self):
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.pelilauta[1][10] = '0'
        self.assertEqual(len(self.ristinolla.seuraavat_siirrot()), 13)
        self.ristinolla.lisaa_merkki((2, 10))
        self.assertEqual(len(self.ristinolla.seuraavat_siirrot()), 7)
