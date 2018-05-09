import random
import time
time_start=time.perf_counter()
numberList=[]
for i in range(20):
    numberList.append(random.randint(1,100))
print(numberList)
for j in range(len(numberList)-1):
    max=j
    for k in range(j+1,len(numberList)):
        if numberList[k]>numberList[max]:
            max=k
    temp=numberList[j]
    numberList[j]=numberList[max]
    numberList[max]=temp
time_stop=time.perf_counter()
print(numberList)
print(time_stop-time_start)