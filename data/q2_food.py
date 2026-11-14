from . import emission_factors as ef
from .answer_values import food_orders

def calculate_q2(answer):
    count = food_orders[answer]
    if count == 0:
        return 0
    return count * (ef.DELIVERY_DISTANCE_KM * ef.DELIVERY + ef.PACKAGING)
