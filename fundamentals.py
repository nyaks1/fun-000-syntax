
#Question 1
get_date_of_birth(id_number): 
    """
    STEP 2: Extract the date of birth from the ID number and return it as a string
    """
    birth_of_date = id_number[4:6] 
    return 


#Question 2    
def get_gender(id_number):
    """
    STEP 3: Extract the gender from the ID number using the formula below and return
    it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is
    female and if it is greater than 4999, the person is male.
    """
    
    if int(id_number[6]) > 4:
    'Male'
    else:
    'Female'

    
#Question 3
def get_citizenship(id_number):
    """
    STEP 4: Extract the citizenship from the ID number using the formula below and 
    return it as a string

    Formula: 1 if the ID number's 11th to 12th digit is less than 01, the person is
    a South African citizen and if it is greater than 01, the person is a non-South 
    African citizen.
    """
if int(id_number[10]) == 0:
'South African'
else:
'Non-South African'


#Question 4

    """
    Fizzbuzz is a programme that prints the numbers from 1 to n, 
    but for multiples of 3, it prints "Fizz" instead of the number, 
    and for multiples of 5, it prints "Buzz" instead of the number. 
    For numbers that are multiples of both 3 and 5, it prints "FizzBuzz.

    TODO: define a function called fizzbuzz and implement the fucntionality above.
    TODO: Create a test class called 'test_my_tests.py' in the root directory, name the class "myTests"
    """
    

            

#Question 5
def check_number(n:int):
    """
    TODO: Given an integer n, perform the following conditions actions:
    non-positive and non-negative digit(s) are neutral
    If n is odd, return weird
    If n is even and in the inclusive range of 2  to 5 , return 'Not Weird'
    If n is even and in the inclusive range of 6  to 20 , return 'Weird'
    If n is even and greater than 20 , return 'Not Weird'
    If n is non-positive and even then return 'Very weird'
    If n is non-positive and odd then return 'Extremely Weird'


    TODO: Implement tests for the above functionality. Create a test file called `test_my_tests.py` in the 
    root directory.
     
    Create a test class called 'MyTestCases' and it should have the following test implementations:
        test_check_number_odd_number
        test_check_number_even_number
        test_check_number_negative_even_number
        test_check_number_negative_odd_number
        test_check_number_neutral
        
        
    """

