import unittest
from ristinolla import Ristinolla

class TestRistinolla(unittest.TestCase):
    def setUp(self):
        self.ristinolla = Ristinolla()
        self.ristinolla.maksimin_vuoro = True
        self.ristinolla.maksin_siirto = (2,7)
        self.ristinolla.minimin_siirto = (0,10)

    def test_lisaa_merkki(self):
        self.ristinolla.lisaa_merkki((2,3))
        self.assertEqual(self.ristinolla.pelitilanne[2][3], 'X')

    def test_tarkista_voitto_vaaka(self):
        self.ristinolla.lisaa_merkki((2,3))
        self.ristinolla.lisaa_merkki((2,4))
        self.ristinolla.lisaa_merkki((2,5))
        self.ristinolla.lisaa_merkki((2,6))
        self.ristinolla.lisaa_merkki((2,7))
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'voitto')
        self.ristinolla.maksimin_vuoro = False
        self.ristinolla.lisaa_merkki((2,6))
        self.ristinolla.maksimin_vuoro = True
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'kesken')

    def test_tarkista_voitto_pysty(self):
        self.ristinolla.lisaa_merkki((0,7))
        self.ristinolla.lisaa_merkki((1,7))
        self.ristinolla.lisaa_merkki((2,7))
        self.ristinolla.lisaa_merkki((3,7))
        self.ristinolla.lisaa_merkki((4,7))
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'voitto')
        self.ristinolla.maksimin_vuoro = False
        self.ristinolla.lisaa_merkki((0,7))
        self.ristinolla.maksimin_vuoro = True
        self.assertEqual(self.ristinolla.tarkista_voitto(), 'kesken')
