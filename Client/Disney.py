import json
import requests
from urlparse import urlparse
import time
import csv
import cv2

def makeBorder(colour):
    BLUE = [255,0,0]
    GREEN = [0,255,0]
    RED = [0,0,255]
    YELLOW = [0,255,255]
    PURPLE = [255,0,205]
    happiness = int(happinessData)
    sadness = int(sadnessData)
    anger = int(angerData)
    disgust = int(disgustData)
    fear = int(fearData)
    print "I am ",happinessData,"% happy, ",sadnessData,"% sad, ",angerData,"% angry, ",disgustData,"% disgusted, ",fearData,"%fearful"
    
    img = cv2.imread('frame.png')
    rows,cols = img.shape[:2]

    dst = img.copy()

    top = int (0.1*rows)
    bottom = int (0.1*rows)

    left = int (0.1*cols)
    right = int (0.1*cols)

    while(True):
    
         cv2.imshow('border',dst)
	 k = cv2.waitKey(500)
    
         if k==27:
              break
         elif happiness >= 40:
              dst = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value = YELLOW)
         elif sadness >= 40:
              dst = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value = BLUE)
         elif anger >= 40:
              dst = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value = RED)
         elif disgust >= 40:
              dst = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value = GREEN)
         elif fear >= 15:
              dst = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value = PURPLE)
	      
         elif k == ord('r'):
              dst = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_REPLICATE)

    cv2.destroyAllWindows()  

    
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
    except (ValueError, TypeError, requests.ConnectionError):
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

happinessData = 0
sadnessData = 0
angerData = 0
fearData = 0
disgustData = 0
rawData = 0
startCSV()	
IP_ADD = "localhost:8080"
while True:
#    pullApi("1", IP_ADD)
    makeBorder("PURPLE")
    pullFace(IP_ADD)
    mobileWait(1)
