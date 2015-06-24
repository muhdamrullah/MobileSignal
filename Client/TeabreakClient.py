import json
import requests
from urlparse import urlparse
import time
import csv

def pullApi(macPower, ipAddress):
    http = 'http://'
    uri = '/todo/api/v1.0/tasks/closest_mac/'
    target = urlparse(http + ipAddress + uri + macPower) #Combines uri and MAC address into a single line
    url = target.geturl() #Combines into a usable url function
    try:
        response = requests.get(url)
        data = response.json
	global rawData
        rawData =  data['Face']['mac']
    except (ValueError, requests.ConnectionError):
        rawData = "None"
        print rawData

def pullFace(ipAddress):
    http = 'http://'
    uri = '/todo/api/v1.0/tasks/face_id'
    target = urlparse(http + ipAddress + uri ) #Combines uri and MAC address into a single line
    url = target.geturl() #Combines into a usable url function
    try:
        response = requests.get(url)
        data = response.json
        ageData =  data['Response']['age']['value']
        agerangeData =  data['Response']['age']['range']
        genderData =  data['Response']['gender']['value']
        sadnessData =  data['Response']['expressions']['sadness']['value']
        neutralData =  data['Response']['expressions']['neutral']['value']
        disgustData =  data['Response']['expressions']['disgust']['value']
        angerData =  data['Response']['expressions']['anger']['value']
        surpriseData =  data['Response']['expressions']['surprise']['value']
        fearData =  data['Response']['expressions']['fear']['value']
        happinessData =  data['Response']['expressions']['happiness']['value']

        b = open('MobileSignalFaceDataLog.csv', 'a')    # open a file for writing
        a = csv.writer(b)                          # create the csv writer object.
        data = [[rawData, '%s+/-%s' % (ageData, agerangeData), genderData, sadnessData, neutralData, disgustData, angerData, surpriseData, fearData, happinessData]]
        a.writerows(data)
        b.close()
    except (TypeError, requests.ConnectionError):
        pass

    ## DATA LOG - CSV FILE WRITING
def startCSV():
    b = open('MobileSignalFaceDataLog.csv', 'a')    # open a file for writing
    a = csv.writer(b)                          # create the csv writer object.
    data = [['Unique_ID', 'Age', 'Gender', 'Sadness_Intensity', 'Neutral_Intensity', 'Disgust_Intensity', 'Anger_Intensity', 'Surprise_Intensity', 'Fear_Intensity', 'Happiness_Intensity']]
    a.writerows(data)
    b.close()


def mobileWait(time_lapse):
    time_start = time.time()
    time_end = (time_start + time_lapse)
    
    while time_end > time.time():
        pass

startCSV()	
IP_ADD = "localhost:8080"
while True:
    pullApi("1", IP_ADD)
    pullFace(IP_ADD)
    mobileWait(1)
