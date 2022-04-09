class Ristinolla:

    def __init__(self):
        '''Luokan konstruktori'''
        self.pelilauta = [['.' for x in range(27)]for y in range(27)]
        self.maksin_vuoro = False
        self.maksin_siirto = None
        self.minin_siirto = None
        self.siirtojen_lkm = 0

    def lisaa_reunat_lautaan(self):
        '''Metodi lisää pelilautaan #-reunat'''
        for i in range(27):
            self.pelilauta[i][0] = '#'
            self.pelilauta[i][26] = '#'
        for i in range(27):
            self.pelilauta[0][i] = '#'
            self.pelilauta[26][i] = '#'

    def tulosta_pelitilanne(self):
        '''Metodi tulostaa sen hetkisen pelitilanteen'''
        for i in range(27):
            for j in range(27):
                print(self.pelilauta[i][j], end=" ")
            print("")
        print("")

    def lisaa_merkki(self, koordinaatit):
        ''' Metodi lisää merkin X tai 0 pelaajan tai botin antamiin koordinaatteihin.'''
        rivi = koordinaatit[0]
        sarake = koordinaatit[1]
        if self.pelilauta[rivi][sarake] == '.':
            if self.maksin_vuoro:
                self.pelilauta[rivi][sarake] = 'X'
            else:
                self.pelilauta[rivi][sarake] = '0'
            self.paivita_viimeisin_siirto(koordinaatit)
            self.siirtojen_lkm += 1

    def paivita_viimeisin_siirto(self, koordinaatit):
        '''Metodi päivittää pelaajan tai botin viimeisimmän siirron ristinolla-olioon'''
        if self.maksin_vuoro:
            self.maksin_siirto = koordinaatit
        else:
            self.minin_siirto = koordinaatit

    def vaihda_vuoro(self):
        '''Metodi vaihtaa pelaajavuoron '''
        if self.maksin_vuoro is True:
            self.maksin_vuoro = False
        else:
            self.maksin_vuoro = True

    def seuraavat_siirrot(self):
        '''Metodi palauttaa listan AIn seuraavien mahdollisten siirtojen koordinaateista.
        Koordinaatit ovat edellisten siirtojen viereiset tyhjät koordinaatit.'''
        siirrot = []
        if self.maksin_siirto is not None:
            for rivi in (-1, 0, 1):
                for sarake in (-1, 0, 1):
                    if self.pelilauta[self.maksin_siirto[0]+rivi][self.maksin_siirto[1]+sarake] == '.':
                        siirrot.append(
                            (self.maksin_siirto[0]+rivi, self.maksin_siirto[1]+sarake))
        if self.minin_siirto is not None:
            for rivi in (-1, 0, 1):
                for sarake in (-1, 0, 1):
                    if self.pelilauta[self.minin_siirto[0]+rivi][self.minin_siirto[1]+sarake] == '.':
                        siirrot.append(
                            (self.minin_siirto[0]+rivi, self.minin_siirto[1]+sarake))
        siirrot = list(set(siirrot))
        return siirrot

    def tarkista_voitto(self):
        '''Metodi tarkistaa täydentääkö viimeisin siirto pelilaudalle 5 peräkkäistä samaa
        merkkiä eli voittaako siirto pelin. Metodi palauttaa voittavan stringin merkin, tai tekstin tasapeli
        '''

        if self.maksin_vuoro and self.maksin_siirto is not None:
            rivi = self.maksin_siirto[0]
            sarake = self.maksin_siirto[1]
        else:
            rivi = self.minin_siirto[0]
            sarake = self.minin_siirto[1]

        alku_rivi = max(rivi-4, 1)
        alku_sarake = max(sarake-4, 1)
        loppu_rivi = min(rivi+5, 25)
        loppu_sarake = min(sarake+5, 25)

        vaaka = 1
        for i in range(alku_sarake, loppu_sarake):

            if self.pelilauta[rivi][i] == self.pelilauta[rivi][i+1]:
                vaaka += 1
                if vaaka == 5:
                    return self.pelilauta[rivi][i]
            else:
                vaaka = 0

        pysty = 1
        for i in range(alku_rivi, loppu_rivi):
            if self.pelilauta[i][sarake] == self.pelilauta[i+1][sarake]:
                pysty += 1
                if pysty == 5:
                    return self.pelilauta[i][sarake]
            else:
                pysty = 0

        #nämä eivät vielä toimi
        #diagonaali = 1
        #j = alku_sarake
        #for i in range(alku_rivi, loppu_rivi):
        #    if self.pelilauta[i][j] == self.pelilauta[i+1][j+1]:
        #        diagonaali += 1
        #        if diagonaali == 5:
        #            return self.pelilauta[i][j]
        #    else:
        #        diagonaali = 0
        #    j += 1

        #diagonaali2 = 1
        #j = loppu_rivi
        #for j in range(alku_sarake, loppu_sarake):
        #    if self.pelilauta[i][j] == self.pelilauta[i-1][j+1]:
        #        diagonaali2 += 1
        #        if diagonaali2 == 5:
        #            return self.pelilauta[i][j]
        #        diagonaali2 = 0
        #    i -= 1
        #    if i < 0:
        #        break

        if self.siirtojen_lkm == 625:
            return 'tasapeli'

        return 'kesken'
