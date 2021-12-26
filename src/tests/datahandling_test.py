import unittest
import data.datahandling
import pygsheets

class TestDataHandling(unittest.TestCase):
    def setUp(self):
        self.datahandler = data.datahandling.DataHandling()
        self.datahandler.worksheet = self.datahandler.spreadsheet[1]
        self.datahandler.worksheet.delete_rows(17, 5)
    
    def test_import_data_gets_correct_number_of_rows(self):
        self.datahandler.import_data()

        self.assertEqual(len(self.datahandler.data), 15)
    
    def test_get_latest_returns_right_value(self):
        latest = {'name': 'Test 15', 'size': '5x5', 'moves': 93, 'biggest': 4}

        self.assertEqual(self.datahandler.get_latest_result(), latest)

    def test_add_line_works(self):
        self.datahandler.import_data()
        self.assertEqual(len(self.datahandler.data), 15)

        results = [1, 2, 3, 4]
        self.datahandler.add_row(results)
        self.datahandler.import_data()
        self.assertEqual(len(self.datahandler.data), 16)
    
    def test_sort_data_works(self):
        self.datahandler.sort_data()
        number_1 = {'name': 'Test 14', 'size': '5x5', 'moves': 37, 'biggest': 2048}
        number_5 = {'name': 'Test 7', 'size': '4x4', 'moves': 40, 'biggest': 512}
        number_10 = {'name': 'Test 11', 'size': '5x5', 'moves': 25, 'biggest': 64}
        number_15 = {'name': 'Test 3', 'size': '3x3', 'moves': 98, 'biggest': 2}

        self.assertEqual(self.datahandler.data[0], number_1)
        self.assertEqual(self.datahandler.data[4], number_5)
        self.assertEqual(self.datahandler.data[9], number_10)
        self.assertEqual(self.datahandler.data[14], number_15)
    
    def test_get_top_10_works(self):
        top_list = self.datahandler.get_top_ten()

        number_1 = 'Test 14\t5x5\t37\t2048'
        number_5 = 'Test 7\t4x4\t40\t512'
        number_10 = 'Test 11\t5x5\t25\t64'

        self.assertEqual(top_list[0], number_1)
        self.assertEqual(top_list[4], number_5)
        self.assertEqual(top_list[9], number_10)

