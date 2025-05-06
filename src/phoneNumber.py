def letter_combinations(digits):
    if not digits:
        return []

    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(index, path):
        if index == len(digits):
            combinations.append("".join(path))
            return
        
        for letter in digit_to_letters[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations

# Ejemplos de uso
if __name__ == "__main__":
    print(letter_combinations("23"))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    print(letter_combinations(""))     # Output: []
    print(letter_combinations("2"))    # Output: ['a', 'b', 'c']