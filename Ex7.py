grades = input("Grades: ").split()
sum = 0
count = 0

for i in grades:
    sum += int(i)
    count += 1

print(float(sum/count))
