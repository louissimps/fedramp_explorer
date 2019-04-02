import os, json, re
from bs4 import BeautifulSoup
import urllib3

records = []

with open("./_data/controls.json", "r") as read_file:
    controls_data = json.load(read_file)

with open("./_data/enhancements.json", "r") as read_file:
    enhancements_data = json.load(read_file)


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True
 


#Loop over controls directory
for root, directories, filenames in os.walk('./_site/controls'):
    for filename in filenames: 
        if(filename.endswith('.html')):
            with open(os.path.join(root,filename),'r') as f:
                soup = BeautifulSoup(f.read(), features="lxml")
                dude = []
                ps = soup.find_all('p', class_='card-text')
                for para in ps:
                    dude.append(para.get_text())

                records.append({
                    "title": soup.title.get_text(),
                    "url": '/controls/' + filename,
                    "text": ' '.join(dude).strip()

                }
                )
                # data = soup.findAll(text=True)
                # result = filter(visible, data)
                # print list(result)
#Loop over the enhancements dir
for root, directories, filenames in os.walk('./_site/enhancements'):
    for filename in filenames: 
        if(filename.endswith('.html')):
            with open(os.path.join(root,filename),'r') as f:
                soup = BeautifulSoup(f.read(), features="lxml")
                dude = []
                for para in soup.find_all('p', class_='card-text'):
                    dude.append(para.get_text())
                records.append({
                    "title": soup.title.get_text(),
                    "url": '/enhancements/'+filename,
                    "text": ' '.join(dude).strip()

                }
                )
with open("./search.json", "w") as data_file:
    json.dump(records, data_file, indent=4)
