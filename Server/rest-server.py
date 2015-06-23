from flask import Flask, jsonify
import json
import airodump_csv_to_json
import webcam

app = Flask(__name__)

#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_tasks():
#    with open('dump.json') as data_file:
#	tasks = json.load(data_file)
#    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    airodump_csv_to_json.convert()
    hexstr = task_id
    hex = ':'.join([hexstr[i:i+2] for i in range(0, len(hexstr), 2)]) #Turns a string of MAC address to MAC hex format
    with open('dump.json') as data_file:
	tasks = json.load(data_file) #Refreshes the dump.json file
    task = [task for task in tasks if task['mac'] == hex] #Selects JSON with 'mac' data
    if len(task) == 0:
	abort(404)
    return jsonify({'Face': task[0]})
    
@app.route('/todo/api/v1.0/tasks/closest_mac/<maxima_id>', methods=['GET'])
def get_MAC(maxima_id):
    airodump_csv_to_json.convert()
    with open('dump.json') as data_file:
	macfile = json.load(data_file) #Refreshes the dump.json file
    count = 0
    List = []
    while True:
	macpower = macfile[count]['power']
	count += 1
	List.append(macpower)
	
	if count == len(macfile):
	    break
    List = map(int, List)
    highestpower = max(List)
    maximum = int(maxima_id)
    orderedhighestpower = sorted(set(List))[-maximum] #Allows us to choose order eg. 1st, 2nd etc within List
    mactask = [mactask for mactask in macfile if mactask['power'] == str(orderedhighestpower)] #Selects JSON with 'mac' data
    if len(mactask) == 0:
	abort(404)
    return jsonify({'Face': mactask[0]})
    
@app.route('/todo/api/v1.0/tasks/face_id', methods=['GET'])
def get_face():
    webcam.getFaceimage()
    with open('face.json') as face_file:
	faces = json.load(face_file)
    if len(faces) == 0:
	abort(404)
    return jsonify({'Response': faces[0]})

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
