from flask import render_template
from flask_ask import Ask, statement, question
from flask_ask import session as ask_session
import logging
from app import ask, app
from app.date_func import countdown

logging.getLogger('flask_ask').setLevel(logging.DEBUG)






@ask.launch
def launched():
    output = render_template('welcome')
    ask_session.attributes['last_speech'] = output
    return question(output)


@ask.intent("which_holiday")
def holiday_countdown(holiday):
    output = countdown(holiday)
    return statement(output)