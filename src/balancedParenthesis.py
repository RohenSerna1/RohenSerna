def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "invalid"
            stack.pop()
    return "valid" if not stack else "invalid"

print(is_balanced("()"))
print(is_balanced("(hello, world)"))
print(is_balanced("Random text (as this) is ok()"))
print(is_balanced(")("))
print(is_balanced("())(()"))