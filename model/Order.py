from flask import jsonify
from project.model.Driver import _get_connection

def orderCar(customerId, carId):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                result = session.run(
                    "MATCH (c:Customer)-[:BOOKED]->(car:Car) WHERE ID(c) = $customerId RETURN car",
                    customerId = customerId
                )
                if result.single():
                    print("You cant book")
                else: 
                    print("You can book")
                    booking = session.run(
                        "MATCH (car:Car) WHERE ID(car) = $carId AND car.status = 'available' "
                        "MATCH (c:Customer) WHERE ID(c) = $customerId "
                        "CREATE (c)-[:BOOKED]->(car) SET car.status = 'booked'",
                        customerId=customerId,
                        carId=carId
                    )
            except Exception as e:
                print(f"Error: {e}")
    return

def cancelOrder(customerId, carId):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                result = session.run(
                    "MATCH (c:Customer)-[b:BOOKED]->(car:Car) WHERE ID(c) = $customerId AND ID(car) = $carId "
                    "DELETE b "
                    "SET car.status = 'available'",
                    customerId=customerId,
                    carId=carId
                )
                return
            except Exception as e:
                print(f"Error: {e}")
    return