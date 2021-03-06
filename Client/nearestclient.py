import json
import requests
from urlparse import urlparse
from triangulate import triangulate
import time
from random import randint

signalPower = 0

#Load JSON data from API of a 'specific' MAC address
def pullApi(macAddress, ipAddress):
    http = 'http://'
    uri = '/todo/api/v1.0/tasks/'
    target = urlparse(http + ipAddress + uri + macAddress) #Combines uri and MAC address into a single line
    url = target.geturl() #Combines into a usable url function
    try:
        response = requests.get(url)
        data = response.json
        rawData =  data['Face']['power']
        return rawData
    except (TypeError, ValueError, requests.ConnectionError):
        rawData = -88
        return rawData

#Process Signal data from API
def enterMAC(MAC, ipstr):
    rawData = pullApi(MAC, ipstr) 
    SignalStrength = 80 + int(rawData)
    SignalPower = "{0:0.1f}".format(SignalStrength)
    return SignalPower
   
   
#Change the 4 Signal data into a float
def getCoordinates(MAC):
    global x
    global y
    global coordinates
    SignalPower = enterMAC(MAC, IP_first)
    Signal1_raw = float(SignalPower)
    SignalPower = enterMAC(MAC, IP_second)
    Signal2_raw = float(SignalPower)
    SignalPower = enterMAC(MAC, IP_third)
    Signal3_raw = float(SignalPower)
#    SignalPower = enterMAC(MAC, IP_fourth)
#    Signal4_raw = float(SignalPower)
    Signal1, Signal2, Signal3 = [x if x > 0 else 0.01 for x in (Signal1_raw, Signal2_raw, Signal3_raw)]
    coordinates = triangulate([(340.0, 70.0, Signal1), (50.0, 100.0, Signal2), (250.0, 200.0, Signal3) ])      #this config depends on actual dimensions of where sensors are placed
    x=coordinates[0] + randint(-4,4)
    y=coordinates[1] + randint(-4,4)
    
def mobileWait(time_lapse):
    time_start = time.time()
    time_end = (time_start + time_lapse)
    
    while time_end > time.time():
        pass

#Load JSON data from API to load 'specific' closest MAC address
def pullMAC(macRank, ipAddress):
    http = 'http://'
    uri = '/todo/api/v1.0/tasks/closest_mac/'
    target = urlparse(http + ipAddress + uri + macRank) #Combines uri and MAC address into a single line
    url = target.geturl() #Combines into a usable url function
    try:
        response = requests.get(url)
        data = response.json
        semirawData =  data['Face']['mac']
	macData = str(semirawData.replace(':',''))
        return macData
    except (TypeError, ValueError, requests.ConnectionError):
        macData = '000000000000'
        return macData
    
    
"""PART II: GUI"""

import turtle
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t8 = turtle.Turtle()
t9 = turtle.Turtle()
t10 = turtle.Turtle()
t11 = turtle.Turtle()
t12 = turtle.Turtle()
t13 = turtle.Turtle()
t14 = turtle.Turtle()
t15 = turtle.Turtle()
t16 = turtle.Turtle()
t17 = turtle.Turtle()
t18 = turtle.Turtle()
t19 = turtle.Turtle()
t20 = turtle.Turtle()

#User-defined coordinate system to shift screen
turtle.setworldcoordinates(-10, -10, 380, 280)

#Adding Icon Shapes
screen = turtle.Screen()
screen.bgcolor("#006400")
screen.addshape("MobileSignal.gif")
t1.shape("MobileSignal.gif")
t2.shape("MobileSignal.gif")
t3.shape("MobileSignal.gif")
t4.shape("MobileSignal.gif")
t5.shape("MobileSignal.gif")
t6.shape("MobileSignal.gif")
t7.shape("MobileSignal.gif")
t8.shape("MobileSignal.gif")
t9.shape("MobileSignal.gif")
t10.shape("MobileSignal.gif")
t11.shape("MobileSignal.gif")
t12.shape("MobileSignal.gif")
t13.shape("MobileSignal.gif")
t14.shape("MobileSignal.gif")
t15.shape("MobileSignal.gif")
t16.shape("MobileSignal.gif")
t17.shape("MobileSignal.gif")
t18.shape("MobileSignal.gif")
t19.shape("MobileSignal.gif")
t20.shape("MobileSignal.gif")

