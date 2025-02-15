#1. Дано целое число N (> 0). Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2

n = input('Введи число n: ')

while type(n) != int: #обработка исключений
  try:
    n = int(n)
    if n <= 0:
        raise ValueError
  except ValueError :
    print('Неправильно ввели!')
    n = input('Введите число заново: ') #пусть пользователь введёт число заново

total_sum = 0
a = n #без приравнивания a <= 2 * n станет бессмысленным
while a <= 2 * n:
  total_sum += a ** 2
  a += 1

print (f'Сумма квадратов от {n} до {2 * n}: {total_sum}')
