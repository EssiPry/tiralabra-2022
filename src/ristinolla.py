class Ristinolla:

    def __init__(self):
        '''Luokan konstruktori'''
        self.pelilauta = [['.' for x in range(27)]for y in range(27)]
        self.maksin_vuoro = False
        self.maksin_siirto = None
        self.minin_siirto = None
        self.siirrot = set()
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


    def paivita_seuraavat_siirrot(self, koordinaatit):
        '''Metodi poistaa annetut koordinaatit seuraavien mahdollisten siirtojen joukosta, ja lisää annettujen
        koordinaattien tyhjät naapurit seuraavien mahdollistojen siirtojen joukkoon'''
        if koordinaatit in self.siirrot:
            self.siirrot.remove(koordinaatit)
        for rivi in (-1, 0, 1):
            for sarake in (-1, 0, 1):
                if self.pelilauta[koordinaatit[0]+rivi][koordinaatit[1]+sarake] == '.':
                    self.siirrot.add(
                        (koordinaatit[0]+rivi, koordinaatit[1]+sarake))

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

        eka_rivi = max(rivi-4, 1)
        eka_sarake = max(sarake-4, 1)
        vika_rivi = min(rivi+5, 25)
        vika_sarake = min(sarake+5, 25)

        vaaka = 0
        for i in range(eka_sarake, vika_sarake):

            if self.pelilauta[rivi][i] == self.pelilauta[rivi][i+1] and self.pelilauta[rivi][i] != '.':
                vaaka += 1
                if vaaka == 4:
                    return self.pelilauta[rivi][i]
            else:
                vaaka = 0

        pysty = 0
        for i in range(eka_rivi, vika_rivi):
            if self.pelilauta[i][sarake] == self.pelilauta[i+1][sarake] and self.pelilauta[i][sarake] != '.':
                pysty += 1
                if pysty == 4:
                    return self.pelilauta[i][sarake]
            else:
                pysty = 0


        d1 = 0
        px = rivi - 4
        py = sarake - 4

        for i in range(9):
            if px > 0 and px < 26 and py > 0 and py < 26:
                if self.pelilauta[px][py] == self.pelilauta[px+1][py+1] and self.pelilauta[px][py] != '.':
                    d1 += 1
                    if d1 == 4:
                        return self.pelilauta[px][py]
                else:
                    d1 = 0
            px += 1
            py += 1

        d2 = 0

        px2 = rivi + 4
        py2 = sarake -4

        for i in range(9):
            if px2 > 0 and px2 < 26 and py2 > 0 and py2 < 26:
                if self.pelilauta[px2][py2] == self.pelilauta[px2-1][py2+1] and self.pelilauta[px2][py2] != '.':
                    d2 += 1
                    if d2 == 4:
                        return self.pelilauta[px2][py2]
                else:
                    d2 = 0
            px2 -= 1
            py2 += 1

        if self.siirtojen_lkm == 625:
            return 'tasapeli'

        return 'kesken'
