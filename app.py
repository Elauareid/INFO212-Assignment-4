from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
from flask import Flask, render_template, redirect, request, jsonify

app = Flask(__name__)

URI = "neo4j+s://1d9eb7a2.databases.neo4j.io:7687"
AUTH = ("neo4j", "GB2CSsX2B-dgthvoGxcaStQD1t1AoO0vVClJeSuh0rI")

driver = GraphDatabase.driver(uri=URI, auth=AUTH)

@app.route("/cars")
def list_cars():
    cars = []
    with driver.session() as session:
        result = session.run("MATCH (c:Car) RETURN c.make as make, c.model as model, c.year as year, c.location as loc, c.status as status")
        for record in result:
            cars.append({
            'make' : record["make"],
            'model' : record["model"],
            'year' : record["year"],
            'loc' : record["loc"],
            'status' : record["status"]
            })
        print(cars)
    return jsonify(cars)

@app.route("/cars/add")
def add_car():
    return jsonify()