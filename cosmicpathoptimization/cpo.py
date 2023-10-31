import math


def getMean(firstNumber, secondLine) -> int:
    mean = 0
    numbers = map(int, secondLine.split())
    for i in numbers:
        mean += i
    mean = mean / firstNumber
    mean = math.floor(mean)
    return mean


if __name__ == "__main__":
    firstNumber = int(input())
    secondLine = str(input())
    result = getMean(firstNumber, secondLine)
    print(result)
