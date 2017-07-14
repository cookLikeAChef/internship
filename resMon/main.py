<<<<<<< HEAD
import myPeriod
import myPlot

myPlot.create_plot([], window_size=10, sigma=3.0, rolling=True) # 그래프 생성

cpu_thread = myPeriod.period(myPlot.plt)
cpu_thread.start()

while cpu_thread.on:
=======
import myPeriod
import myPlot

myPlot.create_plot([], window_size=10, sigma=3.0, rolling=True) # 그래프 생성

cpu_thread = myPeriod.period(myPlot.plt)
cpu_thread.start()

while cpu_thread.on:
>>>>>>> 928e7c3dba607a2cbd1893acc8f382fbf6f5c907
    cpu_thread.on = bool(input()) # ""를 입력할때까지