'''
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
Hash Tables: Ransom Note
'''
import math
import os
import random
import re
import sys
from collections import Counter

# Solution 1 
def checkMagazine(magazine, note):
    # Write your code here
    dict_words = {}
    dict_note = {}
    for i in magazine:
        if dict_words.get(i):   
            dict_words[i] += 1
        else:
            dict_words[i] = 1
    
            
    for j in note:
        if dict_note.get(j):   
            dict_note[j] += 1
        else:
            dict_note[j] = 1
            
    # print(dict_words)
    # print(dict_note)
    
    result = "Yes"
    for k, v in dict_note.items():
        if dict_words.get(k):
            if v > dict_words.get(k):
                result = "No"
                break
        else:
            result = 'No'
            break
    print(result)



# solution 2

def checkMagazine2(magazine, note):
    # Write your code here
    dict_elements = {}
    dict_note = {}
    set_magazine = set()
    set_note = set()
    for i in magazine:
        if dict_elements.get(i):
            dict_elements[i] += 1
        else:
            dict_elements[i] = 1

    for i in note:
        if dict_note.get(i):
            dict_note[i] += 1
        else:
            dict_note[i] = 1
    
    for k, v in dict_elements.items():
        set_magazine.add(str(f"{k}:{v}"))

    for k, v in dict_note.items():
        set_note.add(str(f"{k}:{v}"))
    
    print(set_magazine)
    print(set_note)
    print(set_note - set_magazine)

    if len(set_note - set_magazine) == 0:
        print("Yes")
    else:
        print("No")

    
    

magazine = 'apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg'
note = 'elo lxkvg bg mwz clm w'
checkMagazine2(magazine.split(), note.split())
