from .q1_transport import calculate_q1
from .q2_food import calculate_q2
from .q3_cafe import calculate_q3
from .q4_clothing import calculate_q4
from .q5_digital import calculate_q5
from .q6_heating import calculate_q6
from .q7_bag import calculate_q7
from .calculations import calculate_total, calculate_score, calculate_level


def calculate_result(answers):
    # 설문 데이터는 기존과 동일하게 7개 선택지만 받음
    answers = {key.lower(): value for key, value in answers.items()}
    q1 = calculate_q1(answers["q1"])
    q2 = calculate_q2(answers["q2"])
    q3 = calculate_q3(answers["q3"])
    q4 = calculate_q4(answers["q4"])
    q5 = calculate_q5(answers["q5"])
    q6 = calculate_q6(answers["q6"])
    q7 = calculate_q7(answers["q7"])

    total = calculate_total(q1, q2, q3, q4, q5, q6, q7)
    score, item_scores = calculate_score(q1, q2, q3, q4, q5, q6, q7)
    level = calculate_level(score)

    return {
        "q1": q1, "q2": q2, "q3": q3, "q4": q4,
        "q5": q5, "q6": q6, "q7": q7,
        "total": total,
        "score": score,
        "item_scores": item_scores,
        "level": level
    }
