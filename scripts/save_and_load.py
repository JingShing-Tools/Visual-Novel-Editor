import json
from settings import *

def save_file(level):
    with open('save_file.txt', 'w') as save_file:
        pass

def load_file(level):
    # if level detect has save file than load file
    if level.has_save:
        with open('save_file.txt') as save_file:
            pass

def list_save_dialogue(path, lines):
    if path:
        with open(path, 'w', encoding='UTF-8') as save_file:
            json.dump(lines, save_file)

def save_dialogue(path, lines):
    if path:
        with open(path, 'w', encoding='UTF-8') as file:
            for line in lines:
                file.write(line + '\n')

def list_load_dialogue(path):
    if path:
        # read all
        with open(resource_path(path), encoding='UTF-8') as save_file:
            lines = json.load(save_file)
            return lines

def load_dialogue(path, lines, start_line = None):
    found = False
    if path:
        lines.clear()
        # read line by line
        with open(resource_path(path), encoding='UTF-8') as file:
            while(1):
                line = file.readline()
                if start_line and not(found):
                    if not(line):break
                    else:
                        line = line.replace('\n', '')
                    if line == start_line:
                        found = True
                        continue
                    elif line!=start_line and not(found):
                        continue
                if not(line):break
                elif line == '\n' or line == '':continue
                else:
                    line = line.replace('\n', '')
                    if line == '@end':break
                    else:
                        lines.append(line)


def found_save_or_not(level):
    # check if save_file.txt exist
    try:
        with open('save_file.txt') as save_file:
            level.has_save = True
    except:
        level.has_save = False

import os
def found_dialogue_or_not(file_name):
    return os.path.exists(resource_path('dialogues/' + file_name))
    # try:
    #     with open(resource_path('dialogues/' + file_name)) as save_file:
    #         return True
    # except:
    #     return False

def found_asset_imgs(folder_path='assets/graphics/characters/', img_dict=None, transform = False, scale=(152, 152)):
    if img_dict:
        img_dict.clear()
        resource_path(folder_path)
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            if '.png' in file_name or '.jpg' in file_name:
                file_fore_name = file_name.split('.')[0]
                if transform:
                    img_dict[file_fore_name] = pygame.transform.scale(pygame.image.load(folder_path + file_name), scale)
                else:
                    img_dict[file_fore_name] = pygame.image.load(folder_path + file_name)