import unittest

from CSVreader.csvreader import csvreader
from Statisticss.statisticss import statisticss
from Statisticss.extendedstat import extendedstat

class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        self.statisticss = statisticss()
        self.extendedstat = extendedstat()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statisticss, statisticss)

    def test_median(self):
        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result.csv').data

        for column in test_result:
            result_test = float(column['Mean'])

        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)

        self.statisticss.median_(listx)
        self.assertEqual(self.statisticss.result, int(result_test))

    def test_mode(self):
        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result.csv').data

        for column in test_result:
            result_test = float(column['Mode'])

        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)

        self.statisticss.mode_(listx)
        self.assertEqual(self.statisticss.result, result_test)

    def test_mean(self):
        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result.csv').data

        for column in test_result:
            result_test = float(column['Mean'])


        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)


        self.statisticss.mean_(listx)
        self.assertAlmostEqual(self.statisticss.result, result_test)

    def test_stdev(self):
        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result.csv').data

        for column in test_result:
            result_test = float(column['Stdev'])

        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)

        self.statisticss.stdev_(listx)
        self.assertEqual(self.statisticss.result, result_test)

    #def test_zscore(self):
        #self.statisticss.zscore_(5, self.statisticss.list)
        #self.assertEqual(self.statisticss.result, 1.2649110640673518)

    # def test_prop(self):
    #     self.extendedstat.proportion(20, 4)
    #     self.assertAlmostEqual(self.statisticss.result, 5)

    def test_results_property(self):
        self.assertEqual(self.statisticss.result, 0)

if __name__ == '__main__':
    unittest.main()
