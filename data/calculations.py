from .q1_transport import calculate_q1
from .q2_food import calculate_q2
from .q3_cafe import calculate_q3
from .q4_clothing import calculate_q4
from .q5_digital import calculate_q5
from .q6_heating import calculate_q6
from .q7_bag import calculate_q7
from .answer_values import (
    transport_types, food_orders, cafe_cups, clothing_purchases,
    digital_hours, heating_hours, bag_types
)

# 0이면 문항별 균등 가중치, 1이면 배출량 비중 그대로 적용
# 문항별 균등 비중 70%, 최대 배출량 비중 30%
EMISSION_WEIGHT_RATIO = 0.3

QUESTION_CALCULATORS = [
    (calculate_q1, transport_types),
    (calculate_q2, food_orders),
    (calculate_q3, cafe_cups),
    (calculate_q4, clothing_purchases),
    (calculate_q5, digital_hours),
    (calculate_q6, heating_hours),
    (calculate_q7, bag_types),
]


def calculate_total(q1, q2, q3, q4, q5, q6, q7):
    return q1 + q2 + q3 + q4 + q5 + q6 + q7


def calculate_score(q1, q2, q3, q4, q5, q6, q7):
    """항목별 배출량에 가중치를 적용한 환경 영향 점수 (0~100점)."""
    emissions = [q1, q2, q3, q4, q5, q6, q7]
    maximums = [
        max(calculator(choice) for choice in options)
        for calculator, options in QUESTION_CALCULATORS
    ]
    maximum_total = sum(maximums)

    if maximum_total == 0:
        return 0.0, {f"q{i}": 0.0 for i in range(1, 8)}

    item_scores = {}
    for i, (value, maximum) in enumerate(zip(emissions, maximums), start=1):
        # 점수 영향력 = 균등 비중 70% + 최대 배출량 비중 30%
        weight = (1 - EMISSION_WEIGHT_RATIO) / 7
        weight += EMISSION_WEIGHT_RATIO * maximum / maximum_total
        # 문항 내에서는 실제 배출량이 최대치의 몇 %인지 반영
        item_scores[f"q{i}"] = 0.0 if maximum == 0 else 100 * weight * value / maximum

    total_score = sum(item_scores.values())
    return round(total_score, 2), {k: round(v, 2) for k, v in item_scores.items()}


def calculate_level(score):
    if score <= 20:
        return 1
    elif score <= 40:
        return 2
    elif score <= 60:
        return 3
    elif score <= 80:
        return 4
    return 5
