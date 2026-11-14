from . import emission_factors as ef
from .answer_values import transport_types

def calculate_q1(answer):
    transport = transport_types[answer]
    factor = ef.TRANSPORT[transport]

    if factor == 0:
        return 0

    return factor * ef.TRANSPORT_DISTANCE_KM[transport] * ef.TRANSPORT_COUNT
