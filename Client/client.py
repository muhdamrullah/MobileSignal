import json
import requests
from urlparse import urlparse
from triangulate import triangulate
import time

signalPower = 0

#Load JSON data from API of a 'specific' MAC address
def pullApi(macAddress, ipAddress):
    http = 'http://'
    uri = '/todo/api/v1.0/tasks/'
    target = urlparse(http + ipAddress + uri + macAddress) #Combines uri and MAC address into a single line
    url = target.geturl() #Combines into a usable url function
    response = requests.get(url)
    
    data = response.json
    rawData =  data['Face']['power']
    return rawData

#Process Signal data from API
def enterMAC(MAC, ipstr):
    rawData = pullApi(MAC, ipstr) 
    SignalStrength = 60 + int(rawData)
    SignalPower = "{0:0.1f}".format(SignalStrength)
    return SignalPower
   
   
#Change the 4 Signal data into a float
def getCoordinates(MAC):
    SignalPower = enterMAC(MAC, IP_first)
    Signal1_raw = float(SignalPower)
    SignalPower = enterMAC(MAC, IP_second)
    Signal2_raw = float(SignalPower)
    SignalPower = enterMAC(MAC, IP_third)
    Signal3_raw = float(SignalPower)
    SignalPower = enterMAC(MAC, IP_fourth)
    Signal4_raw = float(SignalPower)
    Signal1, Signal2, Signal3, Signal4 = [x if x > 0 else 0.1 for x in (Signal1_raw, Signal2_raw, Signal3_raw, Signal4_raw)]
    coordinates = triangulate([(0.0, 0.0, Signal1), (0.0, 35.0, Signal2), (80.0, 0.0, Signal3), (80.0, 35.0, Signal4) ])
    
    global x
    global y
    x=coordinates[0]
    y=coordinates[1]
    
def mobileWait(time_lapse):
    time_start = time.time()
    time_end = (time_start + time_lapse)
    
    while time_end > time.time():
        pass
    
    
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
turtle.setworldcoordinates(-40, -40, 400, 400)

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
t.speed(100)

def drawBoard():
    """draw grid board"""
    
    length= int(raw_input("Enter the place's length (metres): "))
    width= int(raw_input("Enter the place's width (metres): "))
    
    t.hideturtle()
    t.goto(0,0)                #starts from middle
    for i in range(2):       #draws frame
        t.down()
        t.forward(40*length)
        t.lt(90)
        t.forward(40*width)
        t.lt(90)
        t.up()
    
    for i in range(1,width):      #draws horizontal lines (y-axis)
        t.goto(0,40*i)
        t.down()
        t.forward(40*length)
        t.up()
    t.lt(90)
    
    for i in range(1,length):     #draws vertical lines (x-axis)
        t.goto(40*i,0)
        t.down()
        t.forward(40*width)
        t.up()

def trackSignal(x,y,MAC):
    
    print "count: ", count
    Signal[count-1].up()
    Signal[count-1].goto(40*x/float(10),40*y/float(10))
    Signal[count-1].write(MAC, font=("Arial", 10))
    #Signal[count-1].clear()


"""PART III: INTEGRATION"""

"""
#MAC = A88E24689880   or D896953F9A4C 
#IP_first = "192.168.1.103:8080"                #Seminar Rooms
#IP_second ="192.168.1.110:8080"
#IP_third = "192.168.1.105:8080"
#IP_fourth = "192.168.1.106:8080"    
"""

IP_first = "192.168.1.120:8080"                  #Living Studio
IP_second = "192.168.1.121:8080"
IP_third = "192.168.1.122:8080"
IP_fourth = "192.168.1.123:8080"  
    

def runInfinitely():
#"""Get coordinates via API every 10 secs and plot it"""
 	
    List=[]
    check=0
    count=0
 	
    while check<20:                   # A max of 20 signals can be inputted	
        MAC = raw_input("Enter the MAC Address: ") 
        
        if MAC=='NO':
            break
        else:
            global check
            check+=1
            List.append(MAC)

    
    while True:
        for i in List:
            global count 
            count+=1
            str.strip(i)           #MAC input, which is stored as str in List will be stripped of str inverted commas
            getCoordinates(i)
            trackSignal(x,y,i)
            
            if count>=check:     #check and count are both representing the MAC/icon's number. Dont worry about too much about this. This is for the sake of having icons following every turtle
                count=0               #resetting count so that count doesn't increase infinitely. We want it to work with the   trackSignal  function above
            
        mobileWait(5)


#FINAL COMMANDS

#drawBoard()        #Draw the grid board
runInfinitely()
turtle.done
