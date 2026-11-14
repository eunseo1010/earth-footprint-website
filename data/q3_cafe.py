from . import emission_factors as ef
from .answer_values import cafe_cups

def calculate_q3(answer):
    cup = cafe_cups[answer]
    factor = ef.CAFE_CUP[cup]
    if factor == 0:
        return 0
    return factor * ef.CAFE_COUNT
