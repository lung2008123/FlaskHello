"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import time
from flask import Flask
from flask import request
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

# https://flask-hello-dragon-1.azurewebsites.net/calculate?number=32
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
    
    temp_dict = {'label': 'Support', 'url': 'google.com', 'evidence': 'Is ghost is human I look out can!!!'}
    temp_dict['search_query'] = search_query
    return temp_dict


'''Android try with time wait (only work in Azure)'''
@app.route('/Android_wait/<search_query>')
def android_API_wait(search_query):
    global temp_dict
    time.sleep(3) # wait 3 second
    # print("Waiting ends, returning " + str(search_query) + " and dictionary.")

    if search_query == "Fake":
        temp_dict = {'label': 'REFUTES', 'url': 'google.com', 'evidence': 'Is ghost is human I look out can!!!'}
    elif search_query == "Fact":
        temp_dict = {'label': 'SUPPORTS', 'url': 'google.com', 'evidence': 'Is ghost is human I look out can!!!'}
    elif search_query == "Ne":
        temp_dict = {'label': 'NOT ENOUGH INFO', 'url': 'google.com', 'evidence': 'Is ghost is human I look out can!!!'}

    temp_dict['search_query'] = search_query
    # temp_dict = {'label': 'Support', 'url': 'google.com', 'evidence': 'Is ghost is human I look out can!!!'}
    # temp_dict['search_query'] = search_query
    return temp_dict


'''works in local'''
@app.route('/Android_wait_local/<search_query>')
def android_API_wait_local(search_query):
    temp_dict_that = {}
    time.sleep(3)  # wait 3 second
    # print("Waiting ends, returning " + str(search_query) + " and dictionary.")

    if search_query == "Fake":
        temp_dict_that['label'] = 'REFUTES'
    elif search_query == "Fact":
        temp_dict_that['label'] = 'SUPPORTS'
    else:
        temp_dict_that['label'] = 'NOT ENOUGH INFO'

    temp_dict_that['search_query'] = search_query
    temp_dict_that['url'] = 'google.com'
    temp_dict_that['evidence'] = 'Is ghost is human I look out can!!!'
    # temp_dict = {'label': 'Support', 'url': 'google.com', 'evidence': 'Is ghost is human I look out can!!!'}
    # temp_dict['search_query'] = search_query
    return temp_dict_that

@app.route("/flask_post_testing_1/", methods=["POST"])
def post_fun_1():

    data_json = request.get_json()
    search_query = data_json["search_query"]

    # print(data_json["uid"])
    # print(data_json["search_query"])

    temp_dict_this = {}

    if search_query == "Fake":
        temp_dict_this['label'] = 'REFUTES'
    elif search_query == "Fact":
        temp_dict_this['label'] = 'SUPPORTS'
    else:
        temp_dict_this['label'] = 'NOT ENOUGH INFO'

    temp_dict_this['search_query'] = data_json["search_query"]
    temp_dict_this['url'] = 'google.com'
    temp_dict_this['evidence'] = 'Is ghost is human I look out can!!!'
    return temp_dict_this


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


"""
git push to git push azure-first-working master

"""
