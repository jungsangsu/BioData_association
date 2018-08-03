import numpy as np
import matplotlib.pyplot as plt
import json
import csv

#데이터에서 헤더를 불러오고, 시작시간 추출
f = open('SampleEMG.txt', 'r')
header = '' 
for i in range(1,3):
    line = f.readline()
    if i==2:
        header = line[2:]
d = json.loads(header)
start_time = ((d['20:17:09:18:47:09']['time'])[:-4]).replace(':','') #시작 시간 추출
#print(start_time)


#CSV 파일에 데이터 저장하는 구문
x=np.loadtxt('Sample.txt')
# print('total t (ms) : {}'.format(len(x)))
# csvf = open('../emotionEMG.csv', 'w', encoding='utf-8', newline='')
# wr = csv.writer(csvf)
# wr.writerow(["Date", "Face expression", "ECG", "EMG", "EDA", "EEG"])
# timebool = True
# for i in range(len(x)//1000):
#     print(' {} EMG value  : {} mV'.format(i,((x[i*1000,-1]/(2**10)-0.5)*3.3/1009*1000)))
#     EMG_value = (x[i*1000,-1]/(2**10)-0.5)*3.3/1009*1000
#     if timebool == False :
#         start_time = None
#
#     if 0<=abs(EMG_value)<=0.5:
#         wr.writerow([start_time,None,None,None,'EMG-1',None])
#     elif 0.5<abs(EMG_value)<=1.0 :
#         wr.writerow([start_time, None, None, None, 'EMG-2', None])
#     else :
#         wr.writerow([start_time, None, None, None, 'EMG-3', None])
#     timebool = False

#그래프 그려주는 구문
plt.plot((x[0:len(x),-2]/(2**10)-0.5)*3.3/1009*1000,'k')
plt.ylim([-1.63,1.63])
plt.ylabel('mV')
plt.xlabel('t (ms)')
plt.savefig('../EMG.png',dpi=300)

f.close()
# csvf.close()