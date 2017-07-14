import myPlot as mp
import scipy

with open("./dataset/sample1.txt", 'r') as f: # 파일을 읽어들임
    data = f.read().split(',') # 콤마(,)를 기준으로 문자열을 나누어 리스트형식으로 리턴

# 문자형 데이터를 숫자형으로 변환
lengthOfData = len(data)
for i in range(lengthOfData):
    data[i] = float(data[i])

percentile = 0.9997
tmp = scipy.stats.norm.ppf(.97)
#mp.createPlot(data, windowSize = 30, sigma = 3.0, rolling = True)
# mp.createPlot(data, windowSize = 30, sigma = test_sigma, rolling = True)