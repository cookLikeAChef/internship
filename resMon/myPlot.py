<<<<<<< HEAD
from myNum import moving_avg, moving_std, std
from myDetection import detect_by_std, detect_by_moving_std
import matplotlib.pyplot as plt

# 그래프 그리는 함수
def create_plot(data, window_size=1, sigma=1.0, rolling=True):
    '''
    print(data) # 데이터 출력
    print(data_moving_avg) # 이동 평균 출력
    print(data_moving_std) # 이동 표준 편차 출력
    '''
    length_of_data = len(data)
    data_std = std(data) # 표준 편차
    data_moving_avg = moving_avg(data, window_size) # 이동 평균
    data_moving_std = moving_std(data, window_size) # 이동 표준 편차

    plt.figure(figsize=(15,9)) # 그래프 사이즈 설정

    plt.plot(data, "k.", markersize=3) # 기존 데이터 표시
    plt.plot(data_moving_avg, color="green", lw=1) # 이동 평균 그리기

    anomaly_x = [] # 이상 지점의 x 좌표 리스트
    anomaly_y = [] # 이상 지점의 y 좌표 리스트

    subline_plus = [] # 이상 탐지 범위 보조선(+) 리스트
    subline_minus = [] # 이상 탐지 범위 보조선(-) 리스트
    events = []

    if rolling:
        events = detect_by_moving_std(data, window_size, sigma) # events 변수에 이동 표준 편차로 이상탐지 후 (index, 수치) 쌍 리스트 전달

        # 이상 지점 index와 수치를 각 리스트에 추가
        for i in events:
            anomaly_x.append(i[0])
            anomaly_y.append(i[1])

        # 이상 탐지 보조선(+,-) 설정 - 표준편차 기준
        for i in range(length_of_data):
            subline_plus.append(data_moving_avg[i] + (sigma * data_moving_std[i]))
            subline_minus.append(data_moving_avg[i] - (sigma * data_moving_std[i]))

    else:
        events = detect_by_std(data, window_size, sigma) # events 변수에 표준 편차로 이상 탐지 후 (index, 수치) 쌍 리스트 전달

        # 이상 지점 index와 수치를 각 리스트에 추가
        for i in events:
            anomaly_x.append(i[0])
            anomaly_y.append(i[1])

        # 이상 탐지 보조선(+,-) 설정
        for i in range(length_of_data):
            subline_plus.append(data_moving_avg[i] + (sigma * data_std))
            subline_minus.append(data_moving_avg[i] - (sigma * data_std))

    # 보조선 그리기
    plt.plot(subline_plus, color="blue", lw=1)
    plt.plot(subline_minus, color="red", lw=1)

    plt.xlim(0, 20)
    plt.plot(anomaly_x, anomaly_y, "r*", markersize=12) # 이상 지점 빨간 별모양으로 표시

    plt.grid(True) # 격자 생성
    plt.tight_layout()  # 여백 줄이기(plot에 내용물이 들어간 이후에 호출해야 정상적으로 여백이 줄여짐)
=======
from myNum import moving_avg, moving_std, std
from myDetection import detect_by_std, detect_by_moving_std
import matplotlib.pyplot as plt

# 그래프 그리는 함수
def create_plot(data, window_size=1, sigma=1.0, rolling=True):
    '''
    print(data) # 데이터 출력
    print(data_moving_avg) # 이동 평균 출력
    print(data_moving_std) # 이동 표준 편차 출력
    '''
    length_of_data = len(data)
    data_std = std(data) # 표준 편차
    data_moving_avg = moving_avg(data, window_size) # 이동 평균
    data_moving_std = moving_std(data, window_size) # 이동 표준 편차

    plt.figure(figsize=(15,9)) # 그래프 사이즈 설정

    plt.plot(data, "k.", markersize=3) # 기존 데이터 표시
    plt.plot(data_moving_avg, color="green", lw=1) # 이동 평균 그리기

    anomaly_x = [] # 이상 지점의 x 좌표 리스트
    anomaly_y = [] # 이상 지점의 y 좌표 리스트

    subline_plus = [] # 이상 탐지 범위 보조선(+) 리스트
    subline_minus = [] # 이상 탐지 범위 보조선(-) 리스트
    events = []

    if rolling:
        events = detect_by_moving_std(data, window_size, sigma) # events 변수에 이동 표준 편차로 이상탐지 후 (index, 수치) 쌍 리스트 전달

        # 이상 지점 index와 수치를 각 리스트에 추가
        for i in events:
            anomaly_x.append(i[0])
            anomaly_y.append(i[1])

        # 이상 탐지 보조선(+,-) 설정 - 표준편차 기준
        for i in range(length_of_data):
            subline_plus.append(data_moving_avg[i] + (sigma * data_moving_std[i]))
            subline_minus.append(data_moving_avg[i] - (sigma * data_moving_std[i]))

    else:
        events = detect_by_std(data, window_size, sigma) # events 변수에 표준 편차로 이상 탐지 후 (index, 수치) 쌍 리스트 전달

        # 이상 지점 index와 수치를 각 리스트에 추가
        for i in events:
            anomaly_x.append(i[0])
            anomaly_y.append(i[1])

        # 이상 탐지 보조선(+,-) 설정
        for i in range(length_of_data):
            subline_plus.append(data_moving_avg[i] + (sigma * data_std))
            subline_minus.append(data_moving_avg[i] - (sigma * data_std))

    # 보조선 그리기
    plt.plot(subline_plus, color="blue", lw=1)
    plt.plot(subline_minus, color="red", lw=1)

    plt.xlim(0, 20)
    plt.plot(anomaly_x, anomaly_y, "r*", markersize=12) # 이상 지점 빨간 별모양으로 표시

    plt.grid(True) # 격자 생성
    plt.tight_layout()  # 여백 줄이기(plot에 내용물이 들어간 이후에 호출해야 정상적으로 여백이 줄여짐)
>>>>>>> 928e7c3dba607a2cbd1893acc8f382fbf6f5c907
    plt.show() # 그래프 표시