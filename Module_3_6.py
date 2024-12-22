def calculate_structure_sum(*values):
    sum = 0
    for component in values:
        if isinstance(component, str):
            sum += len(component)
        elif isinstance(component, int):
            sum += component
        elif isinstance(component, float):
            sum += component
        elif isinstance(component, bool):
            sum += component
        elif isinstance(component, list):
            sum += calculate_structure_sum(*component)
        elif isinstance(component, tuple):
            sum += calculate_structure_sum(*component)
        elif isinstance(component, set):
            sum += calculate_structure_sum(*component)
        elif isinstance(component, dict):
            sum += calculate_structure_sum(*tuple(component.items()))
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)