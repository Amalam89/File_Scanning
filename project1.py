# Ali Malam 26643054

from pathlib import Path

import os

import shutil


def get_files_in_subdirectories(directory: 'path object') -> list:
    
    '''sorts files in directory first then files in subdirectories
    all in lexographical order'''
    
    file_list = []
    s= sorted(os.listdir(directory))
    for file in s:
        p = directory / Path(file)
        if(p.is_file()):
            file_list.append(p)
    for file in s:
        p = directory / Path(file)
        if(p.is_dir()):
            file_list.extend(get_files_in_subdirectories(p))
    return file_list


def get_files_in_directory(directory: 'path object') -> list:
    
    'Returns list of files in a directory'
    
    file_list = []
    s = sorted(os.listdir(directory))
    for file in s:
        p = directory / Path(file)
        if(p.is_file()):
            file_list.append(p)
    return file_list


def file_search_first_input() -> list:
    
    '''Returns list of files based on the first input or prints ERROR
    if format is incorrect'''
    
    file_list = []
    print('Enter "D filepath" for only directory files ')
    print('Enter "R filepath" for recursive display of files')
    command = input()
    while(True):
        if (command[:2] == 'R ' and command[2:] != ""):
            try:
                directory = Path(command[2:])
                for file in get_files_in_subdirectories(directory):
                    file_list.append(file)
                break
            except:
                print('', end ='')
        if (command[:2] == 'D ' and command[2:] != ""):
            try:
                directory = Path(command[2:])
                for file in get_files_in_directory(directory):
                    file_list.append(file)
                break
            except:
                print('', end ='')
        print('ERROR')
        command = input()
    for file in file_list:
        print(file)
    return file_list
        
def file_search_second_input(file_list: ['path object']) -> list:
    
    '''Returns list of files based on the second input or prints ERROR
    if format is incorrect'''
    
    new_file_list =[]
    print('Enter "A" for all files ')
    print('Enter "N filename" for named file')
    print('Enter "E file-extension" for files with named extension')
    print('Enter "T search-phrase" for files containing search-phrase')
    print('Enter "< file-size" for file less than file-size')
    print('Enter "> file-size" for file greater than file-size')
    command = input()
    while(True):
        if (command == 'A'):
            for file in file_list:
                new_file_list.append(file)
            break
        elif (command[:2] == 'N ' and command[2:] != ""):
            for file in file_list:
                if (file.name == command[2:]):
                    new_file_list.append(file)
            break
        elif (command[:2] == 'E ' and command[2:] != ""):
            for file in file_list:
                if (file.suffix == command[2:] or file.suffix[1:] == command[2:]):
                    new_file_list.append(file)
            break
        elif (command[:2] == 'T ' and command[2:] != ""):  
            for file in file_list:
                try:
                    if(command[2:] in file.read_text()):
                        new_file_list.append(file)
                except UnicodeDecodeError:
                    print('', end = '')
            break
        elif (command[:2] == '< ' and command[2:] != ""):
            try:
                int(command[2:])
                for file in file_list:
                    if(file.write_bytes(file.read_bytes()) <= int(command[2:])):
                        new_file_list.append(file)
                break
            except ValueError:
                print('', end = '')
        elif (command[:2] == '> ' and command[2:] != ""):
            try:
                int(command[2:])
                for file in file_list:
                    if(file.write_bytes(file.read_bytes()) >= int(command[2:])):
                        new_file_list.append(file)
                break
            except ValueError:
                print('', end = '')
        print('ERROR')
        command = input()
    for file in new_file_list:
        print(file)
    return new_file_list


def file_search_third_input(new_file_list: ['path object']) -> list:
    
    '''Takes action on list of files based on the third input
    or prints ERROR if format is incorrect'''

    print('Enter "F" to print first line of text from file')
    print('Enter "D" make a duplicate copy of the file')
    print('Enter "T" to modify timestamp for current date/time')
    command = input()
    while(True):
        if(command == 'F'):
            for file in new_file_list:
                try:
                    the_file = open(str(file), 'r')
                    print(the_file.readline().rstrip('\n'))
                except:
                    print('NOT TEXT')
                finally:
                    the_file.close()
            break
        if(command == 'D'):
            for file in new_file_list:
                shutil.copyfile(str(file), str(file) + '.dup')
            break
        if(command == 'T'):
            for file in new_file_list:
                os.utime(file, None)
            break
        print('ERROR')
        command = input()
    return None


if __name__ == '__main__':
    file_list = file_search_first_input()
    if (len(file_list) != 0):
        new_file_list = file_search_second_input(file_list)
        if (len(new_file_list) != 0):
            file_search_third_input(new_file_list)

