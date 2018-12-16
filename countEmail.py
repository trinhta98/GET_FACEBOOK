file = open('list_Email.txt', 'r', encoding='utf-8')
file2 = file.read()
file2 = file2.split(', ')
file3 = open('list_Email2.txt', 'w', encoding='utf-8')

for j in range(0, file2.__len__() // 25):
    for i in range(25*j, 25*(j + 1)):
        print(i)
        file3.write(file2[i] + ',')
    file3.write('\n')