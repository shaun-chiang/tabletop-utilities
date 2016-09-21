from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: Homepage & dice roller
    return render_template('index.html')

@app.route('/scoreboard/<name>')
def scoreboard(name):
    #TODO: scoreboard id
    return 'Scoreboard for ' + name

@app.route('/rpg_helper/<name>')
def rpg_helper(name):
    #TODO: rpg_helper
    return render_template('page.html', name=name)

@app.route('/dice_roller')
def dice_rollers():
    #TODO: dice_rollers
    return render_template('dice.html')

if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True, host='0.0.0.0')