import yaml


def decc(file_name):
    with open(file_name, "r", encoding="utf-8") as stream:
            match_str = stream.read()
            a = yaml.load(match_str)
            print(a)
            for key, value in a.items():
                #for i1,z1 in z:
                #    print(z1)
                print(str(key) + ': ', value)
            #print(len(a))


decc(r'C:\Users\Z510\Desktop\sofe\sofe_technology_l_english.yml')