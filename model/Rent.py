from project.model.Driver import _get_connection

def rentCar(customerId, carId):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "MATCH (c:Customer)-[b:BOOKED]->(car:Car) WHERE ID(c) = $customerId AND ID(car) = $carId "
                    "DELETE b "
                    "CREATE (c)-[:RENTED]-> (car) SET car.status = 'rented'",
                    customerId=customerId,
                    carId=carId
                )
            except Exception as e:
                print(f"Error: {e}")
    return

def returnCar(customerId, carId, carStatus):
    driver =_get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "MATCH (c:Customer)-[r:RENTED]->(car:Car) WHERE ID(c) = $customerId AND ID(car) = $carId "
                    "DELETE r ",
                    customerId=customerId,
                    carId=carId
                )
                if carStatus == 'ok':
                    session.run(
                        "MATCH (c:Car) WHERE ID(c) = $carId "
                        "SET c.status = 'available'",
                        carId=carId
                    )
                else:
                    session.run(
                        "MATCH (c:Car) WHERE ID(c) = $carId "
                        "SET c.status = 'damaged'",
                        carId=carId
                    )
            except Exception as e:
                print(f"Error: {e}")
    return