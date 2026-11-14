from . import emission_factors as ef
from .answer_values import heating_hours

def calculate_q6(answer):
    hours = heating_hours[answer]
    if hours == 0:
        return 0
    return hours * ef.HEATING_POWER_KW * ef.HEATING_ELECTRICITY
