numbers = input('Введите элементы первого списка через запятую: ')
numbers = numbers.replace(';', ',').replace('/', ',').split(',')
for i in range(len(numbers)):
  numbers[i] = int(numbers[i])
numbers_set = set(numbers)
numbers_2 = input('Введите элементы второго списка через запятую: ')
numbers_2 = numbers_2.replace(';', ',').replace('/', ',').split(',')
for i in range(len(numbers_2)):
  numbers_2[i] = int(numbers_2[i])
numbers_2_set = set(numbers_2)
result = numbers_set - numbers_2_set
result = list(result)
print(result)