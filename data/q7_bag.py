from . import emission_factors as ef
from .answer_values import bag_types

def calculate_q7(answer):
    bag = bag_types[answer]
    factor = ef.BAG[bag]
    if factor == 0:
        return 0
    return factor * ef.BAG_COUNT
