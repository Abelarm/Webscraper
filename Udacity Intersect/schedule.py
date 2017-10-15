import urllib3
import wget
import os
import io
import json
from bs4 import BeautifulSoup

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

urllib3.disable_warnings()
http = urllib3.PoolManager()
site = http.request('GET','https://www.udacity.com/intersect/agenda')
data = site.data
soup = BeautifulSoup(data,'html.parser')
schedule_wrappers = soup.find_all('div',attrs={'class':'schedule__wrapper'})
time = []
events = []
meta = []

for schedule__wrapper in schedule_wrappers:
	schedule_list = schedule__wrapper.find_all('li')
	for schedule in schedule_list: 
		
		dictionary = {"title":[],"time":[],'location':None,"microlocation":[],"speakers":{"name":[],"organisation":[]}}
		dictionary['location'] = 'Computer History Museum, 1401 N Shoreline Blvd, Mountain View, CA 94043'
		dictionary['time'].append((schedule.find('div',attrs={'class':'time'})).text.split('\n')[1])
		if schedule__wrapper.find('div',attrs={'class':'schedule__session'}).find('h3').text!='Afternoon' :
			for speaker in schedule.find_all('p',attrs={'class':"large mb-0 gray-medium"}):
				name, *org = speaker.text.split(',')
				org = (',').join(org)
				dictionary['speakers']['name'].append(name)
				try:
					dictionary['speakers']['organisation'].append(org)
				except:
					dictionary['speakers']['organisation'].append('""')
			dictionary['microlocation'].append('Hahn Auditorium')
		else:
			for m_location in schedule.find_all('p',attrs={'class':"large mb-half gray-medium"}):
				dictionary['microlocation'].append(m_location.text)
		for title in schedule.find_all('h4'):
			dictionary['title'].append(title.text)

		meta.append(dictionary)

path = "Data/Agenda/"
if not os.path.exists(path):
	os.makedirs(path)

with io.open('Data/Agenda/session.json', 'w+', encoding='utf8') as outfile:
	str_ = json.dumps(meta, indent=2, sort_keys=False,
	                      separators=(',', ': '), ensure_ascii=False)
	outfile.write(to_unicode(str_))


	
