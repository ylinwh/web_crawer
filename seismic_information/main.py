import requests
import os, time

max_record = 438
record_range = list((range(1, max_record, 45))) + [max_record+1]

headers = {'Connection': 'keep-alive', 
   'Accept': 'application/xml, text/xml, */*; q=0.01', 
   'X-Requested-With': 'XMLHttpRequest', 
   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36', 
   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
   'Origin': 'http://www.js-seism.gov.cn', 
   'Referer':'http://www.js-seism.gov.cn/col/col981/index.html?uid=926&pageNum=1', 
   'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7', 
   'Cookie': 'JSESSIONID=3C2BF5F1EAEDCE181F1266AF9E6AD5FE'} 

data = {'col': '1',
 'appid': '1',
 'webid': '1',
 'path': '%2F',
 'columnid': '981',
 'sourceContentType': '1',
 'unitid': '926',
 'webname': '%E6%B1%9F%E8%8B%8F%E9%98%B2%E9%9C%87%E5%87%8F%E7%81%BE',
 'permissiontype': '0'
 }

request_url = 'http://www.js-seism.gov.cn/module/web/jpage/dataproxy.jsp?startrecord={}&endrecord={}&perpage=15'
# website: http://www.js-seism.gov.cn/col/col981/index.html

store_dire = 'new_web_site'
for idx in range(len(record_range)-1):
    r = requests.post(request_url.format(record_range[idx], record_range[idx+1]-1), headers=headers, data=data)
    translated = r.text.encode('utf-8')
    with open(os.path.join(store_dire, f'new_{idx+1}_page.txt'), 'wb') as fd:
        fd.write(translated)
    time.sleep(1)