#revision for day2 

#lists
tasks = ["eat", "sleep", "code", "repeat"]
tasks.append("exercise")

tasks.remove("sleep")



#dictionaries
person = {
    "name": "Sangharsha",
    "age": 22,
    "city": "Kathmandu",
    "hobbies": ["coding", "gaming", "traveling"]
}

#error handling
def username():
    while True:
        name = input("Enter your username: ")
        if not name:
            print ("Username cannot be empty")
            continue
        if len(name) < 3:
            print("Username must be at least 3 characters long")
            continue
        return name    


def  age():
    while True:
        age = input("Enter your age: ")
        try:
            age_int= int(age)
        except ValueError:
            print("Please enter a valid number for age")
            continue
            
        if age_int < 0 or age_int > 120:
            print("Please enter a valid age between 0 and 120")
            continue    
        return age_int

user_name = username()
user_age = age()
print( "your username is:", user_name)
print( "your age is:", user_age)
