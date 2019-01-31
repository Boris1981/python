#!/usr/bin/env python3

ignore=['duplex','alias','version']

def ignore_command(command, ignore):
    return any(word in command for word in ignore)

def convert(conf):
    '''Функция конвертирует файл конфигурации в словарь:
    -все команды верхнего уровня (начинаются без " ") будут ключами
    -если у команды верхнего уровня есть подкоманды, они представлены в виде списка
     в значении соответствующего ключа
    -функция ожидает имя файла конфигурации
    '''
    result={}
    with open(conf,'r') as f:
        for line in f:
            if line != '!' and not ignore_command(line, ignore):
                if not line.startswith(' '):
                    global_configure_command=line.strip()
                    result[global_configure_command]=[]
                elif line.startswith(' '):
                    result[global_configure_command].append(line.strip())
    return result

print(convert('config_sw1.txt'))
