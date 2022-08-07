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

def load_dialogue(path):
    if path:
        # read line by line
        lines = []
        with open(resource_path(path), encoding='UTF-8') as file:
            while(1):
                line = file.readline()
                if not(line):break
                else:
                    line = line.replace('\n', '')
                    lines.append(line)
            return lines


def found_save_or_not(level):
    # check if save_file.txt exist
    try:
        with open('save_file.txt') as save_file:
            level.has_save = True
    except:
        level.has_save = False

def found_dialogue_or_not(file_name):
    try:
        with open(resource_path('dialogues/' + file_name)) as save_file:
            return True
    except:
        return False