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

### Ohjelman testaus

```bash
poetry run invoke test
```

### Pylint

```bash
poetry run invoke lint
```

Pelissä on tekstikäyttöliittymä. Pelaaja aloittaa pelin. Pelaajan merkki on '0' ja botin merkki on 'X'.
