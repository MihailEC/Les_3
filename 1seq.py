items = int(input('Введите количество элементов: '))
numbers = []

for i in range(items):
  number = int(input(f'Введите {i+1} число:'))
  numbers.append(number)

numbers.sort()
print(numbers)
