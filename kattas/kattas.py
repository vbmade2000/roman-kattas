#!/usr/bin/env python

import os
import re
import sys

def convert_roman_to_arabic(roman):
    """Converts Roman numerals to Arabic number equilvalents
       @param num: Roman numeral to convert
       @type num: str
       @rtype: int
       @return: Integer equivalent of Roman numeral
    """
    roman_numeral_pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    if not re.search(roman_numeral_pattern, str(roman)):
        raise ValueError("Invalid Roman numerals") 
    d = dict()
    d["I"] = 1
    d["IV"] = 4
    d["V"] = 5
    d["IX"] = 9
    d["X"] = 10
    d["XL"] = 40
    d["L"] = 50
    d["XC"] = 90
    d["C"] = 100
    d["CD"] = 400
    d["D"] = 500
    d["CM"] = 900
    d["M"] = 1000

    result = None
    try:
        result = d[roman[-1]]

        for i in range(len(roman)-2, -1, -1):
            if d[roman[i]] < d[roman[i+1]]:
                result -= d[roman[i]]
            else:
                result += d[roman[i]]
    except Exception as e:
        raise e
    return result

def convert_arabic_to_roman(num):
    """Converts Arabic number to Roman numerals equilvalents
       @param num: Arabic number to convert
       @type num: int
       @rtype: str
       @return: String containing Roman numerals
    """
    roman = ""
    roman_numerals = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numbers = [
        1000, 900, 500,  400, 100,  90,   50,  40,   10,   9,   5,    4,   1]
    try:
        for i in range(len(numbers)):
            while num >= numbers[i]:
                roman += roman_numerals[i]
                num = num - numbers[i]
    except Exception as e:
        raise e
    return roman



def _print_usage(error_msg=None):
    """ Prints usage
        @param error_msg: Error message to print
        @type error_msg: str
    """
    if error_msg:
        sys.stderr.write(error_msg + "\n")
        sys.stderr.write("-------------------------------------\n")
    sys.stderr.write(sys.argv[0] + " mode=<mode> <number>\n")
    sys.stderr.write("Mode=1 for Arabic to Roman conversion\n")
    sys.stderr.write("Mode=2 for Roman to Arabic conversion\n")
    sys.stderr.write(str(type(e)))


if __name__ == "__main__":
    exit_code = os.EX_OK
    try:
        conversion_mode = sys.argv[1].split("=")[1]
        result = None
        if conversion_mode == "1":
            # Mode is Arabic to Roman conversion
            result = convert_arabic_to_roman(int(sys.argv[2]))
        else:
            # Mode is Roman to Arabic conversion
            result = convert_roman_to_arabic(sys.argv[2])
        sys.stdout.write(str(result))
        sys.stdout.write("\n")
        sys.stdout.flush()
    except IndexError:
        exit_code = os.EX_USAGE
        _print_usage("Too few arguments supplied")
    except ValueError:
        exit_code = os.EX_DATAERR
        _print_usage("Incorrect input format found")
    except Exception as e:
        exit_code = os.EX_SOFTWARE
        _print_usage("Internal error occured")
    finally:
        sys.exit(exit_code)
