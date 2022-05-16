## Käyttöohje

### Pelin asennus

Ennen kuin käynnistät pelin ensimmäistä kertaa, asenna riippuvuudet komennolla:

```bash
poetry install
```

### Pelin käynnistäminen

Asennuksen ja alustustoimenpiteiden jälkeen voit käynnistää pelin komennolla:

```bash
poetry run invoke start
```
### Pelaaminen

Pelissä on tekstikäyttöliittymä.

![Ristinolla tekstikäyttäliittymä](https://github.com/EssiPry/tiralabra-2022/blob/main/dokumentaatio/kuvat/ristinolla.png)

Pelaaja aloittaa pelin. Pelaajan merkki on '0' ja botin merkki on 'X'.

### Ohjelman testaus

```bash
poetry run invoke test
```

### Pylint

```bash
poetry run invoke lint
```
