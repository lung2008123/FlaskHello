"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import request
from time import sleep
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
@app.route('/thereisahello')
def hello():
    """Renders a sample page."""
    print("Hellow concole")
    return "Hello World!"

@app.route('/input/<name>')
def hello_1(name):
    return "Hello " + name

''' haven't figure out how to do query parameter in this way'''
''' working example in below section'''
# @app.route('/input123/<name>?message=<msg>')
@app.route('/hello/<name>?message=<msg>')
def hello_134(name, msg):
    print(name)
    print(str(name))
    print(msg)
    print(str(msg))
    return "Hello " + name + "! Message is " + msg + "."


'''working'''
@app.route('/input123')
def hello_2():
    msg_in = request.args.get('message', default = "trying hard", type = str)
    print(msg_in)
    return "Hello " + msg_in

'''not working'''
@app.route('/calculate/<float:number>')
def cal(number):
    print(number)
    answer = number + 2
    print(answer)
    print(str(answer))
    return str(answer)

'''working'''
@app.route('/calculate')
def cal_1():
    num = request.args.get('number', default = 1, type = float)
    answer = num + 2
    print(answer)
    print(str(answer))
    return str(answer)

'''Android try'''
@app.route('/Android/<search_query>')
def android_API(search_query):
    # sleep(1.5) # wait 1.5 second
    # print("Waiting ends, returning " + str(search_query) + " and dictionary.")
    
    temp_dict = {'label': 'Support', 'url': 'google.com'}
    temp_dict['search_query'] = search_query
    return temp_dict


'''
Note:
1. must return string or something, not int
'''

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
