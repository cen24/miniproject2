import unittest

from CSVreader.csvreader import csvreader
from Statisticss.extendedstat import extendedstat

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.extendedstat = extendedstat()


    def test_zscore(self):

        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result2.csv').data

        for column in test_result:
            result_test = float(column['zscore'])
            z = float(column['zvalue4zscore'])

        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)


        self.assertEqual(round(self.extendedstat.zscore_(z,listx)), round(result_test))

    def test_samplevar(self):

        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result2.csv').data

        for column in test_result:
            result_test = float(column['samplevar'])


        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)


        self.assertEqual(round(self.extendedstat.samplevar(listx)), round(result_test))

    # def test_proportion(self):
    #
    #     test_data = csvreader('csvdata/Array3.csv').data
    #     test_result = csvreader('csvdata/Array3_result2.csv').data
    #
    #     for column in test_result:
    #         result_test = float(column['proportion'])
    #
    #     listx = []
    #
    #     for row in test_data:
    #         result = float(row['Array'])
    #         listx.append(result)
    #
    #     self.extendedstat.proportion_(5,6)
    #     self.assertEqual(round(self.extendedstat.result), round(result_test))

    def test_populationvar(self):

        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result2.csv').data

        for column in test_result:
            result_test = float(column['populationvar'])


        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)


        self.assertEqual(round(self.extendedstat.populationvar(listx)), round(result_test))

    def test_samplemean(self):

        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result2.csv').data

        for column in test_result:
            result_test = float(column['samplemean'])

        listx = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)


        self.assertEqual(round(self.extendedstat.samplemean(listx)), round(result_test))

    def test_population_correlation_coefficient(self):
        test_data = csvreader('csvdata/Array3.csv').data
        test_result = csvreader('csvdata/Array3_result2.csv').data

        for column in test_result:
            result_test = float(column['population_correlation_coefficient'])

        listx = []
        listy = []

        for row in test_data:
            result = float(row['Array'])
            listx.append(result)
            result2 = float(row['Array2'])
            listy.append(result2)

        self.assertAlmostEqual(float(self.extendedstat.population_correlation_coefficient_(listx,listy)), float(result_test))

    def test_pvalue(self):

        test_data = csvreader('csvdata/UnitArgument.csv').data
        test_result = csvreader('csvdata/Array3_result2.csv').data

        for column in test_result:
            result_test = float(column['pvalue'])

        for column in test_data:
            a = float(column['a'])
            b = float(column['b'])
            c = float(column['c'])
            d = float(column['d'])



        self.assertEqual(round(self.extendedstat.pvalue_(a,b,c,d)), round(result_test))

