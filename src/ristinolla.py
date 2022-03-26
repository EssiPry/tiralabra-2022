class Ristinolla:

    def __init__(self):
        self.pelitilanne = [['.' for x in range(3)]for y in range(3)]
        self.AIn_vuoro = False

    def tulosta_pelitilanne(self):
        for i in range(3):
            for j in range(3):
                print(self.pelitilanne[i][j], end=" ")
            print("")
        print("")

    def onko_siirto_sallittu(self, rivi, sarake):
        if rivi < 0 or rivi > 2 or sarake < 0 or sarake > 2:
            return False
        if self.pelitilanne[rivi][sarake] == 'X' or self.pelitilanne[rivi][sarake] == '0':
            return False
        return True

    def lisaa_merkki(self, rivi, sarake, pelaaja):
        if self.onko_siirto_sallittu(rivi, sarake):
            if pelaaja == 'AI':
                self.pelitilanne[rivi][sarake] = '0'
            else:
                self.pelitilanne[rivi][sarake] = 'X'
        else:
            print('Valitse toinen ruutu')

    def paattyko_peli(self):
        for i in range(3):
            if self.pelitilanne [i] == ['X', 'X', 'X']:
                return 'X'
        for i in range(3):
            if self.pelitilanne [i] == ['0', '0', '0']:
                return '0'

        for i in range(3):
            if self.pelitilanne[0][i] != '.' and self.pelitilanne[0][i] == self.pelitilanne[1][i] and self.pelitilanne[1][i] == self.pelitilanne[2][i]:
                return self.pelitilanne[0][i]

        if self.pelitilanne[0][0]!= '.' and self.pelitilanne[0][0] == self.pelitilanne[1][1] and self.pelitilanne[1][1] == self.pelitilanne[2][2]:
            return self.pelitilanne[0][0]

        if self.pelitilanne[2][0]!= '.' and self.pelitilanne[2][0] == self.pelitilanne[1][1] and self.pelitilanne[1][1] == self.pelitilanne[0][2]:
            return self.pelitilanne[2][0]

        for i in range(3):
            for j in range(3):
                if self.pelitilanne[i][j] == '.':
                    return 'kesken'
        return 'tasapeli'

    def voitto(self, voittaja):
        if voittaja == 'X':
            return -1
        elif voittaja == '0':
            return 1
        elif voittaja == 'tasapeli':
            return 0

def minimax(self):
    pass

def suurin_arvo(self, ristinolla):
    if ristinolla.paattyyko_peli() != 'kesken':
        return ristinolla.voitto(ristinolla.paattyyko_peli())
    arvo = -100
    return arvo

def pienin_arvo(self, ristinolla):
    if ristinolla.paattyyko_peli != 'kesken':
        return ristinolla.voitto(ristinolla.paattyyko_peli())
    arvo = 100
    return arvo
