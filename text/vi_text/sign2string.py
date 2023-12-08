import re 
import unicodedata

# normalize text data 
# def norm_text(text):
#     return unicodedata.normalize('NFC', text)

#  replace "." by "chấm"
def one_dot_replace(string:str):
    num = re.split(r'\.',string)
    return ' ' + num[0] + " chấm " + num[1] + ' '

def one_comma_replace(string:str):
    num = re.split(r'\,',string)
    return ' ' + num[0] + " phẩy " + num[1] + ' '

def x_replace(string:str):
    num = re.split(r'x', string)
    return ' ' + num[0] + " nhân " + num[1] + ' '

def add_replace(string:str):
    num = re.split(r'\+', string)
    return ' ' + num[0] + " cộng " + num[1] + ' '

def div_replace(string:str):
    num = re.split(r'\:', string)
    return ' ' + num[0] + " chia " + num[1] + ' '
def frac_replace(string:str):
    num = re.split(r'\/', string)
    return ' ' + num[0] + " trên " + num[1] + ' '

def sub_replace(string:str):
    num = re.split(r'\-|\,|\;|\.', string)
    # having 2 options 
    # return num[0] + " trừ " + num[1]

    if int(num[0]) < int(num[1]):
        return ' ' + num[0] + " đến " + num[1] + ' '
    else:
        return string 


#  remove multiple '.' or ','
def multi_dot_removal(string:str):
    num = re.split('\.|\,',string)
    return ''.join(num)

def sign2string(paragraph:str):

    #  normalize text 
    # text = norm_text(paragraph)
    text = paragraph

    #  lower text 
    text = text.lower()

    # remove space 
    # text = re.sub('\s{2,}', ' ', text)


    #  + one or limited, * zero or limited, [] list of char, {} times, 
    # dot_re1 = r"([\s][0-9]+[\.]{1}[0-9]*)" # regex for one '.'
    dot_re1 = r"([\s][0-9]+[\.]{1}[0-9]+[\s]*)" # regex for one '.'
    # dot_re1 = r"([\s][0-9]+[\.]{1}[0-9]{1,2}[\s])"    
    # dot_re2 = r"([\s][0-9]+[\.]{1}[0-9]{3,}[\s])" 

    # multi_dot_re2 = r"([0-9]+[\.|\,]{1}[0-9]+[\,|\.0-9]+)"
    multi_dot_re2 = r"([0-9]+[\.|\,]{1}[0-9]{3}[\,|\.|\s]+)"  # regex for multiple '.' or ','
    # dot_re2 = r"([0-9]+[\.|\,]{1}[[0-9]{1,3})"  


    comma_re1 = r"([\s]*[0-9]+[\,]{1}[0-9]+[\s]*)"  # regex for one ','
    # comma_re1 = r"([\s][0-9]+[\,]{1}[0-9]{1,2}[\s])" 
    # comma_re2 = r"([\s][0-9]+[\,]{1}[0-9]{3}[\s])" 

    x_re1 = r"([\s][0-9]+[x]{1}[0-9]+[\s|\.|\,|\w+])"  # regex for x 

    add_re1 = r"([\s][0-9]+[+]{1}[0-9]+[\s|\.|\,|\w+])" # regex for + 

    div_re1 = r"([\s][0-9]+[\:]{1}[0-9]+[\s|\.|\,|\w+])" # regex for : 

    # frac_re1 = r"([\s][0-9]+[\/]{1}[0-9]+[\s|\.|\,|\w+])" #regex for /

    sub_re1 = r"([\s][0-9]+[\-]{1}[\s]*[0-9]+[\s|\.|\,|\w+])" # regex for - 



    # find all tokens 2
    multi_dot_tokens2 = re.findall(multi_dot_re2,text)
    # print(dot_tokens2)
    if len(multi_dot_tokens2)>0:
        for token in multi_dot_tokens2:
            new_token = multi_dot_removal(token)
            text = text.replace(token, new_token)


    # find all tokens 1
    dot_tokens1 = re.findall(dot_re1,text)
    # print(dot_tokens1)
    if len(dot_tokens1)>0:
        for token in dot_tokens1:
            new_token = one_dot_replace(token)
            text = text.replace(token, new_token)




    comma_tokens1 = re.findall(comma_re1,text)
    # print(comma_tokens1)
    if len(comma_tokens1)>0:
        for token in comma_tokens1:
            new_token = one_comma_replace(token)
            text = text.replace(token, new_token)



    x_tokens1 = re.findall(x_re1,text) 
    # print(x_tokens1)
    if len(x_tokens1)>0:
        for token in x_tokens1:
            new_token = x_replace(token)
            text = text.replace(token, new_token)



    add_tokens1 = re.findall(add_re1,text) 
    # print(add_tokens1)
    if len(add_tokens1)>0:
        for token in add_tokens1:
            new_token = add_replace(token)
            text = text.replace(token, new_token)


    sub_tokens1 = re.findall(sub_re1,text) 
    # print(sub_tokens1)
    if len(sub_tokens1)>0:
        for token in sub_tokens1:
            new_token = sub_replace(token)
            text = text.replace(token, new_token)


    div_tokens1 = re.findall(div_re1,text) 
    # print(div_tokens1)
    if len(div_tokens1)>0:
        for token in div_tokens1:
            new_token = div_replace(token)
            text = text.replace(token, new_token)

    # frac_tokens1 = re.findall(frac_re1,text) 
    # # print(frac_tokens1)
    # if len(frac_tokens1)>0:
    #     for token in frac_tokens1:
    #         new_token = frac_replace(token)
    #         text = text.replace(token, new_token)

    return text 


# if __name__=='__main__':
#     ex = 'hôm nay là 40.5 độ C. và 50,6 cùng với 4 x3 với 1,123 và 15-4 và 2,75 và 3,4567 va '
#     text = sign2string(ex)
#     print(text)