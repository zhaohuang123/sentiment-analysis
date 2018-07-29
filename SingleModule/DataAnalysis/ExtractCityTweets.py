#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import string

#读入函数，输入参数为文件指针，返回四元组list
def ReadFileLine(f):
    line = f.readline()
    if not line:
        return False
    try:
        ID = line.split("|")[0]
        user = line.split("|")[1]
        review = line.split("|")[2]
        time = line.split("|")[4]
    except Exception as e:
        print 'Read File ERROR' + str(e) + str(k)
        ID = str(k)
        user = 'Read File ERROR'
        review = 'no City'
        time = '000000'
    return ID, user, review, time


def WriteFileLine(FilePath, DataList, style):
    try:
        f = open(FilePath, style)
        for DataLine in DataList:
            f.write(DataLine)
        f.close()
    except Exception as e:
        print 'Create File ERROR' + str(e)


def Classifier(DataLine, CityDict):
    #review = DataLine[2]
    CityList = CityDict.keys()
    for City in CityList:
        if DataLine.find(City) != -1:
            # WriteFileLine('Finished/' + City + '.txt', DataLine, 'a')#在这一部分加buffer缓冲修改
            #strLine = DataLine[0] + '|' + DataLine[1] + '|' + DataLine[2] + '|' + DataLine[3] + '|' + '\n'
            CityDict[City].append(DataLine)  # 将当前符合的值写入字典的缓存之中
            if len(CityDict[City]) > 10000:  # 当缓冲值大于10000时，写入一次文件，该步骤的目的主要是利用缓存加快速度
                WriteFileLine('Data/Classified/' + City + '.txt', CityDict[City], 'a')  # 写入缓冲区的内容
                CityDict[City] = []  # 清空缓存区内容


def CreateCityDict(CityFileName):
    f = open(CityFileName)
    CityList = []  # 定义列表
    while True:
        line = f.readline()
        if not line:
            break
        CityList.append(line.split('\t')[1])  # 读出城市，在第二个字段
    CityDict = {}.fromkeys(CityList)  # 建立字典
    for City in CityList:
        CityDict[City] = []
    f.close()
    return CityDict


def FileClassifier(FileName, CityFileName):
    # 创建城市索引
    CityDict = CreateCityDict(CityFileName)
    global k  # 显示当前读取的行号
    k = 0
    f = open(FileName)  # 打开文件
    while True:  # 读取文件
        DataLine = f.readline()#直接读取一行数据
        if not DataLine:
            break
        Classifier(DataLine, CityDict)
        k += 1
    try:
        CityList = CityDict.keys()  # 写入缓冲区剩余内容
        for City in CityList:
            if len(CityDict[City]):
                WriteFileLine('Data/Classified/' + City + '.txt', CityDict[City], 'a')
    except Exception as e:
        print 'Write Last file ERROR!' + str(e)
    f.close()

def main():
    FileName = 'Data/twitter/Matched__English_Twitter.txt'
    CityFileName = 'Data/City/City.txt'
    try:
        time_start = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
        FileClassifier(FileName, CityFileName)
        time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
        print str((time_end - time_start) / 60) + 'min'
    except Exception as e:
        print 'ERROR!' + str(e)

if __name__ == "__main__":
    main()