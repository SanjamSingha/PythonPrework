#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    """Print "hello_USERNAME!" """    
    print("hello_" + user_name + "!")
hello_name('USERNAME')

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds(oddnumbers):
    """Print odd numbers from 1-00 and return nothing"""
    return first_odds
for oddnumbers in range(1,100):
    if oddnumbers %2!=0:
         print(oddnumbers)
         
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """Return the max number of a given list"""
    max_number=a_list[0]
    for number in a_list:
        if number>max_number:
            max_number=number
    return max_number
a_list=[5,7,8,12,42]
max_number=max_num_in_list(a_list)
print(max_number)

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """Determine if the given year is a leap year"""
    a_year=int(a_year)
    if a_year %4==0:
        print(str(a_year) + " is a leap year.")
        return True
    elif a_year %100!=0 or a_year %400==0:
        print(str(a_year) + " is not a leap year.")
        return False
print(is_leap_year(2023))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
 """see if all numbers in list are consecutive numbers"""
 for number in range(0,len(a_list)-1):
        if a_list[number]+1!=a_list[number +1]:
            return False
        else:
            return True
print(is_consecutive([3,4,5,6]))
