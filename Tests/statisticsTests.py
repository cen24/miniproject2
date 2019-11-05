import unittest

from Statisticss.statisticss import statisticss
from Statisticss.extendedstat import extendedstat

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statisticss = statisticss()
        self.extendedstat = extendedstat()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statisticss, statisticss)

    def test_median(self):
        self.statisticss.median_(self.statisticss.list)
        self.assertEqual(self.statisticss.result, 3)

    def test_mode(self):
        self.statisticss.mode_(self.statisticss.list_mode)
        self.assertEqual(self.statisticss.result, 2)

    def test_mean(self):
        self.statisticss.mean_(self.statisticss.list)
        self.assertEqual(self.statisticss.result, 3)

    def test_stdev(self):
        self.statisticss.stdev_(self.statisticss.list)
        self.assertEqual(self.statisticss.result, 1.5811388300841898)

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
