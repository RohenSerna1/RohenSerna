def deep_equals(obj1, obj2):
    if type(obj1) != type(obj2):
        return False

    if isinstance(obj1, dict):
        if obj1.keys() != obj2.keys():
            return False
        return all(deep_equals(obj1[key], obj2[key]) for key in obj1)

    return obj1 == obj2

# Ejemplos de uso
if __name__ == "__main__":
    print(deep_equals({'a': 1, 'b': {'c': 3}}, {'a': 1, 'b': {'c': 3}}))
    print(deep_equals({'a': 1, 'b': {'c': 5}}, {'a': 1, 'b': {'c': 6}}))