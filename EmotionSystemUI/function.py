#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os


def CreateCityDict(CityFileName):
    """返回城市列表"""
    f = open(CityFileName)
    CityList = []  # 定义列表
    while True:
        line = f.readline()
        if not line:
            break
        CityList.append(line.split('\t')[1])  # 读出城市，在第二个字段
    return CityList

def ModelList():
    """返回模型列表"""
    return ['MultinomialNB', 'LinearSVC', 'LogisticRegression', 'VotingClassifier']

def WriteFileLine(FilePath, DataList, style):
    try:
        f = open(FilePath, style)
        for DataLine in DataList:
            f.write(DataLine)
        f.close()
    except Exception as e:
        print('Create File ERROR' + str(e))

def CreateDir(FilePath):
    if not os.path.exists(FilePath):  # 目录不存在时，创建目录
        os.mkdir(FilePath)

def ReadFile(FilePath):
    """读取预处理文件，返回值为Dict"""
    try:
        f = open(FilePath)
    except IOError:
        print("Can't find the file")
        return
    tweets = {}
    while True:
        line = f.readline()
        if not line:
            break
        try:
            ID = line.split('|')[0]
            Text = line.split('|')[1].strip('\n')
            tweets[ID] = set(Text.strip(' ').split(' '))
        except IndexError:
            continue
    return tweets

def ReadFileInLDA(FilePath):
    """读取预处理文件，返回值为Dict"""
    try:
        f = open(FilePath)
    except IOError:
        print("Can't find the file")
        return
    tweets = ""
    while True:
        line = f.readline()
        if not line:
            break
        try:
            tweets += line.split('|')[1].strip('\n')
        except IndexError:
            continue
    return tweets

def ReadDocList(FilePath, k):
    DocLst = []
    for i in range(k):
        DocLst.append(ReadFileInLDA(FilePath + 'C' + str(i) + '.txt'))

    return DocLst

def GetWordNum(DocLst):
    DocSet = set()
    for i in DocLst:
        DocSet = DocSet.union(set(i.split(' ')))
    return DocSet

def ReadTable(FilePath):
    f = open(FilePath, 'r')
    Data = {}
    while True:
        line = f.readline()
        if not line:
            break
        Data[line.split(":")[0]] = line.split(":")[1]
    f.close()
    return Data

def GetKParam(filepath):
    f = open(filepath, 'r')
    line = f.readline()
    f.close()
    return int(line.split(' = ')[1])

def ReadData(FilePath, city):
    tweets = {}
    f = open(FilePath, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        tweets[line.split('|')[0]] = line.split('|')[1].strip().replace(city, '')

    return tweets