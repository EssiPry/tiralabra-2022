class Ristinolla:

    def __init__(self):
        '''Luokan konstruktori'''
        self.pelitilanne = [['.' for x in range(25)]for y in range(25)]
        self.maksimin_vuoro = False
        self.maksin_siirto = None
        self.minin_siirto = None
        self.siirtojen_lkm  = 0

    def tulosta_pelitilanne(self):
        '''Metodi tulostaa sen hetkisen pelitilanteen'''
        for i in range(25):
            for j in range(25):
                print(self.pelitilanne[i][j], end=" ")
            print("")
        print("")

    def lisaa_merkki(self, koordinaatit):
        ''' Metodi lisää merkin X tai 0 pelaajan tai botin antamiin koordinaatteihin.'''
        rivi = koordinaatit[0]
        sarake = koordinaatit[1]
        if self.maksimin_vuoro:
            self.pelitilanne[rivi][sarake] = 'X'
        else:
            self.pelitilanne[rivi][sarake] = '0'

    def paivita_viimeisin_siirto(self, siirto):
        '''Metodi päivittää pelaajan tai botin viimeisimmän siirron ristinolla-olioon'''
        if self.maksimin_vuoro:
            self.maksin_siirto = siirto
        else:
            self.minin_siirto = siirto

    def seuraavat_siirrot(self):
        siirrot = []
        if self.maksin_siirto != None:
            for rivi in (-1,0,1):
                for sarake in (-1,0,1):
                    if self.pelitilanne[self.maksin_siirto[1]+rivi][self.maksin_siirto+sarake] == '.':
                        siirrot.append((self.maksin_siirto[1]+rivi,self.maksin_siirto+sarake))
        if self.minin_siirto != None:
            for rivi in (-1,0,1):
                for sarake in (-1,0,1):
                    if self.pelitilanne[self.minin_siirto[1]+rivi][self.minin_siirto+sarake] == '.':
                        siirrot.append((self.minin_siirto[1]+rivi,self.minin_siirto+sarake))
        print(siirrot)
        return siirrot

    def tarkista_voitto(self):
        '''Metodi tarkistaa täydentääkö viimeisin siirto pelilaudalle 5 peräkkäistä samaa
        merkkiä eli voittaako siirto pelin'''

        if self.maksimin_vuoro:
            rivi = self.maksin_siirto[0]
            sarake = self.maksin_siirto [1]
        else:
            rivi = self.minin_siirto[0]
            sarake = self.minin_siirto[1]

        alku_rivi = max(rivi-4, 0)
        alku_sarake = max(sarake-4,0)
        loppu_rivi = min(rivi+5, 24)
        loppu_sarake = min(sarake + 5, 24)

        vaaka = 1
        for i in range(alku_sarake, loppu_sarake):

            if self.pelitilanne[rivi][i] == self.pelitilanne[rivi][i+1]:
                vaaka += 1
                if vaaka == 5:
                    return 'voitto'
            else:
                vaaka = 0

        pysty = 1
        for i in range(alku_rivi, loppu_rivi):
            if self.pelitilanne[i][sarake] == self.pelitilanne[i+1][sarake]:
                pysty += 1
                if pysty == 5:
                    return 'voitto'
            else:
                pysty = 0

        diagonaali = 1
        j = alku_sarake
        for i in range(alku_rivi, loppu_rivi):
            if self.pelitilanne[i][j] == self.pelitilanne[i+1][j+1]:
                diagonaali += 1
                if diagonaali == 5:
                    return 'voitto'
            else:
                diagonaali = 0
            j += 1

        diagonaali2 = 1
        j = loppu_rivi
        for j in range(alku_sarake, loppu_sarake):
            if self.pelitilanne[i][j] == self.pelitilanne[i-1][j+1]:
                diagonaali2 += 1
                if diagonaali2 == 5:
                    return 'voitto'
            else:
                diagonaali2 = 0
            i -= 1
            if i < 0:
                break

        if self.siirtojen_lkm == 625:
            return 'tasapeli'

        return 'kesken'
