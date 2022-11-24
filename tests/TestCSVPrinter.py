import unittest
from speciallecture.CSVPrinter import CSVPrinter
import sys
sys.path.append("/tests")


class TestCSVPrinter(unittest.TestCase):

    def test_read1(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertEqual(3, len(line))

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertEqual("value2B", line[1][1])

    def test_read3(self):
        try:
            printer = CSVPrinter("nothing.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            pass
