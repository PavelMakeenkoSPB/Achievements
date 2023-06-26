import os
import shutil
from sys import argv


# Извлечение шагов B-файла в отдельный файл
def StepsFromB():
    os.rename('B.side', 'B.txt')
    b = open("B.txt", 'r').read()
    StepsB = open("StepsB.txt", 'w')
    cutB = str(b[b.index('"tests"'):b.index('"suites":')])
    cutB = str(',' + cutB[10:])
    StepsB.write(cutB)
    StepsB.close()

# Извлечение шагов A-файла в отдельный файл
def HeadStepsFromA():
    os.rename('A.side', 'A.txt')
    a = open("A.txt", 'r').read()
    StepsA = open("StepsA.txt", 'w')
    cuttingA = str(a[:a.index('"suites"')])
    a = str(cuttingA[:-5])
    StepsA.write(a)
    StepsA.close()


# Извлечение нижней части документа A
def CutttingFlatA():
    a = open('A.txt', 'r').read()
    flat = open('Flat.txt', 'w')
    cutFlat = str('"' + a[a.index("suites"):])
    flat.write(cutFlat)
    flat.close()

#Слияние файла A и шагов из B
def StepsAStepsB():
    stA = open('StepsA.txt', 'a+')
    stB = open("StepsB.txt", 'r')
    stA.write(stB.read())
    stA.close()
    stB.close()
    
#Слияние суммарного файла шагов A и B с нижним куском файла А 
def StepsAFlat():
    stA = open('StepsA.txt', 'a+')
    flat = open("Flat.txt", 'r')
    stA.write(flat.read())
    stA.close()
    flat.close()
    
#Создание конечного файла Final    
def CopyToFinal():
    with open('StepsA.txt', 'r') as steps, open('Final.txt', 'a+') as final:
        for line in steps:
            final.write(line)

# Удаление лишних файлов
def DeleteTempFiles():
    os.remove('StepsA.txt')
    os.remove('StepsB.txt')
    os.remove('Flat.txt')
    os.remove('A.txt')
    os.remove('B.txt')    
    
#Переименование конечного файла Final
def RenameToSide():
    os.rename('Final.txt', 'Final.side')
    

    
def Main():
    StepsFromB()
    HeadStepsFromA()
    CutttingFlatA()
    StepsAStepsB()
    StepsAFlat()
    CopyToFinal()    
    DeleteTempFiles()
    RenameToSide()
    
Main()

