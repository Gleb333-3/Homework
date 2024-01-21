s = input("Sentence: ").split()
result = []

for i in s:
    result.append(i[::-1])

print(" ".join(result))