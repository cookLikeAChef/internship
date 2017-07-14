<<<<<<< HEAD
from math import sqrt

# 리스트의 평균 구하는 함수
def avg(data):
    sum = float(0)
    length_data = len(data)

    if length_data != 0:
        for i in data:
            sum += i
        return sum / len(data)

    else:
        pass


# 리스트의 표준편차 구하는 함수
def std(data):
    sum = float(0)
    length_data = len(data)
    tmp_avg = avg(data) # 리스트의 평균을 구함

    if length_data != 0:
        for i in data:
            sum += (i-tmp_avg)**2
        return sqrt(sum/len(data))

    else:
        pass

# 리스트의 이동 평균 구하는 함수
def moving_avg(data, window_size=1):
    window = []
    avg_list = []
    length_data = len(data)

    if length_data != 0: # 값이 있을 때만
        # 우선 window_size만큼 값을 window에 읽어들임
        for i in range(window_size):
            window.append(data[i])

    tmp_avg = avg(window) # window에 있는 값들의 평균을 구함

    # 이동 평균 앞부분 값 처리(최초값으로 다 넣어줌)
    for i in range(window_size):
        avg_list.append(tmp_avg)

    # 이후의 값을 data가 끝날 때까지 읽어옴
    for tmp in data[window_size:]:
        window.pop(0) # 가장 앞의 값 하나를 제거
        window.append(tmp) # 읽어온 data 하나를 추가
        avg_list.append(avg(window)) # window의 평균을 구해 이동평균 리스트에 넣어줌

    return avg_list

# 리스트의 이동 표준 편차 구하는 함수
def moving_std(data, window_size=1):
    window = []
    std_list = []
    length_data = len(data)

    if length_data != 0: # 값이 있을때만
        # 우선 window_size만큼 값을 window에 읽어들임
        for i in range(window_size):
            window.append(data[i])

    tmp_std = std(window) # window에 있는 값들의 표준 편차를 구함

    # 이동 표준 편차 앞부분 값 처리(최초값으로 다 넣어줌)
    for i in range(window_size):
        std_list.append(tmp_std)

    # 이후의 값을 data가 끝날 때까지 읽어옴
    for tmp in data[window_size:]:
        window.pop(0) # 가장 앞의 값 하나를 제거
        window.append(tmp) # 읽어온 data 하나를 추가
        std_list.append(std(window)) # window의 표준 편차를 구해 표준편차 리스트에 넣어줌

=======
from math import sqrt

# 리스트의 평균 구하는 함수
def avg(data):
    sum = float(0)
    length_data = len(data)

    if length_data != 0:
        for i in data:
            sum += i
        return sum / len(data)

    else:
        pass


# 리스트의 표준편차 구하는 함수
def std(data):
    sum = float(0)
    length_data = len(data)
    tmp_avg = avg(data) # 리스트의 평균을 구함

    if length_data != 0:
        for i in data:
            sum += (i-tmp_avg)**2
        return sqrt(sum/len(data))

    else:
        pass

# 리스트의 이동 평균 구하는 함수
def moving_avg(data, window_size=1):
    window = []
    avg_list = []
    length_data = len(data)

    if length_data != 0: # 값이 있을 때만
        # 우선 window_size만큼 값을 window에 읽어들임
        for i in range(window_size):
            window.append(data[i])

    tmp_avg = avg(window) # window에 있는 값들의 평균을 구함

    # 이동 평균 앞부분 값 처리(최초값으로 다 넣어줌)
    for i in range(window_size):
        avg_list.append(tmp_avg)

    # 이후의 값을 data가 끝날 때까지 읽어옴
    for tmp in data[window_size:]:
        window.pop(0) # 가장 앞의 값 하나를 제거
        window.append(tmp) # 읽어온 data 하나를 추가
        avg_list.append(avg(window)) # window의 평균을 구해 이동평균 리스트에 넣어줌

    return avg_list

# 리스트의 이동 표준 편차 구하는 함수
def moving_std(data, window_size=1):
    window = []
    std_list = []
    length_data = len(data)

    if length_data != 0: # 값이 있을때만
        # 우선 window_size만큼 값을 window에 읽어들임
        for i in range(window_size):
            window.append(data[i])

    tmp_std = std(window) # window에 있는 값들의 표준 편차를 구함

    # 이동 표준 편차 앞부분 값 처리(최초값으로 다 넣어줌)
    for i in range(window_size):
        std_list.append(tmp_std)

    # 이후의 값을 data가 끝날 때까지 읽어옴
    for tmp in data[window_size:]:
        window.pop(0) # 가장 앞의 값 하나를 제거
        window.append(tmp) # 읽어온 data 하나를 추가
        std_list.append(std(window)) # window의 표준 편차를 구해 표준편차 리스트에 넣어줌

>>>>>>> 928e7c3dba607a2cbd1893acc8f382fbf6f5c907
    return std_list