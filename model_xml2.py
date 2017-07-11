#Created by yhwang on 2017/7/11.
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,"name",attrib={'errllod':"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
age.text = '33'
sex = ET.SubElement(name,"sex")
sex.text = '2'

#-----同上------


et = ET.ElementTree(new_xml)
et.write("test.xml",encoding='utf-8',xml_declaration=True)

#ET.dump(new_xml)