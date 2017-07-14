from myNum import getMovingAvg_list, getMovingStd_list, getStd

# 표준 편차로 이상 탐지하는 함수
def detectByStd_list(data, windowSize=1, sigma=1.0):
    anomaly_list = [] # 이상 탐지된 값의 (index, 수치) 쌍
    lengthOfData = len(data)

    movingAvg_list = getMovingAvg_list(data, windowSize) # 이동 평균
    std = getStd(data) # 표준 편차

    # 데이터를 읽으면서 이상 탐지
    for i in range(lengthOfData):
        if not ((movingAvg_list[i] + (sigma * std)) >= data[i] >= (movingAvg_list[i] - (sigma * std))): # 이동 평균을 기준으로 표준편차 범위안에 없을 때
            anomaly_list.append((i, data[i])) # 이상 탐지된 부분을 튜플로 anomaly_list에 추가

    return anomaly_list # 이상 지점의 (index, 수치) 쌍


# 이동 표준 편차로 이상 탐지하는 함수
def detectByMovingStd_list(data, windowSize=1, sigma=1.0):
    anomaly_list = [] # 이상 탐지된 값의 (index, 수치) 쌍
    lengthOfData = len(data)

    movingAvg_list = getMovingAvg_list(data, windowSize) # 이동 평균
    data_moving_std = getMovingStd_list(data, windowSize) # 이동 표준 편차

    # 데이터를 읽으면서 이상 탐지
    for i in range(lengthOfData):
        if not ((movingAvg_list[i] + (sigma * data_moving_std[i])) >= data[i] >= (movingAvg_list[i] - (sigma * data_moving_std[i]))): # 이동 평균을 기준으로 이동 표준 편차 범위 안에 없을 때
            anomaly_list.append((i, data[i])) # 이상 탐지된 부분을 튜플로 anomaly_list에 추가

    return anomaly_list # 이상 지점의 (index, 수치) 쌍