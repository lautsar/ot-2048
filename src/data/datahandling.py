import operator
import pygsheets

class DataHandling():
    def __init__(self):
        self.file = pygsheets.authorize(service_file='src/data/credentials.json')
        self.spreadsheet = self.file.open('data')
        self.worksheet = self.spreadsheet[0]
        self.data = []

    def show_data(self):
        if len(self.data) == 0:
            self.import_data()

        self.sort_data()

    def import_data(self):
        self.data = self.worksheet.get_all_records()

    def add_row(self, results):
        self.worksheet.append_table(results)

    def sort_data(self):
        self.import_data()
        self.data.sort(key=operator.itemgetter('moves'))
        self.data.sort(key=operator.itemgetter('biggest'), reverse=True)

        for i in range(10):
            print(self.data[i])

    def print_all_data(self):
        for row in self.data:
            print(row)

    def get_latest_result(self):
        self.import_data()

        return self.data[len(self.data) - 1]
