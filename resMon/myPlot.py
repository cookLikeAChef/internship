from myNum import getMovingAvg_list, getMovingStd_list, getStd
from myDetection import detectByStd_list, detectByMovingStd_list
import matplotlib.pyplot as plt

# 그래프 그리는 함수
def createPlot(data, windowSize = 1, sigma = 1.0, rolling = True):
    lengthOfData = len(data)
    std = getStd(data) # 표준 편차
    movingAvg = getMovingAvg_list(data, windowSize) # 이동 평균
    movingStd = getMovingStd_list(data, windowSize) # 이동 표준 편차

    fig = plt.figure(figsize=(15,5)) # 그래프 사이즈 설정
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)

    # 다이나믹 그래프를 위한 소스
    plt.ion()
    plt.show(False)

    plt.plot(data, "k.", markersize = 3) # 기존 데이터 표시
    plt.plot(movingAvg, color = "green", lw = 1) # 이동 평균 그리기

    anomalyX_list = [] # 이상 지점의 x 좌표 리스트
    anomalyY_list = [] # 이상 지점의 y 좌표 리스트

    sublinePlus_list = [] # 이상 탐지 범위 보조선(+) 리스트
    sublineMinus_list = [] # 이상 탐지 범위 보조선(-) 리스트
    events_list = []

    if rolling:
        events_list = detectByMovingStd_list(data, windowSize, sigma) # events_list 변수에 이동 표준 편차로 이상탐지 후 (index, 수치) 쌍 리스트 전달

        # 이상 지점 index와 수치를 각 리스트에 추가
        for i in events_list:
            anomalyX_list.append(i[0])
            anomalyY_list.append(i[1])

        # 이상 탐지 보조선(+,-) 설정 - 표준편차 기준
        for i in range(lengthOfData):
            sublinePlus_list.append(movingAvg[i] + (sigma * movingStd[i]))
            sublineMinus_list.append(movingAvg[i] - (sigma * movingStd[i]))

    else:
        events_list = detectByStd_list(data, windowSize, sigma) # events_list 변수에 표준 편차로 이상 탐지 후 (index, 수치) 쌍 리스트 전달

        # 이상 지점 index와 수치를 각 리스트에 추가
        for i in events_list:
            anomalyX_list.append(i[0])
            anomalyY_list.append(i[1])

        # 이상 탐지 보조선(+,-) 설정
        for i in range(lengthOfData):
            sublinePlus_list.append(movingAvg[i] + (sigma * std))
            sublineMinus_list.append(movingAvg[i] - (sigma * std))

    # 보조선 그리기
    plt.plot(sublinePlus_list, color = "blue", lw = 1)
    plt.plot(sublineMinus_list, color = "red", lw = 1)

    plt.plot(anomalyX_list, anomalyY_list, "r*", markersize = 12) # 이상 지점 빨간 별모양으로 표시

    print("anomaly count : %d" % len(anomalyX_list)) # anomaly 개수 출력

    plt.grid(True) # 격자 생성
    plt.tight_layout()  # 여백 줄이기(plot에 내용물이 들어간 이후에 호출해야 정상적으로 여백이 줄여짐)

    return plt, fig, ax1, ax2