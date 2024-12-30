"""Write a program to create a list of the cubes of only the even integers appearing in the input
list (may have elements of other types also) using the following:
a. 'for' loop """
# def cuve_of_num(input_list):
#     cuves = []
#     for item in input_list:
#         if isinstance(item,int) and item%2==0:
#             cuves.append(item**3)
#     return cuves
# input_list = [2,3,4,5,6,"al",8,9,10]
# result = cuve_of_num(input_list)
# print(result) 

""" Write a program to accept a number ‘n’ and  Generate all prime
numbers till ‘n’ c."""
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# n = int(input("Enter the value : "))
# for i in range(2,n+1):
#     if is_prime(i):
#         print(i) 

"""Write a program that accepts a character and performs the following:
a. print whether the character is a letter or numeric digit or a special character. """
# def check_character(char):
#     if char.isalpha():
#         return "this is a character"
#     elif char.isdigit():
#         return "this is a numver"
#     else:
#         return "this is a special character"
    
# char = input("Enter the value : ")
# print(check_character(char)) 

""". 4) (V)if the character is a letter, print whether the letter is uppercase or lowercase"""
# def upper(char):
#     if char.isalpha():
#         if char.isupper():
#             return "is in upper case"
#         else:
#             return "this is in lowercase"
#     elif char.isdigit():
#         return "this is a numeric character"
#     else:
#         return "this is a special character"
    
# char = input("Enter the value : ")
# print(upper(char))

"""4 (c) if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is
NINE)"""
# digit = {
#     '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR',
#     '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE','10':'ten'
# }

# char = input("Enter value: ")

# if char.isdigit():
#     print(digit[char])
# else:
#     print("it is a different character.")

"""5 (a) Write a program to perform the following operations on a string
a. Find the frequency of a character in a string. """
# string = input("Enter the string: ")
# char = input("Enter the letter for frequency calculation:")

# frequency = string.count(char)
# if len(char)==1:
#     print(f"frequency of {char} in {string} is ",frequency)
# else:
#     print("please enter only 1 char")

"""5 (b) Write a program to perform the following operations on a string
Replace a character by another character in a string. """
# string = input("Enter the string : ")
# old_char = input("enter the char you want to replace it in string : ")
# new_char = input("enter the string to replace with : ")

# if len(old_char)==1:
#     new_str = string.replace(old_char,new_char)
#     print(new_str)
# else:
#     print("Please enter only one char at a time ")

"""5 (c) Remove the first occurrence of a character from a string. """
# string = input("Enter the string: ")
# remove = input("enter what do you want to remove : ")

# if len(remove)==1:
#     new_str = string.replace(remove,"",1)
#     print(new_str)
# else:
#     print("enter only one char ar a time ")

""". 5 (D) Remove all occurrences of a character from a string. 
"""
# string = input("Enter the string:")
# remove = input("Enter the char to remove: ")

# if len(remove)==1:
#     new_str = string.replace(remove,"")
#     print(new_str)
# else:
#     print("enter only one char ar a time ")

"""6. Write a program to swap the first n characters of two strings"""
# string1 = input("enter the string 1: ")
# string2 = input("Enter the string 2:")
# n = int(input("NO. of vits to change :"))

# if n > len(string1) and n > len(string2):
#     print("no. of letter cant ve more than strings")
# else:
#     new_string1 = string1[:n] + string2[n:]
#     new_string2 = string1[:n] + string2[n:]
#     print("new string 1= ", new_string1)
#     print("new string 2= ", new_string1)

"""8 (v) Write a program to create ist of the cubes of only the even integers appearing in the input
list (may have elements of other types also) using the following  "b. list comprehension" 
"""
# def cuves(input_list):
#     cuves = [item**3 for item in input_list if isinstance (item,int) and item%2==0]
#     return cuves

# input_list = [2,3,4,5,6,"al",8,9,10]
# result = cuves(input_list)
# print(result)

"""10. Write a program to define a class Point with coordinates x and y as attributes. Create
relevant methods and print the objects. Also define a method distance to calculate the distance
between any two point objects. """
# import math

# class Point:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __str__(self):
#         return f"Point({self.x}, {self.y})"

#     def distance(self, other):
#         return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# # Example usage
# p1, p2 = Point(3, 4), Point(7, 1)
# print(p1, p2)
# print("Distance:", p1.distance(p2))

"""11. Write a function that prints a dictionary where the keys are numbers between 1 and 5 and
the values are cubes of the keys. """
# def print_cubes():
#     cubes_dict = {i: i**3 for i in range(1, 6)}
#     print(cubes_dict)

