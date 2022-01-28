'''
Question 2 
Write a Python program to print 'n' terms of Fibonacci series using 
recursion.
'''
def iterate_a_function(n : int):
    for i in range(1, n+1):
        print(fabionacci_with_recursion(i), end=" ")

def fabionacci_with_recursion(n: int):
    if n<=1:
        return n
    else:
        return fabionacci_with_recursion(n-1)+fabionacci_with_recursion(n-2)

n = int(input("Enter a number: "))
iterate_a_function(n)
