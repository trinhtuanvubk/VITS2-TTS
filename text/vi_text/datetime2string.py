import re 
from dateutil import parser
from datetime import datetime 
import unicodedata


# normalize text data 
def norm_text(text):
    return unicodedata.normalize('NFC', text)


# build default format class for datetime 
class sentinel:
    def __init__(
        self,
        year=0,
        month=0,
        day=0,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        default=None,
    ):
        # We can probably just use the `res` passed
        # to the _build_naive method instead.
        self._year = year
        self._month = month
        self._day = day

        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond

        if default is None:
            default = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        self.default = default

    def __getattr__(self, attr):
        return getattr(self.default, attr)

    @property
    def has_year(self):
        return self._year != 0

    @property
    def has_month(self):
        return self._month != 0

    @property
    def has_day(self):
        return self._day != 0

    def todatetime(self):
        res = {
            attr: value
            for attr, value in [
                ("year", self._year),
                ("month", self._month),
                ("day", self._day),
                ("hour", self._hour),
                ("minute", self._minute),
                ("second", self._second),
                ("microsecond", self._microsecond),
            ]
            if value
        }
        return self.default.replace(**res)

    def replace(self, **res):
        return sentinel(**res, default=self.default)

    def __repr__(self):
        return "%s(%d, %d, %d, %d, %d)" % (
            self.__class__.__qualname__,
            self._year,
            self._month,
            self._day,
            self._hour,
            self._minute,
        )



def check_wrong_special_datetime(datetime:str):
    # NOTE: any wrong if day == month, so this function is used to fix it 
    d_m_y =  re.split('\_|\-|\/|\|',datetime)
    if d_m_y[0] == d_m_y[1]:
        return True 
    else: 
        return False 



def check_special_date_month_case(datetime:str):
    # NOTE: check in case datetime is month-year but the output is day-month (year->day,month->month)
    d_m_y =  re.split('\_|\-|\/|\|',datetime)
    if len(d_m_y)==2 and int(d_m_y[1])>12 and int(d_m_y[1])<31 and int(d_m_y[0])<12: 
        return True
    else:  
        return False

def check_special_from_time_to_time_case(datetime:str):
    # NOTE: check in case data time is from day to day. ex: 15-25/10
    re_check = r"\D+"
    if len(set(re.findall(re_check,datetime)))>1: 
        return True
    else: 
        return False


def ngay_thang_removal(paragraph:str,d_m_y_tokens:list):
    text = paragraph
    for date in d_m_y_tokens:
        date_idx = text.find(date)
        if text[(date_idx-5):(date_idx-1)]=="ngày":
            text = text[:date_idx-5] + text[date_idx:]
        if text[(date_idx-6):(date_idx-1)]=="tháng":
            text = text[:date_idx-6] + text[date_idx:]
    return text



def replace_date_string(datetime:str):
    dt_object = parser.parse(datetime,dayfirst=True,default = sentinel())    
    # dt_object = parser.parse(datetime,dayfirst=True)   
    dict_ ={}
    dict_[dt_object._day]="ngày"
    dict_[dt_object._month]="tháng"
    dict_[dt_object._year]="năm"
    text = ""
    if check_special_from_time_to_time_case(datetime):
        time = re.split(r"[\_|\-|\/|\|]",datetime)
        # print("check0")
        if 0 < int(time[2]) < 12:
            text = "ngày {} đến ngày {} tháng {} ".format(time[0],time[1],time[2])
        elif int(time[2]) < 50 :
            text = "tháng {} đến tháng {} năm 20{} ".format(time[0],time[1],time[2])
        elif int(time[2]) <= 99 : 
            text = "tháng {} đến tháng {} năm 19{} ".format(time[0],time[1],time[2])
        else :
            text = "tháng {} đến tháng {} năm {} ".format(time[0],time[1],time[2])
        return text
    if check_wrong_special_datetime(datetime):
        # print('check1')
        if dt_object._year != 0:
            text = "ngày {} tháng {} năm {}".format(dt_object._month,dt_object._month,dt_object._year) 
        else: 
            text = "ngày {} tháng {}".format(dt_object._month,dt_object._month) 
        return text 
    if check_special_date_month_case(datetime):
        # print('check2')
        text = "tháng {} năm 20{}".format(dt_object._month,dt_object._day) 
        return text 
    for dt in dict_.keys():
        if dt != 0:
            text += dict_[dt] + " " + str(dt) + " "
    return text.rstrip()


    
def datetime_to_string(paragraph:str): 
    text = norm_text(paragraph)
    text = text.lower()
    # text = re.sub('\s{2,}', ' ', text)
    d_m_y_re = r"[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}|[0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}|[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}"
    # d_m_y_re = r"[0-9]{1,4}[\_|\-|\/|\|][0-9]{1}[0-2]{1}[\_|\-|\/|\|][0-9]{1,4}|[0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}|[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}"
    # ngày tháng năm - tháng năm - năm tháng - tháng ngày 
    d_m_y_tokens = re.findall(d_m_y_re,text)
    # print(d_m_y_tokens)
    text = ngay_thang_removal(text,d_m_y_tokens)
    for datetime in d_m_y_tokens :
        try:
            # print(text)
            # print(datetime)
            new_datetime = replace_date_string(datetime)
            # print(new_datetime)
            text = text.replace(datetime,new_datetime)
        except:
            pass
    return text




# if __name__ == "__main__": 

#     example = 'Ngày hôm    nay    là ngày 5/5 và tháng 4/98, chúng tôi  sẽ đến vào ngày  8/10, sau tháng 12 ngày'
#     example1 = "Ngày 10-10: Bộ Quốc phòng ra quyết định thành lập Tiểu đoàn Tên lửa bờ 680 Hải quân, \
#                 lực lượng nòng cốt là Tiểu đoàn 678 trực thuộc Bộ Tư lệnh Hải quân.\
#                 Trước yêu cầu nhiệm vụ bảo vệ chủ quyền biển, đảo trong tình hình mới, ngày 3/4/1993, \
#                 Bộ Quốc phòng ra Quyết định số 142/QĐ-QP nâng cấp Tiểu đoàn Tên lửa bờ 680 Hải quân thành \
#                 Đoàn Tên lửa bờ 680 Hải quân trực thuộc Quân chủng Hải quân. \
#                 Ngày 4-5-2012, Đoàn được điều chuyển về trực thuộc Vùng 3 Hải quân. \
#                 Tiếp đó, ngày 22-5-2013, Bộ trưởng Bộ Quốc phòng ra Quyết định số 1687/QĐ-BQP về việc tổ chức lại \
#                 Đoàn Tên lửa bờ 680 thành Lữ đoàn Tên lửa bờ 680 và trực thuộc Vùng 3 Hải quân."
#     example1 = 'Nhiệt độ hôm nay là 19.0'
#     example2 = 'ngày 9/2022 code chạy như cứt'
#     paragraph = datetime_to_string(example2) 
#     print(paragraph)
    