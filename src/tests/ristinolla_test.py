import unittest
from ristinolla import Ristinolla


class TestRistinolla(unittest.TestCase):
    def setUp(self):
        self.ristinolla = Ristinolla()
        self.ristinolla.lisaa_reunat_lautaan()

    def test_onko_siirto_sallittu(self):
        self.assertTrue(self.ristinolla.onko_sallittu_siirto((2, 3)))

    def test_onko_siirto_sallittu_ei(self):
        self.ristinolla.pelilauta[2][3] = 'X'
        self.assertFalse(self.ristinolla.onko_sallittu_siirto((2, 3)))

    def test_onko_siirto_sallittu_reuna(self):
        self.assertFalse(self.ristinolla.onko_sallittu_siirto((20, 0)))

    def test_tarkista_voitto_vaaka(self):
        self.ristinolla.pelilauta[2][3] = 'X'
        self.ristinolla.pelilauta[2][4] = 'X'
        self.ristinolla.pelilauta[2][5] = 'X'
        self.ristinolla.pelilauta[2][6] = 'X'
        self.ristinolla.pelilauta[2][7] = 'X'
        self.assertEqual(self.ristinolla.tarkista_voitto(2, 7), 'X')
        self.ristinolla.pelilauta[2][6] = '0'
        self.assertEqual(self.ristinolla.tarkista_voitto(2, 7), 'kesken')

    def test_tarkista_voitto_pysty(self):
        self.ristinolla.pelilauta[1][7] = 'X'
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.pelilauta[3][7] = 'X'
        self.ristinolla.pelilauta[4][7] = 'X'
        self.ristinolla.pelilauta[5][7] = 'X'
        self.assertEqual(self.ristinolla.tarkista_voitto(5, 7), 'X')
        self.ristinolla.pelilauta[1][7] = '0'
        self.assertEqual(self.ristinolla.tarkista_voitto(5, 7), 'kesken')

    def test_tarkista_voitto_d1(self):
        self.ristinolla.pelilauta[1][6] = 'X'
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.pelilauta[3][8] = 'X'
        self.ristinolla.pelilauta[4][9] = 'X'
        self.ristinolla.pelilauta[5][10] = 'X'
        self.assertEqual(self.ristinolla.tarkista_voitto(5, 10), 'X')
        self.ristinolla.pelilauta[5][10] = '0'
        self.assertEqual(self.ristinolla.tarkista_voitto(5, 10), 'kesken')

    def test_tarkista_voitto_d2(self):
        self.ristinolla.pelilauta[5][4] = 'X'
        self.ristinolla.pelilauta[4][5] = 'X'
        self.ristinolla.pelilauta[3][6] = 'X'
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.pelilauta[1][8] = 'X'
        self.assertEqual(self.ristinolla.tarkista_voitto(1, 8), 'X')
        self.ristinolla.pelilauta[3][6] = '0'
        self.assertEqual(self.ristinolla.tarkista_voitto(1, 8), 'kesken')

    def test_paivita_mahdolliset_siirrot(self):
        siirrot = []
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((2, 7), siirrot)
        self.assertEqual(len(siirrot), 8)
        print(siirrot)
        self.assertEqual(siirrot,
                         [(1, 6), (1, 7), (1, 8), (2, 6), (2, 8), (3, 6), (3, 7), (3, 8)])

    def test_paivita_mahdolliset_siirrot_useampi_merkki_laudalla(self):
        siirrot = []
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((2, 7), siirrot)
        self.ristinolla.pelilauta[3][7] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((3, 7), siirrot)
        siirrot.remove((3, 7))
        self.ristinolla.pelilauta[4][7] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((4, 7), siirrot)
        siirrot.remove((4, 7))
        self.ristinolla.pelilauta[4][8] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((4, 8), siirrot)
        siirrot.remove((4, 8))
        self.assertEqual(len(siirrot), 14)
