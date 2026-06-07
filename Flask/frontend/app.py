from flask import Flask, request, render_template
from datetime import datetime
import requests

BACKEND_URL = 'http://0.0.0.0:9000'

app = Flask(__name__)

@app.route('/')
def home():
    dayof_week = datetime.today().strftime('%A')
    print(dayof_week)
    return render_template('index.html', day_of_week = dayof_week)

@app.route('/submit', methods=['POST'])
def submit():
    formData = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=formData)
    return "Data Retrieved"

@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL + '/view')
    return response.json()
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8000)