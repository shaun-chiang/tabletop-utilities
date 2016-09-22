
from flask import Flask, render_template, flash,request, redirect, url_for
from flask_bootstrap import Bootstrap

from wtforms import StringField, SubmitField
from flask_wtf import Form
import random

app = Flask(__name__)
scoreboard_dict = dict()
current_room_id = 0

class scoreboard_form(Form):
    player_names_field = StringField('Player Names:', description='Input your player names seperated by commas. (e.g. Shaun, Ryan, Junsheng)')
    submit_button = SubmitField("Let's Play!!")

@app.route('/')
def index():
    # TODO: Homepage & dice roller
    return render_template('index.html')

@app.route('/scoreboard', methods=['GET', 'POST'])
def scoreboard():
    global current_room_id
    form = scoreboard_form()
    if request.method == 'POST' and form.validate():
        input = form.player_names_field.data
        list_of_names = input.split(",")
        current_room_id+=1
        scoreboard_dict[current_room_id]=dict()
        for i in xrange(len(list_of_names)):
            list_of_names[i] = list_of_names[i].strip()
            scoreboard_dict[current_room_id][list_of_names[i]] = 0
        return redirect(url_for('scoreboardid', id=current_room_id))
    print(scoreboard_dict)
    return render_template('scoreboard_home.html', form=form)

@app.route('/scoreboard/<id>')
def scoreboardid(id):
    global current_room_id
    try:
        if scoreboard_dict[int(id)]:
            print(scoreboard_dict[int(id)])
            return render_template('scoreboard.html', id=id)
        else:
            current_room_id += 1
            scoreboard_dict[current_room_id] = dict()
            return render_template('scoreboard.html', id=current_room_id)
    except:
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
    Bootstrap(app)
    app.secret_key = 'devkey'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
    app.run(debug=True, host='0.0.0.0')
