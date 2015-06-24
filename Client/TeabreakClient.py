import json
import requests
from urlparse import urlparse
import time

def pullApi(macPower, ipAddress):
    http = 'http://'
    uri = '/todo/api/v1.0/tasks/closest_mac/'
    target = urlparse(http + ipAddress + uri + macPower) #Combines uri and MAC address into a single line
    url = target.geturl() #Combines into a usable url function
    try:
        response = requests.get(url)
        data = response.json
        rawData =  data['Face']['mac']
        print rawData
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
        print ageData
        genderData =  data['Response']['gender']['value']
        print genderData
        sadnessData =  data['Response']['expressions']['sadness']['value']
        print sadnessData
        neutralData =  data['Response']['expressions']['neutral']['value']
        print neutralData
        disgustData =  data['Response']['expressions']['disgust']['value']
        print disgustData
        angerData =  data['Response']['expressions']['anger']['value']
        print angerData
        surpriseData =  data['Response']['expressions']['surprise']['value']
        print surpriseData
        fearData =  data['Response']['expressions']['fear']['value']
        print fearData
        happinessData =  data['Response']['expressions']['happiness']['value']
        print happinessData
    except (TypeError, requests.ConnectionError):
        pass
        

IP_ADD = "localhost:8080"
pullApi("1", IP_ADD)
pullFace(IP_ADD)
