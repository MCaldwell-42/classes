import datetime

class Employee:

    def __init__(self, name, job_title):
        # Establish the properties of each pizza
        # with a default value
        self.name = name
        self.job_title = job_title
        self.start_date = datetime.datetime.now()
        

allison = Employee("Allison", "code girl")
anna = Employee("Anna", "mystery girl")
laura = Employee("Laura", "helper girl")
savannah = Employee("Savannah", "rap girl")
kelly = Employee("Kelly", "building girl")


class Company:

    def __init__(self, name, address, industry):
        # Establish the properties of each pizza
        # with a default value
        self.name = name
        self.address = address
        self.industry_type = industry
        self.employees = list()

    def hire(self, employee):
        self.employees.append(employee)

    def about_me(self):
        emps = ""
        for names in self.employees:
            emps += f"\n * {names.name}"
        print(f"{self.name} is in the {self.industry_type} industry and has the following employees: {emps}")


hasbro = Company("Hasbro", "toy lane blvd.", "toys, bitch!")
kyowa = Company("Kyowa", "666 hell rd", "misery, bitch!")

kyowa.hire(allison)
kyowa.hire(savannah)
hasbro.hire(anna)
hasbro.hire(kelly)
hasbro.hire(laura)

kyowa.about_me()
hasbro.about_me()


