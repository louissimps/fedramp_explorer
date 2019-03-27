import os, json, re
from bs4 import BeautifulSoup

records = []

# with open("./_data/controls.json", "r") as read_file:
#     controls_data = json.load(read_file)

# with open("./_data/enhancements.json", "r") as read_file:
#     enhancements_data = json.load(read_file)


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
                records.append({
                    "title": soup.title.get_text(),
                    "url": '/controls/' + filename,
                    "text": soup.p.get_text()

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
                records.append({
                    "title": soup.title.get_text(),
                    "url": '/enhancements/'+filename,
                    "text": soup.p.get_text()

                }
                )
with open("./search.json", "w") as data_file:
    data_file.write('---\n')
    data_file.write('---\n')
    json.dump(records, data_file, indent=4)