Signal = t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20

#Drawing speeds
t.speed(1000)

def drawBoard():
    """draw grid board"""
    
    #length= int(raw_input("Enter the place's length in metres (x-axis): "))
    #width= int(raw_input("Enter the place's width in metres (y-axis): "))
    length= 36
    width= 14            #dimensions of CONFIG 1 (refer to hand-drawn map)
    
    t.hideturtle()
    t.goto(0,0)                #starts from middle
    for i in range(2):       #draws frame
        t.down()
        t.forward(10*length)
        t.lt(90)
        t.forward(10*width)
        t.lt(90)
        t.up()
    
    for i in range(1,width):      #draws horizontal lines (y-axis)
        t.goto(0,10*i)
        t.down()
        t.forward(10*length)
        t.up()
    t.lt(90)
    
    for i in range(1,length):     #draws vertical lines (x-axis)
        t.goto(10*i,0)
        t.down()
        t.forward(10*width)
        t.up()

def trackSignal(x,y,MAC):
    Signal[count-1].clear()
    Signal[count-1].up()
    Signal[count-1].goto(10*x/float(10),10*y/float(10))
    
    if MAC=='609217ACCEE7':
        NAME='Ibnur'
    elif MAC=='549F1394942C':
        NAME='Julia'
    elif MAC=='D4970B5D2FE2':
        NAME='Mei'
    elif MAC=='9CF3871E6E17':
        NAME='Farez'
    elif MAC=='D890E849D6DE':
        NAME='Sid'
    elif MAC=='54A050EA61FE':
        NAME='Hui Ying'
    elif MAC=='E4F8EF5F1063':
        NAME='Eugene'
    elif MAC=='D022BE680959':
        NAME='Lai Hock'
    elif MAC=='843835E15530':
        NAME='Xu Hong'
    elif MAC=='A88E24689880':
        NAME='Amrullah'
    elif MAC=='8863DF4FC4F8':
        NAME='Chloe'
    elif MAC=='CC3A61881CC1':
        NAME='Sam'
    elif MAC=='90187C72017C':
        NAME='Nick'
    elif MAC=='C81EE73376BB':
        NAME='Fred'
    elif MAC=='D896953F9A4C':
        NAME='Felicia'
    else:
	NAME=MAC
    
    Signal[count-1].write('   '+NAME, font=("Arial", 10))

# This function generates a list of MAC addresses inputed and nearby and returns the List
def generateList():
 	
    global check
    global count
    List = []
    a = 0 #This is an arbitrary variable used to count the list
    
    while check<20:                   # A max of 20 signals can be inputted	
        NAME = raw_input("Enter a name: ") 
        
        if NAME=='NO':
	    for x in range(1,6): # An arbitrary number based on how many closest '6' mobile signals you want to discover
                check+=3
		macData = pullMAC(str(x), IP_first)
	        MAC = macData
	        print MAC
	        List.append(MAC)
		macData = pullMAC(str(x), IP_second)
	        MAC2 = macData
	        print MAC2
	        List.append(MAC2)
		macData = pullMAC(str(x), IP_third)
	        MAC3 = macData
	        print MAC3
	        List.append(MAC3)
	    break
        else:
            check+=1
        
            if NAME=='Ibnur':
                MAC='609217ACCEE7'
            if NAME=='Julia':
                MAC='549F1394942C'
            if NAME=='Mei':
                MAC='D4970B5D2FE2'
            if NAME=='Farez':
                MAC='9CF3871E6E17'
            if NAME=='Sid':
                MAC='D890E849D6DE'
            if NAME=='Hui Ying':
                MAC='54A050EA61FE'
            if NAME=='Eugene':
                MAC='E4F8EF5F1063'
            if NAME=='Lai Hock':
                MAC='D022BE680959'
            if NAME=='Xu Hong':
                MAC='843835E15530'
            if NAME=='Amrullah':
                MAC='A88E24689880'
            if NAME=='Chloe':
                MAC='8863DF4FC4F8'
            if NAME=='Sam':
                MAC='CC3A61881CC1'
            if NAME=='Nick':
                MAC='90187C72017C'
            if NAME=='Fred':
                MAC='C81EE73376BB'
            if NAME=='Felicia':
                MAC='D896953F9A4C'
            
            List.append(MAC)
	    a = len(List)
    generateList.takeforList = a
    return List

