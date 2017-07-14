import myPeriod
import myPlot

myPlot.create_plot([], window_size=10, sigma=3.0, rolling=True) # 그래프 생성

cpu_thread = myPeriod.period(myPlot.plt)
cpu_thread.start()

while cpu_thread.on:
    cpu_thread.on = bool(input()) # ""를 입력할때까지