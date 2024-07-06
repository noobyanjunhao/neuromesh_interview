def check_parentheses(strings):
    result = []
    for string in strings:
        stack = []
        output = list(string)
        marks = [' '] * len(string)
        for index, char in enumerate(string):
            if char == '(':
                stack.append(index)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    marks[index] = '?'
        while stack:
            marks[stack.pop()] = 'x'
        result.append(''.join(output))
        result.append(''.join(marks))
    return result

# Test cases
input_strings = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

output = check_parentheses(input_strings)
for line in output:
    print(line)