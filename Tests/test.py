import unittest

from CSVreader.csvreader import csvreader
from Statisticss.stattest import stattest

class MytestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = stattest()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, stattest)

    def test_data_property(self):
        self.assertEqual(self.statistics.data, [])

    def test_mean(self):

        test_data = csvreader('csvdata/list.csv').data
        result_data = csvreader('csvdata/list2.csv').data

        for row in test_data:

            result = result_data(row['v'])

            self.assertEqual(self.statistics.mean_(row['vresult'], result))

            self.assertEqual(self.statistics.result, row['v'])


    def test_instantiate_statistical_calculator(self):
        self.assertIsInstance(self.statistics, stattest)

if __name__ == '__main__':
    unittest.main()


#to be deleted