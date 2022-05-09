
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
            if self.ristinolla.onko_sallittu_siirto(pelaajan_siirto) is True:
                self.ristinolla.pelilauta[pelaajan_siirto[0]
                                          ][pelaajan_siirto[1]] = '0'
                print('pelaajan siirto', pelaajan_siirto)
                self.ristinolla.tulosta_pelitilanne()
                if self.ristinolla.tarkista_voitto(pelaajan_siirto[0], pelaajan_siirto[1]) != 'kesken':
                    break
                self.siirtojen_lkm += 2
                if self.siirtojen_lkm == 625:
                    print('tasapeli')
                    break
                if pelaajan_siirto in mahdolliset_siirrot:
                    mahdolliset_siirrot.remove(pelaajan_siirto)
                self.ristinolla.paivita_mahdolliset_siirrot(
                    pelaajan_siirto, mahdolliset_siirrot)


                #tästä alkaa botin(max) siirto
                arvo = -100

                for koordinaatit in mahdolliset_siirrot:
                    self.ristinolla.pelilauta[koordinaatit[0]
                                          ][koordinaatit[1]] = 'X'
                    kloonisiirrot = list(mahdolliset_siirrot)
                    kloonisiirrot.remove(koordinaatit)
                    self.ristinolla.paivita_mahdolliset_siirrot(koordinaatit, kloonisiirrot)
                    siirron_arvo = self.botti.minimax_ab(
                    self.ristinolla, 4, -100, 100, False, koordinaatit, kloonisiirrot)
                    kloonisiirrot.append(koordinaatit)
                    if siirron_arvo > arvo:
                        arvo = siirron_arvo
                        botin_siirto = koordinaatit
                        if arvo == 10:
                            break
                    self.ristinolla.pelilauta[koordinaatit[0]
                                          ][koordinaatit[1]] = '.'

                print('botin siirto', botin_siirto)
                self.ristinolla.pelilauta[botin_siirto[0]
                                          ][botin_siirto[1]] = 'X'
                self.ristinolla.tulosta_pelitilanne()
                if self.ristinolla.tarkista_voitto(botin_siirto[0], botin_siirto[1]) != 'kesken':
                    break
                mahdolliset_siirrot.remove(botin_siirto)
                self.ristinolla.paivita_mahdolliset_siirrot(
                    botin_siirto, mahdolliset_siirrot)
            else:
                print('Ruutu on jo pelattu. Kokeile toista ruutua.')

        print('Tittidii. Peli loppui.')

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
