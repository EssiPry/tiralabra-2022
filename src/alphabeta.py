class AlphaBeta:

    def __init__(self):
        pass

    def minimax_ab(self, ristinolla, syvyys, alpha, beta, vuoro, viimeisin_siirto, siirrot):
        '''Minimax-algoritmi alpha-beta-karsinnalla. Palauttaa annetun siirron arvon.
        '''

        loppu = ristinolla.tarkista_voitto(
            viimeisin_siirto[0], viimeisin_siirto[1])

        if loppu == 'X':
            return 10 + syvyys
        if loppu == '0':
            return -10 + (-syvyys)
        if syvyys == 0:
            return 0

        # maksin vuoro
        if vuoro is True:
            arvo = -100
            for koordinaatit in reversed(siirrot):
                kloonisiirrot = list(siirrot)
                ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = 'X'
                kloonisiirrot.remove(koordinaatit)
                ristinolla.paivita_mahdolliset_siirrot(
                    koordinaatit, kloonisiirrot)

                vertailu = self.minimax_ab(
                    ristinolla, syvyys-1, alpha, beta, False, koordinaatit, kloonisiirrot)
                arvo = max(arvo, vertailu)
                ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '.'
                if arvo > beta:
                    break
                alpha = max(alpha, arvo)
            return arvo

        # minin vuoro
        arvo = 100

        for koordinaatit in reversed(siirrot):
            kloonisiirrot = list(siirrot)
            ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '0'
            kloonisiirrot.remove(koordinaatit)
            ristinolla.paivita_mahdolliset_siirrot(
                koordinaatit, kloonisiirrot)
            vertailu = self.minimax_ab(
                ristinolla, syvyys-1, alpha, beta, True, koordinaatit, kloonisiirrot)
            arvo = min(arvo, vertailu)
            ristinolla.pelilauta[koordinaatit[0]][koordinaatit[1]] = '.'
            if arvo < alpha:
                break
            beta = min(beta, arvo)
        return arvo
