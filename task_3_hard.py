
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    sum = 0

    for elem in args[0]:
        if isinstance(elem, list | set | tuple):
            sum += calculate_structure_sum(elem)
        elif isinstance(elem, dict):
            sum += calculate_structure_sum(elem.keys())
            sum += calculate_structure_sum(elem.values())
        elif isinstance(elem, str):
            sum += len(elem)
        else:
            sum += int(elem)

    return sum


print(calculate_structure_sum(data_structure))
