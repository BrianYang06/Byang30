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
- "No hablo queso!" is printed but pring(__name__) isnt shown
- You have to open localhost:5000 to see the program run
- function hello_world is automatically used even through its never called
- If you remove app.run() you cannot connect to localhost:5000

QCC:
0. What does @app.route("/") do?
1. Why is the return statement shown but not the print statement?
2. Why is function hello_world used when its never called?
3. What does __name__ in app = Flask(__name__) do?
4. Where does print(__name__) print to?
5. What's the difference between keyword from and import?
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
