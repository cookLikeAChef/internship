import psutil
import time
from datetime import datetime

class Resource():
    def getCpu(self):
        return datetime.now(), psutil.cpu_percent(interval=1) # 시간과 cpu 퍼센트 반환