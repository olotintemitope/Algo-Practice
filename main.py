# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
favourite = "I love {} and {} for real".format("family", "children")
#print(favourite)

list_of_days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'];

#print('Tue' not in list_of_days)
#print('Mon' in list_of_days)

msr_param = (10, 20)

height, width = msr_param;

print("The height of the wood is {} and the width of the wood is {}".format(height, width))


# names = ["Carol", "Albert", "Ben", "Donna"]
# print(" & ".join(sorted(names)))

population = {"ek": 200, "ak": 500};

pop_keys = sorted(population.keys())

print(pop_keys[0])

if str(pop_keys[0]) == "ak":
    print("welcome to akure")
elif str(pop_keys[0]) == "ek":
    print("welcome to ekiti")
else:
    print("welcome to the jungle")


print(list(range(4)))

squares = [x**2 for x in range(9) if x % 2 == 0]

print(squares)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)
