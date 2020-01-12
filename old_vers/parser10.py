# -*- Encoding: utf-8 -*-
import re
import os
from time import strftime


def parse_file(file_name, raw_str=r'''(?P<key>^[A-Za-z._0-9]*):(?P<value>.+["]*)''', file_encoding="utf_8"):

    print('\nfile_name: ', file_name,
          '\nraw_str: ', raw_str,
          '\nencoding: ', file_encoding,
          '\nfile: \n')

    with open(file_name, "r", encoding=file_encoding) as stream:
        match_str = stream.read()
        parse_result = re.findall(raw_str, match_str, re.MULTILINE)
        # p = 0
        # cotege = {}
        # for i in parse_result:
        #     print(i)
        #     cotege[i[0]] = i[1]
        #     p += 1
        #     # print(i)
        #     print(str(i[0]) + ':' + cotege[i[0]])
    return parse_result


def text_compare(b, d, a, c):
    filename = f'result{strftime("%H_%M")}.yml'
    with open(filename, 'w', encoding="utf-8-sig") as result_file:
        result_file.write('l_russian:\n')
        result_file.write(f'\n# old file - {a}\n')
        result_file.write(f'# new file - {c}\n\n\n')
        l_1 = []
        l_2 = []

        # сортировка старых ключей
        for i_1 in b:
            l_1.append(i_1[0])

        # сортировка новых ключей
        for i_2 in d:
            l_2.append(i_2[0])

        print('differences:',
              'O - old',
              'N - new')
        # поиск страых существующих ключей
        for number1, key1 in enumerate(l_1):
            if key1 in l_2:
                result_file.write(f'{b[number1][0]}:{b[number1][1]}\n')

                for number2, key2 in enumerate(d):
                    for i in key2:
                        if i == key1:
                            result_file.write(f'#  :{d[number2][1]}\n')
                            # print(d[key2][1])

                # O - old
                print('O - ', key1)

        result_file.write(f'\n###НОЫЕ_СТРОКИ###\n\n')
        # поиск новых существующих ключей среди старых
        for number2, key2 in enumerate(l_2):
            if key2 not in l_1:
                result_file.write(f'{d[number2][0]}:{d[number2][1]}\n')
                # N - new
                print('N - ', key2)

    # перепись кодировки с винды на линку
    # мб и не нужно но пускай будет
    windows_line_ending = b'\r\n'
    unix_line_ending = b'\n'
    with open(filename, 'rb') as open_file:
        content = open_file.read()
    content = content.replace(windows_line_ending, unix_line_ending)
    with open(filename, 'wb') as open_file:
        open_file.write(content)


def text_parse():
    example = r"""
    пример: 
    C:\Users\Z510\Desktop\sofe\sofe_technology_l_english.yml
    """
    print(example)
    a = input(r'Введите путь \ полное имя старого файла (через \): ')
    c = input(r'Введите путь \ полное имя нового файла (через \): ')
    b = parse_file(file_name=f'{a}')
    d = parse_file(file_name=f'{c}')
    print('\n\nрабочий каталог: ', os.path.abspath(__file__))
    text_compare(b, d, a, c)
    return print("\nFINISHED")


if __name__ == '__main__':
    text_parse()
