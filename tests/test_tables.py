#!/usr/bin/env python3

from context import utilities as util
import pandas as pd
import unittest

class TestUtilites(unittest.TestCase):

    def test_findDiameter(self):
        material = 'Music Wire'
        guage = '16'
        value = util.tables.find_guage_diameter(guage, material)
        self.assertEqual(value, 0.037)

if __name__ == "__main__":
    unittest.main()