#Q6

class A:
    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        print("Name:", self.name)

# Single Inheritance
class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def display_age(self):
        print("Age:", self.age)

# Multiple Inheritance
class C:
    def __init__(self, job):
        self.job = job
    
    def display_job(self):
        print("Job:", self.job)

class D(A, C):
    def __init__(self, name, job):
        A.__init__(self, name)
        C.__init__(self, job)

# Multilevel Inheritance
class E(B):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby
    
    def display_hobby(self):
        print("Hobby:", self.hobby)