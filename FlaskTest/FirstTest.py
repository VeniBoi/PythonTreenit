from flask import Flask
from flask import jsonify
from flask import request
import datetime
import flask
app = Flask(__name__)

@app.route('/moro', methods=['POST'])
def hello():
    datenow = datetime.datetime.now()
    data = request.json
    if data['first_name'] == '' or data['last_name'] == '' or data['year_of_birth'] == '':
        return jsonify({'message': 'paskaks män'}), 400
    else:
        whole_name = str(data['first_name'] + " " + data['last_name'])
        age = datenow.year - data['year_of_birth']
        returnedItem = {"whole_name": whole_name, "age": age}
        return jsonify(returnedItem)
