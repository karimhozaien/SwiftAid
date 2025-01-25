from flask import Flask, render_template

app = Flask(__name__)

# cchange
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', person='John Doe')

if __name__ == '__main__':
    app.run()
