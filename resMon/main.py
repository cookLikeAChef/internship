import myPeriod
import myPlot

plt, fig, ax1, ax2 = myPlot.createPlot([0], windowSize=10, sigma=3.0, rolling=True) # 그래프 생성

cpu_thread = myPeriod.period()
cpu_thread.run(plt, fig, ax1, ax2)

while cpu_thread.on:
    cpu_thread.on = bool(input()) # ""를 입력할때까지