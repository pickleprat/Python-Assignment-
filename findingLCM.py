'''
Question 4 
Write a python function to return of LCM of any given numbers passed. 
'''
def lowest_common_multiple(a: int, b:int):
    num = min(a, b)
    bigger = max(a, b)
    for i in range(2, num+1):
        if num%i==0 and bigger%i==0:
            return i
    else:
        return f"The numbers {a} and {b} do not share a common multiple."

print(lowest_common_multiple(7484, 14))
