# 2048-peli

Tämä on kurssin *TKT20002 Ohjelmistotekniikka* harjoitustyö. Sovellus on 2048-peli.

2048-pelin tavoitteena on yhdistää pelilaudalla olevia laattoja. Samanarvoiset laatat yhdistyvät ja niiden arvo kasvaa. Tavoitteena on saada
mahdollisimman suuriarvoinen laatta. Peli päättyy, kun siirtoja ei enää ole mahdollista tehdä tai kun pelaaja saa 2048-arvoisen laatan ja
voittaa pelin. 

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

- [Käyttöohje](dokumentaatio/kayttoohje.md)

## Releaset

- [Viikko 5](https://github.com/lautsar/ot-2048/releases/tag/viikko5)
- [Viikko 6](https://github.com/lautsar/ot-2048/releases/tag/viikko6)

## Tunnistettuja puutteita (viikon 6 palautus)

* Tietoturvan kannalta kyseenalainen tapa tallentaa credentials-tiedot repoon. Riskit katsottu tämän kurssin puitteissa riittävän pieneksi.
* Graafista käyttöliittymää ei ole muotoiltu millään tavalla, vaan kaikki tiedot tulevat peräkkäin.

## Komentorivikomennot

Riippuvuudet voi asentaa komennolla
```
poetry install
```

Sovelluksen voi käynnistää komennolla
```
poetry run invoke start
```

Testit voi suorittaa komennolla
```
poetry run invoke test
```

Testikattavuusraportin voi muodostaa komennolla
```
poetry run invoke coverage-report
```
Raportti muodostuu *htmlcov*-hakemistoon

Tiedoston [.pylintrc](.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:
```
poetry run invoke lint
```
