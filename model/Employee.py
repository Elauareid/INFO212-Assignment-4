from project.model.Driver import _get_connection

class Employee:
    def __init__(self, name, address, branch):
        self.name = name
        self.address = address
        self.branch = branch

def listEmployees():
    employees = []
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                result = session.run("MATCH (e:Employee) RETURN ID(e) as id, e.name as name, e.address as address, e.branch as branch")
                for record in result:
                    employees.append({
                    'id' : record["id"],
                    'name' : record["name"],
                    'address' : record["address"],
                    'branch' : record["branch"]
                    })
            except Exception as e:
                print(f"Error: ",e)
    return employees

def addEmployee(name, address, branch):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "CREATE (e:Employee {name: $name, address: $address, branch: $branch})",
                    name=name,
                    address=address,
                    branch=branch
                    )
            except Exception as e:
                print(f"Error: {e}")
    return

def updateEmployee(id, newBranch):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "MATCH (e:Employee) WHERE ID(e) = $id SET e.branch = $newBranch", 
                    id=id, 
                    newBranch=newBranch
                )
            except Exception as e:
                print(f"Error: ",e)
    return

def deleteEmployee(id):
    driver = _get_connection()
    if driver != None:
        with driver.session() as session:
            try:
                session.run(
                    "MATCH (e:Employee) WHERE ID(e) = $id DELETE e",
                    id=id
                )
            except Exception as e:
                print(f"Error: {e}")
    return