# Exploring *args and **kwargs in Python

def show_profile(**profile_data):
  print("Type:", type(profile_data))
  print("Name:", profile_data["name"])
  print("Age:", profile_data["age"])
  print("All data:", profile_data)

show_profile(name = "Sangharsha", age = 22, city = "Bhaktapur")

def show_user(user_name, **more_data):
  print("Username:", user_name)
  print("Additional details:")
  for item, value in more_data.items():
    print(" ", item + ":", value)

show_user("sangharsha", age = 25, city = "Bhaktapur", hobby = "coding")

#exploring scope in python
def outer_function():
  outer_var = "I am from the outer function."
  
  def inner_function():
    inner_var = "I am from the inner function."
    print(outer_var)  # Accessing outer variable
    print(inner_var)  # Accessing inner variable
  
  inner_function()
  # print(inner_var)  # This would raise an error because inner_var is not accessible here  

#exploring Decoators in Python
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Sangharsha"

print(myfunction())

#exploring lambda functions in Python
add = lambda x, y: x + y 
print(add(5, 3))
 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))