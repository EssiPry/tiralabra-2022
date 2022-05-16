import unittest
from alphabeta import AlphaBeta
from ristinolla import Ristinolla
from pelilooppi import Pelilooppi


class TestAlphaBeta(unittest.TestCase):
    def setUp(self):
        self.botti = AlphaBeta()
        self.ristinolla = Ristinolla()
        self.ristinolla.lisaa_reunat_lautaan()
        self.pelilooppi = Pelilooppi(self.ristinolla, self.botti)

    def test_palauta_negatiivinen_arvo(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (1, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (3, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 7), '0', siirrot)

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
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (1, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (3, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 7), '0', siirrot)
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
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 1), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 2), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 3), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 4), 'X', siirrot)
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

    def test_estaa_neljan_suoran_vaaka_max(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 6), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 8), '0', siirrot)

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

    def test_estaa_neljan_suoran_pysty_min(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (3, 5), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 6), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 5), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 5), 'X', siirrot)

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

    def test_estaa_neljan_suoran_diagonaali_min(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (6, 3), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (6, 4), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 4), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 5), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 5), 'X', siirrot)

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

    def test_estaa_neljan_suoran_diagonaali_max(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 3), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 4), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (6, 4), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 5), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (7, 5), '0', siirrot)

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
        self.ristinolla.tulosta_pelitilanne()
        self.assertEqual(botin_siirto, (8, 6))

    def test_kolmen_suoran_jatkaminen_diagonaali_max(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (6, 3), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (6, 4), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 4), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 5), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 5), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 6), '0', siirrot)

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
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 6), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 7), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 8), 'X', siirrot)

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
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 1), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (3, 2), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 3), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (3, 3), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 3), '0', siirrot)

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
        self.assertEqual(botin_siirto, (5, 3))

    def test_neljan_suoran_jatkaminen_vaaka_max(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 6), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 7), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 8), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (10, 9), 'X', siirrot)

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
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (20, 6), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (21, 6), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (22, 6), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (23, 6), '0', siirrot)

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
        self.assertEqual(botin_siirto, (24, 6))

    def test_kaksi_kaksi_suoran_taydentaminen_vaaka_min(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (15, 4), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (14, 6), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (15, 5), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (14, 7), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (15, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (14, 8), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (15, 8), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (14, 9), 'X', siirrot)

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
        self.assertEqual(botin_siirto, (15, 6))

    def test_viiden_suoran_estaminen_vaaka_max(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (15, 5), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (14, 6), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (15, 6), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (14, 7), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (15, 8), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (14, 8), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (15, 9), '0', siirrot)

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
        self.assertEqual(botin_siirto, (15, 7))

    def test_kaksi_kaksi_diagonaalin_taydentaminen_min(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (1, 1), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 6), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 2), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (3, 6), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 4), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 6), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 5), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 6), 'X', siirrot)

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
        self.assertEqual(botin_siirto, (3, 3))

    def test_kolme_yksi_diagonaalin_taydentaminen_max(self):
        siirrot = []
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 1), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 2), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 3), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (2, 4), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (3, 4), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (3, 5), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 4), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 6), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 7), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (5, 8), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (4, 8), '0', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (6, 8), 'X', siirrot)
        self.pelilooppi.tee_siirto_ja_paivita_botin_siirrot(
            (1, 3), '0', siirrot)

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
