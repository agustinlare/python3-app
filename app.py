from flask import Flask, jsonify
from flask import request
from boto3.session import Session
import logging
import os
import threading

app = Flask(__name__)

counter = 0
counter_lock = threading.Lock()
switch_status = True
switch_lock = threading.Lock()

@app.route("/")
def get_caller_identity():
    session = Session()
    sts_client = session.client('sts')

    try:
        response = sts_client.get_caller_identity()
        caller_identity = {
            'Account': response['Account'],
            'Arn': response['Arn'],
            'UserId': response['UserId']
        }
        return jsonify(caller_identity), 200
    except Exception as e:
        logging.error("Error retrieving caller identity: %s", str(e))
        return jsonify({'error': 'Failed to retrieve caller identity'}), 500

@app.route("/counter")
def get_counter():
    response = {'count': counter}
    return jsonify(response), 200

@app.route("/ping")
def ping():
    return 'pong', 200

@app.route("/switch", methods=['GET', 'POST'])
def toggle_switch():
    global switch_status
    switch_lock.acquire()
    switch_status = not switch_status
    switch_lock.release()

    response = {'status': switch_status}
    return jsonify(response), 200

@app.route("/liveness")
def liveness():
    global switch_status
    if switch_status:
        return 'Liveness Probe', 200
    else:
        return 'Liveness Probe', 503

@app.route("/readiness")
def readiness():
    global switch_status
    if switch_status:
        return 'Readiness Probe', 200
    else:
        return 'Readiness Probe', 503

def increment_counter():
    global counter
    with counter_lock:
        counter += 1

@app.before_request
def before_request():
    increment_counter()

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=os.getenv("EXPOSED_PORT"))