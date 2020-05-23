#!/usr/bin/env python3

from context import utilities as util
import pandas as pd
import unittest

class TestUtilites(unittest.TestCase):

    def test_importTable(self):
        testData = pd.read_csv(
            "artifacts/test_data/A-28.csv",
            header=0
        )
        column_title = testData.columns[0]
        testData.set_index(column_title, inplace=True)
        material = 'Music Wire'
        guage = '16'

        value = util.tables.lookup_property(testData, guage, material)

        self.assertEqual(value, 0.037)

if __name__ == "__main__":
    unittest.main()