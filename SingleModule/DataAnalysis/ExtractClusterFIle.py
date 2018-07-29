#!/usr/bin/python
# -*- coding: UTF-8 -*-

import InitialFilter

class Extract:
    """根据ID从源文件之中提取原始的推文数据"""
    def __init__(self):
        self.Twitter = {}

    def ReadTwitter(self, FilePath):
        f = open(FilePath)
        while True:
            line = f.readline()
            if not line:
                break
            self.Twitter[line.split('|')[0]] = line

    def ExtractTwitter(self, FilePath):
        Cluster = {}
        f = open(FilePath)
        while True:
            line = f.readline()
            if not line:
                break
            Cluster[line.split('|')[0]] = self.Twitter[line.split('|')[0]]
        return Cluster

def SaveExtractFile(Cluster, FilePath):
    Str = ""
    for i in Cluster:
        Str += Cluster[i]
    f = open(FilePath, 'w')
    f.write(Str)
    f.close()

def Ex():
    FilePath = 'Data/DataProcessing/Boston/'
    ex = Extract()
    ex.ReadTwitter(FilePath + 'FilterData.txt')
    InitialFilter.CreateDir(FilePath + 'ClusterResult/')
    for i in range(27):
        path = FilePath + 'KMeans/k-27/C' + str(i) + '.txt'
        WritePath = FilePath + 'ClusterResult/C' + str(i) + '.txt'
        SaveExtractFile(ex.ExtractTwitter(path), WritePath)

if __name__ == '__main__':
    Ex()