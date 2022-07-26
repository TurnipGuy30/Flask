from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
	bmi = ''
	comment = ''
	if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
		weight = float(request.form.get('weight'))
		height = float(request.form.get('height'))
		bmi = round(weight/((height/100)**2), 2)
		
		if bmi > 39.9:
			comment = 'morbidly obese'
		elif bmi > 30:
			comment = 'obese'
		elif bmi > 25:
			comment = 'overweight'
		elif bmi > 18.5:
			comment = 'in the healthy range'
		else:
			comment = 'underweight'

	return render_template('index.html', bmi=bmi, comment=comment)

if __name__ == '__main__':
	app.run()
