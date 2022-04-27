class Pelilooppi:

    def __init__(self, ristinolla, alphabeta):
        '''Luokan konstruktori'''
        self.ristinolla = ristinolla
        self.botti = alphabeta

    def aloita_peli(self):
        '''Metodi aloittaa ristinolla peli ja pyörittää pelilooppia
        kunnes peli loppuu. '''

        self.ristinolla.lisaa_reunat_lautaan()
        print('Tervetuloa pelamaan ristinollaa.')
        while True:
            pelaajan_siirto = self.kysy_pelaajan_siirto()
            if self.ristinolla.onko_sallittu_siirto(pelaajan_siirto) is True:
                self.ristinolla.lisaa_merkki(pelaajan_siirto)
                self.ristinolla.tulosta_pelitilanne()
                if self.ristinolla.tarkista_voitto() != 'kesken':
                    break
                self.ristinolla.paivita_seuraavat_siirrot(pelaajan_siirto)
                self.ristinolla.vaihda_vuoro()
                botin_siirto = self.botti.minimax_ab(
                    self.ristinolla, 3, -100, 100, True)[1]
                print('botin siirto', botin_siirto)
                self.ristinolla.lisaa_merkki(botin_siirto)
                self.ristinolla.tulosta_pelitilanne()
                if self.ristinolla.tarkista_voitto() != 'kesken':
                    break
                self.ristinolla.paivita_seuraavat_siirrot(botin_siirto)
                self.ristinolla.vaihda_vuoro()
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
