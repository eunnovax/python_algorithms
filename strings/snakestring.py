def snake_string(s):
    parts = []
    for i in range(1, len(s), 4):
        parts.append(s[i])

    for i in range(0, len(s), 2):
        parts.append(s[i])

    for i in range(3, len(s), 4):
        parts.append(s[i])

    return ''.join(parts)

print(snake_string('Fantastic Four!'))