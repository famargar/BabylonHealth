__author__ = 'fabriziomargaroli'

import bottle
from score_calculator import scoreToLikelihood

app = bottle.app()
DOC_ROOT = ''

# This is the not found error page
@bottle.error(404)
def error404(error):
    return bottle.template("not_found")

# This is the error page
@bottle.error(500)
def error500(error):
    return bottle.template("error")

# This route is the main page
@bottle.route('/')
def publication_index():
    return bottle.redirect('welcome')

@bottle.get('/welcome')
def welcome():
    return bottle.template('welcome')

@bottle.post('/person_detail')
def process_risk():

    name = bottle.request.forms.get("name")
    lastname = bottle.request.forms.get("lastname")
    email = bottle.request.forms.get("email")
    sex = bottle.request.forms.get("sex")
    height = float(bottle.request.forms.get("height"))
    weight = float(bottle.request.forms.get("weight"))
    glucose = float(bottle.request.forms.get("glucose"))
    HDLC = float(bottle.request.forms.get("HDLC"))
    trygl = float(bottle.request.forms.get("trygl"))
    blpress = float(bottle.request.forms.get("blpress"))
    age = int(bottle.request.forms.get("age"))
    fam = bottle.request.forms.get("fam")
    smoke = bottle.request.forms.get("smoke")
    alchool = bottle.request.forms.get("alchool")

    data = {'sex': sex, 'height': height, 'weight': weight, 'glucose': glucose, 'HDLC': HDLC,
            'trygl': trygl, 'blpress': blpress, 'age': age, 'family': fam, 'smoke': smoke,
            'alchool': alchool}

    risk = scoreToLikelihood(data)

    return bottle.template("result", dict(name="%s %s" % (name, lastname), risk=risk))

if __name__ == '__main__':

    bottle.debug(True)
    bottle.run(host='localhost', port=8084, reloader=True)  # Start the webserver running and wait for requests