import re


def parse_file(file_name):
    # pre installs
    raw_str = r'''(?P<key>[ ]*[A-Za-z._0-9]*):(?P<value>.+)'''
    file_encoding = "utf_8"

    print('\nfile_name: ', file_name,
          '\nraw_str: ', raw_str,
          '\nencoding: ', file_encoding,
          '\nfile: \n')

    with open(file_name, "r", encoding=file_encoding) as stream:
        match_str = stream.read()
        parse_result = re.findall(raw_str, match_str, re.MULTILINE)
        # print(parse_result)
        cortege = {}
        for i in parse_result:
            cortege[i[0]] = i[1]
        for i in cortege:
            print(i, cortege[i])

    return cortege


print(parse_file(r'C:\Users\KIP\Desktop\my_projects\dzettoapp\old\old.yml'))
print(parse_file(r'C:\Users\KIP\Desktop\my_projects\dzettoapp\new\new.yml'))
