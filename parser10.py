# -*- Encoding: utf-8 -*-
import re, os


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
    

if __name__ == '__main__':
    a = parse_file(file_name=r'/storage/emulated/0/bluetooth/sofe_event_l_russian1.yml')
    type(a)
    #print(a)
