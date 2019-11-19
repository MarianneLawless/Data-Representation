#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='',
			# go back to parent directory
            static_folder='../')

# JSON where inital cars are coming from
cars = [
    {
        "reg":"181 G 1234",
        "make":"Ford",
        "model":"Mondeo",
        "price":18000
    },
    {
        "reg":"11 MO 1234",
        "make":"Nissan",
        "model":"Micra",
        "price":8000
    },
    {
        "reg":"171 D 4321",
        "make":"Toyota",
        "model":"Yaris",
        "price":600
    }
]

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify( {'cars' : cars})

@app.route('/cars/<string:reg>', methods =['GET'])
def get_car(reg):
    foundCars = list(filter(lambda t : t['reg'] == reg , cars))
    if len(foundCars) == 0:
        return jsonify( { 'car' : '' }),204
    return jsonify( { 'car' : foundCars[0] })

@app.route('/cars', methods=['POST'])
def create_car():
    if not request.json:
        abort(400)
    if not 'reg' in request.json:
        abort(400)
    car={
        "reg":  request.json['reg'],
        "make": request.json['make'],
        "model":request.json['model'],
        "price":request.json['price']
    }
    cars.append(car)
    return jsonify( {'car':car }),201

@app.route('/cars/<string:reg>', methods =['PUT'])
def update_car(reg):
    foundCars=list(filter(lambda t : t['reg'] ==reg, cars))
    if len(foundCars) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'make' in request.json and type(request.json['make']) != str:
        abort(400)
    if 'model' in request.json and type(request.json['model']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400)
    foundCars[0]['make']  = request.json.get('make', foundCars[0]['make'])
    foundCars[0]['model'] =request.json.get('model', foundCars[0]['model'])
    foundCars[0]['price'] =request.json.get('price', foundCars[0]['price'])
    return jsonify( {'car':foundCars[0]})

@app.route('/cars/<string:reg>', methods =['DELETE'])
def delete_car(reg):
    foundCars = list(filter (lambda t : t['reg'] == reg, cars))
    if len(foundCars) == 0:
        abort(404)
    cars.remove(foundCars[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug = True)