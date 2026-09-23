# what is indexing 

# indexing is the process of accessing an individual elements
# within a sequence-such as a string, list 
# or tupple-by referring to 
# its specific postion number

# string = "Hello a World"
# print(string[0])

# string = "Hello World is a common programming term"
# print(string.find("p"))

# text = "Ishiwu Emmanuel"
# print(text[0])
# print(text[14])


# slicing 
#  slicing accessing a portions of s sequence


# string = "Hello a World"
# print(string[0:5])

# string = "Hello World is a common term in programming"
# print(len(string))
# print(string[0:-1:2])
# print(string[-43])


# methods
# method is a function that belongs to a specific object or class

# capitalize() casefold() center() count()
# endwith() find() format() index() 
# isalpha() isdigit() join() lower() replace() split() strip()

# string = "hello World is a common term in programming"
# print(string.count("m"))

# string = "hello World is a common term in programMMing"
# print(string.casefold())


# string = "***hello World is a common term in programming***"
# print (string.center(70))


# Numbers: integers, floats, complex numbers, mathematical operations 
# +, -, * , /, //, %, **

# comp1 = 5+2j
# comp2 = 4+6j
# print(comp1 + comp2)
# print(comp1 + 5)

# num = 10
# rad = math.radians(num)
# print(math.cos(rad))
# print(math.sin(rad))
# print(math.tan(rad))


# num = 10
# print(math.pi)
# rad = math.radians(num)
# print(math.cos(rad))
# print(math.sin(rad))
# print(math.tan(rad))

# print(math.factorial(5))
# print(math.lcm(20, 8))
# print(math.gcd(20, 8))
# print(math.pow(2, 3))
# print(math.floor(5/2))
# print(math.ceil(5/2))

# rand = random.randint(1, 10)
# print(random)
# print(random.choice(["Hello", "Hi", "Hey"]))
# print(random.sample(["Hello", "Hi", "Hey", 3, 4, 5], k=2))
# print(random.uniform(1, 10))
# print(random.choices(["Hello", "Hi", "Hey", 3, 4, 5], k=2))
# list1 = ["Hello", "Hi", "Hey", 3, 4, 5]
# print(random.shuffle(list1))
# print(list1)
# fac = Fraction(5/2)
# print(fac)


# BOOLEAN: logical operations, conditional statements , comparison
# print(1==1)
# print(1==11)


# is_student = True
# name = "Emmanuel"

# conditonal statements
# if is_student:
#     print(f"{name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student") 


       
# is_student = bool(input("Are you a student:"))
# name = "Emmanuel"

# if is_student == True:
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student") 


    
# is_student = bool(input("Are you a student:"))
# name = input("Enter your name:")
    
# if is_student == True:
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student") 




# is_student = bool(input("Are you a student:"))
# name = input("Enter your name:")
    
# if is_student != True:
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student") 


# logical statements     

# is_student = bool(input("Are you a student:"))
# name = input("Enter your name:")
    
# if is_student == True or name=="emmanuel":
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student")    


# name = input("What is your name:")
# age = input("How old are you:")
# school = input("What school do you attend:")
# course = input("Which course do you offer:")
# state = input("Which state are from:")

# print(f"My name is {name} and I am {age} years old, I do attend {school}, and I offer {course} as my course, and my state of origin is {state}.")






# first_number = int(input("Enter your first number:"))
# second_number = int(input("Enter your second number:"))

# add = first_number + second_number
# sub = first_number - second_number
# mul = first_number * second_number
# div = first_number / second_number
# mod = first_number % second_number
# exp = first_number ** second_number

# print(add)
# print(sub)
# print(mul)
# print(div)
# print(mod)
# print(exp)




# string = "=====MY PROFILE====="
# print (string.center(50))
# name = "name:Emmanuel"
# age = "age:18"
# country = "country:Nigeria"
# favorite_course = "favorite_course:python"
# print(name)
# print(age)
# print(country)
# print(favorite_course)
# string = "====================="
# print (string.center(5))





# Shopping Receipt Program

# # User input
# product_name = input("Enter the product name: ")
# price = float(input("Enter the price of the product: "))
# quantity = int(input("Enter the quantity purchased: "))
# discount_percent = float(
#     input("Enter discount percentage (e.g., 10 for 10%): ")
# )

# # Calculations
# total_cost = price * quantity
# discount_amount = (discount_percent / 100) * total_cost
# final_amount = total_cost - discount_amount

# # Display receipt
# print("\n" + "=" * 30)
# print(f"{'RECEIPT':^30}")
# print("=" * 30)
# print(f"Item: {product_name}")
# print(f"Price per unit: ${price:.2f}")
# print(f"Quantity: {quantity}")
# print(f"Subtotal: ${total_cost:.2f}")
# print(f"Discount ({discount_percent:.1f}%): -${discount_amount:.2f}")
# print("-" * 30)
# print(f"Total Amount Due: ${final_amount:.2f}")
# print("=" * 30)




# Age Category and Eligibility Program

