# -*- Encoding: utf-8 -*-
import re, os
from time import strftime


def parse_file(file_name, raw_str=r'''(?P<key>^[A-Za-z._0-9]*):(?P<value>.+["]*)''', file_encoding="utf_8"):

    print('\nfile_name: ', file_name,
          '\nraw_str: ', raw_str,
          '\nencoding: ', file_encoding,
          '\nfile: \n')

    with open(file_name, "r", encoding=file_encoding) as stream:
        match_str = stream.read()
        parse_result = re.findall(raw_str, match_str, re.MULTILINE)
        p = 0
        cotege = {}
        for i in parse_result:
            #print(i)
            cotege[i[0]] = i[1]
            p += 1
            #print(i)
            print(str(i[0]) + ':' + cotege[i[0]])
    return parse_result


def text_compare(b, d):
    filename = f'result{strftime("%H_%M")}.yml'
    with open(filename, 'w', encoding="utf-8-sig") as result_file:
        result_file.write('l_russian:\n')
        l_1 = []
        l_2 = []
        print('\nold\n')
        # сортировка старых ключей
        for i_1 in b:
            l_1.append(i_1[0])
        print('\nnew\n')
        # сортировка новых ключей
        for i_2 in d:
            l_2.append(i_2[0])
        print('differencies:')
        # поиск страых существующих ключей
        for m, n in enumerate(l_1):
            if n in l_2:
                result_file.write(f'{b[m][0]}{b[m][1]}\n')
                print('старые живые', n)
        result_file.write(f'\n###НОЫЕ_СТРОКИ###\n\n')
        # поиск новых существующих ключей среди старых
        for j, i in enumerate(l_2):
            if i not in l_1:
                result_file.write(f'{d[j][0]}{d[j][1]}\n')
                print('абсолютно новые', i)

    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'
    # перепись кодировки с винды на линку
    with open(filename, 'rb') as open_file:
        content = open_file.read()
    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    with open(filename, 'wb') as open_file:
        open_file.write(content)


def text_parse():
    a = input('Введите имя старого файла (без расширения): ')
    c = input('Введите имя нового файла (без расширения): ')
    b = parse_file(file_name=f'{a}')
    d = parse_file(file_name=f'{c}')
    print('\n\nрабочий каталог: ', os.path.abspath(__file__))
    text_compare(b, d)
    return print("\nFINISHED")


if __name__ == '__main__':
    text_parse()
