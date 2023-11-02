#Calculating area and perimter of the circle
class calculation:
    pi=3.14

    #Displaying the pi value
    def pi_value(self):
        print("Pi value is : ",self.pi)
    
    #Calcuating area of the circle using formula(3.14*radius*radius)
    def area_of_circle(self, radius):
        area = self.pi * radius * radius
        print("Area of the circle : ", area)
    
    #Calculating perimeter of circle using formula(2*3.14*radius)
    def perimeter_of_circle(self, radius):
        perimeter = 2 * self.pi * radius
        print("Perimiete of the circle : ", perimeter)


radius=[10,501,22,37,100,999,87,351]

print("Radius of the circle is :", radius[0])

#creating an object for the class cirlce
s=calculation()

s.pi_value()
s.area_of_circle(radius[0])
s.perimeter_of_circle(radius[0])