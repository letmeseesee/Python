#Create by yhwang on 2017/7/11.
import shutil
#拷贝文件
f_source = open('a.txt','w',encoding='utf-8')
f_target = open('b.txt','w',encoding='utf-8')
#shutil.copyfileobj(f_source,f_target)#copyfile可以直接输入文件地址而不用打开

#copymode拷贝权限
#shutil.copymode()
#shutil.rmtree()
#shutil.make_archive('archive1','zip','a.txt')

#可以调用zipfile来压缩
import zipfile
zip = zipfile.ZipFile('arch.zip','w')
zip.write('second.py')
zip.close()