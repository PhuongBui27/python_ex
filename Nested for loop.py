for i in range(1, 10):
    print('===============')
    for j in range(1, 10):
        print('%2d *%2d = %2d' % (i, j, i * j))
students = [('Phuong', ['Ly', 'Hoa']), ('Hien', ['Hoa', 'Van'])]
for (name, subjects) in students:
    print(name, 'take', len(subjects), 'courses')
counter = 0
for (name, subjects) in students:
    for s in subjects:
        if s == 'Hoa':
            counter += 1
print(counter)
# Bài tập về nhà
print('\t\t\tMultiplication Table\n')
for i in range(1, 10, 1):
    print('\t%3d' % i, end='')
print()
print('-----------------------------------------')
for j in range(1, 10, 1):
    print('%2d |%3d%4d%4d%4d%4d%4d%4d%4d%4d' % (j,j,j*2,j*3,j*4,j*5,j*6,j*7,j*8,j*9))


