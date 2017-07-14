import psutil


class Resource():
    cpu_percent_list = []

    def __init__(self):
        self.cpu_percent_list = []

    def getCpu(self):
        if len(self.cpu_percent_list) > 20:
            self.cpu_percent_list.pop(0)  # 20개를 넘어가면 앞의 데이터를 하나 뺀다

        # tmp_cpu_percent =  # blocking으로 1초간격으로 cpu의 현재 사용률을 받아온다
        self.cpu_percent_list.append(psutil.cpu_percent(interval=1)) # 사용률을 받아온 다음, 리스트에 추가한다.
        yield self.cpu_percent_list