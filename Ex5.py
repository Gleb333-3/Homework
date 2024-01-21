s = str(input("String: "))
vowels = "aeiouy"
new_s = ""
indexes = list(enumerate(s, start=1))

for ind, chr in indexes:
    if chr in vowels:
        new_s += str(ind)
    else:
        new_s += chr
print(new_s)