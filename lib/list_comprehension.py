#!/usr/bin/env python3

def return_evens(num_list):
    return [even for even in num_list if even % 2 == 0]  
    pass

def make_exclamation(sentence_list):
    return [f"{string}!" for string in sentence_list]
    pass