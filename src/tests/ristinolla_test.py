import unittest
from ristinolla import Ristinolla


class TestRistinolla(unittest.TestCase):
    def setUp(self):
        self.ristinolla = Ristinolla()
        self.ristinolla.lisaa_reunat_lautaan()
        self.ristinolla.maksin_vuoro = True
        self.ristinolla.maksin_siirto = (2, 7)
        self.ristinolla.minin_siirto = (1, 10)

    def test_onko_siirto_sallittu(self):
        self.assertTrue(self.ristinolla.onko_sallittu_siirto((2, 3)))
        self.ristinolla.lisaa_merkki((2, 3), True)
        self.assertFalse(self.ristinolla.onko_sallittu_siirto((2, 3)))
        self.assertFalse(self.ristinolla.onko_sallittu_siirto((20, 0)))

    def test_lisaa_merkki(self):
        self.ristinolla.lisaa_merkki((2, 3), True)
        self.assertEqual(self.ristinolla.pelilauta[2][3], 'X')
        #self.ristinolla.vaihda_vuoro()
        self.ristinolla.lisaa_merkki((0, 11), False)
        self.assertEqual(self.ristinolla.pelilauta[0][11], '#')
        self.ristinolla.lisaa_merkki((1, 10), False)
        self.assertEqual(self.ristinolla.pelilauta[1][10], '0')

    def test_poista_merkki(self):
        self.ristinolla.lisaa_merkki((2, 3), True)
        self.ristinolla.poista_merkki((2, 3))
        self.assertEqual(self.ristinolla.pelilauta[2][3], '.')

    #def test_vaihda_vuoro(self):
    #    self.ristinolla.vaihda_vuoro()
    #    self.assertFalse(self.ristinolla.maksin_vuoro)
    #    self.ristinolla.vaihda_vuoro()
    #    self.assertTrue(self.ristinolla.maksin_vuoro)

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

    def test_tarkista_voitto_d1(self):
        self.ristinolla.pelilauta[1][6] = 'X'
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.pelilauta[3][8] = 'X'
        self.ristinolla.pelilauta[4][9] = 'X'
        self.ristinolla.pelilauta[5][10] = 'X'
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'X')
        self.ristinolla.pelilauta[5][10] = '0'
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'kesken')

    def test_tarkista_voitto_d2(self):
        self.ristinolla.pelilauta[5][4] = 'X'
        self.ristinolla.pelilauta[4][5] = 'X'
        self.ristinolla.pelilauta[3][6] = 'X'
        self.ristinolla.pelilauta[2][7] = 'X'
        self.ristinolla.pelilauta[1][8] = 'X'
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'X')
        self.ristinolla.pelilauta[3][6] = '0'
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'kesken')

    def test_paivita_seuraavat_siirrot(self):
        self.ristinolla.lisaa_merkki((2, 7),True)
        self.ristinolla.paivita_seuraavat_siirrot((2, 7))
        self.assertEqual(len(self.ristinolla.seuraavat_siirrot), 8)
        self.assertEqual(self.ristinolla.seuraavat_siirrot, {
                         (1, 6), (1, 7), (1, 8), (2, 6), (2, 8), (3, 6), (3, 7), (3, 8)})

    def test_paivita_seuraavat_siirrot_useampi_merkki(self):
        self.ristinolla.lisaa_merkki((2, 7), True)
        self.ristinolla.paivita_seuraavat_siirrot((2, 7))
        self.ristinolla.lisaa_merkki((3, 6), False)
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((3,6))
        self.ristinolla.paivita_seuraavat_siirrot((3, 6))
        self.ristinolla.lisaa_merkki((3, 7), True)
        self.ristinolla.paivita_seuraavat_siirrot((3, 7))
        self.ristinolla.poista_koordinaatit_seuraavista_siirroista((3,7))
        self.assertEqual(len(self.ristinolla.seuraavat_siirrot), 12)
        self.assertEqual(self.ristinolla.seuraavat_siirrot, {(1, 6), (1, 7), (1, 8), (
            2, 5), (2, 6), (2, 8), (3, 5), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8)})
