import pygsheets

class DataHandling():
    def __init__(self):
        self.file = pygsheets.authorize(service_file='src/data/credentials.json')
        self.spreadsheet = self.file.open('data')
        self.worksheet = self.spreadsheet[0]

    def import_data(self):
        data = self.worksheet.get_all_records()
        for row in data:
            print(row)

    def add_row(self, results):
        self.worksheet.append_table(results)
