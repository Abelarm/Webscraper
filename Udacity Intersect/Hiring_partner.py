import urllib3
import wget
import os
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
urllib3.disable_warnings()
site = http.request('GET', 'http://www.udacity.com/intersect')
data = site.data
soup = BeautifulSoup(data, 'html.parser')
hiring_partner_list = soup.find_all(
    'img', attrs={'class': 'hiring-partners--logo'})
path = "Udacity Intersect/Data/Hiring Partner/"
if not os.path.exists(path):
    os.makedirs(path)
for images in hiring_partner_list:
    url = images.get("src")
    file = wget.download(url, path)
    print(file)
