# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on tarjota 2048-peli. Pelissä pelaaja liikuttaa numeroituja laattoja pelilaudalla eri suuntiin. Tavoitteena on saavuttaa samanarvoisia laattoja yhdistelemällä mahdollisimman suuriarvoinen laatta. Kunkin siirron jälkeen laudalle asetetaan uusi numerolaatta. Pelaaja voittaa, jos hän saa yhdistettyä Peli päättyy, jos siirtoja ei enää ole mahdollista tehdä.

## Käyttäjät

Sovelluksella on vain yksi käyttäjärooli: peruskäyttäjä eli pelin pelaaja.

## Käyttöliittymä

**Aloitusnäkymä**

Aloitusnäkymällä on kaksi nappia: uusi peli ja tuloslista.

Jos käyttäjä aloittaa uuden pelin, peliruudukko aukeaa omaan ikkunaan. Kun pelin suoritus päättyy, siirrytään yhteenvetonäkymälle.

Jos käyttäjä haluaa katsoa tuloslistoja, siirrytään tulosnäkymälle. 

**Yhteenvetonäkymä**

Yhteenvetonäkymällä näytetään juuri pelatun ja päättyneen pelin tulokset.

Pelaaja voi tältä näkymältä siirtyä nappia painamalla takaisin etusivulle. Pelaaja voi myös valita katsoa tuloslistoja, jolloin siirrytään tulosnäkymälle.

**Tulosnäkymä**

Tulosnäkymällä näytetään tuloksia jo pelatuista peleistä.


## Perusversion tarjoama toiminnallisuus
* Yksinkertainen graafinen käyttöliittymä
* Käyttäjän toiminnot
    * Käyttäjä voi aloittaa uuden pelin
        * Käyttäjä voi halutessaan antaa nimimerkin ennen pelin aloitusta
            * Tällöin nimimerkki näytetään top-listalla
            * Jos käyttäjä ei anna nimimerkkiä, top-listalla ei näytetä nimeä
        * Käyttäjä voi valita peliruudukon koon annetuista vaihtoehdoista
    * Käyttäjä voi katsoa top-listaa
* Pelilliset toiminnot
    * Uuden pelin aloitus arpoo halutun kokoisen aloitusruudukon
    * Laattoja voi liikuttaa nuolinäppäimillä
    * Samanarvoiset laatat yhdistyvät ja niiden arvo kasvaa
    * Jos siirto toteutuu, arvotaan johonkin tyhjään ruutuun uusi laatta
    * Peli päättyy, kun laillisia siirtoja ei enää ole jäljellä
    * Peli päättyy, jos pelaaja saa 2048-arvoisen laatan
    * Pelin aikana pidetään kirjaa tehdyista siirroista
    * Pelin jälkeen näytetään kyseisen pelin tulokset
* Tuloslistan toiminnot
    * Sovellus pitää kirjaa pelattujen pelien tuloksista
    * Tulokset tallennetaan
    * Tuloslistalla voi tarkastella top 10 -tuloksia

## Jatkokehitysideoita
* Tietoturvallisempi tapa tallentaa tietoja
* Monipuolisempi pisteenlasku
* Monipuolisemmat tavat tarkastella tuloksia
