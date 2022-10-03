'''
Brian Yang & Harry Zhu
SoftDev
k07 --
2022-10-03
time spent:
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs? Python __main__

@app.route("/") # Q1: What points of reference do you have for meaning of '/'? File location
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print? Probably the console. It will print the name of the app
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?  No bc the return is never used

app.run()  # Q5: Where have you seen similar constructs in other languages? Processing to run a file


'''
DISCO: 

QCC:
0.
1.
2.
3.
4.
5.
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
