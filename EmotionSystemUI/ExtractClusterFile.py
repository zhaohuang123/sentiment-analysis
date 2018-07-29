#!/usr/bin/python
# -*- coding: UTF-8 -*-

import function

class Extract:
    """根据ID从源文件之中提取原始的推文数据"""
    def __init__(self):
        self.Twitter = {}
        self.Cluster = None

    def ReadTwitter(self, FilePath):
        f = open(FilePath, 'r')
        while True:
            try:
                line = f.readline()
            except:
                continue
            if not line:
                break
            self.Twitter[line.split('|')[0]] = line.strip()

    def ExtractTwitter(self, FilePath):
        Cluster = {}
        f = open(FilePath)
        while True:
            line = f.readline()
            if not line:
                break
            try:
                Cluster[line.split('|')[0]] = self.Twitter[line.split('|')[0]]
            except:
                continue
        self.Cluster = Cluster
        return Cluster

    def SaveExtractFile(self, FilePath):
        Str = ""
        for i in self.Cluster:
            Str += self.Cluster[i] + '\n'
        f = open(FilePath, 'w')
        f.write(Str)
        f.close()

def Ex():
    FilePath = 'Data/DataProcessing/Boston/'
    ex = Extract()
    ex.ReadTwitter(FilePath + 'FilterData.txt')
    function.CreateDir(FilePath + 'ClusterResult/')
    for i in range(27):
        path = FilePath + 'KMeans/k-27/C' + str(i) + '.txt'
        WritePath = FilePath + 'ClusterResult/C' + str(i) + '.txt'
        ex.ExtractTwitter(path)
        ex.SaveExtractFile(WritePath)

if __name__ == '__main__':
    Ex()