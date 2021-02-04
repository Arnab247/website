from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    name = name
    return render_template('home.html', hi=name)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')