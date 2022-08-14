import json, re
from settings import *

def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

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

import os
def load_config(path='dialogues\config\config.txt', config=None):
    if config:
        if os.path.exists(path):
            with open(resource_path(path), encoding='UTF-8') as file:
                while(1):
                    line = file.readline()
                    if not(line):break
                    if '#' in line:
                        pass
                    elif '=' in line:
                        line = line.replace('\n', '')
                        # sets = re.split('=| ',  line)
                        sets = line.split('=')
                        stat = sets[0]
                        value = sets[-1]
                        if stat == 'need_help' or stat == 'only_cpu':
                            if value == 'True':
                                value = True
                            else:value = False
                        elif stat == 'shader_default' or stat == 'text_frame_alpha':
                            value = int(value)
                        elif stat == 'text_frame_color':
                            value = value.split(',')
                            value = list(map(int, value))
                        elif stat == 'resolution' or stat == 'window_size':
                            value = eval(value)
                        elif stat == 'allow_img_format':
                            value = value.split(',')
                        config[stat] = value

def save_config(path='dialogues\config\config.txt', config=None):
     if config:
        if os.path.exists(path):
            with open(resource_path(path), encoding='UTF-8') as file:
                pass

def found_save_or_not(level):
    # check if save_file.txt exist
    try:
        with open('save_file.txt') as save_file:
            level.has_save = True
    except:
        level.has_save = False

def found_dialogue_or_not(file_name):
    return os.path.exists(resource_path('dialogues/' + file_name))

def found_asset_imgs(folder_path='assets/graphics/characters/', img_dict=None, transform = False, scale=(152, 152), allow_img_format = ['png', 'jpg', 'bmp']):
    if img_dict:
        img_dict.clear()
        folder_path = resource_path(folder_path)
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            file_format = file_name.split('.')[-1]
            if file_format in allow_img_format:
                file_fore_name = file_name.split('.')[0]
                if transform:
                    img_dict[file_fore_name] = pygame.transform.scale(pygame.image.load(folder_path + file_name), scale)
                else:
                    img_dict[file_fore_name] = pygame.image.load(folder_path + file_name)

def found_asset_sounds(folder_path='assets/audio/sound/', sound_dict=None, allow_sound_format = ['mp3', 'wav']):
    if sound_dict:
        sound_dict.clear()
        folder_path = resource_path(folder_path)
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            file_format = file_name.split('.')[-1]
            if file_format in allow_sound_format:
                file_fore_name = file_name.split('.')[0]
                sound_dict[file_fore_name] = pygame.mixer.Sound(folder_path + file_name)

def found_max_scene(file_path):
    if os.path.exists(resource_path(file_path)):
        max_scene = 0
        with open(resource_path(file_path), encoding='UTF-8') as file:
            while(1):
                line = file.readline()
                if not(line):break
                else:
                    if '@scene' in line:
                        scene_num = line.replace('@scene', '')
                        if int(scene_num) > max_scene : max_scene = int(scene_num)
            return max_scene
    else:
        return 0

def found_all_bgm(folder_path = 'assets/audio/bgm/', bgm_list = None):
    if bgm_list:
        bgm_list.clear()
        bgm_list.append('none')
        folder_path = resource_path(folder_path)
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            if '.mp3' in file_name:
                file_name = file_name.split('.')[0]
                bgm_list.append(file_name)
