from flask import Flask, render_template, request
import random
app = Flask(__name__)

def open_file(grade, subject):
    infile = open('files/{}/{}.txt'.format(grade, subject), 'r')
    allofit = infile.readlines()
    splitdata = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
    return splitdata

def find_unit(data):
    x = len(data)
    x = random.randint(0, x-1)
    return data[x]

def find_question(data):
    data = data.split("! !")
    x = random.randint(1, (len(data)/2))
    x = 2*x - 2
    return [data[x], data[x+1]]

@app.route("/")
def main():
    return render_template('home.html')

@app.route("/biology30S", methods=["GET", "POST"])
def biology30S():
    if request.method == "GET":
        return render_template('grade-11/biology.html', question="Test Yourself!", answer="Click one of the options below...")
    else:
        text = open_file("11", "biology")
        text = find_unit(text)
        text = find_question(text)
        return render_template('grade-11/biology.html', question=text[0], answer=text[1])

@app.route("/<name>")
def hello(name):
    name = name
    return render_template('welcome-home.html', hi=name)

if __name__ == '__main__':
#     app.run(debug=True)
    app.run(debug=False, host='0.0.0.0')
