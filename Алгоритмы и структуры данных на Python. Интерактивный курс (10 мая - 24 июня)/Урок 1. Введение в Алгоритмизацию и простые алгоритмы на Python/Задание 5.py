'''
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
inp1 = int(input('Введите букву: '))
letter = let[inp1-1]
print(letter)