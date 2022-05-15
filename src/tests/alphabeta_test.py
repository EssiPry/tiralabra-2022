import unittest
from alphabeta import AlphaBeta
from ristinolla import Ristinolla


class TestAlphaBeta(unittest.TestCase):
    def setUp(self):
        self.botti = AlphaBeta()
        self.ristinolla = Ristinolla()
        self.ristinolla.lisaa_reunat_lautaan()

    def test_palauta_negatiivinen_arvo(self):
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
                if arvo == -14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(arvo, (-14))

    def test_palauta_arvo_nolla(self):
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

    def test_palauta_positiivinen_arvo(self):
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
                if arvo == 14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(arvo, (14))

    def test_estaa_kolme_vaaka_max(self):
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
                if arvo == 14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (10, 9))

    def test_estaa_kolme_pysty_min(self):
        siirrot = []
        self.ristinolla.pelilauta[3][5] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((3, 5), siirrot)
        self.ristinolla.pelilauta[4][6] = '0'
        siirrot.remove((4, 6))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 6), siirrot)
        self.ristinolla.pelilauta[4][5] = 'X'
        siirrot.remove((4, 5))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 5), siirrot)
        self.ristinolla.pelilauta[4][7] = '0'
        siirrot.remove((4, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 7), siirrot)
        self.ristinolla.pelilauta[5][5] = 'X'
        siirrot.remove((5, 5))
        self.ristinolla.paivita_mahdolliset_siirrot((5, 5), siirrot)

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
                if arvo == -14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (6, 5))

    def test_estaa_kolme_diagonaali_min(self):
        siirrot = []
        self.ristinolla.pelilauta[6][3] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((6, 3), siirrot)
        self.ristinolla.pelilauta[6][4] = '0'
        siirrot.remove((6, 4))
        self.ristinolla.paivita_mahdolliset_siirrot((6, 4), siirrot)
        self.ristinolla.pelilauta[5][4] = 'X'
        siirrot.remove((5, 4))
        self.ristinolla.paivita_mahdolliset_siirrot((5, 4), siirrot)
        self.ristinolla.pelilauta[5][5] = '0'
        siirrot.remove((5, 5))
        self.ristinolla.paivita_mahdolliset_siirrot((5, 5), siirrot)
        self.ristinolla.pelilauta[4][5] = 'X'
        siirrot.remove((4, 5))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 5), siirrot)

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
                if arvo == -14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (3, 6))

    def test_kolmen_suoran_jatkaminen_diagonaali_max(self):
        siirrot = []
        self.ristinolla.pelilauta[6][3] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((6, 3), siirrot)
        self.ristinolla.pelilauta[6][4] = '0'
        siirrot.remove((6, 4))
        self.ristinolla.paivita_mahdolliset_siirrot((6, 4), siirrot)
        self.ristinolla.pelilauta[5][4] = 'X'
        siirrot.remove((5, 4))
        self.ristinolla.paivita_mahdolliset_siirrot((5, 4), siirrot)
        self.ristinolla.pelilauta[5][5] = '0'
        siirrot.remove((5, 5))
        self.ristinolla.paivita_mahdolliset_siirrot((5, 5), siirrot)
        self.ristinolla.pelilauta[4][5] = 'X'
        siirrot.remove((4, 5))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 5), siirrot)
        self.ristinolla.pelilauta[4][6] = '0'
        siirrot.remove((4, 6))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 6), siirrot)

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
                if arvo == 14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (3, 6))

    def test_kolmen_suoran_jatkaminen_vaaka_max(self):
        siirrot = []
        self.ristinolla.pelilauta[10][6] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((10, 6), siirrot)
        self.ristinolla.pelilauta[10][7] = 'X'
        siirrot.remove((10, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 7), siirrot)
        self.ristinolla.pelilauta[10][8] = 'X'
        siirrot.remove((10, 8))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 8), siirrot)

        arvo = -100
        for siirto in reversed(siirrot):
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = 'X'
            kloonisiirrot = list(siirrot)
            kloonisiirrot.remove(siirto)
            self.ristinolla.paivita_mahdolliset_siirrot(siirto, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, True, siirto, kloonisiirrot)
            if siirron_arvo > arvo:
                arvo = siirron_arvo
                botin_siirto = siirto
                if arvo == 14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (10, 9))

    def test_kolmen_suoran_jatkaminen_pysty_min(self):
        siirrot = []
        self.ristinolla.pelilauta[10][6] = '0'
        self.ristinolla.paivita_mahdolliset_siirrot((10, 6), siirrot)
        self.ristinolla.pelilauta[11][6] = '0'
        siirrot.remove((11, 6))
        self.ristinolla.paivita_mahdolliset_siirrot((11, 6), siirrot)
        self.ristinolla.pelilauta[12][6] = '0'
        siirrot.remove((12, 6))
        self.ristinolla.paivita_mahdolliset_siirrot((12, 6), siirrot)

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
                if arvo == -14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (13, 6))

    def test_neljan_suoran_jatkaminen_vaaka_max(self):
        siirrot = []
        self.ristinolla.pelilauta[10][6] = 'X'
        self.ristinolla.paivita_mahdolliset_siirrot((10, 6), siirrot)
        self.ristinolla.pelilauta[10][7] = 'X'
        siirrot.remove((10, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 7), siirrot)
        self.ristinolla.pelilauta[10][8] = 'X'
        siirrot.remove((10, 8))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 8), siirrot)
        self.ristinolla.pelilauta[10][9] = 'X'
        siirrot.remove((10, 9))
        self.ristinolla.paivita_mahdolliset_siirrot((10, 9), siirrot)

        arvo = -100
        for siirto in reversed(siirrot):
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = 'X'
            kloonisiirrot = list(siirrot)
            kloonisiirrot.remove(siirto)
            self.ristinolla.paivita_mahdolliset_siirrot(siirto, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, True, siirto, kloonisiirrot)
            if siirron_arvo > arvo:
                arvo = siirron_arvo
                botin_siirto = siirto
                if arvo == 14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (10, 10))

    def test_neljan_suoran_jatkaminen_pysty_min(self):
        siirrot = []
        self.ristinolla.pelilauta[10][6] = '0'
        self.ristinolla.paivita_mahdolliset_siirrot((10, 6), siirrot)
        self.ristinolla.pelilauta[11][6] = '0'
        siirrot.remove((11, 6))
        self.ristinolla.paivita_mahdolliset_siirrot((11, 6), siirrot)
        self.ristinolla.pelilauta[12][6] = '0'
        siirrot.remove((12, 6))
        self.ristinolla.paivita_mahdolliset_siirrot((12, 6), siirrot)
        self.ristinolla.pelilauta[13][6] = '0'
        siirrot.remove((13, 6))
        self.ristinolla.paivita_mahdolliset_siirrot((13, 6), siirrot)

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
                if arvo == -14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (14, 6))

    def test_neljan_suoran_taydentaminen(self):
        siirrot = []
        self.ristinolla.pelilauta[2][1] = '0'
        self.ristinolla.paivita_mahdolliset_siirrot((2, 1), siirrot)
        self.ristinolla.pelilauta[2][2] = 'X'
        siirrot.remove((2, 2))
        self.ristinolla.paivita_mahdolliset_siirrot((2, 2), siirrot)
        self.ristinolla.pelilauta[2][3] = '0'
        siirrot.remove((2, 3))
        self.ristinolla.paivita_mahdolliset_siirrot((2, 3), siirrot)
        self.ristinolla.pelilauta[2][4] = 'X'
        siirrot.remove((2, 4))
        self.ristinolla.paivita_mahdolliset_siirrot((2, 4), siirrot)
        self.ristinolla.pelilauta[3][4] = '0'
        siirrot.remove((3, 4))
        self.ristinolla.paivita_mahdolliset_siirrot((3, 4), siirrot)
        self.ristinolla.pelilauta[3][5] = 'X'
        siirrot.remove((3, 5))
        self.ristinolla.paivita_mahdolliset_siirrot((3, 5), siirrot)
        self.ristinolla.pelilauta[4][4] = '0'
        siirrot.remove((4, 4))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 4), siirrot)
        self.ristinolla.pelilauta[4][6] = 'X'
        siirrot.remove((4, 6))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 6), siirrot)
        self.ristinolla.pelilauta[4][7] = '0'
        siirrot.remove((4, 7))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 7), siirrot)
        self.ristinolla.pelilauta[5][8] = 'X'
        siirrot.remove((5, 8))
        self.ristinolla.paivita_mahdolliset_siirrot((5, 8), siirrot)
        self.ristinolla.pelilauta[4][8] = '0'
        siirrot.remove((4, 8))
        self.ristinolla.paivita_mahdolliset_siirrot((4, 8), siirrot)
        self.ristinolla.pelilauta[6][8] = 'X'
        siirrot.remove((6, 8))
        self.ristinolla.paivita_mahdolliset_siirrot((6, 8), siirrot)
        self.ristinolla.pelilauta[1][3] = '0'
        siirrot.remove((1, 3))
        self.ristinolla.paivita_mahdolliset_siirrot((1, 3), siirrot)

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
                if arvo == 14:
                    break
            self.ristinolla.pelilauta[siirto[0]][siirto[1]] = '.'
        self.assertEqual(botin_siirto, (5, 7))
