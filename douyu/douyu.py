import jsonpath
import requests
import time

name = input('请输入图片关键字:')
# 发送请求
url = 'https://www.douyu.com/japi/search/api/searchShow?kw=' + name + '&page=1&pageSize=20'
# 模拟浏览器
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
# 解析数据
response = requests.get(url, headers=headers).json()

n = 0

# jsonpath需要位置，和目标
img_url_list = jsonpath.jsonpath(response, '$..roomSrc')

for img in img_url_list:
    # 延迟一下
    time.sleep(1)
    # 获取名字,因为有些分割有dy1所以用if
    if (img.split('/')[-1]) == 'dy1':

        file_name = img.split('/')[-2]
        print(file_name)
    else:
        file_name = img.split('/')[-1]
        print(file_name)

    # 再次发送请求,转换为二进制数

    data = requests.get(img, headers=headers).content

    # 保存数据
    # with open(file_name, 'wb')as f:
    #
    #     f.write(data)
    #     n = n + 1
    #     print('第%d张保存成功' % n)
