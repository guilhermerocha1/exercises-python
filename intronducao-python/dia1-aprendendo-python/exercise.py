# exercicio 01
# number = int()

# def sum(num1, num2):
#     if num1 > num2:
#         number = num1
#     else:
#         number = num2
#     return number

# print('Maior número: ', sum(10, 20))

# exercicio 2
# numbers = [2, 4, 10, 0]

# def average(arr):
#     sum = 0
#     for value in arr:
#         sum += value
#     return sum / len(arr)

# print('Média de valores:', average(numbers))

# exercicio 3
# n > 1

# n = 5
# last = 0

# while last < n:
#     print(5 * '*')
#     last += 1

# exercicio 4
name = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

def qtyCaracter(arr):
    intervalName = ''
    for name in arr:
        if len(name) > len(intervalName):
            intervalName = name
    return intervalName

print('Nome com mais caracteres: ', qtyCaracter(name))

