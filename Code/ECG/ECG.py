import fitbit
import gather_keys_oauth2 as Oauth2
import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime
# 상수
CLIENT_ID = 'ID'
CLIENT_SECRET = 'SECRETKEY'


server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

print('ACCESS_TOKEN  : {} '.format(ACCESS_TOKEN))
print('REFRESH_TOKEN  : {} '.format(REFRESH_TOKEN))

auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
"""Getting data"""
fitbit_stats = auth2_client.intraday_time_series('activities/heart', base_date='2018-06-10', detail_level='1sec',start_time='2:0',end_time='2:2')

"""Getting only 'heartrate' and 'time'"""
stats = fitbit_stats['activities-heart-intraday']['dataset']
print(stats)


f = open('../emotionECG.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(["Date", "Face expression", "ECG", "EMG", "EDA", "EEG"])

templist = [0 for i in range(120)] #그림을 그리기 위한 리스트



#엑셀에 저장
count = 0
for i in stats:
    ECG_value = i['value']
    indexECG = str(i['time'])[-2:]
    # print(indexECG)
    templist[int(indexECG)] = ECG_value
    if count==0:
        wr.writerow([str(i['time']).replace(":", ""), None, ECG_value, None, None, None])
        # if 49<= ECG_value <=55:
        #     wr.writerow([str(i['time']).replace(":", ""), None, 'ECG-1', None, None, None])
        # elif 56<= ECG_value <=61 :
        #     wr.writerow([str(i['time']).replace(":", ""), None, 'ECG-2', None, None, None])
        # elif 62 <= ECG_value <= 65:
        #     wr.writerow([str(i['time']).replace(":", ""), None, 'ECG-3', None, None, None])
        # elif 66 <= ECG_value <= 69:
        #     wr.writerow([str(i['time']).replace(":", ""), None, 'ECG-4', None, None, None])
        # elif 70 <= ECG_value <= 73:
        #     wr.writerow([str(i['time']).replace(":", ""), None, 'ECG-5', None, None, None])
        # elif 74 <= ECG_value <= 81:
        #     wr.writerow([str(i['time']).replace(":", ""), None, 'ECG-6', None, None, None])
        # else :
        #     wr.writerow([str(i['time']).replace(":", ""), None, 'ECG-7', None, None, None])
        count+=1
    #print('{} / {} '.format(i['time'],i['value']))

# 그림을 틈이 안생기게 padding 작업해줌
#print(templist)
for i in range(len(templist)):
    if templist[i] == 0  and i==0:
        templist[i] = 0
    elif templist[i] == 0 :
        templist[i] = templist[i-1]
print(templist)

for i in range(1,len(templist)):
    ECG_value = templist[i]
    wr.writerow([None, None, ECG_value, None, None, None])
    # if 49 <= ECG_value <= 55:
    #     wr.writerow([None, None, 'ECG-1', None, None, None])
    # elif 56 <= ECG_value <= 61:
    #     wr.writerow([None, None, 'ECG-2', None, None, None])
    # elif 62 <= ECG_value <= 65:
    #     wr.writerow([None, None, 'ECG-3', None, None, None])
    # elif 66 <= ECG_value <= 69:
    #     wr.writerow([None, None, 'ECG-4', None, None, None])
    # elif 70 <= ECG_value <= 73:
    #     wr.writerow([None, None, 'ECG-5', None, None, None])
    # elif 74 <= ECG_value <= 81:
    #     wr.writerow([None, None, 'ECG-6', None, None, None])
    # else:
    #     wr.writerow([None, None, 'ECG-7', None, None, None])

xx = np.array(templist)
#그래프 그려주는 구문
plt.plot(xx[0:-1],'k')
plt.ylim([0,120])
plt.ylabel('bpm')
plt.xlabel('t')
plt.savefig('../ECG.png',dpi=300)


f.close()