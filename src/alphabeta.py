from copy import deepcopy
from ristinolla import Ristinolla

class Alphabeta:

    def __init__(self):
        pass

    def minimax_ab(self, ristinolla, syvyys, alpha, beta):
        '''Minimax-algoritmi alpha-beta-karsinnalla
        '''
        if ristinolla.maksin_vuoro:
            return self.maksimi_ab(ristinolla, syvyys, alpha, beta)
        return self.minimi_ab(ristinolla, syvyys, alpha, beta)

    def maksimi_ab(self, ristinolla, syvyys, alpha, beta):
        loppu = ristinolla.tarkista_voitto()

        if loppu == 'X':
            return 1 ,0
        if loppu == '0':
            return -1, 0
        if loppu == 'Tasapeli':
            return 0, 0
        if syvyys == 0:
            return 0, 0

        arvo = -100

        for koordinaatit in ristinolla.siirrot:
            seuraava_siirto = koordinaatit
            kopio_peli = deepcopy(ristinolla)
            kopio_peli.lisaa_merkki(koordinaatit)
            kopio_peli.paivita_seuraavat_siirrot(koordinaatit)
            arvo = max(arvo, self.minimi_ab(kopio_peli, syvyys-1, alpha, beta)[0])
            if arvo >= beta:
                break
            alpha = max(alpha, arvo)
        #print('maksimi', arvo, seuraava_siirto)
        return [arvo, seuraava_siirto]


    def minimi_ab(self, ristinolla, syvyys, alpha, beta):
        loppu = ristinolla.tarkista_voitto()

        if loppu == 'X':
            return 1, 0
        if loppu == '0':
            return -1, 0
        if loppu == 'Tasapeli':
            return 0, 0
        if syvyys == 0:
            return 0, 0

        arvo = 100
        seuraava_siirto = 0
        for koordinaatit in ristinolla.siirrot:
            seuraava_siirto = koordinaatit
            kopio_peli = deepcopy(ristinolla)
            kopio_peli.lisaa_merkki(koordinaatit)
            kopio_peli.paivita_seuraavat_siirrot(koordinaatit)
            arvo = min(arvo, self.maksimi_ab(kopio_peli, syvyys-1, alpha, beta)[0])
            if arvo <= alpha:
                break
            beta = max(beta, arvo)
        #print('minimi', arvo, seuraava_siirto)
        return [arvo, seuraava_siirto]
