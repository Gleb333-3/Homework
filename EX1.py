line = input("Write an initial line: ").split()
names = input("Names to delete: ").split()

for i in names:
    line.remove(i)

print(' '.join(line))