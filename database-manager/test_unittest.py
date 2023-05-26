import unittest
import logging
import logging.config

import query
import pandas as pd
import openpyxl


from config import read_configuration
config = read_configuration()


class Test_PDF_Naming_And_Path(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_equals(self):
        # there are more than 30 assert methods
        self.assertEqual("string", "string")

# def suite():
#     suite = unittest.TestSuite()
#     runner = unittest.TestResult()
#     suite.addTest(unittest.makeSuite(Test_PDF_Naming_And_Path))
#     runner = unittest.TextTestRunner()
#     print(runner.run(suite))
# suite()


if __name__ == '__main__':
    unittest.main()
