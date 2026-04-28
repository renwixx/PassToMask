import os
import re
import sys

def get_mask(char, symbols):
    if char.isupper(): return "?u"
    if char.islower(): return "?l"
    if char.isdigit(): return "?d"
    if char in symbols: return "?s"
    return "?b"

def calculate_difficulty(chars, symbols, max_difficulty):
    difficulty = 1.0
    for c in chars:
        if c.isalpha(): difficulty *= 26
        elif c.isdigit(): difficulty *= 10
        elif c in symbols: difficulty *= 33
        else: difficulty *= 161
        
        if difficulty > max_difficulty or difficulty == float('inf'):
            return -1
    return difficulty

def main_work(path, max_difficulty):
    symbols = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    result_masks = set()
    
    if os.path.exists("masks.txt"):
        os.remove("masks.txt")

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue
            _, _, target = clean_line.partition(':')
            if not target: 
                target = clean_line
            
            chars = list(target)
            diff = calculate_difficulty(chars, symbols, max_difficulty)
            
            if diff == -1:
                continue
            
            mask = "".join([get_mask(c, symbols) for c in chars])
            
            if mask not in result_masks:
                result_masks.add(mask)
                with open("masks.txt", "a", encoding='utf-8') as out:
                    out.write(f"{mask}\n")

while True:
    path = input("Load a file ( log:pass / pass ): ").strip().replace("\"", "")
    
    if not os.path.exists(path):
        print("Drop valid file that exists.")
        continue
    
    try:
        max_diff = float(input("What max variations do you want?: "))
        if max_diff < 10:
            raise ValueError
    except ValueError:
        print("Write valid number.")
        continue
        
    main_work(path, max_diff)
    
    exit_choice = input("Do you want to exit? ( y / n ):")
    if exit_choice.lower() == 'y':
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
