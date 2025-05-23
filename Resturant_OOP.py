import time

class Employee ():
    def __init__ (self,name,age,id,hours):
        self.name = name
        self.age = age
        self.id = id
        self.hours = hours

    def Clock_in (self):
        print (self.name," clocked in at ",time.strftime ("%I:%M:%S"))

    def Clock_out (self):
        print (self.name," clocked out at ",time.strftime ("%I:%M:%S"))

    def Find_Wage (self):
        self.wage = self.hours * 15

    def WHO_AM_I (self):
        print ("I am an Employee.")

class Waitress ():
    def __init__ (self,name,age,id,hours,customers):
        self.name = name
        self.age = age
        self.id = id
        self.hours = hours
        self.num_customers = customers

    def Clock_in (self):
        print (self.name," clocked in at ",time.strftime ("%I:%M:%S"))

    def Clock_out (self):
        print (self.name," clocked out at ",time.strftime ("%I:%M:%S"))


    def Find_Wage (self):
        self.wage = (self.hours * 9) + (self.num_customers * 5)

    def WHO_AM_I (self):
        print ("I am a Waitress.")

class Cashier ():
    def __init__ (self,name,age,id,hours):
        self.name = name
        self.age = age
        self.id = id
        self.hours = hours
        self.num_customers = 0

    def Find_Wage (self):
        self.wage = (self.hours * 9) + (self.num_customers * 5)

    def Customers_Served (self,number):
        self.num_customers = number
        print (self.name,"the cashier has served",self.num_customers,"customers")

    def WHO_AM_I (self):
        print ("I am a Cashier.")

    def __repr__ (self):
        return "CASHIER ({}, {})".format (self.name, self.id)

Customer_list = {}

class Customer ():

    def __init__ (self,name,order,price):
        self.name = name
        self.order = order
        self.price = price
        Customer_list[self.name] = [self.order,self.price]

    def WHO_AM_I (self):
        print ("I am a Cashier.")

Emp1 = Employee ("Bob",19,1000,8)
Emp2 = Employee ("John",19,1001,6)
Emp1.Find_Wage ()
Emp2.Find_Wage ()
print (Emp1.name,"Made",Emp1.wage)
print (Emp2.name,"Made",Emp2.wage)

Cust1 = Customer ("Jeff","pizza, pop",23.45)
Cust2 = Customer ("Fred","pie, water",18.85)
Cust3 = Customer ("Joe","ribs, pop",33.33)
print (Customer_list)
Cust1.WHO_AM_I ()
Cust2.WHO_AM_I ()
Cust3.WHO_AM_I ()

Wai1 = Waitress ("Jane",23,1100,7,24)
Wai1.Find_Wage ()
print (Wai1.wage)
Wai1.Clock_in ()
Wai1.Clock_out ()

Cash1 = Cashier ("Suzy",34,1200,7)
Cash1.Customers_Served (20)
print (Cash1)