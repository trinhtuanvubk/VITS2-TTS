replacements = [
    (':', ','),
    ('?', ' . '),
    # ('¿','ˑ'),
    # ('!', ' . '),
    (',', ' , '),
    ('.', ' . '),
    (';', ' , '),
    (' - ', ' , '),
    ('-', ' '),
    ('(', ' , '),
    (')',' , '),
    ('…', ' , '),
    ('...', ' , '),
    # ('/', ' , '),
    # ('\n', ' . '),
    # ('\n', '\n'),
    ('%', ' phần trăm '),
    ('@', ' a còng '),
    ('&', ' và '),
    ('#', ' thăng '),
    ('°c', ' độ c'),
    (' b ', ' bê '),
    (' c ', ' xê '), 
    (' d ', ' đê '),
    (' f ', ' ép '),
    (' g ', ' gờ '),
    (' h ', ' hát '),
    (' j ', ' di '),
    (' k ', ' ca '),
    (' l ', ' lờ '),
    (' n ', ' nờ '),
    (' m ', ' mờ '),
    (' p ', ' pê '),
    (' q ', ' quy '),
    # (' r ', ' e rờ '),
    (' s ', ' ét '),
    (' t ', ' tê '),
    (' v ', ' vê '),
    (' x ', ' ích '),
    ( ' w ', ' vê kép '),
    ( ' z ', ' dét '),
]

en_to_vn = [
    ('game', 'gêm'),
    ('chatbot', 'chát bót'),
    (' ok ', ' ô kê '),
    (' okela ', ' ô kê la '),
    (' okay ', ' ô kê '),
]

# In case abbreviation is just a part of word, need space after replaced word
# Having function 'remove_multiple_space' in another module 
abbreviation_to_vn = [
# Vietnamese
    ('MTGPMNVN', ' mặt trận giải phóng miền nam việt nam '),
    ('CHXHCNVN', ' cộng hòa xã hội chủ nghĩa việt nam '),
    ('UBMTTQ', ' ủy ban mặt trận tổ quốc '),
    ('TPHCM',' thành phố hồ chí minh '),
    ('LĐ-TB&XH', ' lao động thương binh và xã hội '),
    ('VH,TT&DL', ' văn hóa thể thao và du lịch '),
    ('TPHN',' thành phố hà nội '),
    ('TP.HN',' thành phố hà nội '),
    ('TP.HCM',' thành phố hồ chí minh '),
    ('GTVT', ' giao thông vận tải '),
    ('KHCN', ' khoa học công nghệ '),
    ('TNMT', ' tài nguyên môi trường '),
    ('NHNNVN', ' ngân hàng nhà nước việt nam '),
    ('CHXHCN', ' cộng hòa xã hội chủ nghĩa '),
    ('NSƯT', ' nghệ sĩ ưu tú '),
    ('NSND', ' nghệ sĩ nhân dân '),
    ('BGD',' bộ giáo dục '),
    ('CLB', ' câu lạc bộ '),
    ('HTX', ' hợp tác xã '),
    ('KTX', ' kí túc xá '),
    ('HLV', ' huấn luyện viên '),
    ('BTV', ' biên tập viên '),
    ('CSGT', ' cảnh sát giao thông '),
    ('HCM', ' hồ chí minh '),
    ('HN', ' hà nội '),
    ('NXB' , ' nhà xuất bản '),
    ('BCĐ', ' ban chỉ đạo '),
    ('BCH', ' bộ chỉ huy '),
    ('UBND', ' ủy ban nhân dân '),
    ('HĐND', ' hội đồng nhân dân '),
    ('QĐND', ' quân đội nhân dân '),
    ('BCH', ' ban chấp hành '),
    ('THCS', ' trung học cơ sở '),
    ('THPT', ' trung học phổ thông '),
    ('LHQ', ' liên hợp quốc '),
    ('VNCH', ' việt nam cộng hòa '),
    ('VNDCCH', ' việt nam dân chủ cộng hòa '),
    ('QDND', ' quân đội nhân dân việt nam '),
    ('k/g', ' kính gửi '),
    ('đ/c',' địa chỉ '),
    ('v.v.', ', vân vân . '),
    (' kg ',' ki lô gam '),
    (' km ', ' ki lô mét '),
    ('BTC',' ban tổ chức '),
    ('TNHH',' trách nhiệm hữu hạn '),
    ('CTCP',' công ty cổ phần '),
    ('TTCP',' thủ tướng chính phủ '),
    ('TP', ' thành phố '),
    ('VN', ' việt nam '),
    ('ĐH', ' đại học '),
    ('CĐ', ' cao đẳng '),
    ('BV', ' bệnh viện '),
    ('TG ', ' thế giới '),
    ('TƯ ', ' trung ương ' ),
    ('TW', ' trung ương '),
    ('DN', ' doanh nghiệp '),
    ('CS', ' cảnh sát '),
    ('QĐ', ' quân đội '),
    ('KM', ' khuyến mại '),
    ('QG', ' quốc gia '),
    ('PV', ' phóng viên '),

# Foreign
    ('FIFA', ' phi pha '),
    ('WHO', ' đáp liu hát o '),
    ('WTO', ' đáp liu tê o '),
    ('UNESCO', ' diu nét cô '),
    ('APEC', ' a pếch '),
    ('ASEAN', ' a se an '),
    ('BBC', ' bi bi si '),
    ('UNICEF', ' diu ni sép '),
    ('UEFA', ' ue pha '),
    ('OPEC', ' o pếch '),
    ('FBI', ' ép bi ai '),
    ('CIA', ' si i a '),
    ('KFC', ' ca ép sê '),
    ('UEFA', ' oe pha '),
    ('USD', ' iu ét đê '),
    ('NATO', ' na tô '),


# Covid Topic  
    ('Covid',' cô vít '),
    ('COVID', ' cô vít '),
    ('PCR', ' pi si a '),
    ('virus',' vi rút '),

# Degree list
    ('Ths', ' thạc sĩ '),
    ('Ths.', ' thạc sĩ '),
    ('TS.', ' tiến sĩ '),
    ('TS', ' tiến sĩ '),
    ('PGS', ' phó giáo sư '),
    ('PGS.', ' phó giáo sư '),
    ('GS.', ' giáo sư '),
    ('GS', ' giáo sư '),

# Social media 
    ('Face Book', ' phây búc '),
    ('facebook', ' phây búc '),
    ('FB', ' phây búc '),
    ('Twitter', ' truýt tơ '),
    ('twitter', ' truýt tơ '),
    ('ZALO', ' da lô '),
    ('Zalo', ' da lô '),
    ('zalo', ' da lô '),
    ('Instagram', ' in sờ ta ram '),
    ('Youtube', ' diu túp '),
    ('youtube', ' diu túp '),
    ('Linkedin', ' linh kin '),
    ('LinkedIn', ' linh kin '),
]

