## Toteutusdokumentti

### Ohjelman yleisrakenne

Ohjelma on toteuettu Python-kielellä (versio 3.8.10). Riippuvuuksien hallintaan on käytetty Poetrya.

Ohjelma on jaettu kolmeen luokkaan: ristinolla, alphabeta ja pelilooppi.

* Ristinolla-luokka luo pelilaudan ja huolehtii sallittujen siirrojen tarkistamisesta, voitontarkistuksesta, botin mahdollisten siirtojen päivittämisestä sekä pelilaudan tulostamisesta.
* Alphabeta -luokka toteuttaa minimax algoritmi alpha-beta karsinnalla.
* Pelilooppi huolehtii nimensä mukaisesti ristinolla-pelistä. Pelilooppi 'kysyy' vuorotellen pelaajalta ja botilta siirron koordinaatit, jonka jälkeen se kutsuu ristinolla luokan metodeja ja tekee siirroon, tulostaa päivitetyn pelitilanteen sekä päivittää botin mahdolliset siirrot -listaa.

Näiden luokkien lisäksi on main-luokka, joka käynnistää pelin.

### Saavutetut aika- ja tilavaativuudet:

Algoritmi taitaa toimia annettujen aikavaativuuksien puitteissa eli pahimman tapauksen O(b^m) ja parhaan tapauksen O(b^m/2), missä b on seuraavien mahdollisten siirtojen määrä ja m on maksimisyvyys. Koko ohjelman aikavaativuus on suurempi.

Algoritmin tilavaativuus on myös annettu O(bm), jossa b on mahdollisten siirtojen määrä ja m on maksimisyvyys. Mahdollisten siirtojen määrä kasvaa jokaisella syvyydellä (max 8 koordinaattiparia), kun mahdollisten siirtojen listaan lisätään uuden siirron tyhjät naapurit, mutta tämä ei vaikutta tilavaativuuteen magnituudiin.

### Työn mahdolliset puutteet ja parannusehdotukset:

Algoritmiä pitäisi optimoida. Se on hidas, varsinkin jos ja kun mahdollisten siirtojen määrä nousee yli 20, eikä botilla tai pelaajalla ole jo kolmen tai neljän suoraa. Botin tämän hetkinen voittostrategia on, että pelaaja kyllästyy odottamaan vuoroaan.

Tällä hetkellä minimaxissa käytettään syvyyttä 4 eli algoritmi tutkii molempien pelaajien kaksi seuraavaa siirtoa. Tämä tarkoittaa, että botti osaa estää pelaajaa saamasta viiden suoraa, mutta se ei osaa rakentaa itselleen voittavaa suoraa, ellei pelilaudalla ole jo kolmea botin merkkiä peräkkäin.

Syvyyden lisääminen lisäisi botin 'älykkyyttä', mutta se lisääminen myös hidastaa bottia, sillä tutkittavien tapausten määrä nousee eksponentiaalisesti (mahdolliset siirrot ^ syvyys).

Käyttöliittymä ei ole kovin käyttäjäystävällinen. Tätä voisi parantaa lisäämällä rivi- ja sarakenumerot pelilaudan tulostukseen, jotta halutun rivin ja sarakkeen löytäminen olisi nopeampaa.

### Lähteet:

* [Abdolsaheb, A. [2020] How to make your Tic Tac Toe game unbeatable by using the minimax algorithm](https://www.freecodecamp.org/news/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37/)
* [Levine, J.[2017] - Minimax with Alpha Beta Pruning (Youtube-video)](https://www.youtube.com/watch?v=zp3VMe0Jpf8)
* [Laaksonen, A. [2021] Tietorakenteet ja algoritmit](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)
* [Roos, T. [2021] Introduction to AI - Part 2 Games](https://materiaalit.github.io/intro-to-ai/part2/)
