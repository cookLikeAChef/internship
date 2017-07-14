from myNum import moving_avg, moving_std, std

# 표준 편차로 이상 탐지하는 함수
def detect_by_std(data, window_size=1, sigma=1.0):
    anomaly_list = [] # 이상 탐지된 값의 (index, 수치) 쌍
    length_data = len(data)

    data_moving_avg = moving_avg(data, window_size) # 이동 평균
    data_std = std(data) # 표준 편차

    # 데이터를 읽으면서 이상 탐지
    for i in range(length_data):
        if not ((data_moving_avg[i] + (sigma * data_std)) >= data[i] >= (data_moving_avg[i] - (sigma * data_std))): # 이동 평균을 기준으로 표준편차 범위안에 없을 때
            anomaly_list.append((i, data[i])) # 이상 탐지된 부분을 튜플로 anomaly_list에 추가

    return anomaly_list # 이상 지점의 (index, 수치) 쌍


# 이동 표준 편차로 이상 탐지하는 함수
def detect_by_moving_std(data, window_size=1, sigma=1.0):
    anomaly_list = [] # 이상 탐지된 값의 (index, 수치) 쌍
    length_data = len(data)

    data_moving_avg = moving_avg(data, window_size) # 이동 평균
    data_moving_std = moving_std(data, window_size) # 이동 표준 편차

    # 데이터를 읽으면서 이상 탐지
    for i in range(length_data):
        if not ((data_moving_avg[i] + (sigma *data_moving_std[i])) >= data[i] >= (data_moving_avg[i] - (sigma * data_moving_std[i]))): # 이동 평균을 기준으로 이동 표준 편차 범위 안에 없을 때
            anomaly_list.append((i, data[i])) # 이상 탐지된 부분을 튜플로 anomaly_list에 추가

    return anomaly_list # 이상 지점의 (index, 수치) 쌍