class patients:
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history
    
    def print_details(self):
        print(f"{self.name}, {self.age}, {self.admission_date}, {self.medical_history}")

# example
p = patients("Tom", 25, "2025-04-09", "Diabetes")
p.print_details()  # output Tom, 25, 2025-04-09, Diabetes