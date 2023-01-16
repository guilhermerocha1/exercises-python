# exercise 01
# def separe_output():
#     last = 0
#     name = str(input('Digite seu nome: '))
#     while last < len(name):
#         print(name[last])
#         last += 1

# exercise 02
def sum_value():
    last = 1
    sum = 0
    while last <= 5:
        try:
            value = int(input(f'Digite {last}° valor: '))
            sum = sum + value
            last += 1
        except ValueError:
            print('Ops!!, valor inválido por favor tente um número')

    return sum

print(sum_value())