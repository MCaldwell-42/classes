class Student:

    def __init__(self, fName, lName, age, cN):

        self.first_name = fName
        self.last_name = lName
        self.age = age
        self.cohort_number = cN
        self.full_name

    @property # The getter
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return "No First Name"

    @first_name.setter # The setter
    def first_name(self, new_fName):
        if isinstance(new_fName, str):
            self.__first_name = new_fName
        else:
            raise TypeError('Gimme a String!')
    
    
    @property # The getter
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return "No Last Name"

    @last_name.setter # The setter
    def last_name(self, new_lName):
        if isinstance(new_lName, str):
            self.__last_name = new_lName
        else:
            raise TypeError('Gimme a String!')
    
    
    @property # The getter
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return "No age"

    @age.setter # The setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self.__age = new_age
        else:
            raise TypeError('Gimme a Number!')
    
    
    @property # The getter
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return "No Cohort Number"

    @cohort_number.setter # The setter
    def cohort_number(self, new_cohort):
        if isinstance(new_cohort, int):
            self.__cohort_number = new_cohort
        else:
            raise TypeError('Gimme a Number!')

    @property # The getter
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return "No NAME!!!!"
    
    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}"

    def __repr__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}"


james = Student("James", "Smith", 24, 32)
print(james)