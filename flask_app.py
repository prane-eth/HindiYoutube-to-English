' Web app which detects Brute force attacks '

import re
from flask import *
from my_main import transcript, download_video

app = Flask(__name__)
app.secret_key = 'my_secret_key_123'


@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = request.form['link']
        download_video(link)
        text = transcript()
    else:
        text = ''
    return render_template_string(var.html_code, msg=msg)

if __name__ == "__main__":
    app.run(port=8080)

