class Ristinolla:

    def __init__(self):
        '''Luokan konstruktori'''
        self.pelilauta = [['.' for x in range(27)]for y in range(27)]
        self.maksin_vuoro = False

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

    def onko_sallittu_siirto(self, koordinaatit):
        '''Metodi tarkistaa voiko annetuille koordinaateille pelata merkkiä vai ei.
        Palauttaa True jos siirto on sallittu, False jos ei ole.'''
        rivi = koordinaatit[0]
        sarake = koordinaatit[1]
        if self.pelilauta[rivi][sarake] == '.':
            return True
        return False

    def paivita_mahdolliset_siirrot(self, koordinaatit, siirrot):
        '''Metodi lisää annettujen koordinaattien tyhjät naapurit seuraavien
        mahdollistojen siirtojen joukkoon.
        Palauttaa seuraavat siirrot listana. '''
        for rivi in (-1, 0, 1):
            for sarake in (-1, 0, 1):
                if self.pelilauta[koordinaatit[0]+rivi][koordinaatit[1]+sarake] == '.':
                    if (koordinaatit[0]+rivi, koordinaatit[1]+sarake) not in siirrot:
                        siirrot.append(
                            (koordinaatit[0]+rivi, koordinaatit[1]+sarake))
                    else:
                        siirrot.remove(
                            (koordinaatit[0]+rivi, koordinaatit[1]+sarake))
                        siirrot.append(
                            (koordinaatit[0]+rivi, koordinaatit[1]+sarake))
        return siirrot

    def tarkista_voitto(self, rivi, sarake):
        '''Metodi tarkistaa täydentääkö viimeisin siirto pelilaudalle 5 peräkkäistä samaa
        merkkiä eli voittaako siirto pelin. Metodi palauttaa voittavan merkin(str), tai tekstin kesken
        jos kumpikaan ei voita.
        '''

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

        diagonaali_1 = 0
        px = rivi - 4
        py = sarake - 4

        for i in range(9):
            if px > 0 and px < 26 and py > 0 and py < 26:
                if self.pelilauta[px][py] == self.pelilauta[px+1][py+1] and self.pelilauta[px][py] != '.':
                    diagonaali_1 += 1
                    if diagonaali_1 == 4:
                        return self.pelilauta[px][py]
                else:
                    diagonaali_1 = 0
            px += 1
            py += 1

        diagonaali_2 = 0

        px2 = rivi + 4
        py2 = sarake - 4

        for i in range(9):
            if px2 > 0 and px2 < 26 and py2 > 0 and py2 < 26:
                if self.pelilauta[px2][py2] == self.pelilauta[px2-1][py2+1] and self.pelilauta[px2][py2] != '.':
                    diagonaali_2 += 1
                    if diagonaali_2 == 4:
                        return self.pelilauta[px2][py2]
                else:
                    diagonaali_2 = 0
            px2 -= 1
            py2 += 1

        # if self.siirtojen_lkm == 625:
        #    return 'tasapeli'

        return 'kesken'
