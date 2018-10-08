from flask import render_template
from flask_ask import Ask, statement, question
from flask_ask import session as ask_session, request as ask_request
import logging
from app import ask, app
from app.date_func import countdown

logging.getLogger('flask_ask').setLevel(logging.DEBUG)






@ask.launch
def launched():
    output = render_template('welcome')
    ask_session.attributes['last_speech'] = output
    return question(output)


@ask.session_ended
def session_ended():
    return "{}", 200



@ask.intent("which_holiday")
def holiday_countdown(holiday):
    print(ask_request.intent)
    try:
        if 'id' in ask_request.intent.slots.holiday.resolutions.resolutionsPerAuthority[0]['values'][0]['value']:
            holiday = ask_request.intent.slots.holiday.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
            print('found')
    except:
        print('no')
    print(holiday)
    output = countdown(holiday)
    return statement(output)