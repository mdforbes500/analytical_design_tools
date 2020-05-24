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

    def test_MinimumTensileStrength(self):
        material = 'Music Wire'
        units = 'US Customary'
        d = 0.037
        tensile_strength = util.tables.find_tensile_strength(material, units, d)
        test_val = 201/0.037**0.145
        self.assertEqual(tensile_strength, test_val)
    
    def test_MaximumTensileStrength(self):
        material = 'Music wire and cold-drwan carbon steel'
        minimum_tensile_strength = 201/0.037**0.145
        maximum_tensile_strength = util.tables.find_maximum_tensile_strength(material, minimum_tensile_strength, set_removed=False)
        test_val = 0.45*minimum_tensile_strength
        self.assertEqual(maximum_tensile_strength, test_val)

if __name__ == "__main__":
    unittest.main()