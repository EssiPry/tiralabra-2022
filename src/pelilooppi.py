import time


class Pelilooppi:

    def __init__(self, ristinolla, alphabeta):
        '''Luokan konstruktori'''
        self.ristinolla = ristinolla
        self.botti = alphabeta
        self.siirtojen_lkm = -1

    def aloita_peli(self):
        '''Metodi aloittaa ristinollapelin ja pyörittää pelilooppia
        kunnes peli loppuu. '''

        self.ristinolla.lisaa_reunat_lautaan()
        mahdolliset_siirrot = []
        print('Tervetuloa pelamaan ristinollaa.')
        while True:
            pelaajan_siirto = self.kysy_pelaajan_siirto()
            print('')
            print('Pelaajan siirto', pelaajan_siirto)
            self.tee_siirto_ja_paivita_botin_siirrot(
                pelaajan_siirto, '0', mahdolliset_siirrot)
            if self.ristinolla.tarkista_voitto(pelaajan_siirto[0], pelaajan_siirto[1]) != 'kesken':
                voittaja = 'Pelaaja'
                break
            self.siirtojen_lkm += 2
            if self.siirtojen_lkm == 625:
                print('tasapeli')
                break

            alkuaika = time.time()
            botin_siirto = self.kysy_max_botin_siirto(mahdolliset_siirrot)
            loppuaika = time.time()
            aika = loppuaika - alkuaika
            print(f'Botin siirron laskentaan kului {aika:.2f}s')
            print('Botin siirto', botin_siirto)
            self.tee_siirto_ja_paivita_botin_siirrot(
                botin_siirto, 'X', mahdolliset_siirrot)
            if self.ristinolla.tarkista_voitto(botin_siirto[0], botin_siirto[1]) != 'kesken':
                voittaja = 'Botti'
                break

        print(f'Tittidii. Peli loppui. {voittaja} voitti pelin.')

    def kysy_pelaajan_siirto(self):
        '''Metodi kysyy pelaajalta seuraavan siirron koordinaatit,
        kunnes annetut koordinaatit ovat pelilaudalla  ja vapaat.
        Palauttaa pelaajan siirron tuplena (rivi, sarake)'''
        rivi = -1
        sarake = -1
        while True:
            while rivi == -1:
                try:
                    rivi = int(
                        input('Anna rivi jolle merkki lisätään. Rivin pitää olla väliltä 1-25. '))
                except ValueError:
                    rivi = -1
                if rivi < 1 or rivi > 25:
                    rivi = -1
            while sarake == -1:
                try:
                    sarake = int(
                        input('Anna sarake jolle merkki lisätään. Sarakkeen pitää olla väliltä 1-25. '))
                except ValueError:
                    sarake = -1
                if sarake < 1 or sarake > 25:
                    sarake = -1
            if self.ristinolla.onko_sallittu_siirto((rivi, sarake)) is True:
                break
            else:
                print('Valitsemasi ruutu on jo pelattu. Kokeile toista ruutua')
                rivi = -1
                sarake = -1
        return (rivi, sarake)

    def kysy_max_botin_siirto(self, mahdolliset_siirrot):
        '''Metodi laskee botille parhaan siirron parametrina annetujen
        mahdollisten siirtojen listalta. Pelaa maksia.
        Palauttaa botin siirron tuplena (rivi, sarake)'''
        arvo = -100

        for koordinaatit in reversed(mahdolliset_siirrot):
            self.ristinolla.pelilauta[koordinaatit[0]
                                      ][koordinaatit[1]] = 'X'
            kloonisiirrot = list(mahdolliset_siirrot)
            kloonisiirrot.remove(koordinaatit)
            self.ristinolla.paivita_mahdolliset_siirrot(
                koordinaatit, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, False, koordinaatit, kloonisiirrot)
            kloonisiirrot.append(koordinaatit)
            if siirron_arvo > arvo:
                arvo = siirron_arvo
                botin_siirto = koordinaatit
                if arvo == 14:
                    break
            self.ristinolla.pelilauta[koordinaatit[0]
                                      ][koordinaatit[1]] = '.'
        return botin_siirto

    def kysy_min_botin_siirto(self, mahdolliset_siirrot):
        '''Metodi laskee botille parhaan siirron parametrina annettun
        mahdollisten siirtojen -listalta. Pelaa miniä.
        Palauttaa botin siirron tuplena (rivi, sarake)'''
        arvo = 100

        for koordinaatit in reversed(mahdolliset_siirrot):
            self.ristinolla.pelilauta[koordinaatit[0]
                                      ][koordinaatit[1]] = '0'
            kloonisiirrot = list(mahdolliset_siirrot)
            kloonisiirrot.remove(koordinaatit)
            self.ristinolla.paivita_mahdolliset_siirrot(
                koordinaatit, kloonisiirrot)
            siirron_arvo = self.botti.minimax_ab(
                self.ristinolla, 4, -100, 100, True, koordinaatit, kloonisiirrot)
            kloonisiirrot.append(koordinaatit)
            if siirron_arvo < arvo:
                arvo = siirron_arvo
                botin_siirto = koordinaatit
                if arvo == -14:
                    break
            self.ristinolla.pelilauta[koordinaatit[0]
                                      ][koordinaatit[1]] = '.'
        return botin_siirto

    def tee_siirto_ja_paivita_botin_siirrot(self, siirto, merkki, mahdolliset_siirrot):
        ''' Metodi lisää annetun merkin pelilaudalle annettuun kohtaan (siirto).
        Poistaa annetun siirron koordinaatit botin mahdollisten siirtojen -listalta.
        Päivittää annetun siirron tyhjät naapurit mahdollisten siirtojen -listalle.

        Parametrit:
            siirto - tuple (rivi, sarake)
            merkki - X tai 0 riippuen pelaajasta
            mahdolliset_siirrot - lista botin seuraavista mahdollisista siirroista
        '''
        self.ristinolla.pelilauta[siirto[0]][siirto[1]] = merkki
        self.ristinolla.tulosta_pelitilanne()
        if siirto in mahdolliset_siirrot:
            mahdolliset_siirrot.remove(siirto)
        self.ristinolla.paivita_mahdolliset_siirrot(
            siirto, mahdolliset_siirrot)
