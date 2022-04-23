### Viikkoraportti 5

---

Ohjelma on edistynyt hitaasti ja hiukan jännittää, että saanko projektia valmiiksi ajoissa.

Tällä viikolla sain diagonaali voitontarkistuksen toimimaan ja tehtyä sille testit. Lisäsin ristinolla -luokkaan joukon (set), joka pitää kirjaa botin seuraavista mahdollisista siirroista. Päädyin käyttämään settiä, sillä jokainen koordinaattipari halutaan käydä läpi vain kerran, joten settiä käyttämällä ei tarvitse miettiä, tuleeko vahingossa tuplia (eli onko lisättävä koordinaattipari jo setissä).

Aloitin käyttöliittymän tekemisen. Nyt pelaaja voi pelata bottia vastaan, mutta botti on vielä tyhmä, eikä voita peliä tai pääse edes tasapeliin. Pikaisella debug-printtauksella näyttää, että minimi_ab- tai maksimi_ab -algoritmissä on joku virhe, mutta en vielä tiedä mikä. Tämän selvittäminen ja korjaaminen on seuraava askel. Sen jälkeen pitäisi korjata algoritmia niin ettei se käytä kopiota vaan tekee ja poistaa siirrot pelattavalta laudalta. Siirron poistamine laudalta -metodi on jo valmis ja toimii, mutta seuraavien siirtojen päivittäminen edestakaisin puuttuu vielä.

Käyttöliittymään pitäisi ehkä lisätä botti vs. botti vaihtoehto, jota voisi esitellä demossa.

Tein myös vertaisarvioinnin. Oli mielenkiintoista tutustua muiden koodiin.

##### Seuraavaksi:

* algoritmin
* algoritmin muokkaaminen niin, että ei käytä kopiota
* lisää testien kirjoittamista
* refaktorointia
* codecoviin tutustuminen + sen lisääminen
* toteutusdokumentin kirjoittaminen

---

Käytetyt tunnit 20h
