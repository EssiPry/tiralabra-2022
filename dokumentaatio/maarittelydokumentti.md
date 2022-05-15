### Määrittelydokumentti

#### Projekti - Ristinolla

Projektin tarkoituksena on kehittää tekoäly, jota vastaan voi pelata ristinollaa 25x25 pelilaudalla. Ristinollassa pelaaja ja tekoäly asettavat pelilaudalle vuorotellen oman merkkinsä X tai 0. Se kumpi saa ensin viiden suoran voittaa pelin.

Tekoälyn valitsee optimaalisen siirron käyttämällä minimax-algoritmia, jota tehostetaan alpha-beta -karsinnalla. Algoritmi saa syötteenä sen hetkisen pelitilanteen. Sen hetkinen pelitilannetta ajatellaan puun juurena. Algoritmi käy läpi mahdollisia siirtoja tiettyyn syvyyteen asti, arvioi eri mahdolliset pelitilanteet ja valitsee niistä mahdollisimman hyvältä vaikuttavan tuloksen. Algoritmin toimimisen oletuksena on, että pelaaja asettaa merkkinsä pelilaudalle mahdollisimman hyvin. Jos pelajaa asettaa merkkinsä satunnaisesti, algoritmi ei toimi kovin hyvin.

#### Aika- ja tilavuusarvio

Minimaxin aikavaativuus on O(b^m) ja tilavaativuus on O(bm), missä b on mahdollisten siirtojen määrä ja m on syvyys.

Alpha-beta karsinnalla pahimman tapauksen aikavaativuus on sama kuin minimaxin eli O(b^m), mutta jos algoritmi valitsee aina parhaan mahdollisen polun, jolla 'turhia' haaroja saadaan karsittua aikavaativuus voi parantua O(b^m/2).

#### Kielet

* ohjelmointikieli: python
* projektin kieli: suomi
* vertaisarviointi myös englanniksi

#### Opinto-ohjelma

* opinto-ohjelma: tietojenkäsittelytieteen kandi

#### Lähteet:

* [Abdolsaheb, A. [2020] How to make your Tic Tac Toe game unbeatable by using the minimax algorithm](https://www.freecodecamp.org/news/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37/)
* [Java  T point - Mini-Max Algorithm in Artificial Intelligence](https://www.javatpoint.com/mini-max-algorithm-in-ai)
* [Java T Point - Alpha-beta pruning](https://www.javatpoint.com/ai-alpha-beta-pruning)how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37)
* [Levine, J.[2017] - Minimax with Alpha Beta Pruning (Youtube-video)](https://www.youtube.com/watch?v=zp3VMe0Jpf8)
* [Laaksonen, A. [2021] Tietorakenteet ja algoritmit](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)
* [Roos, T. [2021] Introduction to AI - 2.2. Minimax-algorithm](https://materiaalit.github.io/intro-to-ai/part2/)
