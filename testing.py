from functools import reduce

class Details():
    def get_details(self, age):
        self.age = age

class Person(Details):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

if __name__ == '__main__':
    print(f'Beginning Operations!')
    man = Person('Nick', 'Ross')
    man.age = 56
    print(f'{man.full_name()} is {man.age}')

    def double(n):
        return n + n


    def multiply_itself(n):
        return n * n

    # map function - takes a function and a iterable (list, array, tuple ect)
    nums = {1, 2, 3, 4}
    result = list(map(double, nums))
    print(result)
    # or
    result = list(map(lambda x: x + x, nums))
    print(f'Using a lambda instead of defining a function. Result is {result}')

    result = list(map(multiply_itself, nums))
    print(result)
    # or
    result = list(map(lambda x: x * x, nums))
    print(f'Using lambda again. Result: {result}')

    strings = ['some', 'string', 'things']
    result = list(map(list, strings))
    print(result)

    # filter function - takes a function a iterable (list, array, tuple ect)
    def more_than(x):
        return x > 15
    nums =  [2, 20, 18, 15.1, 14]
    result = list(filter(more_than, nums))
    print(f'Result with function: {result}')

    # with lambda
    result = list(filter(lambda x: x > 15, nums))
    print(f'Result with a lambda: {result}')

    # reduce method - need to import "reduce" from "functools" - takes a function and an iterable (list, array, tuple ect)
    def add_two_nums(x, y):
        return x + y
    nums = (1, 2, 3, 4)
    result = reduce(add_two_nums, nums)
    print(f'Reduce with function. Result: {result}')

    # with lambda
    result = reduce(lambda x, y: x + y, nums)
    print(f'Reduce with lambda. Result: {result}')