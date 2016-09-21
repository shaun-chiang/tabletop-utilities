from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from flask_wtf import Form
import random

app = Flask(__name__)

class scoreboard_form(Form):
    player_names_field = StringField('Player Names:', description='Input your player names seperated by commas. (e.g. Shaun, Ryan, Junsheng)')
    submit_button = SubmitField("Let's Play!!")

@app.route('/')
def index():
    # TODO: Homepage & dice roller
    return render_template('index.html')

@app.route('/scoreboard')
def scoreboard():
    form = scoreboard_form()
    return render_template('scoreboard_home.html', form=form)

@app.route('/scoreboard/<id>')
def scoreboardid(id):
    try:
        if (scoreboard_dict[int(id)]):
            return render_template('scoreboard.html', id=id)
        else:
            room_id = random.randint(0,10000)
            scoreboard_dict[room_id] = dict()
            return render_template('scoreboard.html', id=room_id)
    except:
        flash('Invalid Room Id', 'error')
        return render_template('invalid_scoreboard.html')


@app.route('/rpg_helper/<name>')
def rpg_helper(name):
    #TODO: rpg_helper
    return render_template('page.html', name=name)

@app.route('/dice_roller')
def dice_rollers():
    #TODO: dice_rollers
    return render_template('dice.html')

if __name__ == '__main__':
    scoreboard_dict = dict()
    Bootstrap(app)
    app.secret_key = 'devkey'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
    app.run(debug=True, host='0.0.0.0')
