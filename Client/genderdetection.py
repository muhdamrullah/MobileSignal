import json
import requests
from urlparse import urlparse
import time
import csv
import cv2
import random

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
	global sadnessData
	global happinessData
	global angerData
	global disgustData
	global fearData
        response = requests.get(url)
        data = response.json()
        ageData =  data['Response']['age']['value']
        agerangeData =  data['Response']['age']['range']
        genderData =  data['Response']['gender']['value']
        genderDataConf = data['Response']['gender']['confidence']
        sadnessData =  data['Response']['expressions']['sadness']['value']
        neutralData =  data['Response']['expressions']['neutral']['value']
        disgustData =  data['Response']['expressions']['disgust']['value']
        angerData =  data['Response']['expressions']['anger']['value']
        surpriseData =  data['Response']['expressions']['surprise']['value']
        fearData =  data['Response']['expressions']['fear']['value']
        happinessData =  data['Response']['expressions']['happiness']['value']
	randomNo = random.randint(1,2)
	print genderData
	print genderDataConf
	if genderData == 'Male' and randomNo == 1 and genderDataConf > 70:
	    with open('video.css', 'r') as file:
		data = file.readlines()
		data[13] = '    display: none;\n'
		data[28] = '    display: block;\n'
		with open('video.css', 'w') as file:
                    file.writelines( data )
    	        time.sleep(10)
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: block;\n'
                data[28] = '    display: none;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
        if genderData == 'Female' and randomNo == 1 and genderDataConf > 70:
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: none;\n'
                data[43] = '    display: block;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
                time.sleep(10)
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: block;\n'
                data[43] = '    display: none;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
        if genderDataConf < 71 and randomNo == 1:
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: none;\n'
                data[58] = '    display: block;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
                time.sleep(10)
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: block;\n'
                data[58] = '    display: none;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
	if genderData == 'Male' and randomNo == 2 and genderDataConf > 70:
	    with open('video.css', 'r') as file:
		data = file.readlines()
		data[13] = '    display: none;\n'
		data[73] = '    display: block;\n'
		with open('video.css', 'w') as file:
                    file.writelines( data )
    	        time.sleep(10)
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: block;\n'
                data[73] = '    display: none;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
        if genderData == 'Female' and randomNo == 2 and genderDataConf > 70:
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: none;\n'
                data[88] = '    display: block;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
                time.sleep(10)
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: block;\n'
                data[88] = '    display: none;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
        if genderDataConf < 71 and randomNo == 2:
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: none;\n'
                data[103] = '    display: block;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
                time.sleep(10)
            with open('video.css', 'r') as file:
                data = file.readlines()
                data[13] = '    display: block;\n'
                data[103] = '    display: none;\n'
                with open('video.css', 'w') as file:
                    file.writelines( data )
    except (ValueError, TypeError, requests.ConnectionError):
        pass

def mobileWait(time_lapse):
    time_start = time.time()
    time_end = (time_start + time_lapse)
    
    while time_end > time.time():
        pass

happinessData = 0
sadnessData = 0
angerData = 0
fearData = 0
disgustData = 0
rawData = 0
IP_ADD = "localhost:8080"
while True:
    pullFace(IP_ADD)
    mobileWait(1)
