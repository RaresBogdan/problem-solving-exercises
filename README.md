Welcome to my repository on GitHub, which contains math and string problems of varying levels of difficulty.

The repository is divided into two folders: "math_problems" and "string_problems".

Each problem in this repository is accompanied by clear comments to help you understand the problem and its solution.

# string_problems contents:
#### 1. Check if a string is a palindrome
    The function "is_str_palindrome" takes in a single argument, which is expected to be a string. 
    The function checks whether the input string is a valid non-empty string, and then removes 
    any punctuation and spaces from the string, and converts it to lowercase. 
    Finally, the function checks whether the cleaned-up string is a palindrome, meaning 
    whether it is the same when read forward and backward. If the cleaned-up string is a 
    palindrome, the function returns True, otherwise it returns False. 
    If the input argument is not a string, or if it is an empty string or consists 
    only of whitespace characters, the function raises an error.

#### 2. Find the longest word in a sentence
    This function takes in a single argument, which is expected to be a string called "sentence".
    The function removes any punctuation from the sentence and splits it into a list of words.
    The function then finds the longest word(s) in the sentence, and returns either the longest word if there is only one,
    or a message stating that there are multiple longest words if there are ties.
    If the input argument is not a string, or if it is an empty string or consists only of whitespace characters,
    the function raises an error. If the input argument is a string consisting only of punctuation marks,
    the function also raises an error.

#### 3. Reverse a string
    This function takes in a single argument, which is expected to be a string called "word".
    The function checks that the input argument is a non-empty string, and then reverses the string by iterating over each character
    in the string and adding it to the beginning of a new string.
    If the input argument is not a string, or if it is an empty string or consists only of whitespace characters,
    the function raises an error.

#### 4.  Find the largest number in a list
    This function takes in a single argument, which is expected to be a list 
    called "number_list" containing integer or float values.
    The function checks that the input argument is a non-empty list containing 
    only integer or float values, and then returns the largest value in the list.
    If the input argument is not a list, or if it is an empty list, the function raises an error. 
    If any of the items in the input list is not an integer or a float,the function also raises an error.

#### 5.  Find the smallest number in a list
    This function takes in a single argument, which is expected to be a list 
    called "number_list" containing integer or float values.
    The function checks that the input argument is a non-empty list containing only integer 
    or float values, and then returns the smallest value in the list.
    If the input argument is not a list, or if it is an empty list, the function raises an error. 
    If any of the items in the input list is not an integer or a float,
    the function also raises an error.

#### 6. Find the most common word in a phrase
    This function takes in a single argument, which is expected to be a string called "phrase".
    The function checks that the input argument is a non-empty string, and then 
    finds the most common word(s) in the string.
    If there is only one most common word, that word is returned. If there are multiple most common 
    words, they are returned in a formatted string.
    If all the words in the input string have the same frequency, the function returns a string indicating that fact.
    The function also handles punctuation by removing it from the input string.

#### 7.  Find the most frequent letter in a string
    This function takes a string as input and returns the most frequent letter(s) in it
    It raises a TypeError if the input is not a string or if it is an empty string or a string with only whitespace characters
    It removes all punctuation marks from the input string
    It converts the input string to lowercase to avoid case sensitivity
    It creates a dictionary with keys being letters in the input string and values being the frequency of each letter in the string
    It finds the maximum frequency of letters in the string and returns the most frequent letter(s)


# math_problems contents
#### 1. Area of a circle
    This function computes the area of a circle given its diameter. The function
    raises a TypeError if the input diameter is not a positive number, either integer
    or float. Otherwise, the function computes the radius as half of the diameter,
    and returns the area of the circle using the formula A = pi * r^2, where pi is
    approximated to 3.14159265359.

#### 2. Armstrong Numbers
    An Armstrong number is a number that is equal to the sum
    of its own digits raised to the power of the number of digits in the number.
    For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
    
    This function checks whether the given number is an Armstrong number by
    calculating the sum of the digits raised to the power of the number of digits
    and comparing it to the original number.

