from flask import Flask, render_template, request

# Flask app
app = Flask(__name__)

# Home Page Avatar Hermess 
@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=1000, debug=True)