from findARestaurant_a import findARestaurant
from models_a import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = 'dummy_foursquare_client_id'
foursquare_client_secret = 'dummy_client_secret'
google_api_key = 'dummy_api_key'

engine = create_engine('sqlite:///restaurants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
    #YOUR CODE HERE
    if request.method == 'GET':
        restaurants = session.query(Restaurant).all()
        return jsonify(Restaurants=[i.serialize for i in restaurants])

    if request.method == 'POST':
        restaurant = findARestaurant(request.args.get('location'), request.args.get('mealType'))
        if type(restaurant) == str:
            return restaurant

        restaurant_to_save = Restaurant(name=restaurant['name'], address=restaurant['address'], image=restaurant['image'])
        session.add(restaurant_to_save)
        session.commit()
        return jsonify(Restaurant=restaurant_to_save.serialize)


@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
    #YOUR CODE HERE
    restaurant = session.query(Restaurant).filter_by(id = id).one()

    if request.method == 'GET':        
        return jsonify(restaurant.serialize)

    if request.method == 'PUT':
        name = request.args.get('name', '')
        location = request.args.get('location', '')
        image = request.args.get('image', '')

        if name:
            restaurant.name = name
        if location:
            restaurant.address = location
        if image:
            restaurant.image = image
        
        session.add(restaurant)
        session.commit()

        return jsonify('Updated')

    if request.method == 'DELETE':
        session.delete(restaurant)
        session.commit()

        return jsonify('Removed')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)


