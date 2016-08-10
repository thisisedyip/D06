import random
import os

def write_ten_numbers():
    f = open('test.txt', 'w')
    numbers = random.sample(range(1, 1000), 10)
    f.write(str(numbers))
    f.close()

write_ten_numbers()
