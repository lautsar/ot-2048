# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on tarjota 2048-peli. Pelissä pelaaja liikuttaa numeroituja laattoja pelilaudalla eri suuntiin. Tavoitteena on saavuttaa samanarvoisia laattoja yhdistelemällä mahdollisimman suuriarvoinen laatta. Kunkin siirron jälkeen laudalle asetetaan uusi numerolaatta. Peli päättyy, kun siirtoja ei enää ole mahdollista tehdä.

## Käyttäjät

Sovelluksella on vain yksi käyttäjärooli: peruskäyttäjä eli pelin pelaaja.

## Käyttöliittymäluonnos

**Aloitusnäkymä**

Aloitusnäkymällä on kaksi nappia: uusi peli ja tuloslista.

Jos käyttäjä aloittaa pelin, siirrytään pelinäkymälle. Jos käyttäjä haluaa katsoa tuloslistoja, siirrytään tulosnäkymälle.

**Pelinäkymä**

Kun peli on käynnissä, kerrotaan, että peli on käynnissä. Varsinainen peliruudukko avautuu omaan ikkunaan. Kun pelin suoritus päättyy, siirrytään yhteenvetonäkymälle.

**Yhteenvetonäkymä**

Yhteenvetonäkymällä näytetään pelatun pelin tulokset.

Pelaaja voi aloittaa uuden pelin, jolloin siirrytään takaisin pelinäkymälle. Pelaaja voi myös valita katsoa tuloslistoja, jolloin siirrytään tulosnäkymälle.

**Tulosnäkymä**

Tulosnäkymällä näytetään tuloksia jo pelatuista peleistä.


## Perusversion tarjoama toiminnallisuus
* Käyttäjän toiminnot
    * Käyttäjä voi halutessaan antaa nimimerkin ennen pelin aloitusta
        * Tällöin nimimerkki näytetään top-listalla
        * Jos käyttäjä ei anna nimimerkkiä, top-listalla ei näytetä nimeä
    * Käyttäjä voi valita peliruudukon koon annetuista vaihtoehdoista
    * Käyttäjä voi katsoa top-listaa
* Pelilliset toiminnot
    * Käyttäjä voi valita muutamasta eri kokoisesta peliruudukosta
    * Uuden pelin aloitus arpoo halutun kokoisen aloitusruudukon
    * Laattoja voi liikuttaa nuolinäppäimillä
    * Samanarvoiset laatat yhdistyvät ja niiden arvo kasvaa
    * Jos siirto toteutuu, arvotaan johonkin tyhjään ruutuun uusi laatta
    * Peli päättyy, kun laillisia siirtoja ei enää ole jäljellä
    * Pelin aikana pidetään kirjaa tehdyista siirroista
    * Pelin aikana pidetään kirjaa kertyneistä pisteistä
    * Pelin jälkeen näytetään kyseisen pelin tulokset
* Tuloslistan toiminnot
    * Sovellus pitää kirjaa pelattujen pelien pisteistä ja käytetyistä siirroista
    * Tuloslistalla voi tarkastella parhaita tuloksia