import requests
from bs4 import BeautifulSoup

# 目标网站的URL
url = 'https://www.yhdmhy.com/'

# 使用requests发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取网页中的特定信息，例如所有的链接
    links = soup.find_all('a')

    for link in links:
        print(link.get('href'))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
