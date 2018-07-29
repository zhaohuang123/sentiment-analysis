#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Classifier
import time
import os

#该程序主要是对原始的twitter数据进行过滤，去除掉中间重复的评论
#以及类似与I'm at 这种无意义的评论，在过滤之后，重建目录结构
#建立城市文件夹，用于分城市（地点）存放各类文件

def Filter(FilePath):
    """输入参数：未过滤文件的文件名
    返回值：过滤之后文件内容的List形式"""
    f = open(FilePath)
    ReviewList = []
    DataList = []
    while True:
        line = f.readline()
        if not line:
            break
        try:
            temp = (line.split('|')[2]).decode('utf-8')
            if temp in ReviewList or temp.find('I\'m at') != -1:
                continue
            else:
                DataList.append(line)
                ReviewList.append(temp)
        except Exception as e:
            print str(e) + '\t'
    return DataList

def CreateDir(FilePath):
    if not os.path.exists(FilePath):  # 目录不存在时，创建目录
        os.mkdir(FilePath)

def test():
    FilePathReadStr = 'Data/Classified/'
    FilePathWriteStr = 'Data/DataProcessing/'
    TextList = Filter(FilePathReadStr  + 'Boston.txt')  # 过滤
    CreateDir(FilePathWriteStr + 'Boston/')
    Classifier.WriteFileLine(FilePathWriteStr + 'Boston/' + 'FilterData.txt', TextList, 'w')  # 文件结构建立重新写


def main():
    CityFileNameStr = 'Data/City/City.txt'
    FilePathReadStr = 'Data/Classified/'
    FilePathWriteStr = 'Data/DataProcessing/'

    CityList = (Classifier.CreateCityDict(CityFileNameStr)).keys()  #创建城市列表

    for i in CityList:  #进行过滤和文件重新整理
        try:
            TextList = Filter(FilePathReadStr + i + '.txt') #过滤
            CreateDir(FilePathWriteStr + i + '/')
            Classifier.WriteFileLine(FilePathWriteStr + i + '/' + 'FilterData.txt', TextList, 'w')    #文件结构建立重新写入
        except Exception as e:
            print str(e) + '\t' + i


if __name__ == '__main__':
    try:
        time_start = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
        test()
        time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
        print str((time_end - time_start) / 60) + 'min'
    except Exception as e:
        print 'ERROR!' + str(e)