#Remember import random function here:
import random
my_list = [4,5,734,43,45]

#The magic is here:
for i in range (0,10):
    n = random.randint(1,30)
    my_list.append(n)
print(my_list)
