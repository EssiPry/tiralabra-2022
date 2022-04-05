class Ristinolla:

    def __init__(self):
        self.pelitilanne = [['.' for x in range(5)]for y in range(5)]
        self.AIn_vuoro = False
        self.viimeisin_siirto = None
        self.jaljella_olevat_siirrot = []

    def luo_jaljella_olevat_siirrot(self):
        siirrot = []
        for i in range(5):
            for j in range(5):
                siirrot.append((i,j))
        self.jaljella_olevat_siirrot = siirrot

    def paivita_jaljella_olevat_siirrot(self):
        if self.viimeisin_siirto in self.jaljella_olevat_siirrot:
            self.jaljella_olevat_siirrot.remove(self.viimeisin_siirto)

    def paivita_viimeisin_siirto(self, siirto):
        self.viimeisin_siirto = siirto

    def tulosta_pelitilanne(self):
        for i in range(5):
            for j in range(5):
                print(self.pelitilanne[i][j], end=" ")
            print("")
        print("")

    def onko_siirto_sallittu(self):
        rivi = self.viimeisin_siirto[0]
        sarake = self.viimeisin_siirto[1]
        if rivi < 0 or rivi > 5 or sarake < 0 or sarake > 5:
            return False
        if self.pelitilanne[rivi][sarake] == 'X' or self.pelitilanne[rivi][sarake] == '0':
            return False
        return True

    def lisaa_merkki(self, rivi, sarake):
        if self.onko_siirto_sallittu(rivi, sarake):
            if self.AIn_vuoro:
                self.pelitilanne[rivi][sarake] = '0'
            else:
                self.pelitilanne[rivi][sarake] = 'X'
        else:
            if not self.AIn_vuoro:
                print('Valitse toinen ruutu')

    def paattyko_peli(self):
        rivi = self.viimeisin_siirto[0]
        sarake = self.viimeisin_siirto[1]

        if self.pelitilanne[rivi] == ['X', 'X', 'X', 'X', 'X']:
                return 'X'
        if self.pelitilanne[rivi] == ['0', '0', '0', '0', '0']:
                return '0'

        if self.pelitilanne[0][sarake] != '.' and self.pelitilanne[0][sarake] == self.pelitilanne[1][sarake] and self.pelitilanne[1][sarake] == self.pelitilanne[2][sarake] and self.pelitilanne[2][sarake] == self.pelitilanne[3][sarake] and self.pelitilanne[3][sarake] == self.pelitilanne[4][sarake] :
                return self.pelitilanne[0][sarake]

        if self.pelitilanne[0][0] != '.' and self.pelitilanne[0][0] == self.pelitilanne[1][1] and self.pelitilanne[1][1] == self.pelitilanne[2][2] and self.pelitilanne[1][1] == self.pelitilanne[3][3] and self.pelitilanne[1][1] == self.pelitilanne[4][4]:
            return self.pelitilanne[0][0]

        if self.pelitilanne[4][0] != '.' and self.pelitilanne[4][0] == self.pelitilanne[3][1] and self.pelitilanne[4][0] == self.pelitilanne[2][2] and self.pelitilanne[4][0] == self.pelitilanne[1][3] and self.pelitilanne[4][0] == self.pelitilanne[0][4]:
            return self.pelitilanne[2][0]

        for i in range(5):
            for j in range(5):
                if self.pelitilanne[i][j] == '.':
                    return 'kesken'
        return 'tasapeli'

    def voitto(voittaja):
        if voittaja == 'X':
            return -1
        elif voittaja == '0':
            return 1
        return 0


def minimax():
    pass


def suurin_arvo(ristinolla):
    if ristinolla.paattyyko_peli() != 'kesken':
        return ristinolla.voitto(ristinolla.paattyyko_peli())
    arvo = -100
    return arvo


def pienin_arvo(ristinolla):
    if ristinolla.paattyyko_peli != 'kesken':
        return ristinolla.voitto(ristinolla.paattyyko_peli())
    arvo = 100
    return arvo
