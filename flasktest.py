from flask import Flask
app = Flask(__name__)


NAMES = ['Kyle']
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/home/<name>')
def hello_person(name):
    NAMES.append(name)
    peeps = ""
    for person in NAMES:
        peeps += f'<br>{person}'
    return peeps

if __name__ == "__main__":
    app.run()
