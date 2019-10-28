import yaml


def file_loading(file_name):
    with open(file_name, 'r', encoding='utf_8')as file:
        file_data = file.read()
        loaded_yml = yaml.load(file_data)
        print(loaded_yml)
        # for key, value in loaded_yml.items():
        #     print(key + ': ' + value)


def first_call():
    file_loading(r'C:\Users\Z510\Desktop\sofe\sofe_technology_l_english.yml')


if __name__ == '__main__':
    first_call()