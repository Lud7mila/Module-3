
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(25, 47, c = 0)
print_params(c = 1, b = True)
print_params(b = 25)
print_params(c = [1,2,3])

print()
values_list = [1, False, 'слова']
print_params(*values_list)
values_dict = {'a' : 48, 'b': 4.5, 'c' : True}
print_params(**values_dict)

print()
values_list_2 = [77, 'электрификация']
print_params(*values_list_2, 42)
