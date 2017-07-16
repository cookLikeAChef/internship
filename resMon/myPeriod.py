from datetime import datetime
import threading
import psutil
import myPlot
import myResData

class period(threading.Thread):
    cpu_percent_list = [0]*61
    on = False
    res = None

    def __init__(self):
        threading.Thread.__init__(self)
        self. res = myResData.Resource()  # 리소스를 담을 스레드 객체 생성
        self.on = True
        self.daemon = True
        self.cpu_percent_list = [0]*61

    def run(self, plt, fig, ax1, ax2):
        while self.on:
            # 데이터 받음
            # cpu_percent = next(self.res.getCpu())
            cpu_percent = psutil.cpu_percent(interval=1) # blocking 상태로 cpu의 상태 리스트를 받아옴(최대길이 20)

            self.cpu_percent_list.pop(0)
            self.cpu_percent_list.append(cpu_percent)

            ax1.cla()
            ax1.set_xlim(0, 60)
            ax1.set_ylim(0, 100)
            ax1.set_title("CPU")
            ax1.grid(True, linestyle='-', lw=0.2)

            ax1.fill_between(range(0,61), self.cpu_percent_list, y2=0, edgecolor="#6B66FF", facecolors="#B2CCFF", lw=2, alpha=0.7)
            ax1.tick_params(axis='x', colors='white')
            ax1.tick_params(axis='y', colors='white')
            ax1.set_xticklabels([60, 50, 40, 30, 20, 10, 0])

            fig.canvas.update()
            fig.canvas.flush_events()

            # 출력 테스트
            #print("%s" % str(cpu_percent[0]))

    def refreshPlot(self, plt):
        pass