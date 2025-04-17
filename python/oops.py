##class,object,inheritance,poly,encap,abstraction

##class-->blueprint of objects
##objects-->instance of class

# class car:
#     name="xyz"
#     year=2020

#     def display(self):
#         print("car name",self.name)
# obj=car()
# obj.display()

class car:
#     name="xyz"
#     year=2020
    def __init__(self,name,year):#constructor
        self.name=name
        self.year=year

    def display(self):
        print("car name",self.name)
obj= car("bmw",2020)
obj.display()

#inheritance
##single,multiple,multilevel,hei,hyb

# single inheritance-->
# class person:
#     def __init__(self,name):
#         self.name=name
# class Employee(person):
#     def __init__(self,name,salary):
#         self.salary=salary
#         super().__init__(name)

##multiple
# class job:
#     def __init__(self,salary):
#         self.salary=salary
# class EmployeePersonJob(Employee,job):
#    Employee(self,name,salary)
#    job.__init__(self,salary)


##multilevel
class Manager(EmployeePersonJob):
