from copy import deepcopy

class AlphaBeta:

    def __init__(self):
        pass

    def minimax_ab(self, ristinolla, syvyys, alpha, beta, vuoro, viimeisin_siirto, siirrot):
        '''Minimax-algoritmi alpha-beta-karsinnalla
        '''
        loppu = ristinolla.tarkista_voitto(viimeisin_siirto[0], viimeisin_siirto[1])
        if loppu == 'X':
            return 10, 0
        if loppu == '0':
            return -10, 0
        if syvyys == 0:
            return 0, 0

        if vuoro is True:
            arvo = -100
            for koordinaatit in siirrot:
                seuraava_siirto = koordinaatit
                klooni_siirrot = set(siirrot)
                ristinolla.pelilauta[seuraava_siirto[0]][seuraava_siirto[1]] = 'X'
                ristinolla.poista_koordinaatit_seuraavista_siirroista(seuraava_siirto, klooni_siirrot)
                ristinolla.paivita_seuraavat_siirrot(seuraava_siirto, klooni_siirrot)

                #ristinolla.tulosta_pelitilanne()
                arvo = max(arvo, self.minimax_ab(ristinolla, syvyys-1, alpha, beta, False, seuraava_siirto, klooni_siirrot)[0])
                ristinolla.pelilauta[seuraava_siirto[0]][seuraava_siirto[1]] = '.'
                ristinolla.lisaa_koordinaatit_seuraaviin_siirtoihin(seuraava_siirto, klooni_siirrot)
                if arvo > beta:
                    print('beta', beta,'arvo', arvo, koordinaatit)
                    break
                alpha = max(alpha, arvo)
            #print('maksimi', arvo, seuraava_siirto)
            return [arvo, seuraava_siirto]
        else:
            arvo = 100
            for koordinaatit in siirrot:
                seuraava_siirto = koordinaatit
                klooni_siirrot = set(siirrot)
                ristinolla.pelilauta[seuraava_siirto[0]][seuraava_siirto[1]] = '0'
                ristinolla.poista_koordinaatit_seuraavista_siirroista(seuraava_siirto, klooni_siirrot)
                ristinolla.paivita_seuraavat_siirrot(seuraava_siirto, klooni_siirrot)

                #ristinolla.tulosta_pelitilanne()

                arvo = min(arvo, self.minimax_ab(ristinolla, syvyys-1, alpha, beta, True, seuraava_siirto, klooni_siirrot)[0])
                ristinolla.pelilauta[seuraava_siirto[0]][seuraava_siirto[1]] = '.'
                ristinolla.lisaa_koordinaatit_seuraaviin_siirtoihin(seuraava_siirto, klooni_siirrot)
                if arvo < alpha:
                    seuraava_siirto = viimeisin_siirto
                    print('alpha', alpha,'arvo', arvo, koordinaatit)
                    break
                beta = min(beta, arvo)
            #print('minimi', arvo, seuraava_siirto)
            return [arvo, seuraava_siirto]
