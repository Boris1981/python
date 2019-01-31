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
                    global_configure_command=line.rstrip()
                    result[global_configure_command]=[]
                elif line.startswith(' '):
                    nextlevel_configure_command=line.rstrip()
                    result[global_configure_command].append(nextlevel_configure_command)
                elif line.startswith('  '):
                    lastlevel_configure_command=line.rstrip()
                    if prev_line.startswith('  '):
                        
                        
                        result[global_configure_command][nextlevel_configure_command].append(lastlevel_configure_command)
                    else:
                        converting_dict={}
                        converting_dict[global_configure_command]=dict()
                        converting_dict[global_configure_command]=nextlevel_configure_command
                        converting_dict[global_configure_command][nextlevel_configure_command]=list()
                        converting_dict[global_configure_command][nextlevel_configure_command].append(lastlevel_configure_command)
                        result[global_configure_command]=converting_dict[global_configure_command]
                        print('converting: '+str(converting_dict))
        prev_line=line
    return result

print(convert('config_r1.txt'))
