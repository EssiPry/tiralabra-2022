## Testausdokumentti

### Testikattavuus

tähän tulee kuva testikattavuus-raportista.

### Testaus

Ristinolla- ja alphabeta-luokkia on testattu yksikkötesteilla. Alphabeta-luokassa on toistaiseksi vasta yksi testi, näitä on tarkoitus lisätä. Yksikkötestien lisäksi Alphabeta-luokkaa on testattu manuaalisesti (vaihtelevin tuloksin) pelaamalla bottia vastaan.

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
