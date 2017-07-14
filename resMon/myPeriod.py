<<<<<<< HEAD
import threading

import time

import myResData

class period(threading.Thread):
    cpu_percent_list = []
    on = False
    plt = None

    res = myResData.Resource() # 리소스를 담을 스레드 객체 생성

    def __init__(self, plt=None):
        threading.Thread.__init__(self)
        self.on = True
        self.daemon = True
        self.plt = plt

    def run(self):
        while self.on:
            # 데이터 받음
            cpu_percent_list = next(self.res.getCpu()) # blocking 상태로 cpu의 상태 리스트를 받아옴(최대길이 20)

            # 그래프 그리기
            self.plt.plot(self.cpu_percent_list, color="black", lw=1)
            self.plt.draw()
            self.plt.pause(1)

            self.refreshPlot(self.plt)

            # 출력 테스트
            print(cpu_percent_list)

    def refreshPlot(self, plt):
        pass
=======
import threading

import time

import myResData

class period(threading.Thread):
    cpu_percent_list = []
    on = False
    plt = None

    res = myResData.Resource() # 리소스를 담을 스레드 객체 생성

    def __init__(self, plt=None):
        threading.Thread.__init__(self)
        self.on = True
        self.daemon = True
        self.plt = plt

    def run(self):
        while self.on:
            # 데이터 받음
            cpu_percent_list = next(self.res.getCpu()) # blocking 상태로 cpu의 상태 리스트를 받아옴(최대길이 20)

            # 그래프 그리기
            self.plt.plot(self.cpu_percent_list, color="black", lw=1)
            self.plt.draw()
            self.plt.pause(1)

            self.refreshPlot(self.plt)

            # 출력 테스트
            print(cpu_percent_list)

    def refreshPlot(self, plt):
        pass
>>>>>>> 928e7c3dba607a2cbd1893acc8f382fbf6f5c907
