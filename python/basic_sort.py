from random import *

def swap(t_list, n1, n2):
    temp = t_list[n1]
    t_list[n1] = t_list[n2]
    t_list[n2] = temp

how_many = input("몇개 할래요? ")

my_list = []
for i in range(0, int(how_many)):
    my_list.append(randint(-10,10))

print(my_list)

swap(my_list, 0, 3)

print(my_list)
