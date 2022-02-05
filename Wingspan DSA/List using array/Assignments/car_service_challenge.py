#lex_auth_0127426245709905921377
# Problem Statement
# Consider a Car class as given in the code. Write a Service class as given in the class diagram below which performs various activities on a list of cars.
# Assume that the car_list is sorted by year in ascending order. 

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

class Service:
  def __init__(self, car_list):
    self.car_list = car_list

  def add_cars(self, new_car_list):
    self.car_list += new_car_list
    print(self.car_list)
    for i in range(len(car_list)):
      for j in range(i+1, len(car_list)):
        if car_list[i].get_year() > car_list[j].get_year():
          temp = car_list[i]
          car_list[i] = car_list[j]
          car_list[j] = temp
        
  def remove_cars_from_karnataka(self):
    for i in range(len(car_list)):
      if "KA" in car_list[i].get_registration_number():
        car_list.pop(i)

  def find_cars_by_year(self, year):
    for i in range(len(car_list)):
      #print(int(car_list[i].get_year()))
      if int(year) == int(car_list[i].get_year()):
        print(car_list[i].__str__())
      else:
        pass
    return None

  def __str__(self):
        for i in range(len(car_list)):
          print(self.car_list[i].__str__())




#Implement Service class here

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
car6=Car("Amio",2009,"Kb54 4312")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
#Create object of Service class, invoke the methods and test your program
service1 = Service(car_list)
#service1.add_cars([car6])
service1.find_cars_by_year(2013)
print(service1)

