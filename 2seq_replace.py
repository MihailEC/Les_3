numbers = input('Введите элементы списка через запятую: ')
numbers = numbers.replace(';', ',').replace('/', ',').split(',')
for i in range(len(numbers)):
  numbers[i] = int(numbers[i])
numbers_uniq = set(numbers)
numbers_uniq = list(numbers_uniq)
print(numbers_uniq)