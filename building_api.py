# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:45:35 2021

@author: 49160
"""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def sample():
    return "This is my first API"

if __name__ == '__main__':
    app.run(debug = True)