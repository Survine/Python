class Employee:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, position):
        self.employees.append({'name': name, 'position': position})

    def display_employees(self):
        for emp in self.employees:
            print(f"Name: {emp['name']}, Position: {emp['position']}")

manager = Employee()
manager.add_employee("Amit", "Developer")
manager.add_employee("Priya", "Designer")
manager.display_employees()