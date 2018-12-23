from set_up_and_calculation import *

grenze = input("Bitte geben sie die Rechengrenze an:")
my_list = get_List(int(grenze))

my_result = calculation(my_list,int(grenze))
print(my_result)