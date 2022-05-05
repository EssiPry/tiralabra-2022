class AlphaBeta:

    def __init__(self):
        pass

    def minimax_ab(self, ristinolla, syvyys, alpha, beta, vuoro, viimeisin_siirto, siirrot):
        '''Minimax-algoritmi alpha-beta-karsinnalla. Palauttaa annetun siirron arvon.
        '''
        #ristinolla.tulosta_pelitilanne()


        loppu = ristinolla.tarkista_voitto(
            viimeisin_siirto[0], viimeisin_siirto[1])

        #print('viimeisin siirto', viimeisin_siirto, 'loppu', loppu)
        if loppu == 'X':
            return 10
        if loppu == '0':
            return -10
        if syvyys == 0:
            return 0

        if vuoro is True:
            arvo = -100
            for koordinaatit in siirrot:
                klooni_siirrot = set(siirrot)
                print('max lisäyskoordinaatit', koordinaatit)
                ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = 'X'
                klooni_siirrot.remove(koordinaatit)
                ristinolla.paivita_mahdolliset_siirrot(
                    koordinaatit, klooni_siirrot)

                #print('koordinaatit', koordinaatit)
                #print('siirrot', klooni_siirrot)
                vertailu = self.minimax_ab(
                    ristinolla, syvyys-1, alpha, beta, False, koordinaatit, klooni_siirrot)
                arvo = max(arvo, vertailu)
                #print('max poistokoordinaatit', koordinaatit)
                ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '.'
                #print('max', 'arvo', arvo, 'alpha', alpha, 'beta', beta)
                if arvo > beta:
                    #print('max', 'arvo', arvo, 'alpha', alpha, 'beta', beta)
                    break
                #print('maksimi', 'alpha', alpha, 'beta', beta,'arvo', arvo, 'siirto', seuraava_siirto)
                alpha = max(alpha, arvo)
            return arvo

        else:
            arvo = 100

            for koordinaatit in siirrot:
                klooni_siirrot = set(siirrot)
                #print('min lisäyskoordinaatit', koordinaatit)
                ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '0'
                klooni_siirrot.remove(koordinaatit)
                ristinolla.paivita_mahdolliset_siirrot(
                    koordinaatit, klooni_siirrot)
                #print('siirrot', klooni_siirrot)
                vertailu = self.minimax_ab(
                    ristinolla, syvyys-1, alpha, beta, True, koordinaatit, klooni_siirrot)
                arvo = min(arvo, vertailu)
                #print('min poistokoordinaatit', koordinaatit)
                ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '.'
                #print('min', 'arvo', arvo, 'alpha', alpha, 'beta', beta)
                if arvo < alpha:
                    #print('arvo', arvo, 'alpha', alpha)
                    break
                #print('minimi', 'alpha', alpha, 'beta', beta, 'arvo', arvo, 'siirto', seuraava_siirto)
                beta = min(beta, arvo)
            return arvo