# # Call the function
# print_cubes()

"""Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). Write a program to perform following
operations:
a. Print half the values of the tuple in one line and the other half in the next line. """

# t1 = (1, 2, 5, 7, 9, 2, 4, 6,11, 8, 10)

# # Calculate the midpoint of the tuple
# mid = len(t1) // 2

# # Print first half of the tuple
# print(t1[:mid])

# print(t1[mid:])

"""Print another tuple whose values are even numbers in the given tuple"""
# # Given tuple
# t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# # Create a new tuple containing only the even numbers
# even_tuple = tuple(x for x in t1 if x % 2 == 0)

# # Print the new tuple
# print(even_tuple)

"""concatenate"""
# # Given tuples
# t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
# t2 = (11, 13, 15)

# # Concatenate t1 and t2
# result = t1 + t2

# # Print the resulting tuple
# print(result)

"""find maximum and minimum value from the tuple"""
# # Given tuples
# t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
# t2 = (11, 13, 15)

# # Concatenate t1 and t2
# result = t1 + t2

# # Get the maximum and minimum values
# max_value = max(result)
# min_value = min(result)

# # Print the maximum and minimum values
# print(f"Maximum value: {max_value}")
# print(f"Minimum value: {min_value}"

"""Write a program to accept a name from a user. Raise and handle appropriate exception(s) if
the text entered by the user contains digits and/or special character"""
# import re

# class InvalidNameError(Exception): pass

# def accept_name():
#     try:
#         name = input("Enter your name: ")
#         if not re.match("^[A-Za-z\s]*$", name):
#             raise InvalidNameError("Name must contain only letters and spaces.")
#         print(f"Hello, {name}!")
#     except InvalidNameError as e:
#         print(f"Error: {e}")

# accept_name()

"""9 (a)  Write a program to read a file and
a. Print the total number of characters, words and lines in the file. 
""" 
# def count_file_details(filename): 
#     try:
#         with open(filename, 'r') as file:  # Open the file in read mode
#             lines = file.readlines()  # Read all lines of the file
#             num_lines = len(lines)  # Number of lines in the file
            
#             num_words = 0
#             num_chars = 0
            
#             for line in lines:
#                 num_words += len(line.split())  # Count words in the current line
#                 num_chars += len(line)  # Count characters in the current line
            
#             print(f"Total lines: {num_lines}")
#             print(f"Total words: {num_words}")
#             print(f"Total characters: {num_chars}")
    
#     except FileNotFoundError:
#         print("The file does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# filename = input("Enter the filename: ")
# count_file_details(filename)

"""9 v . Calculate the frequency of each character in the file. Use a variable of dictionary type
to maintain the count. """
# def count_char_frequency(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#         char_frequency = {char: content.count(char) for char in set(content)}
#         for char, freq in char_frequency.items():
#             print(f"'{char}': {freq}")
#     except FileNotFoundError:
#         print("The file does not exist.")

# # Example usage
# filename = input("Enter the filename: ")
# count_char_frequency(filename)

"""9 c . Print the words in reverse order. """
# def print_words_reverse(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#         words = content.split()  # Split content into words
#         print(" ".join(reversed(words)))  # Print words in reverse order
#     except FileNotFoundError:
#         print("The file does not exist.")

# # Example usage
# filename = input("Enter the filename: ")
# print_words_reverse(filename)

"""9 D  Copy even lines of the file to a file named ‘File1’ and odd lines to another file named
‘File2’. """
# def copy_lines(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()  # Read all lines from the file
        
#         with open('File1', 'w') as file1, open('File2', 'w') as file2:
#             for index, line in enumerate(lines, start=1):
#                 if index % 2 == 0:
#                     file1.write(line)  # Write even lines to File1
#                 else:
#                     file2.write(line)  # Write odd lines to File2
                    
#         print("Even lines copied to 'File1' and odd lines copied to 'File2'.")
    
#     except FileNotFoundError:
#         print("The file does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# filename = input("Enter the filename: ")
# copy_lines(filename)
 
""" 3. Write a program to create a pyramid of the character ‘*’ and a reverse pyramid 
"""
# def pyramid(height):
#     for i in range(1, height + 1):
#         print(' ' * (height - i) + '*' * (2 * i - 1))

# def reverse_pyramid(height):
#     for i in range(height, 0, -1):
#         print(' ' * (height - i) + '*' * (2 * i - 1))

# # Example usage
# height = int(input("Enter pyramid height: "))
# pyramid(height)
# reverse_pyramid(height)

