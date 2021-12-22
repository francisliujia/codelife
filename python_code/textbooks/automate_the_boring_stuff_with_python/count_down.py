import time 
import subprocess 
timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='\n')
    time.sleep(1)
    timeLeft = timeLeft - 1
    
subprocess.Pope(['start', 'alarm.wav'], shell=True)
