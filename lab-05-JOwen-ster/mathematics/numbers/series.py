def sum(*, list) -> int:
    sum : int = 0
    for number in list:
        sum += number
    return sum

from statistics import mean as avg
def average(*, list) -> float:
    return float(avg(list))




        