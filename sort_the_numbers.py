'''
Question 5
Write a python function to sort numbers passed to it.

'''
def number_sorting(*iterable: tuple):
    iterabled = list(iterable)
    iterabled.sort()
    return iterabled 

number = number_sorting(5, 6, 7, 8, 3, 6, 9, 20)
print(number)