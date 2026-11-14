TRANSPORT = {
    "walk": 0, 
    "bike_scooter": 0.107, 
    "bus": 0.027, 
    "subway": 0.014, 
    "car": 0.131, 
    "taxi": 0.156
    } 
TRANSPORT_DISTANCE_KM = {
    "walk": 2,
    "bike_scooter": 3,
    "bus": 6,
    "subway": 27,
    "car": 12,
    "taxi": 8,
    }
TRANSPORT_COUNT = 1

DELIVERY = 0.110  # 배달 km당 배출계수
DELIVERY_DISTANCE_KM = 3  # 배달 1회 평균 거리
PACKAGING = 0.280 # 주문 1회당 포장 배출량

CAFE_CUP = {"none": 0, "dine_in": 0.020, "tumbler": 0.019, "disposable_cup": 0.060}  # 컵 1개당 배출량
CAFE_COUNT = 1  # 선택한 컵의 기준 사용 횟수

CLOTHING = 14.200  # 새 옷 1벌 구매당 배출량

DIGITAL_POWER_KW = 0.1056  # 디지털 기기 평균 소비전력
DIGITAL_ELECTRICITY = 0.5216  # 전력 kg CO2e/kWh

HEATING_POWER_KW = 1.25  # 냉난방 평균 소비전력
HEATING_ELECTRICITY = 0.5216 # 전력 kg CO2e/kWh

BAG = {"none": 0, 
       "paper_bag": 0.064, 
       "plastic_bag": 0.020, 
       "reusable_bag": 0.3 / 100
       }  # 봉투 1개당 배출량
BAG_COUNT = 1  # 기준 사용 개수
