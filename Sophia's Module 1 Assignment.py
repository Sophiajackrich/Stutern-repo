# Data types
# 1. Numeric
# 1a. Integer
age = 12

# 1b. Float
height = 1.85

# 1c. Complex Number
print("Question 1")
some_random_value = 12j
print("age", age)
print("height", height)
print("some_random_value", some_random_value)
print()


# 2. Dictionary i.e key-value pair
print("Question 2")
my_dict = {"age": 12}
print(my_dict)
print()
# 3. Boolean
# It has 2 values/types which are True and False
print("Question 3")
is_session_holding = True
print(is_session_holding)
d = {1: "hello"}
print(d)

print()
# 4. Set
set_fruits = {"orange", "mango", "pineapple"}

# 5. Sequence Types
# 5a. Strings
print("Question 4 & 5")
state = "Lagos State"
# 5b. Tuple. Tuple is immutable. i.e you can't change the content.
tuple_fruit = ("orange", "mango", "pineapple", "orange")
# 5c. List. List is mutable.
list_fruit = ["orange", "mango", "pineapple", "mango"]

print("set_fruits: ", set_fruits)
print("tuple_fruit: ", tuple_fruit)
print("list_fruit: ", list_fruit)
print()

list_fruit[0] = "apple"
list_fruit[3] = "pawpaw"
print(list_fruit)
print()
print(set(["orange", "mango", "pineapple", "mango"]))
print()
another_set = {1, 2, 3, 1, 2, 3}
print(another_set)

print()
# Count from 0 thru 5: 0, 1, 2, 3, 4, 5
# my_count = range(6)
my_count = range(0, 10)  # range(10)
print(list(my_count))
print()
number_of_elements = len(list(my_count))

print(number_of_elements)