#### 3. Collatz conjecture
    Take any positive integer n. If n is even, divide n by 2 to get n / 2.
    If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely.
    The conjecture states that no matter which number you start with, you will always reach 1 eventually.
    Given a number n, return the number of steps required to reach 1.

#### 4. Differences of squares
    This function takes a positive integer and repeatedly sums its digits until a single-digit number is obtained.
    It uses a while loop to iteratively sum the digits of the input number until it becomes a single-digit number.
    The resulting single-digit sum is then returned as the output of the function.

#### 5. Even or odd
    This function takes an input integer and determines whether it is even or odd. An even
    number is a number that is divisible by 2 without a remainder, while an odd number is
    not divisible by 2 without a remainder. If the input number is even, the function returns
    the message "The number you have chosen is even". If the input number is odd, the function
    returns the message "The number you have chosen is odd".

#### 6. Factorial of a number
    This function computes the factorial of a non-negative integer, which is the
    product of all positive integers up to and including the input number. The
    function raises a TypeError if the input is not a non-negative integer. Otherwise,
    the function initializes the result to 1 and multiplies it successively by all
    positive integers up to and including the input number using a for loop. Finally,
    the function returns the computed result.

#### 7. Find the maximum of three numbers
    This function returns the maximum of three input values, which can be of any comparable
    type. The function uses nested ternary operators to compare the input values and return
    the largest of the three. The function assumes that the input values are comparable, and
    does not perform any type checking or error handling.

#### 8. Grains problem
    This function calculates the total number of grains of wheat on a chessboard where the number of grains on each square is doubled from the previous square. The 'square' function calculates the number of grains on a particular square, raising a 'ValueError' if the input is not between 1 and 64. The 'total' function then calls the 'square' function for each square and adds up the resulting number of grains, returning the total number of grains on the chessboard.

#### 9. Is number a perfect square
    This function takes an input integer and checks if it is a perfect square, i.e., if it is
    equal to the square of an integer. To do this, the function calculates the square root of
    the input number using the `sqrt` function from the `math` module. If the square root is an
    integer, then the input number is a perfect square and the function returns `True`. 
    Otherwise, the function returns `False`.

#### 10. Is a number a prime number
    This function determines whether an input integer is a prime number, which is a number
    greater than 1 that is only divisible by 1 and itself. The function returns True if the
    input number is a prime number, and False otherwise. The function uses a for loop to check
    if the input number is divisible by any integer between 2 and half the input number, and
    returns False if such a divisor is found. If the loop completes without finding a divisor,
    the function returns True, indicating that the input number is a prime number.

#### 11. Perfect numbers
    This function classifies a given positive integer as perfect, abundant, or deficient
    based on the sum of its proper divisors. A perfect number has a sum equal to the number
    itself, an abundant number has a sum greater than the number, and a deficient number
    has a sum less than the number. The function raises a ValueError for non-positive inputs.

#### 12. Sum of digits
    This function takes an input integer and calculates the sum of its digits. To do this,
    the function first checks that the input is an integer with more than one digit. If it
    passes this check, the function iterates over the digits of the input number and adds
    them up. The resulting sum is then returned as the output of the function.

#### 13. Sum of digits until one
    This function takes an input integer and repeatedly sums its digits until a single-digit
    number is obtained. To do this, the function first checks that the input is a positive
    integer. It then iteratively sums the digits of the input number using a while loop and
    updates the input number until it becomes a single-digit number. The resulting single-digit
    sum is then returned as the output of the function.

#### 14. Sum of numbers
    The sum_of_numbers function takes a non-negative integer number as input and
    calculates the sum of all the numbers from 0 up to number, inclusive.
    For example, if the input is 4, the function calculates the sum of 0 + 1 + 2 + 3 + 4, which is 10.
    The function returns this sum as an integer.

#### 15. Sum of squares
    This function takes an input integer and calculates the sum of the squares of all integers
    from 0 to the input number (inclusive). To do this, the function initializes a variable to
    store the running sum, and then iterates over a range from 0 to the input number. During each
    iteration, the function squares the current integer and adds it to the running sum. Finally,
    the function returns the resulting sum as its output.
