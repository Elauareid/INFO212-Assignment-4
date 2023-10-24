import errno
from project import app
from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
from project.model.Car import listCars, addCar, updateCar, deleteCar
from flask import Flask, render_template, redirect, request, jsonify

@app.route('/cars')
def index():
    data = []
    try:
        data = listCars()
    except errno:
        print (errno)
    return jsonify(data)
    return render_template('cars.html.j2', data = data)

@app.route('/cars/list')
def car_list():
    data = []
    try:
        data = listCars()
    except errno:
        print (errno)
    return render_template('cars.html.j2', data = data)

@app.route('/cars/add', methods=["GET", "POST"])
def add_car():
    data = []
    if request.method == "POST":
        make = request.form["make"]
        model = request.form["model"]
        year = request.form["year"]
        location = request.form["location"]
        status = request.form["status"]
        try:
            addCar(make,model,year,location,status)
            data = listCars()
        except Exception as e:
            print(f"Error {e}")
        return jsonify(data)
        return render_template('cars.html.j2', data=data)
    return render_template('add_car.html.j2')

@app.route('/cars/update', methods=["GET", "POST"])
def update_car():
    if request.method == "POST":
        id = int(request.form["id"])
        newStatus = request.form["newStatus"]
        try:
            updateCar(id, newStatus)
            data = listCars()
            return jsonify(data)    
        except Exception as e:
            print(f"Error: {e}")
    return render_template('update_car.html.j2')

@app.route('/cars/delete', methods=["GET", "POST"])
def delete_car():
    if request.method == "POST":
        id = int(request.form["id"])
        try:
            deleteCar(id)
            data = listCars()
            return jsonify(data)
        except Exception as e:
            print(f"Error: {e}")
    return render_template('delete_car.html.j2')

@app.route('/cars/list/delete', methods=["GET", "POST"])
def delete_car_from_list():
    if request.method == "POST":
        id = int(request.form["id"])
        try:
            deleteCar(id)
            data = listCars()
            return render_template('cars.html.j2', data=data)
        except Exception as e:
            print(f"Error: {e}")
    return render_template('delete_car.html.j2')