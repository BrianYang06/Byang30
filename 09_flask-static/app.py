"""
Brian Yang, Donald Bi, Faiyaz Rafee - Dual Ducks
SoftDev
K09 -- Using flask to serve static files.
2022-10-12
time spent: .5 hours

Disco:
- Static webpages never change
- If you dont have a file extension and you try to open it on the webpage it downloads the files
- Static webpages are good for showing Dq1

QCC:
- What if you put non .html files in there and try to open it on the webpage?
- What exactly makes flask recognize the static folder and allow for it to work?
"""


# Clyde 'Thluffy' Sinclaird
# SoftDev
# Oct 2022

# DEMO
# basics of /static folder

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
