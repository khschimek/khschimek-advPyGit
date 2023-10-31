import unittest
from cpo import getMean


class Test1(unittest.TestCase):
    def testA(self) -> None:
        firstNumber = 1
        secondLine = "1"
        self.assertEqual(1, getMean(firstNumber, secondLine))

    def testB(self) -> None:
        firstNumber = 2
        secondLine = "2 3"
        self.assertEqual(2, getMean(firstNumber, secondLine))

    def testC(self) -> None:
        firstNumber = 3
        secondLine = "6 4 5"
        self.assertEqual(5, getMean(firstNumber, secondLine))

    def testD(self) -> None:
        firstNumber = 3
        secondLine = "10 11 12"
        self.assertEqual(11, getMean(firstNumber, secondLine))

    def testE(self) -> None:
        firstNumber = 2
        secondLine = "90 30"
        self.assertEqual(60, getMean(firstNumber, secondLine))

    def testF(self) -> None:
        firstNumber = 1
        secondLine = "12345"
        self.assertEqual(12345, getMean(firstNumber, secondLine))
