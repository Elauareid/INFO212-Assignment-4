from project.model.Driver import _get_connection

class Customer:
    def __init__(self, name, age, address, bookedCar, rentedCar):
        self.name = name
        self.age = age
        self.address = address
        self.bookedCar = bookedCar
        self.rentedCar = rentedCar

def listCustomers():
    customers = []
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                result = session.run(
                    "MATCH (c:Customer) "
                    "OPTIONAL MATCH (c)-[:BOOKED]->(bookedCar:Car) "
                    "OPTIONAL MATCH (c)-[:RENTED]->(rentedCar:Car) "
                    "RETURN ID(c) as id, c.name as name, c.age as age, c.address as address, ID(bookedCar) as bookedCar, ID(rentedCar) as rentedCar"
                    )
                for record in result:
                    customers.append({
                    'id' : record["id"],
                    'name' : record["name"],
                    'age' : record["age"],
                    'address' : record["address"],
                    'bookedCar' : record["bookedCar"],
                    'rentedCar' : record["rentedCar"]
                    })
            except Exception as e:
                print(f"Error: ",e)
    return customers

def addCustomer(name, age, address):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "CREATE (c:Customer {name: $name, age: $age, address: $address})",
                    name=name,
                    age=age,
                    address=address
                    )
            except Exception as e:
                print(f"Error: {e}")
    return

def updateCustomer(id, newAddress):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "MATCH (c:Customer) WHERE ID(c) = $id SET c.address = $newAddress", 
                    id=id, 
                    newAddress=newAddress
                )
            except Exception as e:
                print(f"Error: ",e)
    return

def deleteCustomer(id):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "MATCH (c:Customer) WHERE ID(c) = $id DELETE c",
                    id=id
                )
            except Exception as e:
                print(f"Error: {e}")
    return
