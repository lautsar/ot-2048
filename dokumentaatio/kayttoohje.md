# Käyttöohje

## Ohjelman käynnistäminen

Asenna riippuvuudet ennen ohjelman käynnistämistä komennolla
```
poetry install
```
Sen jälkeen ohjelman voi käynnistää komennolla
```
poetry run invoke start
```
## Aloitusnäkymä

Peli aukeaa aloitusnäkymälle, jossa vaihtoehtoina on uuden pelin aloitus tai tuloslistan katselu.

## Uuden pelin aloitus

Uusi peli aloitetaan antamalla pelaajan nimi, valitsemalla peliruudukon koko ja painamalla "Start"-painiketta.

Pelaajan nimi ei ole pakollinen ja oletuskooksi on valittu 4x4.

## Pelin pelaaminen

Pelilauta aukeaa omaan ikkunaan. Pelilaudan laattoja voi liikuttaa nuolinäppäimillä.

## Tuloslistan tarkastelu

Tuloslistaa voi katsella painamalla päävalikosta "View"-nappulaa.

Tällä hetkellä tuloslista näyttää kymmenen parasta tulosta. Tulosjärjestyksen määrittää tällä hetkellä ensisijaisesti 
suurimman laatan arvo ja sen jälkeen tuloksen saavuttamiseksi käytettyjen siirtojen määrä.
