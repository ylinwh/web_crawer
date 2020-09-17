import os, re

store_dir = 'new_web_site'
prog = re.compile(r"据江苏省地震台网测定：(\d+)年(\d+)月(\d+)日(\d+)时(\d+)分，在(.+)[\(（]北纬([0-9.]+)度[,，]东经([0-9.]+)度[\)）]发生(M?[0-9.]+)级地震")
templete = "{}年{}月{}日{}时{}分, {}(北纬{}度, 东经{}度)发生{}级别地震。"
# prog = re.compile(r"据江苏省地震台网测定：(\d+)年(\d+)月(\d+)日(\d+)时(\d+)分，在(.+)\'>")
# 据江苏省地震台网测定：2020年06月27日19时09分，在江苏盐城市射阳县

final_result = ""

for idx in range(1, 11):
    with open(os.path.join(store_dir, f'new_{idx}_page.txt'), 'r', encoding="utf-8") as fd:
        total_text = fd.read()
        for line in total_text.split('</a></td>'):
            res = prog.search(line)
            if res:
                final_result += templete.format(*[res.group(ii) for ii in range(1, 10)]) + '\n'
    
with open('final_result.txt', 'wb') as fd:
    fd.write(final_result.encode('utf-8'))