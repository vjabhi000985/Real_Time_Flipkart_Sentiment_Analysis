from flask import Flask, render_template, request
import joblib

# load the models
try:
	model = joblib.load('models/model_v2.pkl')
	vectorizer = joblib.load('models/vectorizer_v2.pkl')
	print('loaded successfully!')
except Exception as e:
	print('error occurred', e)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def prediction():
	new_review = request.form.get('review-text')
	new_review_features = vectorizer.transform([new_review]).toarray()
	prediction = model.predict(new_review_features)[0]

	return render_template("result.html", new_review=new_review, prediction=prediction)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)