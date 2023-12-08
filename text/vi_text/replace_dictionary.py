import re 
from text.vi_text.dictionary import (
    replacements, 
    en_to_vn,
    abbreviation_to_vn,
    comparision_symbols,
)


def replace(text):
    for pair in replacements:
        text = text.replace(pair[0], pair[1])
    for pair in en_to_vn:
        text = text.replace(pair[0], pair[1])
    # for pair in abbreviation_to_vn:
        # text = text.replace(pair[0], pair[1])
    return text


def replace_abbreviation(text):
    # example: TPHCM

    for pair in abbreviation_to_vn:
        text = text.replace(pair[0], pair[1])
    for token in re.findall(r"[\s|\(|\,|\;|\.]+[A-Z]+[\s|\)|\,|\;|\.]+",text):
        text =  text.replace(token,'  '.join(list(token)))
    return text


def split_char_num(text):
    # example: 56abc abr46 

    # re_split_char_num = r"(\d+)"
    re_split_char_num = ""

    # re_find_char_num = r"[a-zA-Z]+\d+\w*|\d+[a-zA-Z]+\d*"
    re_find_char_num = r"[\s][a-zA-Z]+[\-|\+|\_]*[\d]+[\-|\+|\_]*[\w]*|[\s][\d+][\-|\+\_]*[a-zA-Z]+[\-|\+|_]*[\d]*"
    
    char_num_tokens = re.findall(re_find_char_num, text)

    for token in char_num_tokens: 
        new_token = ' '.join(re.split(re_split_char_num,token))
        new_token = new_token.replace("-","")
        text = text.replace(token, new_token)
    return text 

def split_foreign_name(text): 
    # example: C.Ronadol

    re_dot = r"[a-zA-Z]+\.[a-zA-Z]+"
    name_tokens = re.findall(re_dot, text)

    for token in name_tokens:
        new_token = ' chấm '.join(re.split(r"\.", token))
        text = text.replace(token, new_token)
    return text

def replace_comparision_symbols(text):
    # example: 4>5 

    re_compare_symbols = r"[\w+|\s+][\<|\>|\=|\<\=|\>\=]{1}[\s+|\w+]"
    compare_symbols = re.findall(re_compare_symbols, text)

    for token in compare_symbols: 
        for symbol in comparision_symbols:
            text = text.replace(symbol[0], symbol[1])
    
    return text 

        