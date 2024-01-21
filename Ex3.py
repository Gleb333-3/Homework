vowel = "aeiouy"
name = str(input("Name: "))

new_name = []
for i in name:
    if i in vowel:
        new_name.append("$")
    else:
        new_name.append('#')

print("".join(new_name))