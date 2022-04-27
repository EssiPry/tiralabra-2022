from copy import deepcopy

class AlphaBeta:

    def __init__(self):
        pass

    def minimax_ab(self, ristinolla, syvyys, alpha, beta, vuoro):
        '''Minimax-algoritmi alpha-beta-karsinnalla
        '''
        ristinolla.maksin_vuoro = vuoro
        loppu = ristinolla.tarkista_voitto()
        if loppu == 'X':
            return 1, 0
        if loppu == '0':
            return -1, 0
        if loppu == 'Tasapeli':
            return 0, 0
        if syvyys == 0:
            return 0, 0

        if ristinolla.maksin_vuoro is True:
            arvo = -100
            for koordinaatit in ristinolla.seuraavat_siirrot:
                seuraava_siirto = koordinaatit
                ristinolla.lisaa_merkki(koordinaatit)
                #ristinolla.tulosta_pelitilanne()
                ristinolla.vaihda_vuoro()
                arvo = max(arvo, self.minimax_ab(ristinolla, syvyys-1, alpha, beta, False)[0])
                ristinolla.poista_merkki(koordinaatit)
                if arvo > beta:
                    break
                alpha = max(alpha, arvo)
            #print('maksimi', arvo, seuraava_siirto)
            return [arvo, seuraava_siirto]
        else:
            arvo = 100
            for koordinaatit in ristinolla.seuraavat_siirrot:
                seuraava_siirto = koordinaatit
                ristinolla.lisaa_merkki(koordinaatit)
                #ristinolla.tulosta_pelitilanne()
                ristinolla.vaihda_vuoro()
                arvo = min(arvo, self.minimax_ab(ristinolla, syvyys-1, alpha, beta, True)[0])
                ristinolla.poista_merkki(koordinaatit)
                if arvo < alpha:
                    break
                beta = min(beta, arvo)
            #print('minimi', arvo, seuraava_siirto)
            return [arvo, seuraava_siirto]
