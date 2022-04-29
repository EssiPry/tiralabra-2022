### Viikkoraportti 6

---

Ohjelma on edistynyt hiukan, tosin tehtyihin työtunteihin nähden todella vähän.

Alkuviikosta yritin selvittää miksi minimax ei toimi ja päädyin kirjoittamaan sen uusiksi niin, että min ja max eivät ole erillisiä metodeja. Kävin ohjauksessa keskiviikkona, jonka jälkeen tein muutoksia ristinolla- ja alphabeta-luokkiin.

Minimax-algoritmi toimii melkein, botti osaa nyt blokata toisen pelaajan voiton, mutta se ei osaa laittaa viittä omaa merkkiä peräkkäin. Tällä hetkellä jos minimax_ab palauttaa botin siirroksi 0 eli kumpikaan pelaaja ei voi vielä voittaa, peliloopissa arvotaan botille satunnainen siirto mahdollisten siirtojen joukosta. Tähän voisi lisätä esim. että botti laittaisi uuden siirron edellisen siirron vieraan tms, jotta viiden suora saattaisi joskus rakentua.

Algoritmi toimii jos syvyys on 2 tai 3, mutta jos syvyys on 4 tai enemmän tämä rikkoo algoritmin ja hidastaa toimintaa melko paljon. Onko tämä ongelma vai riittääkö, että algoritmi toimii vain tietyillä syvyyksillä?

Lisäksi mietin, että riittääkö ristinollalle yksikkötestaus ja manuaalinen testaus vai pitäisikö tähän lisätä suorituskykytestausta, jos niin millaista?

##### Seuraavaksi:

* syvyyden muuttamisen selvittäminen
* lisää testien kirjoittamista alphabeta-luokalle
* heuristiikan lisäämistä & muokkaamista
* refaktorointi, ehkä oma luokka apumetodeille?
* codecoviin tutustuminen + sen lisääminen
* toteutusdokumentin aloittaminen
* käyttöohjeiden täydentäminen

---

Käytetyt tunnit n. 20h
