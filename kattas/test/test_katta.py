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

        # Replace keys and values of _arabic_to_roman_test_cases and create new dictionary
        # as both are same.
        self._roman_to_arabic_test_cases = dict(zip(
            self._arabic_to_roman_test_cases.values(), self._arabic_to_roman_test_cases.keys()))

    def test_roman_to_arabic(self):
        """Test Roman to Arabic numeral conversion"""
        for input, expected in self._roman_to_arabic_test_cases.items():
            actual = kattas.convert_roman_to_arabic(input)
            self.assertEqual(expected, actual)

    def test_arabic_to_roman(self):
        """Test Arabic to Roman numeral conversion"""
        for input, expected in self._arabic_to_roman_test_cases.items():
            actual = kattas.convert_arabic_to_roman(input)
            self.assertEqual(expected, actual)

    def test_arabic_to_roman_wrong_type_exception(self):
        """Test arabic_to_roman raises exception in case of wrong input"""
        self.assertRaises(
            TypeError, kattas.convert_arabic_to_roman, "some_string_data")

    def test_roman_to_arabic_invalid_roman_exception(self):
        """Test roman_to_arabic raises exception in case of invalid roman"""
        self.assertRaises(
            ValueError, kattas.convert_roman_to_arabic, "invalid_roman_numerals")

        self.assertRaises(
            ValueError, kattas.convert_roman_to_arabic, 1343897)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
