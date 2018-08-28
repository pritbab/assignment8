#question 1
print("<------solution 1------>")
class circle():
    def __init__(self,r):
        self.rad=r
    def getArea(self):
        return 3.14*self.rad*self.rad
    def getCircumference(self):
        return 2*3.14*self.rad

r=int(input("Enter radius "))
c=circle(r)
print("Area is ",c.getArea())
print("Circumference is ", c.getCircumference())


#question 2
print("<------solution 2------>")
class student():
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def display(self):
        print("Name: ",self.name,"\nroll no: ",self.roll,"\nage: ",self.age,"\nmarks: ",self.marks,)
    def getAge(self,a):
        self.age=a
    def getMarks(self,m):
        self.marks=m
n=input("Enter name of student ")
r=int(input("Enter roll no of student "))
age=int(input("Enter age "))
marks=int(input("Enter marks "))
s=student(n,r)
s.getAge(age)
s.getMarks(marks)
s.display()

#question 3

print("<------solution 3------>")

class temprature():
    def convertFahrenheit(self,cel):
        self.cel=cel
        far=(self.cel*9/5)+32
        print(far)
    def convertCelsius(self,farh):
        self.farh=farh
        cel=(self.farh-32)*5/9
        print(cel)
n=int(input("Convert \n 1.Celsius to Farhenheit \n 2.Farhenheit to Celsius\n"))
ob=temprature()
if(n==1):
    x=float(input("Enter celsius\n"))
    ob.convertFahrenheit(x)
else:
    x=float(input("Enter farhenheit\n"))
    ob.convertCelsius(x)
    

#question 4

print("<------solution 4------>")
class MovieDetails():
    def __init__(self):
        self.artist='NA'
        self.year='NA'
        self.rating='NA'
    def add(self,a,y,r):
        self.artist=a
        self.year=y
        self.rating=r
    def display(self):
        print("artist: ",self.artist,"\nYear of release: ",\
              self.year,"\nRatings: ",self.rating)
n=input("Do you want to add detais? Y:N")
ob=MovieDetails()
if(n=='y' or n=='Y'):
    a=input("Enter artist name")
    b=int(input("Enter year"))
    c=int(input("Enter ratings"))
    ob.add(a,b,c)
    ob.display()
else:
    ob.display()


#question 5
print("<------solution 5------>")
class Animals:
    def animal_attribute(self):
        print("base class function")
class Tiger(Animals):
    pass

t=Tiger()
t.animal_attribute()

#question 6
'''<------solution 6------>
it will show error as the brackets are missing in print statement
if we corrrect the error it will display
A B
A B
'''

#question 7

print("<------solution 7------>")
class shape():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area is ",self.l*self.b)
class square(shape):
    pass
class rectangle(shape):
    pass
l=int(input("Enter length\n"))
b=int(input("Enter breadth \n"))
if(l==b):
    obj=square(l,b)
    obj.area( )
else:
    obj=rectangle(l,b)
    obj.area( )
