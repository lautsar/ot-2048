# 2048-peli

Tämä on kurssin *TKT20002 Ohjelmistotekniikka* harjoitustyö. Sovellus on 2048-peli.

2048-pelin tavoitteena on yhdistää pelilaudalla olevia laattoja. Samanarvoiset laatat yhdistyvät ja niiden arvo kasvaa. Tavoitteena on saada
mahdollisimman suuriarvoinen laatta. Peli päättyy, kun siirtoja ei enää ole mahdollista tehdä. 

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

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
