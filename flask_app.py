' Web app which detects Brute force attacks '

import re
from flask import *
from my_main import transcript, download_video

app = Flask(__name__)
app.secret_key = 'my_secret_key_123'

class var:
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
    '''


@app.route('/', methods = ['POST', 'GET'])
def home():
    msg = ''
    if request.method == 'POST':
        link = request.form['link']
        msg = 'Link added to queue'
    else:
        msg = ''
    return render_template_string(var.html_code, msg=msg)

if __name__ == "__main__":
    app.run(port=8080)

