# Python Basic Beginners Exercises 
# 1. Given two integer numbers return their product only if the product is equal to or lower than 1000, 
#else return their sum.
# Solution
print("Exercise 1")
def multiply_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

# first
result = multiply_or_sum(20, 30)
print("The result is", result)

# Second 
result = multiply_or_sum(40, 30)
print(f"Output is, {result}")


# 2.Write a program to iterate the first 10 numbers and
# in each iteration, print the sum of the current and previous number.
# Solution
print("Exercise 2")
previous_num = 0

for i in range(0, 10):
    sum = previous_num + i
    print(f"Current Number {i}, Previous Number {previous_num}, Sum:  {sum}")
    # modifying previous number
    previous_num = i
    
# 3.Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
# Solution
# accept input string from a user
def a_word(word):
    print("Original String:", word)

    # get the length of a string
    size = len(word)

    # iterate a each character of a string
    # start: 0 to start with first character
    # stop: size-1 because index starts with 0
    # step: 2 to get the characters present at even index like 0, 2, 4
    print("Printing only even index chars")
    for i in range(0, size - 1, 2):
        print("index[", i, "]", word[i])
result = a_word("pynative")
print(result)
    


# 4. Write a program to remove characters from a string starting from zero up to n
# and return a new string.
# Solution
print("Exercise 4")
def remove_chars(word, n):
    print('Main string:', word)
    x = word[n:]
    return x
print("Removing characters from a string")
print(remove_chars("pynative", 7))
print(remove_chars("pynative", 2))  

# 5. Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False
# Solution
# Function that takes in nList as a parameter
print("Exercise 5")
def fnum_and_lnum(nList):
    # Print 
    print("Given list:", nList)
    # Begins from 0,start of s list
    fnum = nList[0]
    # Lastnumber starts from the end of a list
    lnum = nList[-1]
    
    # introduce if and else clause
    if  fnum == lnum:
        return True
    else:
        return False
# First given numbers
numbers_x = [10, 20, 30, 40, 10]
print("Result is:", fnum_and_lnum(numbers_x))

# Second given numbers
numbers_y = [75, 65, 35, 75, 30]
print("Result is:", fnum_and_lnum(numbers_y))


# 6. Iterate the given list of numbers and
# print only those numbers which are divisible by 5
# Solution
print("Exercise 6")
my_list = list([10, 20, 30, 14, 38, 22])

for i in my_list:
    if i % 5 == 0:
        print("Yes, this i is divisible by 5:", i )


# 7. Write a program to find how many times,
# substring “Emma” appears in the given string.
# Solution
print("Exercise 7")
str_x = "Emma is good developer. Emma is a writer"
Count = str_x.count("Emma")
print(Count)


# 8. print a pattern.
# Solution
# Use loop in loop
print("Exercise 8")
for num in range(10):
    for i in range(num):
        #print number
        print (num, end=" ") 
    # new line after each row to display pattern correctly
    print("\n")
    

# 9. Write a program to check if the given number is a palindrome number.
# Solution
print("Exercise 9")
def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check conditioned numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)


# 10. Create a new list from a two list using the following condition
# Given a two list of numbers, 
# write a program to create a new list such that the new list should contain odd numbers from the first list,
# and even numbers from the second list
# Solution
print("Exercise 10")
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result_list= []
# Iterate first list 
for num in list1:
    if num % 2 != 0:
        result_list.append(num)
# Iterate second list
for num in list2:
    if num % 2 == 0:
        result_list.append(num)
print(result_list)
    
# 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“,
# with a space separating the digits.
# Solution
print("Exercise 11")
def extract_int(number):
    # Print statement
    print("Original number", number)
    # Using a while loop
    while number > 0:
        # get the last digit
        digit = number % 10
        # remove the last digit and repeat the loop
        number = number // 10
        print(digit, end=" ")
    # Given number
number = extract_int(7536)
print(number)


# 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Solution
print("Exercise 12")
income = 45000
tax_pay = 0
print("Given income:", income)
# Using a conditional statement
if income <= 10000:
    # no tax on first 10,000
    tax_pay = 0
elif income <= 20000:
    x = income - 10000
    # 10% tax
    tax_pay = x * 10 / 100
else:
    # first 10,000
    tax_pay = 0

    # next 10,000 10% tax
    tax_pay = 10000 * 10 / 100

    # remaining 20%tax
    tax_pay += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_pay)


# 13: Print multiplication table form 1 to 10
# Solution
print("Exercise 13")

for x in range(1, 11):
    for y in range(1, 11):
        print(x * y, end=",")
    print("\t\t")
    

# 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# Solution
print("Exercise 14")
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("\r")



# 15. Write a function called exponent(base, exp),
#that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
# Solution
print("Exercise 15")
def exponent(base, exp):
    base_1 = 1
    expo_1 = exp
    return base ** exp
first_val = exponent(2, 5)
print("2 raises to the power of 5:", first_val)

second_val = exponent(5, 4)
print("5 raises to the power of 4:", second_val)
    