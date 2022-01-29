'''
Question 5
Write a python function to sort numbers passed to it.

'''
def number_sorting(*iterable: tuple):
    iterabled = list(iterable)
    iterabled.sort()
    return iterabled 

def anamize(collection: list):
    sorted_list = list()
    for i in range(len(collection)):
        smallest = min(collection)
        sorted_list.append(smallest)
        collection.remove(smallest)
    return sorted_list

a_list = [6, 6, 2, 6, 0, 5]
a_list = anamize(a_list)
print(a_list)

number = number_sorting(5, 6, 7, 8, 3, 6, 9, 20)
print(number)