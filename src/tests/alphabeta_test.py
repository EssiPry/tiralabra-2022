import unittest
from alphabeta import AlphaBeta
from ristinolla import Ristinolla


class TestAlphaBeta(unittest.TestCase):
    def setUp(self):
        self.botti = AlphaBeta()
        self.ristinolla = Ristinolla()
        self.ristinolla.lisaa_reunat_lautaan()

    def test_minimax_ab_negatiivinen_arvo(self):
        siirrot = []
        self.ristinolla.pelilauta[1][7] = '0'
        self.ristinolla.paivita_mahdolliset_siirrot((1, 7), siirrot)
        self.ristinolla.pelilauta[2][7] = '0'
        siirrot.remove((2, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((2, 7), siirrot)
        self.ristinolla.pelilauta[3][7] = '0'
        siirrot.remove((3, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((3, 7), siirrot)
        self.ristinolla.pelilauta[4][7] = '0'
        siirrot.remove((4, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 7), siirrot)
        arvo = 100
        for siirto in reversed(siirrot):
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '0'
            kloonisiirrot = list(siirrot)
            kloonisiirrot.remove(siirto)
            self.ristinolla.paivita_mahdolliset_siirrot(siirto, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, True, siirto, kloonisiirrot)
            if siirron_arvo < arvo:
                arvo = siirron_arvo
                if arvo == -10:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(arvo, (-10))

    def test_minimax_ab_arvo_nolla(self):
        siirrot = []
        self.ristinolla.pelilauta[1][7] = '0'
        self.ristinolla.paivita_mahdolliset_siirrot((1, 7), siirrot)
        self.ristinolla.pelilauta[2][7] = '0'
        siirrot.remove((2, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((2, 7), siirrot)
        self.ristinolla.pelilauta[3][7] = '0'
        siirrot.remove((3, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((3, 7), siirrot)
        self.ristinolla.pelilauta[4][7] = '0'
        siirrot.remove((4, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 7), siirrot)
        arvo = -100
        for siirto in reversed(siirrot):
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = 'X'
            kloonisiirrot = list(siirrot)
            kloonisiirrot.remove(siirto)
            self.ristinolla.paivita_mahdolliset_siirrot(siirto, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, False, siirto, kloonisiirrot)
            if siirron_arvo > arvo:
                arvo = siirron_arvo
                if arvo == 10:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(arvo, (0))

    def test_minimax_ab_positiivinen_arvo(self):
        siirrot = []
        self.ristinolla.pelilauta[1][7] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((1, 7), siirrot)
        self.ristinolla.pelilauta[2][7] = 'X'
        siirrot.remove((2, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((2, 7), siirrot)
        self.ristinolla.pelilauta[3][7] = 'X'
        siirrot.remove((3, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((3, 7), siirrot)
        self.ristinolla.pelilauta[4][7] = 'X'
        siirrot.remove((4, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 7), siirrot)
        arvo = -100
        for siirto in reversed(siirrot):
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = 'X'
            kloonisiirrot = list(siirrot)
            kloonisiirrot.remove(siirto)
            self.ristinolla.paivita_mahdolliset_siirrot(siirto, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, False, siirto, kloonisiirrot)
            if siirron_arvo > arvo:
                arvo = siirron_arvo
                if arvo == 10:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(arvo, (10))

    def test_minimax_ab_kolmen_suoran_blokkaus(self):
        siirrot = []
        self.ristinolla.pelilauta[10][6] = '0'
        self.ristinolla.paivita_mahdolliset_siirrot((10, 6), siirrot)
        self.ristinolla.pelilauta[10][7] = '0'
        siirrot.remove((10, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 7), siirrot)
        self.ristinolla.pelilauta[10][8] = '0'
        siirrot.remove((10, 8))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 8), siirrot)

        arvo = -100
        for siirto in reversed(siirrot):
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = 'X'
            kloonisiirrot = list(siirrot)
            kloonisiirrot.remove(siirto)
            self.ristinolla.paivita_mahdolliset_siirrot(siirto, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, False, siirto, kloonisiirrot)
            if siirron_arvo > arvo:
                arvo = siirron_arvo
                botin_siirto = siirto
                if arvo == 10:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (10, 9))

    def test_minimax_ab_kolmen_suoran_jatkaminen(self):
        siirrot = []
        self.ristinolla.pelilauta[10][6] = '0'
        self.ristinolla.paivita_mahdolliset_siirrot((10, 6), siirrot)
        self.ristinolla.pelilauta[10][7] = '0'
        siirrot.remove((10, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 7), siirrot)
        self.ristinolla.pelilauta[10][8] = '0'
        siirrot.remove((10, 8))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 8), siirrot)

        arvo = 100
        for siirto in reversed(siirrot):
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '0'
            kloonisiirrot = list(siirrot)
            kloonisiirrot.remove(siirto)
            self.ristinolla.paivita_mahdolliset_siirrot(siirto, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, True, siirto, kloonisiirrot)
            if siirron_arvo < arvo:
                arvo = siirron_arvo
                botin_siirto = siirto
                if arvo == -10:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (10, 9))
