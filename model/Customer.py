from project.model.Driver import _get_connection
import re

class Customer:
    def __init__(self, name, age, address, bookedCar):
        self.name = name
        self.age = age
        self.address = address
        self.bookedCar = bookedCar

def listCustomers():
    customers = []
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                result = session.run(
                    "MATCH (c:Customer) "
                    "OPTIONAL MATCH (c)-[:BOOKED]->(car:Car) "
                    "RETURN ID(c) as id, c.name as name, c.age as age, c.address as address, ID(car) as bookedCar"
                    )
                for record in result:
                    customers.append({
                    'id' : record["id"],
                    'name' : record["name"],
                    'age' : record["age"],
                    'address' : record["address"],
                    'bookedCar' : record["bookedCar"]
                    })
                print(customers)
                return customers
            except Exception as e:
                print(f"Error: ",e)
                return customers
    print("Driver not connected")
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
                return
            except Exception as e:
                print(f"Error: {e}")
                return
    print("Driver not connected")
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
                return
            except Exception as e:
                print(f"Error: ",e)
                return
    print("Driver is not connected")
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
                return
            except Exception as e:
                print(f"Error: {e}")
                return
    print("Driver is not connected")
    return
