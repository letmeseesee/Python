#Created by yhwang on 2017/7/11.
import xml.etree.ElementTree as ET
tree = ET.parse("xml")
root = tree.getroot()
# print(root)
# print(root.tag)
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text,i.attrib)

print('-------写xml-------')

for node in root.iter('year'):
    #print(node.tag, node.text, node.attrib)
    new_year = int(node.text) +1
    node.text = str(new_year)
    node.set("update",'YES')



print('-------删除-------')
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank>50:
        print("------",rank)
        #root.remove(country)

tree.write('xml')

