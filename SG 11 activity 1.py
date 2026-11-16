class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        print("Patient Name: ", self.name)

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        print("Original Bill: ₱", self.bill_amount)
    
    def set_bill_amount(self, bill_amount):
        self.name = bill_amount

    def calculate_bill(self):
        total_bill = self.bill_amount
        print("Final Bill: ₱", total_bill)

    def display_patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):
    def calculate_bill(self):
        total_bill = self.bill_amount - (self.bill_amount*0.2)
        print("Final Bill: ₱", total_bill)

    def display_patient_type(self):
            print("Patient Type: Senior Citizen")

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        total_bill = self.bill_amount - (self.bill_amount*0.15)
        print("Final Bill: ₱", total_bill)

    def display_patient_type(self):
            print("Patient Type: PhilHealth Member")


patient = Patient("Juan Dela Cruz", 15000.00)
senior_patient = SeniorPatient("Maria Santos", 15000.00)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000.00)


print("Hospital Billing System")
print("-----------------------")
patient.get_name()
patient.display_patient_type()
patient.get_bill_amount()
patient.calculate_bill()
print()

senior_patient.get_name()
senior_patient.display_patient_type()
senior_patient.get_bill_amount()
senior_patient.calculate_bill()
print()

philhealth_patient.get_name()
philhealth_patient.display_patient_type()
philhealth_patient.get_bill_amount()
philhealth_patient.calculate_bill()
