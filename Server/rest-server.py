from flask import Flask, jsonify
import json
import airodump_csv_to_json

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

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
