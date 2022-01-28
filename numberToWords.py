'''
Question: Write a function that takes a number as an input argument and returns 
the corresponding text in words, for example, if input is 368, the 
function should return `Three`, `Six`, `Eight`. Use a dictionary for mapping 
digits to their string representation
'''



numbers = {
        0:"Zero", 
        1:"One",
        2:"Two", 
        3:"Three",
        4:"Four", 
        5:"Five", 
        6:"Six", 
        7:"Seven", 
        8:"Eight", 
        9:"Nine"
    }

def number_to_words_recursive(n : int):
    floored_value = n//10
    remainder = n%10
    if n<10:
        print(numbers[remainder], end =" ")
        return 
    
    number_to_words_recursive(floored_value)
    print(numbers[remainder], end=" ")

def number_to_words_the_boring_way(n: int):
    num_str = str(n)
    for i in range(len(str(n))):
        print(numbers[int(num_str[i])])
        
# code using recursion 
number_to_words_recursive(138)

print()
# code in the boring way
number_to_words_the_boring_way(138)