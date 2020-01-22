"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count = 0
with open('file.txt', 'r') as f:
    line = f.readlines()

    for l in line:
        if len(l) > 1:
            count += 1
            ls = l.split()
            if len(ls) == 1:
                print(f'Word  count is: {len(ls)} in line № {count}')  # if 1 word
            else:
                print(f'Words count is: {len(ls)} in line № {count}')  # > 1 words in line
    print(f'Total count of lines is: {count}')
