"""
Demo Flask application to test the operation of Flask with socket.io

Aim is to create a webpage that is constantly updated with random numbers from a background python process.

30th May 2014

===================

Updated 13th April 2018

+ Upgraded code to Python 3
+ Used Python3 SocketIO implementation
+ Updated CDN Javascript and CSS sources

"""
import eventlet
# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
import monitor


__author__ = 'slynn'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode='eventlet', logger=True, engineio_logger=True)
use_eventlet = False

def randomNumberGenerator():
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    global use_eventlet
    #infinite loop of magical random numbers
    print("Making random numbers")
    use_eventlet=True
    while True:
        number = round(random()*10, 3)
        print(number)
        socketio.emit('newnumber', {'number': number}, namespace='/test')
        eventlet.sleep(5)
        
@socketio.on('connect', namespace='/test')
def test_connect():
    if not use_eventlet:
        print("fffffffffffffffffffffffffffffff")
        eventlet.spawn(randomNumberGenerator)
    
    # monitor.RandomThread().run()
    
# @socketio.on('disconnect', namespace='/test')
# def test_disconnect():
#     print('Client disconnected')

# @socketio.on('connect', namespace='/test')
# def test_connect():
#     #eventlet.spawn(randomNumberGenerator)
#     global use_eventlet
#     if not use_eventlet:
#         use_eventlet=True
#         monitor.RandomThread().run()

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

if __name__ == '__main__':
    print("22262626262626262626")
    print(socketio)
    socketio.run(app, host='0.0.0.0')
