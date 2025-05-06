def compare_triplets(a, b):
    alice_score = 0
    bob_score = 0

    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1

    return [alice_score, bob_score]

# Ejemplos de uso
if __name__ == "__main__":
    print(compare_triplets([1, 2, 3], [3, 2, 1]))
    print(compare_triplets([5, 6, 7], [3, 6, 10]))
    print(compare_triplets([17, 18, 30], [99, 16, 8]))
    print(compare_triplets([20, 20, 30], [20, 20, 50]))
    print(compare_triplets([6, 8, 12], [7, 9, 15]))
    print(compare_triplets([10, 15, 20], [5, 6, 7]))