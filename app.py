from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

userName = []

def open_file(grade, subject):
    infile = open('files/{}/{}.txt'.format(grade, subject), 'r')
    allofit = infile.readlines()
    data = []
    for n in range(len(allofit)):
        data.append(allofit[n])
    return data

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
    # global userName
    # while len(userName) > 1:
    #     userName.pop()
    if request.method == "GET":
        return render_template('grade-11/biology.html', question="Test Yourself!", answer="Click one of the options below...")
    else:
        text = open_file("11", "biology")
        if request.form.get('1') == 'Homeostasis and Wellness':
            text = find_question(text[0])
        elif request.form.get('2') == 'Digestion and Nutrition':
            text = find_question(text[1])
        elif request.form.get('3') == 'Biochemistry':
            text = find_question(text[2])
        elif request.form.get('4') == 'Transportation and Respiration':
            text = find_question(text[3])
        elif request.form.get('5') == 'Excretion and Waste Management':
            text = find_question(text[4])
        elif request.form.get('6') == 'Protection and Control':
            text = find_question(text[5])
        else:
            text = find_unit(text)
            text = find_question(text)
        # return redirect('/biology30S/{}'.format(name), question=text[0], answer=text[1])
        return render_template('grade-11/biology.html', question=text[0], answer=text[1])

@app.route("/ivyisthebest")
def ivy():
    return render_template("ivy.html")

@app.route("/<name>", methods=["GET", "POST"])
def hello(name):
    global userName
    # for n in range(len(userName)):
    #     if userName[n] == 'favicon.ico':
    #         userName.remove(userName[n])
    if request.method == "GET":
    #     userName.append(name)
    #     if userName[0] == 'favicon.ico':
    #         return render_template('welcome-home.html', hi=userName[1])
    #     else:
    #         return render_template('welcome-home.html', hi=userName[0])
        render_template('welcome-home.html', name=name)
    else:
        print('hi')
        print(request.form.get('Biology'))
        print(userName)
        if request.form.get('Biology') == 'Biology':
            return redirect(url_for('biology30S'))
        
@app.route("/driverz")
def driverz():
    if request.method == "GET":
        return render_template('driverz.html', question="Start", answer1="Start", answer2 ="Start", answer3 ="Start", answer4="Start", answer5 ="Start")
    else:
        text = open_file("na", "driverz")
        text = find_question(text)
        answers = text[1].split(",")
        return render_template('driverz.html', question=text[0], answer1=answers[0], answer2 = answers[1], answer3 = answers[2], answer4=answers[3], answer5 = answers[4])


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False, host='0.0.0.0')
