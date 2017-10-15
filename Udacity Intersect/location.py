import urllib3
import json
import os
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

urllib3.disable_warnings()
http = urllib3.PoolManager()
site = http.request('GET', 'https://geode.udacity.com/')
data = site.data.decode('utf-8')
parsed = json.loads(data)
# Write JSON file
path = "Udacity Intersect/Data/Location/"
if not os.path.exists(path):
    os.makedirs(path)
with io.open('Udacity Intersect/Data/Location/location_data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(parsed,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