# # Get user input
# age = int(input("Enter your age: "))

# # Determine age category using if/elif/else
# if age < 13:
#     category = "Child"
# elif 13 <= age <= 17:
#     category = "Teenager"
# elif 18 <= age <= 59:
#     category = "Adult"
# else:
#     category = "Senior Citizen"

# # Determine eligibility using comparison operators and boolean logic
# can_vote = age >= 18
# can_drive = age >= 18

# Convert boolean results to "Yes"/"No" strings
# voting_eligibility = "Yes" if can_vote else "No"
# driver_eligibility = "Yes" if can_drive else "No"

# # Display results
# print(f"Category: {category}")
# print(f"Voting eligibility: {voting_eligibility}")
# print(f"Driver's licence eligibility: {driver_eligibility}")

# data structures 
# list = mutabe collection of data 
# tuple = immutable collections of data 
# dictionaries = mutable collection of datain key , value pair


# python data structures are specialized contanier used to organize,
# store, manage, and manipulate collection of data efficiently in computer
# memory 

# numbers = range(1,10)

# list1 = ["EM", "Uche", 20, True, 5+2j, 5/2, 1==1, 5.5]
# list2 = list(numbers)
# print(list2)
# print(list1)

# tuples = (3,4)
# print(type(tuples))

# tuples = tuple(numbers)
# print(tuples)




# list1 = ["EM", "Uche", 20, True, 5+2j, 5/2, 1==1, 5.5]
# appen = list1.append("Python")
# print(list1)

# kwargs = dict(name="emma", age=20, course="Python")
# dict1 = {"name": "EM", "age": 20, "course": "Python"}
# # dict2 = dict(kwargs)
# # print(dict2)
# dict3 = dict([("name", "EM"), ("age", 20), ("course", "Python")])
# print(dict1)
# print(kwargs)
# print(dict3)



# indexing

# name = "programming"
# print(name[0])
# print(name[1])

# print(name[-1])
# print(name[-2])


# list1 = ["EM", "Uche", 20, True, 5+2j, 5/2, 1==1, 5.5]
# tuple1 = ["EM", "Uche", 20, True, 5+2j, 5/2, "Many", 5.5]

# print(list1[0], list1[3])
# print(tuple1[0], tuple1[5])

# slicing

# list1 = ["EM", "Uche", 20, True, 5+2j, 5/2, 1==1, 5.5]
# tuple1 = ["EM", "Uche", 20, True, 5+2j, 5/2, "Many", 5.5]

# print(list1[0:4])
# print(tuple1[0:4])



# method
# dict, str, list, tuple, int
# dictionary method
# pop(), copy(), popitem(), items(), get(), keys(), values(), update(), fromkeys(), setdefault()


# pop
# dict3 = dict([("name", "EM"), ("age", 20), ("course", "Python")])
# print(dict3)
# dictionary = dict3.pop("age")
# print(dict3)

# print(dictionary)

# popitem

# dict3 = dict([("name", "EM"), ("age", 20), ("course", "Python")])
# print(dict3)
# dictionary = dict3.popitem()
# print(dict3)

# print(dictionary)

# .items

# dict3 = dict([("name", "EM"), ("age", 20), ("course", "Python")])
# print(dict3)
# dictionary = dict3.items()

# print(dictionary)



# update

# dict3 = dict([("name", "EM"), ("age", 20), ("course", "Python")])
# print(dict3)
# dictionary = dict3.update({"name":"emma"})
# print(dict3)

# print(dictionary)


# fromkeyt

# dict1 = {}
# print(dict1.fromkeys(["name", "age", "course"], "Nano"))



# dict3 = dict([("name", "EM"), ("age", 20), ("course", "Python")])
# print(dict3)
# dictionary = dict3.setdefault("name","emmanue")
# print(dict3)

# print(dictionary)

# new = dict3.setdefault("new", "Nano")
# print(new)
# print(dict3)



# List method
# append() clear() copy() count() extend() insert() remove() pop() index()
# reverse() sort()

# list1 = [1,2,3,4,5,6]
# tuple1 = ["JM", "Uche", 20, True, 5+2j, 5/2, "Many", 5.5]

# # listappend = list1.append("Python")
# print(list1)


# # listclear = list1.clear()
# # print(list1)


# listcopy = list1.copy()
# print(listcopy)


# listcount = list1.count(20)
# print(listcount)


# listextend = list1.extend([1,2,3,4,5])
# print(list1)


# listinsert = list1.insert(1, "JM")
# print(list1)


# listremove = list1.remove("JM")
# print(list1)


# listpop = list1.pop()
# print(list1)


# # listindex = list1.index("JM")
# # print(listindex)


# listreverse = list1.reverse()
# print(list1)


# listsort = list1.sort()
# print(list1)


tuple1 = ("JM", "Uche", 20, True, 5+2j, 5/2, "Many", 5.5, "JM" )


tupleops = tuple1.index("Uche")
print(tupleops)

tuplecount = tuple1.count("JM")
print(tuplecount)