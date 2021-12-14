import unittest
import data.datahandling
import pygsheets

class TestDataHandling(unittest.TestCase):
    def setUp(self):
        self.datahandler = data.datahandling.DataHandling()
        self.datahandler.worksheet = self.datahandler.spreadsheet[1]
    
#    def test_add_line(self):
#        results = [1, 2, 3, 4]
#        self.datahandler.add_row(results)
    
    def test_import_data_gets_correct_number_of_rows(self):
        self.datahandler.import_data()

        self.assertEqual(len(self.datahandler.data), 15)
    
    def test_get_latest_returns_right_value(self):
        latest = {'name': 'Test 15', 'size': '5x5', 'moves': 93, 'biggest': 4}

        self.assertEqual(self.datahandler.get_latest_result(), latest)