#/usr/bin/env python
from twilio.twiml.voice_response import VoiceResponse, Gather, Say
from twilio.rest import Client
from flask_wtf import Form
from flask import Flask, request, redirect, render_template, flash, url_for
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

account_sid = "AC2425372beab1b202441153b8ebb251b8"
auth_token = "7d47175071b77edc716e761bafbaafb4"
client = Client(account_sid, auth_token)

#Homepage with a form to submit a specified phone number
@app.route('/', methods=['GET', 'POST'])
def index():
	form = ContactForm(request.form)

	#If the action is a POST, make a call and redirect to /greet
	if request.method == 'POST':
		to_num = request.form['to_num']
		make_call(to_num)
		return redirect(url_for('greet'))
		
	return render_template('index.html', form = form)

#Uses Twilio's API to prompt a caller to play the fizzbuzz game
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    resp = VoiceResponse()
    gather = Gather(action='/fizzbuzz', method='POST')
    gather.say('Press a number to initiate fizz buzz.')
    resp.append(gather)
    return str(resp)

#Creates an appropriate fizzbuzz response to keypad input from the user
@app.route('/fizzbuzz', methods=['GET', 'POST'])
def fizz_buzz():
	num = int(request.values.get('Digits', None))
	ret = ''
	for i in range(1, num+1):
		if i%15 == 0:
			ret += 'Fizz Buzz '
		elif i%3 == 0:
			ret += 'Fizz '
		elif i%5 == 0:
			ret += 'Buzz '
		else:
			ret += str(i) + ' '

	#If the user inputs 0, prompt again
	if num == 0:
		return redirect('/greet')

	resp = VoiceResponse()
	resp.say(ret)

	return str(resp)

#Using Twilio's API, make a call and execute TwiML at the specified URL
def make_call(number):
	call = client.calls.create(
		to= number,
		from_="+14243873255",
		url="https://269d2e8d.ngrok.io"
)


if __name__ == "__main__":
    app.run(debug=True)


