
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    sum = 0

    if isinstance(args[0], dict):
        sum += calculate_structure_sum(args[0].keys())
        sum += calculate_structure_sum(args[0].values())
        return sum

    for elem in args[0]:
        if isinstance(elem, int):
            sum += elem
        elif isinstance(elem, str):
            sum += len(elem)
        elif isinstance(elem, float):
            sum += elem
        elif isinstance(elem, bool):
            sum += int(elem)
        else:
            sum += calculate_structure_sum(elem)

    return sum


print(calculate_structure_sum(data_structure))
