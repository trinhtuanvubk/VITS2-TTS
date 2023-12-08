import os 
import numpy as np 
import re

# this function is to split a novel or paper to some paragraph
def split_paragraph(text: str):
    return re.split(r'\n{1,}', text)

# this function is to split a paragraph to sentences
def split_sentences(paragraphs: list):
    all_sentences=[]
    for para in paragraphs:
        sentence=re.split(r'[.!?]+[ ]',para.strip())
        all_sentences.append(sentence)
    return all_sentences

# if __name__=='__main__':
#     text='hôm nay trời đẹp.\n\n TS.Bùi lê minh nói'
#     params = split_paragraph(text)
#     print(split_sentences(params))