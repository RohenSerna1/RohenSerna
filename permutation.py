from itertools import permutations

def permute(nums):
    return [list(p) for p in permutations(nums)]

print(permute([1,2,3]))
print(permute([0,1]))
print(permute([1]))