## Function to log the key header of elements into CSV
def beginLog():
    b = open('MobileSignalDataLog.csv', 'a')    # open a file for writing
    a = csv.writer(b)                          # create the csv writer object.
    data = [['Name', 'x', 'y', 'No. of signals tracked']]
    a.writerows(data)
    b.close()

"""PART III: INTEGRATION"""
import csv

IP_first = "192.168.0.120:8080"                  # 0. Seminar Room entrance
IP_second = "192.168.0.121:8080"             # 1. Toilet
IP_third = "192.168.0.122:8080"                # 2. 20 footer TV
#IP_fourth = "192.168.1.123:8080"             # 3. 20 footer Air con
    
def runInfinitely():
#"""Get coordinates via API every 10 secs and plot it"""
 	
    List=[]          #List will include mobile signals to be tracked. If List has 3 elements, we wish to track 3 ppl
    global check
    global count
    check=0
    count=0
    
    ## OBTAIN LIST OF MAC ADDRESSES
    List = generateList()
    n = generateList.takeforList

    ## DATA LOG - CSV FILE WRITING
    beginLog()
    
    while True:
	List = list(set(List))
	totallengthList = len(List)
        for i in List:
            count+=1
            getCoordinates(i) 
            
            if i == '609217ACCEE7':	#An elif function must be used or else the 'else' function will be used by default
                NAME='Ibnur'
            elif i == '549F1394942C':
                NAME='Julia'
            elif i == 'D4970B5D2FE2':
                NAME='Mei'
            elif i == '9CF3871E6E17':
                NAME='Farez'
            elif i == 'D890E849D6DE':
                NAME='Sid'
            elif i == '54A050EA61FE':
                NAME='Hui Ying'
            elif i == 'E4F8EF5F1063':
                NAME='Eugene'
            elif i == 'D022BE680959':
                NAME='Lai Hock'
            elif i == '843835E15530':
                NAME='Xu Hong'
            elif i == 'A88E24689880':
                NAME='Amrullah'
            elif i == '8863DF4FC4F8':
                NAME='Chloe'
            elif i == 'CC3A61881CC1':
                NAME='Sam'
            elif i == '90187C72017C':
                NAME='Nick'
            elif i == 'C81EE73376BB':
                NAME='Fred'
            elif i == 'D896953F9A4C':
                NAME='Felicia'
	    else:
		NAME=i

	    print NAME, 'is at ', '(',x,',',y,')'
            
            trackSignal(x,y,i)
            
            #DATA LOG UPDATE - CSV FILE WRITING
            b = open('MobileSignalDataLog.csv', 'a')    # open previous csv file for writing (appending)
            a = csv.writer(b)                         # create the csv writer object.
            data = [[NAME, x,y, check]] 
            a.writerows(data)
            b.close()   
                 
                           
            if count>=check or count>=totallengthList:     #check and count are both representing the MAC/icon's number.
                count=0          #resetting count so that count doesn't increase infinitely. We want it to work with the   trackSignal  function above
		print "Refreshing list..."
		List = List[:n]  #Takes the first n digits from list
		for k in range(1,6): # An arbitrary number based on how many closest '6' mobile signals you want to discover
		    macData = pullMAC(str(k), IP_first)
	            MAC = macData
		    print MAC
	            List.append(MAC)
		    macData = pullMAC(str(k), IP_second)
	            MAC2 = macData
		    print MAC2
	            List.append(MAC2)
		    macData = pullMAC(str(k), IP_third)
	            MAC3 = macData
		    print MAC3
	            List.append(MAC3)
            
        mobileWait(5)       # Refreshes every 10s
        

#FINAL COMMANDS

drawBoard()        #Draw the grid board
runInfinitely()
turtle.done
