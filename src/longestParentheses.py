def longest_valid_parentheses(s:str) -> int:
    stack = []
    count = 0

    for char in s:
        if char == "(":
            stack.append(char)
        elif char ==")":
            if stack and stack[-1] == "(":
                stack.pop()
                count+=1
    return count


print(longest_valid_parentheses("(()"))
print(longest_valid_parentheses("(()))()"))