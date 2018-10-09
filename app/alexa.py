from flask import render_template
from flask_ask import Ask, statement, question
from flask_ask import session as ask_session, request as ask_request, context
import logging
from app import ask, app
from app.date_func import countdown, get_random_quote, check_holiday_exists

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
    holiday = holiday.lower()
    check_holiday = check_holiday_exists(holiday)
    print(check_holiday)
    if check_holiday is False:
        return question(
            "I don't know that holiday. Would you like to ask about another holiday?")
    days_to_holidate = countdown(holiday)
    random_quote = get_random_quote(holiday)
    display = context.System.device.supportedInterfaces.Display
    if days_to_holidate == 0:
        response = f'Today is {holiday}. I hope you have a great day'
    else:
        response= f'{days_to_holidate} days till {holiday}. {random_quote}'
    textContent = {'primaryText': {'type': 'RichText', 'text': response}}
    if display == None:
        return statement(response) \
            .standard_card(title='Holiday Countdown',
                           text= f'{response}')
    else:
        return statement(
            response).display_render(
            template='BodyTemplate2',
            title='Holiday Countdown',
            text=textContent,
            )
    #return statement(output)


@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
@ask.intent('AMAZON.NoIntent')
def goodbye():
    return statement('Good bye')


@ask.intent('AMAZON.HelpIntent')
def help():
    return question("if you name a holiday I can tell you how many days till we celebrate")


@ask.intent('AMAZON.FallbackIntent')
def fallback():
    return question('Sorry I need more information. '
                    'Please give me the name of a holiday')


@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_speech = ask_session.attributes['last_speech']
    return question(repeat_speech)