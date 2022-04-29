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
                klooni_siirrot = set(siirrot)
                ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = 'X'
                klooni_siirrot.remove(koordinaatit)
                ristinolla.paivita_mahdolliset_siirrot(koordinaatit, klooni_siirrot)
                vertailu, seuraava_siirto = self.minimax_ab(ristinolla, syvyys-1, alpha, beta, False, koordinaatit, klooni_siirrot)
                arvo = max(arvo, vertailu)
                ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '.'
                klooni_siirrot.add(koordinaatit)
                if arvo > beta:
                    seuraava_siirto = koordinaatit
                    break
                alpha = max(alpha, arvo)
            return [arvo, seuraava_siirto]

        arvo = 100
        for koordinaatit in siirrot:
            klooni_siirrot = set(siirrot)
            ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '0'
            klooni_siirrot.remove(koordinaatit)
            ristinolla.paivita_mahdolliset_siirrot(koordinaatit, klooni_siirrot)
            vertailu, seuraava_siirto = self.minimax_ab(ristinolla, syvyys-1, alpha, beta, False, koordinaatit, klooni_siirrot)
            arvo = min(arvo, vertailu)
            ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '.'
            klooni_siirrot.add(koordinaatit)
            if arvo < alpha:
                seuraava_siirto = koordinaatit
                break
            beta = min(beta, arvo)
        return [arvo, seuraava_siirto]
