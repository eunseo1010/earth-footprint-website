from . import emission_factors as ef
from .answer_values import digital_hours

def calculate_q5(answer):
    hours = digital_hours[answer]
    if hours == 0:
        return 0
    return hours * ef.DIGITAL_POWER_KW * ef.DIGITAL_ELECTRICITY
