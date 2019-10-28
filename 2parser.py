import yaml


def decc(file_name):
    with open(file_name, "r", encoding="utf-8-sig") as stream:
            match_str = stream.read()
            a = yaml.dump(yaml.load(match_str), default_flow_style=False)
            print(a)
            for key, value in a['i_rus'].items():
                #for i1,z1 in z:
#                    print(z1)
                print(key + ': ', value)
            #print(len(a))

decc(r'C:\Users\Z510\Desktop\sofe\sofe_technology_l_english — копия.yml')