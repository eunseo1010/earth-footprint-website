from . import emission_factors as ef
from .answer_values import clothing_purchases

def calculate_q4(answer):
    # TODO: 설문은 '새 옷 구매', 이전 계산표는 '세탁 횟수'였음.
    # 현재는 새 옷 구매 기준으로 작성. 확정 후 필요하면 변경.
    count = clothing_purchases[answer]
    if count == 0:
        return 0
    return count * ef.CLOTHING / 7
