"""
Write an expression that initializes the dictionary my_dict to be the empty dictionary. 
"""

my_dict = {}

# Tests
print(type(my_dict))
print(my_dict)

"""Write an expression that initializes the dictionary my_name to contain two key/value pairs: "Chima" : 1 and "Ihueze" : 2 """

"""
Template - Create a dictionary my_dict that contains 
two specified value/pairs 
"""

my_name = {"Chima": 1, "Ihueze": 2}

# Tests
print(type(my_name))
print(my_name["Chima"])
print(my_name["Ihueze"])
print(my_name)

""" Write a Python statement that adds the key/value pair "Kingsley" : 3 to this dictionary. """ 

"""
Template - Add the specified key/value pair to an
existing dictionary my_dict
"""

# Initialize dictionary
my_name = {"Chima" : 1, "Ihueze" : 2}

my_name["Kingsley"] = 3

# Tests
print(type(my_name))
print(my_name["Kingsley"])
print(my_name)


"""
Write an expression that determines whether
a key is in a dictionary
"""

# Initialize dictionary
my_names = {"Chima" : 1, "Ihueze" : 2, "Kingsley" : 3}

# Print True/False depending on whether the key "Chima" is in my_names
print("Chima" in my_names)

# Print True/False depending on whether the key "Ihueze" is in my_names
print("Ihueze" in my_names)

# Print True/False depending on whether the key "Mmesoma" is in my_names
print("Mmesoma" in my_names)





