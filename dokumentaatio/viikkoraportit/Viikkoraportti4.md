### Viikkoraportti 4

---

Tämä viikko on valitettavasti jatkunut samoissa tunnelmissa kuin edellinen eli koronassa. Väsymys ja aivosumu ovat hidastaneet projektin etenemistä, mutta jotain edistystä on tapahtunut.

Muutin ruudukon vihdoin 25x25 kokoiseksi ja lisäsin siihen reunat. Tein voitontarkistuksen, jossa hyödynnetään viimeistä lisättyä siirtoa. Diagonaali voitontarkistus kaipaa vielä hiomista ja testausta. Tällä hetkellä diagonaali voitontarkistus menee reunojen yli ja voi antaa index out of range -virheen, joka kaataa ohjelman.

Aloitin minimax-algoritmin kirjoittamisen, mutta se on vielä kesken. En ole ehtinyt testata algoritmia kunnolla ja tämä ei onnistu ennen kuin diagonaali voitontarkistus toimii. Algoritmi käy läpi kahden viimeisimmän siirron naapurit ja valitsee niistä parhaan. Tähän parhaan siirron evaluointiin pitäisi varmaakin lisätä heuristiikkaa sillä nyt kaikki siirrot, joilla kumpikaan pelaaja ei voita peliä ovat samanarvoisia. Pitää myös testata miten syvyys vaikuttaa pelin kulkuun ja mikä olisi sopiva syvyys, että botti joskus voittaisi, mutta oikean vaihtoehdon löytäminen ei kestäisi liian pitkään.

Lisäksi aloitin yksikkötestin kirjoittamisen ja lisäsin koodin kommentoinnin. Pitääkö testi kommentoida vai riittääkö, että muu koodi on kommentoitu? Tein myös alustavan peliloopin mainiin, jossa botit pelaavat toisiaan vastaan, mutta tämä päättyy Unbound Local Erroriin, jota en ole vielä ehtinyt jäljittää.

##### Seuraavaksi:

* diagonaali voitontarkistuksen korjaaminen
* algoritmin työstäminen, heuristiikan lisääminen?
* käyttöliittymän suunnittelu & koodaaminen
* peliloopin suunnittelu & koodaaminen
* lisää testien kirjoittamista
* codecoviin tutustuminen + sen lisääminen
* testausdokumentin aloittaminen

---

Käytetyt tunnit 20h