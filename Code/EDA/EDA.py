import numpy as np
import matplotlib.pyplot as plt
import json
import csv

#데이터에서 헤더를 불러오고, 시작시간 추출
f = open('SampleEDA.txt', 'r')
header = '' 
for i in range(1,3):
    line = f.readline()
    if i==2:
        header = line[2:]
d = json.loads(header)
start_time = ((d['20:17:09:18:47:09']['time'])[:-4]).replace(':','') #시작 시간 추출
#print(start_time)


#CSV 파일에 데이터 저장하는 구문
xx = []
x=np.loadtxt('Sample.txt')
print('total t (ms) : {}'.format(len(x)))
csvf = open('../emotionEDA.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(csvf)
wr.writerow(["Date", "Face expression", "ECG", "EMG", "EDA", "EEG"])
timebool = True
for i in range(len(x)//1000):
    print(' {} EDA value  : {} uS'.format(i, (x[i*1000,-1]/1024.*3.3-0.259388)/0.2))
    EDA_value = round((x[i*1000,-1]/1024.*3.3-0.259388)/0.2,2)
    xx.append(EDA_value)
    if timebool == False :
        start_time = None

    # if 0<=EDA_value<=4:
    #     wr.writerow([start_time,None,None,None,'EDA-1',None])
    # elif 4<EDA_value<=8 :
    #     wr.writerow([start_time, None, None, None, 'EDA-2', None])
    # elif 8<EDA_value<=12 :
    #     wr.writerow([start_time, None, None, None, 'EDA-3', None])
    # elif 12<EDA_value<=16 :
    #     wr.writerow([start_time, None, None, None, 'EDA-4', None])
    # else :
    #     wr.writerow([start_time, None, None, None, 'EDA-5', None])
    wr.writerow([start_time, None, None, None, EDA_value, None])
    timebool = False

#그래프 그려주는 구문
plt.plot(xx[:-1],'k')
# plt.plot((x[0:len(x),-1]/1024.*3.3-0.259388)/0.2,'k')
plt.ylim([0,20])
plt.ylabel('uS')
plt.xlabel('t')
plt.savefig('../EDA.png',dpi=300)

f.close()
csvf.close()