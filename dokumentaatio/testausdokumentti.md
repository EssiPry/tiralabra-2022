## Testausdokumentti

### Testikattavuus

tähän tulee kuva testikattavuus-raportista.

### Testaus

Ristinolla- ja alphabeta-luokkia on testattu yksikkötesteilla. Alphabeta-luokkaa testatessa algoritmille on annettu erilaisia pelitilanteita, joiden avulla testataan löytääkö algoritmi optimaalisen siirron. Algoritmin palauttamaan siirtoa verrataan optimisiirtoon.



Yksikkötestien lisäksi Alphabeta-luokkaa on testattu manuaalisesti pelaamalla bottia vastaan.

Pelilooppia on testattu manuaalisesti ja tämä on todettu toimivaksi. Peli hyväksyy koordinaateiksi ainoastaan numerot 1-25 välillä. Liian suurten tai pienten lukujen, tai kirjainten antaminen koordinaateiksi ei kaada ohjelmaa.

Lisäksi ristinolla-, alphabeta- ja pelilooppi-luokkien oikeellisutta on testattu kehityksen aikana useilla debuggaus-printeillä.

### Mahdollisten siirtojen määrä ja botin siirron laskentaan kulunut aika

Mahdollisten siirtojen lukumäärä vaikuttaa botin optimaalisen siirron laskenta-aikaan. Jos mahdollisia siirtoja on enemmän kuin 20, eikä botilla ole 'optimaalista' siirtoa, eli botti voisi estää toisen pelaajan kolmen suoran tai voisi jatkaa omaa kolmen tai neljän suoraa, siirron löytyminen hidastuu huomattavasti. Jos optimaalinen siirto on olemassa, algoritmin alpha-beta valitsee sen ja karsii loput läpikäytävät siirrot, joka nopeuttaa algoritmin toimintaa.

Alla muutama esimerkki siirtojen määräästä ja kuinka kauan botilla menee sopivan siirron löytämiseen (s).

Peli 1 - diagonaali alku

| Siirto | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :---  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Mahdollisten siirtojen lkm | 8 | 15 | 20 | 23 | 24 | 26 | 27 | 26 |
| Aika (sekunti) | 5.48 | 41.09 | 54.03 | 166.89 | 58.06 | 42.07 | 367.67 | 40.06 |

Peli 2 - riviin pelattu alku

| Siirto | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :---  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Mahdollisten siirtojen lkm | 8 | 12 | 14 | 16 | 22 | 26 | 33 | 34 | 41 |
| Aika (sekunti) | 5.74 | 22.24 | 12.33 | 53.05 | 191.29 | 120.38 | 100.57 | 1299.98 | 3300.2 |


### Testin suorittaminen

Ohjelman yksikkötestit voi suorittaa komennolla

```bash
poetry run invoke test
```

Testikattavuusraportin saa luotua komennolla

```bash
poetry run invoke coverage-report
```

Raportti generoituu htmlcov -kansioon.

Huom. testikattavuusraportin generointi kestää n. 4-5 minuuttia.
