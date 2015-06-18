"""PART I: GUI"""

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
t.speed(100)           #speed of grid/board drawer

for i in Signal:          #speed of mobile signal icon, i.e. t1-t20
    i.speed(1)        

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

def trackSignal(x,y,NAME):
    Signal[count-1].up()
    Signal[count-1].goto(10*x/float(10),10*y/float(10))
    Signal[count-1].write('   '+NAME, font=("Arial", 10))

drawBoard()                  #draw Board

"""PART II: Read csv"""
#To  read csv formated files, first import the csv module
import csv

List=[]          #List will include mobile signals to be tracked. If List has 3 elements, we wish to track 3 ppl
track=0

while track<=20:                # ask for raw_input only for a relevant no. of times
    with open('MobileSignalDataLog.csv', 'rb') as f:
        reader = csv.reader(f)     # creates the reader object
        count=0
        enter = raw_input("Enter the name of a person with a tracked signal\n Type 'NO' once you have finished the name input(s)\n Type 'ALL' if you wish to replay all recorded tracked signals: ") 
        
        if enter=='ALL':
            track+=20                     #random large no. Ensures that we break out of while track<=check loop 
            
            for row in reader:           # iterates the rows of the file in orders
                if ('Name' not in row):        #if the row is not a header row, i.e. (Name,x,y)

                    NAME=row[0]             #e.g. of NAME will be 'Felicia'           
                    x=float(row[1])           #converting str to float - x coordinate
                    y=float(row[2])           #converting str to float - y coordinate
                    check=int(row[3])       #check represents the number of mobile signals tracked, i.e. the number of icons we should have
                    trackSignal(x,y,NAME)

                    count+=1
                    if count==check:    #e.g. if no. of mobile signals tracked is 3, check = 3.
                        count=0             #once count increases till 3 (t1 is deployed, then t2, then t3),
                                                #we reset count so that count doesn't increase infinitely but goes back to 0
                                                #this means that signal from person A will always be drawn by t1,
                                                # signal from person B will always be drawn by t2, so on.
       
        if enter=='NO':
            break
                                                                                 
        else:
            for row in reader:           # iterates the rows of the csv file
                if enter in row:           #if entered name was a tracked signal
                    List.append(row)

            for row in List:
                NAME=row[0]             #e.g. of NAME will be 'Felicia'           
                x=float(row[1])           #converting str to float - x coordinate
                y=float(row[2])           #converting str to float - y coordinate
                check=track       #check represents the number of mobile signals tracked, i.e. how many names the user entered and the number of icons we should have
                trackSignal(x,y,NAME)

                count+=1
                if count==check:    #e.g. if no. of mobile signals tracked is 3, check = 3.
                    count=0             #once count increases till 3 (t1 is deployed, then t2, then t3),
                                            #we reset count so that count doesn't increase infinitely but goes back to 0
                                            #this means that signal from person A will always be drawn by t1,
                                            # signal from person B will always be drawn by t2, so on.
