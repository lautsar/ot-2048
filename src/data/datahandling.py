import pygsheets

class DataHandling():
    def __init__(self):
        self.file = pygsheets.authorize(service_file='src/data/credentials.json')
        self.spreadsheet = self.file.open('data')
        self.worksheet = self.spreadsheet[0]
        self.data = []
        self.new_added = False

    def show_data(self):
        if len(self.data) == 0:
            self.import_data()

        self.sort_data()

    def import_data(self):
        self.data = self.worksheet.get_all_records()

    def add_row(self, results):
        self.worksheet.append_table(results)
        self.new_added = True

    def sort_data(self):
        if self.new_added is True:
            self.import_data()

