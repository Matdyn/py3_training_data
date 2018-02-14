# Filter method for even numbers
from typing import List


# def find_even_numbers(nums: list): #type declarations let you use types methods

def find_even_numbers(nums: List[int]):  # type declarations with types [alt+enter]
    other_numbers = []  # to import List let you use types methods
    for n in nums:
        if n % 2 == 0:
            other_numbers.append(n)
    return other_numbers


def find_numbers(nums: List[int], test):  # type declarations with types [alt+enter]
    other_numbers = []  # to import List let you use types methods
    for n in nums:
        if test(n):
            other_numbers.append(n)
    return other_numbers


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


data = [1, 9, -1, 20, 5, -100, 24]

print(find_numbers(data, is_even))
print(find_numbers(data, lambda n: n % 2 == 0))  # lambda way!

print(find_numbers(data, is_odd))
print(find_numbers(data, lambda n: n % 2 != 0), 'lambda way')  # lambda way!

print(find_numbers(data, lambda n: n % 6 == 0))  # lambda way!

# sort data
data.sort()
print(data)

data.sort(key=lambda n: abs(n))  # key parameter
print(data)