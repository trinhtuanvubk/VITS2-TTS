import re 
import unicodedata 
from text.vi_text.dictionary import SI_units_to_vn
# from dictionary import SI_units_to_vn



def units_dectection(text):
    # number_and_space = "([0-9]+\s+)"
    # prefix = "(Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y)"
    # unit = "(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)"
    # power = "(\^[+-]?[1-9]\d*)"
    # unitAndPrefix = "(" + prefix + "?" + unit + power + "?" + "|1" + ")"
    # multiplied = unitAndPrefix + "(?:·" + unitAndPrefix + ")*"
    # withDenominator = number_and_space +   multiplied + "(?:\/" + multiplied + ")?"

    # regex = r"(kg|m|s|A|K|cd|mol|\d+)((\*|\^)(kg|m|s|A|K|cd|mol|\d+))*(/(kg|m|s|A|K|cd|mol|\d+)((\*|\^)(kg|m|s|A|K|cd|mol|\d+))*)?"
    # regex = r"(\d+\s{0,1}[(mg)g(kg)(ms)s(mm)(cm)(dm)m(km)(mol)(mA)A(mV)V(kV)(KV)(ml)l])"
    # regex = r"([\s]*[\d]+[\.|\,]{0,1}[\d]*[\s]{0,1})(mg|g|kg|Kg|ms|s|mm|cm|dm|m2|m3|m|km|km2|Km2|Km|mol|mA|A|mV|V|kV|KV|ml|l|L|hz|Hz|KHz|khz|rad|W|Kwh|kWh|h)([\s|\,|\.|\/])(mg|g|kg|Kg|ms|s|mm|cm|dm|m2|m3|m|km|km2|Km2|Km|mol|mA|A|mV|V|kV|KV|ml|l|L|hz|Hz|KHz|khz|rad|W|Kwh|kWh|h|\s){0,1}"
    regex = r"([\s]*[\d]+[\.|\,|\(]{0,1}[\d]*[\s]{0,1})(mg|g|kg|Kg|ms|s|mm|cm|dm|m2|m3|m|km|km2|Km2|Km|ha|mol|mA|A|mV|V|kV|KV|ml|l|L|hz|Hz|KHz|khz|rad|W|Kwh|kWh|h|%)([\s|\,|\.|\/|\;|\)])(\w*)"
    tokens = re.findall(regex,text)
    # example tokens: [('100 ', 'ml'), ('14 ', 'kg'), ('22 ', 'g')]
    return tokens

def units2string(text):
    tokens = units_dectection(text)
    # print(tokens)
    for token in tokens:
        if token[2]== '/': 
            old_string = token[0] + token[1] + token[2] + token[3]
            try: 
                new_string = token[0] + ' ' + SI_units_to_vn[token[1]] + ' trên ' + SI_units_to_vn[token[3].strip()]
            except:
                new_string = token[0] + ' ' + SI_units_to_vn[token[1]] + ' trên ' + token[3]

        else:
            old_string = token[0] + token[1]
            new_string = token[0] + ' ' + SI_units_to_vn[token[1]]
        text = text.replace(old_string,new_string)
    return text


# if __name__=="__main__":
#     test = 'tao nặng 100 m3, mày cao 1.7 m2 và chạy với 5 m/s và rộng 100m2'
#     test1 = 'cái này nè 15 kg^2/m^3 và kg*2/m va 16 s'
#     # https://vnexpress.net/tau-cao-toc-canh-ngam-dien-bay-thu-lan-dau-tien-4428906.html
#     print(units2string(test))