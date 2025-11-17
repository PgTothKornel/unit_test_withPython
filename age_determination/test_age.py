##import unittest
import pytest

from age import categorize_by_age

#class TestCategorizeByAge(unittest.TestCase):
#    def test_child(self):
#        self.assertEqual(categorize_by_age(5), "Gyerek")
#        self.assertEqual(categorize_by_age(7), "Gyerek")
#        self.assertEqual(categorize_by_age(19), "Felnőtt")
#        self.assertEqual(categorize_by_age(130), "csal: 130")
#        self.assertEqual(categorize_by_age(66), "Nyugdíjas")
#        self.assertEqual(categorize_by_age(91), "DédSzülő")
#    def test_boundary_child(self):
#        self.assertEqual(categorize_by_age(18), "Felnőtt")
#        self.assertEqual(categorize_by_age(130), "csal: 130")

def test_age():
    assert categorize_by_age(120) == "csal: 120"
    assert categorize_by_age(66) == "Nyugdíjas"
    assert categorize_by_age(100) == "DédSzülő"
    assert categorize_by_age(9) == "Gyerek"
