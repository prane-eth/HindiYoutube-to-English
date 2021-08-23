' Web app which detects Brute force attacks '

import os, threading, time, sys
from flask import *
from my_main import transcript, download_video

app = Flask(__name__)
app.secret_key = 'my_secret_key_123'
sys.stdout = open('output.txt', 'a')


class var:
    link = ''
    html_code = '''
        <title> Youtube to English </title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <div align="center" class="border"> 
            <div class="header">
                <h1 class="word"> Youtube to English </h1>
                <br>
            </div>
            <h2 class="word"> 
                <form action="/" method="post"> 
                <input id="link" name="link" type="text" placeholder="Enter YouTube link" class="textbox"> </br> </br> 
                <input type="submit" class="btn btn-primary" value="Translate">
                </form> 
                <div class="msg"> {{ msg }} </div> 
            </h2> 
        </div>
        Last translated: <br>
        <a href='./last_translated'> Click here </a> <br>
    '''


# https://stackoverflow.com/questions/59850517/how-to-run-background-tasks-in-python
class BackgroundTasks(threading.Thread):
    def run(self, *args, **kwargs):
        os.system('python3 my_main.py ' + var.link)


@app.route('/', methods = ['POST', 'GET'])
def home():
    msg = ''
    txt = '-'
    if request.method == 'POST':
        link = request.form['link']
        msg = 'Link added to queue'
        var.link = link
        t = BackgroundTasks()
        t.start()
    #
    return render_template_string(var.html_code, msg=msg)


@app.route('/last_translated/')
def output():
    output1 = ''
    with open('last_translated.txt') as file:
        output1 = file.read()
    return output1


@app.route('/output/')
def output():
    output1 = ''
    with open('output.txt') as file:
        output1 = file.read()
    return output1


if __name__ == "__main__":
    app.run(port=8080)

