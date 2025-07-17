
# if statements

x= 5
if x < 10:
    print("x is greater than 10")


# if else statments

x=5
if x > 10:
    print(f"the value is greater than {x}")
else:
    print(f"the value is less than {x} ")

# if elif statements

x=15
if x> 30:
    print("X is greater ") 
elif x<30:
    print(f"the value is greter {x}")
else:
    print("Everthing is fine")

#loops

fruits={"apple","banna","Cherry","mango"}
for fruit in fruits:
    print(fruit)

Laptops={"Acer","Lenovo","Mac","Dell"}
for laps in Laptops:
    print(laps)


i=5
while i<10:
    print(i)
    i+=1

for i in range(5):
    while i==5:
        break
    print(i)

for i in range(5):
    while i==5:
        continue
    print(i)

for i in range(5):
    while i==5:
        pass
    print(i)

# functions in python

def swamy(name):
    print(f"you name is {name} ")

swamy("Muthuswamy")


















