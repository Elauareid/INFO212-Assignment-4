from project.model.Driver import _get_connection

class Car:
    def __init__(self, make, model, year, location, status):
        self.make = make
        self.model = model
        self.year = year
        self.location = location
        self.status = status

def listCars():
    cars = []
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                result = session.run("MATCH (c:Car) RETURN ID(c) as id, c.make as make, c.model as model, c.year as year, c.location as location, c.status as status")
                for record in result:
                    cars.append({
                    'id' : record["id"],
                    'make' : record["make"],
                    'model' : record["model"],
                    'year' : record["year"],
                    'location' : record["location"],
                    'status' : record["status"]
                    })
            except Exception as e:
                print(f"Error: ",e)
    return cars

def addCar(make,model,year,location,status):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "CREATE (c:Car {make: $make, model: $model, year: $year, location: $location, status: $status})",
                    make=make,
                    model=model,
                    year=year,
                    location=location,
                    status=status
                    )
            except Exception as e:
                print(f"Error: {e}")
    return

def updateCar(id, newStatus):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "MATCH (c:Car) WHERE ID(c) = $id SET c.status = $newStatus", 
                    id=id, 
                    newStatus=newStatus
                )
            except Exception as e:
                print(f"Error: ",e)
    return

def deleteCar(id):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "MATCH (c:Car) WHERE ID(c) = $id DETACH DELETE c",
                    id=id
                )
            except Exception as e:
                print(f"Error: {e}")
    return