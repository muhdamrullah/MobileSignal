import cv2
import sys
import requests
import time
import json
import os

def getFaceimage():
	#Get current directory
	script_dir = os.path.dirname(__file__)
	#Add 3 second timer
	timeout = time.time() + 3
	RelcascPath = 'haarcascade_frontalface_default.xml'
	cascPath = os.path.join(script_dir, RelcascPath)
	faceCascade = cv2.CascadeClassifier(cascPath)

	video_capture = cv2.VideoCapture(0)

	while True:
	    # Capture frame-by-frame
	    ret, frame = video_capture.read()
	
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    faces = faceCascade.detectMultiScale(
	        gray,
	        scaleFactor=1.1,
	        minNeighbors=5,
	        minSize=(30, 30),
	        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	    )
	
	    # Draw a rectangle around the faces
	    for (x, y, w, h) in faces:
	        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

	    # Saving the image
	    roi = frame[y:y+h, x:x+w]
	    cv2.imwrite("roi.png", roi) 
	    cv2.imwrite("/home/odroid/MobileSignal/Client/frame.png", frame)
	    # Display the resulting frame
	    cv2.imshow('Video', frame)
	    
	    # Get path to save image
	    RelimagePath = 'roi.png'
	    imagePath = os.path.join(script_dir, RelimagePath)
	    if time.time() > timeout:
	    	json_resp = requests.post( 'http://api.sightcorp.com/api/detect/',
				data = { 'app_key'	: 'cf34361b889d44c2bc85c46295853ecb',
					'client_id'	: 'a8608c77397e4494b47336e73ac1255d' },
				files = { 'img'		: ('filename', open( imagePath, 'rb') ) } )
		faceresponse = json_resp.text
		out_file = open('face.txt', 'w+')
		out_file.write("%s" % json_resp.text)
		out_file.close()
		lines = open('face.txt').readlines()
		superoutfile = open('faces.txt', 'w+')
		superoutfile.writelines(lines[2:-4]) #Remove 2nd line and 4th line
		superoutfile.readline()
		superoutfile.close()
		#Add in the bracket necessary
		with open('faces.txt') as fin:
		    lines = fin.readlines()
		lines[0] = lines[0].replace('{', '[{')
		lines[68] = lines[68].replace('}','}]')

		with open('face.json', 'w') as fout:
		    for line in lines:
			fout.write(line)
	    	break

# When everything is done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()

#MAIN Code
if __name__ == '__main__':
	getFaceimage()
