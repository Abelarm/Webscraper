import urllib3
import wget
import os
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
urllib3.disable_warnings()
site = http.request('GET', 'https://www.udacity.com/intersect/speakers')
data = site.data
soup = BeautifulSoup(data, 'html.parser')
speakers_list = soup.find_all('img', attrs={'class': 'photo mb-1'})
path = "Udacity Intersect/Data/Speakers/"
if not os.path.exists(path):
    os.makedirs(path)
for images in speakers_list:
    url = images.get("src")
    file = wget.download(url, path)
    print(file)