comparision_symbols = [
    ('>=', ' lớn hơn hoặc bằng '),
    ('<=', ' nhỏ hơn hoặc bằng '),
    ('>', ' lớn hơn '),
    ('<', ' nhỏ hơn '),
    ('=', ' bằng '),
]


'''
Using dictionary because all tokens is 2 parts (number, unit)
Just need to replace unit 
'''
SI_units_to_vn = {
    'mg' : 'mi li gam ',
    'kg' : 'ki lô gam ',
    'Kg' : 'ki lô gam ',
    'g' : 'gam ',
    'ms' : 'mi li giây ',
    's' : 'giây ',
    'mm' : 'mi li mét ',
    'cm' : 'xăng ti mét ',
    'dm' : 'đề si mét ',
    'm2': 'mét vuông ',
    'm3': 'mét khối ',
    'km': 'ki lô mét ',
    'km2': 'ki lô mét vuông ',
    'Km': 'ki lô mét ',
    'm' : 'mét ',
    'ha': 'héc ta ',
    'mol': 'mon ',
    'mA': 'mi li am pe ',
    'A': 'am pe ',
    'mV': 'mi li vôn ',
    'kV': 'ki lô vôn ',
    'KV': 'ki lô vôn ',
    'V': 'vôn ',
    'ml': 'mi li lít ',
    'l': 'lít ',
    'L': 'lít ',
    'KHz': 'ki lô héc ',
    'khz': 'ki lô héc ',
    'hz': 'héc ',
    'Hz': 'héc ',
    'rad': 'ra đi an ',
    'Kwh' :'ki lô oắt giờ ',
    'kWh' : 'ki lô oắt giờ ',
    'W': 'oắt ',
    'h':'giờ ',
    '%':'phần trăm '

}