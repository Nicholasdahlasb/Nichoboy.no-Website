from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')
@app.route('/mc')
def index():
    return render_template('index.html')

@app.route('/mario')
def mario():
    return render_template('mario.html')

@app.route('/updates')
def updates():
    return render_template('update-log.html')

@app.route('/bluemap')
def bluemap():
    return render_template('bluemap.html')

@app.route('/doom')
def doom():
    return render_template('doom.html')

@app.route('/discord')
def discord():
    return render_template('discord.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
