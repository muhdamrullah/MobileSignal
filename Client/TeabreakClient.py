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
        rawData =  data['Response']['age']['value']
        print rawData
    except (ValueError, requests.ConnectionError):
        rawData = "None"
        print rawData

IP_ADD = "localhost:8080"
pullApi("1", IP_ADD)
pullFace(IP_ADD)
