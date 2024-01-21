name = list(input("Name: "))
asci_listt = []
name_list = []

for i in name:
    asci_listt.append(ord(i))
print(asci_listt)

for i in asci_listt:
    name_list.append(chr(i))
print("".join(name_list))