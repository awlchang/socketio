import eventlet
# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from application import socketio

class RandomThread():
    # def __init__(self):
    #     super(RandomThread, self).__init__()
        
    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print("Making random numbers")
        while True:
            number = round(random()*10, 3)
            print(number)
            socketio.emit('newnumber', {'number': number}, namespace='/test')
            socketio.sleep(5)
            
    def run(self):
        print("monononononononononono")
        print(socketio)
        eventlet.spawn(self.randomNumberGenerator)
        # self.randomNumberGenerator()