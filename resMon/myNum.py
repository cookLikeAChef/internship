from math import sqrt
import numpy

# 리스트의 평균 구하는 함수
def getAvg(data):
    lengthOfData = len(data)
    if lengthOfData == 0:
        return None

    #return sum(data, 0.0) / lengthOfData
    return numpy.median(data)

# 리스트의 표준편차 구하는 함수
def getStd(data):
    lengthOfData = len(data)
    if lengthOfData == 0:
        return None

    sum = 0.0
    tmpAvg = getAvg(data) # 리스트의 평균을 구함
    for i in data:
        sum += (i - tmpAvg) ** 2

    tmpTest = sqrt(sum / lengthOfData)
    return tmpTest

# 리스트의 이동 평균 구하는 함수
def getMovingAvg_list(data, windowSize = None):
    lengthOfData = len(data)
    if lengthOfData == 0:
        return None

    avg_list = []
    # 최초 이동 평균값으로 이전값 처리
    tmpAvg = getAvg(data[0:windowSize])
    avg_list.append(tmpAvg)
    avg_list *= windowSize

    # 남은 리스트의 이동 평균값 처리
    for i in range(lengthOfData - windowSize):
        tmpAvg = (tmpAvg * windowSize - data[i] + data[i + windowSize]) / windowSize # windowSize가 클 경우 연산을 빠르게 하기 위함
        avg_list.append(tmpAvg)

    return avg_list

# 리스트의 이동 표준 편차 구하는 함수
def getMovingStd_list(data, windowSize = None):
    lengthOfData = len(data)
    if lengthOfData == 0:
        return None

    std_list = []
    # 최초 이동 표준 편차값으로 이전값 처리
    tmpStd = getStd(data[0:windowSize])
    std_list.append(tmpStd)
    std_list *= windowSize

    # 남은 리스트의 이동 표준 편차값 처리
    for i in range(1, lengthOfData - windowSize + 1):
        std_list.append(getStd(data[i:i + windowSize]))

    return std_list