def is_additive_number(s: str) -> bool:
    n = len(s)

    def check_sequence(first: str, second: str, start: int) -> bool:
        while start < n:
            next_num = str(int(first) + int(second))
            if not s.startswith(next_num, start):
                return False
            start += len(next_num)
            first, second = second, next_num
        return True

    for i in range(1, n):
        for j in range(i + 1, n):
            first = s[:i]
            second = s[i:j]
            if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                continue
            if check_sequence(first, second, j):
                return True

    return False

print(is_additive_number("112358"))
print(is_additive_number("199100199"))