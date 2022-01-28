'''
Question 3
Write a python program for default keyword and variable length 
argument parameter passing methods in function.
'''

def string_length(string="Anam Malik"):
    return "The length of the string is "+str(len(string))
    
print(string_length("yay amazing"))
print(string_length())


