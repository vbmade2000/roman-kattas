#!/usr/bin/env python

import os
import sys


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


def _print_usage():
    sys.stderr.write(sys.argv[0] + " <number>\n")
    sys.stdout.write(str(type(e)))

if __name__ == "__main__":
    exit_code = os.EX_OK
    try:
        sys.stdout.write(convert_arabic_to_roman(int(sys.argv[1])))
        sys.stdout.write("\n")
        sys.stdout.flush()
    except IndexError:
        exit_code = os.EX_USAGE
        _print_usage()
    except ValueError:
        exit_code = os.EX_DATAERR
        _print_usage()
    except Exception as e:
        sys.stderr.write(sys.argv[0] + " <number>\n")
        _print_usage()
    finally:
        sys.exit(exit_code)
