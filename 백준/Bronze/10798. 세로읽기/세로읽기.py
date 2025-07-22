words = [input() for _ in range(5)]
result = ""

for col in range(15):
    for row in range(5):
        if col < len(words[row]):
            result += words[row][col]

print(result)