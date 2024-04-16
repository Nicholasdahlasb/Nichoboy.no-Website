from flask import Flask, render_template

app = Flask(__name__)

@app.route('/old')
def main():
    return render_template('main.html')
@app.route('/mc')
def index():
    return render_template('index.html')

@app.route('/mario')
def mario():
    return render_template('mario.html')

@app.route('/skribbl')
def skribbl():
    return render_template('skribbl.html')

@app.route('/gartic-phone')
def gartic():
    return render_template('gartic-phone.html')

@app.route('/fnaf')
def fnaf():
    return render_template('fnaf.html')
@app.route('/mods')
def mods():
    return render_template('mods.html')
@app.route('/gartic-join')
def garticjoin():
    return render_template('gartic-join.html')


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




# Under her finner du alle funksjoner til new website overhaul
@app.route('/')
def main2():
    return render_template('2-main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
