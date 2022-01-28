'''
Question 6
Write a python function immolate “Tower of Hanoi” problem
'''


def tower_of_hanoi(initial: str, destination:str, empty_one: str, n: int):
    if n==1:
        print(f"Move disc {n} from {initial} to {destination}")
        return

    tower_of_hanoi(initial, empty_one, destination, n-1)
    print(f"Move disc {n} from {initial} to destination {destination}")
    tower_of_hanoi(empty_one, destination, initial, n-1)

tower_of_hanoi('A', 'B', 'C', 3)