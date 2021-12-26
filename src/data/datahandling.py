import operator
import pygsheets

class DataHandling():
    """Luokka, joka huolehtii tietojen tallennuksesta ja hausta Google Docs -tiedostosta.

    Attribuutit:
        file: Käytettävä yhteys
        spreadsheet: Käytettävä tiedosto
        worksheet: Käytettävä välilehti
        data: Tiedot vanhoista peleistä, haetaan tiedostosta
    """
    def __init__(self):
        """Luokan konstruktori, joka avaa yhteyden käytettävään tiedostoon.
        """
        self.file = pygsheets.authorize(service_account_file='src/data/credentials.json')
        self.spreadsheet = self.file.open('data')
        self.worksheet = self.spreadsheet[0]
        self.data = []

    def import_data(self):
        """Metodi, joka hakee kaikki tallennetut tiedot tiedostosta.
        """
        self.data = self.worksheet.get_all_records()

    def add_row(self, results):
        """Metodi, joka lisää viimeisimmän pelin tuloksen tiedostoon.

        Args:
            results: Lista, joka sisältää päättyneen pelin tulokset
        """
        self.worksheet.append_table(results)

    def sort_data(self):
        """Metodi, joka järjestää tiedostossa olevan datan top-listan näyttämistä varten.
        """
        self.import_data()
        self.data.sort(key=operator.itemgetter('moves'))
        self.data.sort(key=operator.itemgetter('biggest'), reverse=True)

    def get_top_ten(self):
        """Metodi hakee kymmenen parasta tulosta kutsumalla datan järjestämisestä huolehtivaa
        metodia ja tallentaa tulokset listaan.

        Returns:
            Lista kymmennestä parhaasta tuloksesta järjestyksessä.
        """
        self.sort_data()
        top_ten = []

        for i in range(10):
            result = list(self.data[i].values())
            top_ten.append(str(result[0]) + '\t' + str(result[1]) + '\t' + str(result[2]) +
                            '\t' + str(result[3]))

        return top_ten

    def get_latest_result(self):
        """Metodi, joka hakee viimeisimmän tallennetun tiedon.

        Returns:
            Dict-tyyppisen arvon, joka sisältää viimeisimmän pelin tulokset.
        """
        self.import_data()

        return self.data[len(self.data) - 1]
