x = "John"
y = 78
v=int(input("number of years added: "))
sentence = f"{x} is now {y+v} years old"
print(sentence)
if (y+v)<50:
    print("John is young")
else:
    print("John is old")
rate = "Old" if (y+v)>50 else "young"
print(f"John is {rate}") 

successful = True
for number in range(3):
    print(f"Attempt {number+1}")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times but failed")

def greeting(first_name,last_name):
    print(f"Hi {first_name} {last_name} and welcome!")

greeting("john","smith") 

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

a =[]
z = input("enter list of numbers: ")
for element in z.split(","):
    a.append(int(element))

b = multiply(a) 
#*a would be needed if the parameter argument for the function was *numbers as this makes it easier to use when not using input from the user#
   
print(f"{b}")
