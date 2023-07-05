import filecmp
import os
import re
import collections

#a = filecmp.cmp('Sample.jpg', 'Sample.tiff')
#if a is True:
    #os.remove('Sample.tiff')



# Получение списка файлов
#def fileList():
    #f_list = os.listdir('c:/temp/QA/Git/Home-Works-Completed/Python/Del_tiff')
    #print(f_list)
    #onlymames_list = []
    
    #for names in f_list:
        #splitting = f_list.split('.')
        
        
    

## Сравнение имен файлов в массиве
#def differenceSeaarch():
    


#fileList()

allFiles = os.listdir('c:/temp/QA/Git/Home-Works-Completed/Python/Del_tiff')

notDots_list = []
temp_list = []
TiffDelList = []

for i in range(len(allFiles)):
    cuttingAfterDots = (allFiles[i].split('.')).pop(0)
    notDots_list.append(cuttingAfterDots)

countering = collections.Counter(notDots_list)
#print(countering)

temp_list.extend(z for z in countering if countering[z] > 1)

for el in range(len(temp_list)):
    tiffing = temp_list[el] + '.tiff'
    TiffDelList.append(tiffing)


for item in TiffDelList:
    if item.endswith(".tiff"):
        os.remove(item)



    


    

