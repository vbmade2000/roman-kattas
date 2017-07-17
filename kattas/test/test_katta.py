"""Module contains tests for Katta module methods"""
import unittest
from kattas import kattas 

class TestKatta(unittest.TestCase):

    def setUp(self):
        self._arabic_to_roman_test_cases = {
            1: "I",
            3: "III",
            9: "IX",
            1066: "MLXVI",
            1989: "MCMLXXXIX"
        }

    def test_roman_to_arabic(self):
        pass
  
    def test_arabic_to_roman(self):
        """Test Arabic to Roman numeral conversion"""
        for input, expected in self._arabic_to_roman_test_cases.items():
            actual = kattas.convert_arabic_to_roman(input)
            self.assertEqual(expected, actual)

    def test_arabic_to_roman_wrong_type_exception(self):
        """Test arabic_to_roman raises exception in case of wrong input"""
        self.assertRaises(TypeError, kattas.convert_arabic_to_roman, "some_string_data")    

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
