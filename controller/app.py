from project import app
from project.model.Car import listCars, addCar, updateCar, deleteCar
from project.model.Customer import listCustomers, addCustomer, updateCustomer, deleteCustomer
from project.model.Employee import listEmployees, addEmployee, updateEmployee, deleteEmployee
from project.model.Order import orderCar, cancelOrder
from project.model.Rent import rentCar, returnCar
from flask import Flask, render_template, request, jsonify

@app.route('/cars')
def car_index():
    data = []
    try:
        data = listCars()
    except Exception as e:
        print (f"Error: {e}")
    return jsonify(data)

@app.route('/cars/list')
def car_list():
    data = []
    try:
        data = listCars()
    except Exception as e:
        print (f"Error: {e}")
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
            return jsonify(data)
        except Exception as e:
            print(f"Error {e}")
    return render_template('add_car.html.j2')

@app.route('/cars/update', methods=["GET", "POST"])
def update_car():
    if request.method == "POST":
        id = int(request.form["id"])
        newStatus = request.form["newStatus"].lower()
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

@app.route('/customers')
def customer_index():
    data = []
    try:
        data = listCustomers()
    except Exception as e:
        print (f"Error: {e}")
    return jsonify(data)

@app.route('/customers/list')
def customer_list():
    data = []
    try:
        data = listCustomers()
    except Exception as e:
        print (f"Error: {e}")
    return render_template('customers.html.j2', data = data)

@app.route('/customers/add', methods=["GET", "POST"])
def add_customer():
    data = []
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        address = request.form["address"]
        try:
            addCustomer(name,age,address)
            data = listCustomers()
            return jsonify(data)
        except Exception as e:
            print(f"Error {e}")
    return render_template('add_customer.html.j2')

@app.route('/customers/update', methods=["GET", "POST"])
def update_customer():
    if request.method == "POST":
        id = int(request.form["id"])
        newAddress = request.form["newAddress"]
        try:
            updateCustomer(id, newAddress)
            data = listCustomers()
            return jsonify(data)    
        except Exception as e:
            print(f"Error: {e}")
    return render_template('update_customer.html.j2')

@app.route('/customers/delete', methods=["GET", "POST"])
def delete_customer():
    if request.method == "POST":
        id = int(request.form["id"])
        try:
            deleteCustomer(id)
            data = listCustomers()
            return jsonify(data)
        except Exception as e:
            print(f"Error: {e}")
    return render_template('delete_customer.html.j2')

@app.route('/customers/list/delete', methods=["GET", "POST"])
def delete_customer_from_list():
    if request.method == "POST":
        id = int(request.form["id"])
        try:
            deleteCustomer(id)
            data = listCustomers()
            return render_template('customers.html.j2', data=data)
        except Exception as e:
            print(f"Error: {e}")
    return render_template('delete_customer.html.j2')

@app.route('/employees')
def employee_index():
    data = []
    try:
        data = listEmployees()
    except Exception as e:
        print (f"Error: {e}")
    return jsonify(data)

@app.route('/employees/list')
def employee_list():
    data = []
    try:
        data = listEmployees()
    except Exception as e:
        print (f"Error: {e}")
    return render_template('employees.html.j2', data = data)

@app.route('/employees/add', methods=["GET", "POST"])
def add_employee():
    data = []
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        branch = request.form["branch"]
        try:
            addEmployee(name,address,branch)
            data = listEmployees()
            return jsonify(data)
        except Exception as e:
            print(f"Error {e}")
    return render_template('add_employee.html.j2')

@app.route('/employees/update', methods=["GET", "POST"])
def update_employee():
    if request.method == "POST":
        id = int(request.form["id"])
        newBranch = request.form["newBranch"]
        try:
            updateEmployee(id, newBranch)
            data = listEmployees()
            return jsonify(data)    
        except Exception as e:
            print(f"Error: {e}")
    return render_template('update_employee.html.j2')

@app.route('/employees/delete', methods=["GET", "POST"])
def delete_employee():
    if request.method == "POST":
        id = int(request.form["id"])
        try:
            deleteEmployee(id)
            data = listEmployees()
            return jsonify(data)
        except Exception as e:
            print(f"Error: {e}")
    return render_template('delete_customer.html.j2')

@app.route('/employees/list/delete', methods=["GET", "POST"])
def delete_employees_from_list():
    if request.method == "POST":
        id = int(request.form["id"])
        try:
            deleteEmployee(id)
            data = listEmployees()
            return render_template('employees.html.j2', data=data)
        except Exception as e:
            print(f"Error: {e}")
    return render_template('delete_employees.html.j2')

@app.route('/cars/order', methods=["GET", "POST"])
def order_car():
    data = []
    if request.method == "POST":
        customerId = int(request.form["customerId"])
        carId = int(request.form["carId"])
        try:
            orderCar(customerId,carId)
            data = listCustomers()
        except Exception as e:
            print(f"Error: {e}")
    return jsonify(data)

@app.route('/cars/order/delete', methods=["GET", "POST"])
def cancel_order():
    data = []
    if request.method == "POST":
        customerId = int(request.form["customerId"])
        carId = int(request.form["carId"])
        try:
            cancelOrder(customerId,carId)
            data = listCustomers()
        except Exception as e:
            print(f"Error: {e}")
    return jsonify(data)

@app.route('/cars/rent', methods=["GET", "POST"])
def rent_car():
    data = []
    if request.method == "POST":
        customerId = int(request.form["customerId"])
        carId = int(request.form["carId"])
        try:
            rentCar(customerId,carId)
            data = listCustomers()
        except Exception as e:
            print(f"Error: {e}")
    return jsonify(data)

@app.route('/cars/return', methods=["GET", "POST"])
def return_car():
    data = []
    if request.method == "POST":
        customerId = int(request.form["customerId"])
        carId = int(request.form["carId"])
        carStatus = request.form["carStatus"].lower()
        try:
            returnCar(customerId,carId,carStatus)
            data = listCustomers()
        except Exception as e:
            print(f"Error: {e}")
    return jsonify(data)