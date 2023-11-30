import os
dir_path = "reinfo_vi/data"
res = []
# Lấy tất cả tên file
for file_path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_path)):
        res.append(file_path)

list_text_files = list(filter(lambda x: "TextGrid" in x,res))

# Chỉ cắt 1000 điểm dữ liệu để sử dụng finetuining
list_text_files = list_text_files[:1000]

# Lấy text của audio từ file TextGrid
import textgrid
all_id = []
all_text = []
with open("reinfo_1000.txt", 'a+') as f:
    for text_file in list_text_files:
        tg = textgrid.TextGrid.fromFile(os.path.join(dir_path, text_file))
        text = ""
        for i in range(len(tg[0])):
            if tg[0][i].mark != '':
                text += tg[0][i].mark + " "
        file_name = text_file.replace(".TextGrid","")
        # all_id.append(file_name)
        # all_text.append(text)
        out_filepath = os.path.join(dir_path, file_name)
        print(out_filepath)
        print(text)
        # f.write(f"{out_filepath}|{text}\n")
        