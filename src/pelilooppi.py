class Pelilooppi:

    def __init__(self, ristinolla, alphabeta):
        '''Luokan konstruktori'''
        self.ristinolla = ristinolla
        self.botti = alphabeta
        self.siirtojen_lkm = -1

    def aloita_peli(self):
        '''Metodi aloittaa ristinolla peli ja pyörittää pelilooppia
        kunnes peli loppuu. '''

        self.ristinolla.lisaa_reunat_lautaan()
        mahdolliset_siirrot = set()
        print('Tervetuloa pelamaan ristinollaa.')
        while True:
            pelaajan_siirto = self.kysy_pelaajan_siirto()
            if self.ristinolla.onko_sallittu_siirto(pelaajan_siirto) is True:
                self.ristinolla.pelilauta[pelaajan_siirto[0]][pelaajan_siirto[1]] = '0'
                self.ristinolla.tulosta_pelitilanne()
                if self.ristinolla.tarkista_voitto(pelaajan_siirto[0],pelaajan_siirto[1]) != 'kesken':
                    break
                self.siirtojen_lkm += 2
                if self.siirtojen_lkm == 625:
                    print('tasapeli')
                    break
                self.ristinolla.poista_koordinaatit_seuraavista_siirroista(pelaajan_siirto, mahdolliset_siirrot)
                self.ristinolla.paivita_seuraavat_siirrot(pelaajan_siirto, mahdolliset_siirrot)
                print(mahdolliset_siirrot)
                klooni_siirrot = set(mahdolliset_siirrot)
                botin_siirto = self.botti.minimax_ab(
                    self.ristinolla, 3, -100, 100, True, pelaajan_siirto, klooni_siirrot)[1]
                print('botin siirto', botin_siirto)
                self.ristinolla.pelilauta[botin_siirto[0]][botin_siirto[1]] = 'X'
                self.ristinolla.tulosta_pelitilanne()
                if self.ristinolla.tarkista_voitto(botin_siirto[0], botin_siirto[1]) != 'kesken':
                    break
                self.ristinolla.poista_koordinaatit_seuraavista_siirroista(botin_siirto, mahdolliset_siirrot)
                self.ristinolla.paivita_seuraavat_siirrot(botin_siirto, mahdolliset_siirrot)
            else:
                print('Ruutu on jo pelattu. Kokeile toista ruutua.')

        print('Tittidii. Peli on ohi.')

    def kysy_pelaajan_siirto(self):
        '''Metodi kysyy pelaajalta seuraavan siirron koordinaatit.
        Palauttaa rivin ja sarakkeen tuplena'''
        rivi = -1
        sarake = -1
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
        return (rivi, sarake)
