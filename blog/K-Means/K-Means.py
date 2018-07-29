#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""基于jaccard 距离的迭代K-Means算法实现
"""

#   一些功能函数
import os

def CreateDir(FilePath):
    if not os.path.exists(FilePath):  # 目录不存在时，创建目录
        os.mkdir(FilePath)


def WriteFileLine(FilePath, DataList, style):
    try:
        f = open(FilePath, style)
        for DataLine in DataList:
            f.write(DataLine)
        f.close()
    except Exception as e:
        print('Create File ERROR' + str(e))


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


import copy
import random as Inrandom
from numpy import random
import time

class KMeans:
    def __init__(self, tweets, k, MaxIterations):
        """初始参数，tweets为推文，数据类型为Dict，键：tweetID，值：分词后的tweet，以集合的形式保存
        k为聚类簇数，MaxIterations为最大迭代次数'"""
        self.tweets = tweets
        self.k = k
        self.MaxIterations = MaxIterations

        self.seeds = []#随机选取的初始均值向量的ID
        self.Clusters = {}#用户存放聚类结果，字典之中的每一个键对应一簇
        self.RevClusters = {}#反向索引，字典之中键为tweets向量ID，值为簇序号
        self.JaccardMatrix = {}#设置为矩阵，用于存储每一对向量的jaccard距离
        self.LenTwitter = len(tweets)#推文的长度

        #运行初始均值向量随机选取函数
        self.InitializeChooseSeeds()
        #运行初始化聚类函数
        self.InitializeClusters()
        #运行计算Jaccard距离矩阵函数，修改：由于增加了LoadJaccardMatrix矩阵，所以不在__init__中直接运行，
        if self.LenTwitter <= 1500:
            self.InitializeJaccardMatrix()

    def JaccardDistance(self, SetA, SetB):
        """计算Jaccard距离函数，SetA 和 SetB为两个集合"""
        try:
            return 1 - float(len(SetA.intersection(SetB))) / float(len(SetA.union(SetB)))
        except TypeError:
            print('Error, SetA or SetB is none.')

    def InitializeChooseSeeds(self):
        """kmeans算法，选取初始均值向量，利用sample函数，从tweets键中随机选取k个ID"""
        self.seeds = Inrandom.sample(list(self.tweets.keys()), self.k)

    def InitializeClusters(self):
        """对聚类进行初始化"""
        #对反向索引进行初始化，由于当前没有进行聚类，反向索引置为-1
        for ID in self.tweets:
            self.RevClusters[ID] = -1

        #对聚类簇字典进行初始化，初始化使用随机选取的初始均值向量
        for i in range(self.k):
            self.Clusters[i] = set([self.seeds[i]]) #将tweet的ID以集合形式存储起来，i为簇序号也是字典键
            self.RevClusters[self.seeds[i]] = i #初始均值向量对应的簇序号已经确定，对反向索引进行赋值

    def InitializeJaccardMatrix(self):
        """计算出每一对tweet的Jaccard距离,动态规划思想，以空间换时间
        数据量过大时，可能会发生memoryerror的错误
        """
        #利用两层循环进行每一对ID的匹配
        k = 0 #调试变量
        try:
            for ID1 in self.tweets:
                self.JaccardMatrix[ID1] = {}
                for ID2 in self.tweets:
                    if ID2 not in self.JaccardMatrix:
                        self.JaccardMatrix[ID2] = {}
                    Distance = self.JaccardDistance(self.tweets[ID1], self.tweets[ID2])#计算出jaccard距离
                    self.JaccardMatrix[ID1][ID2] = Distance#距离赋值
                    self.JaccardMatrix[ID2][ID1] = Distance
                    k += 1
        except MemoryError:
            print(k)

    def LoadJaccardMatrix(self, FilePath):
        """导入已经计算好的Jaccard矩阵
        数据格式为：ID1 | ID2 | Value
        """
        try:
            f = open(FilePath, 'r')
        except IOError:
            print("Error! The file don't exist")
            return
        while True:
            line = f.readline()
            if not line:
                break
            try:
                #读出当前行的ID1 ID2 Distance
                ID1 = line.split('|')[0]
                ID2 = line.split('|')[1]
                Distance = float(line.split('|')[2])
                #若不存在啊ID1 ID2等相关键，则进行创建
                if ID1 not in self.JaccardMatrix:
                    self.JaccardMatrix[ID1] = {}
                if ID2 not in self.JaccardMatrix:
                    self.JaccardMatrix[ID2] = {}
                self.JaccardMatrix[ID1][ID2] = Distance  # 距离赋值
                self.JaccardMatrix[ID2][ID1] = Distance
            except IndexError:
                continue
        f.close()

    def CalcNewClusters(self):
        """计算新的聚类"""
        #初始化
        NewClusters = {}#新的聚类
        NewRevCluster = {}#新的反向索引
        for i in range(self.k):
            NewClusters[i] = set()#初始化为空集

        #遍历tweets中每一个元素，通过之前的聚类簇，构造出新的聚类
        k = 0   #调试变量
        for ID1 in self.tweets:
            MinDist = float("inf")  #将最小距离初始化为无穷小，保证存在出口
            MinCluster = self.RevClusters[ID1]

            #遍历每一个簇，计算出对于元素ID具有最小的簇数
            for j in self.Clusters:
            #for j in SampleResult:
                Dist = 0
                Count = float(0)
                #遍历当前簇之中的所有元素，计算出ID与其他元素的Jaccard之和
                #计算当前ID与当前簇的距离
                for ID2 in self.Clusters[j]:
                    if self.LenTwitter <= 1500:
                        Dist += self.JaccardMatrix[ID1][ID2]
                    else:
                        Dist += 1 - \
                                float(len(self.tweets[ID1].intersection(self.tweets[ID2]))) \
                                / float(len(self.tweets[ID1].union(self.tweets[ID2])))  # 计算当前选定元素ID与该类之中其他元素的距离和
                    #Dist += self.jaccardMatrix[ID1][ID2]
                    Count += 1 #计算当前类里元素的数量
                    k += 1  #调试变量
                if Count > 0:#若之前遍历的簇不为空，则进行距离判定
                    AvgDist = Dist / Count
                    if MinDist > AvgDist: #如果当前最小距离小于当前元素与该类的距离，则修改最小距离
                        MinDist = AvgDist
                        MinCluster = j
            NewClusters[MinCluster].add(ID1)#将当前元素添加到具有最小距离的类中
            NewRevCluster[ID1] = MinCluster#添加反向索引
        return NewClusters, NewRevCluster#返回新的聚类结果

    def Converge(self):
        """聚类顶层函数"""
        #初始化运行赋值
        NewClusters, NewRevCluster = self.CalcNewClusters()
        self.Clusters = copy.deepcopy(NewClusters)
        self.RevClusters = copy.deepcopy(NewRevCluster)

        #开始进行迭代，直至收敛或达到最大迭代次数
        Interations = 1
        while Interations < self.MaxIterations:#循环出口条件，小于最大迭代次数
            NewClusters, NewRevCluster = self.CalcNewClusters()
            Interations += 1
            if self.RevClusters != NewRevCluster: #当最新的迭代结果与之前结果不一致时，对聚类结果进行更新
                self.Clusters = copy.deepcopy(NewClusters)
                self.RevClusters = copy.deepcopy(NewRevCluster)
            else:#若结果收敛，则循环结束，聚类完成
                print(Interations)
                return Interations
        print('Get the Max!')
        return self.MaxIterations + 1

    def OneClusterSSE(self, Cluster):
        """计算每一簇聚类之中的误差平方"""
        OneClusterSSE = 0
        Len = len(Cluster)
        for ID1 in Cluster:
            S = 0
            for ID2 in Cluster:
                if self.LenTwitter <= 1500:
                    S += self.JaccardMatrix[ID1][ID2]
                else:
                    S += self.JaccardDistance(self.tweets[ID1], self.tweets[ID2])
            S /= Len
            #S = S*S
            OneClusterSSE += S*S

        return OneClusterSSE

    def CalculateSSE(self):
        """用于计算误差平方和，Sum Of The Squared Errors, SSE"""
        SSE = 0 #误差平方和
        for Ci in self.Clusters:
            SSE += self.OneClusterSSE(self.Clusters[Ci])
        return SSE

    def CalculateMinValue(self, Cluster1, Cluster2):
        MinValue = float("inf")#表示值为无穷大
        for ID1 in Cluster1:
            for ID2 in Cluster2:
                if self.LenTwitter <= 1500:
                    Dist = self.JaccardMatrix[ID1][ID2]
                else:
                    Dist = self.JaccardDistance(self.tweets[ID1], self.tweets[ID2])
                if MinValue > Dist:
                    MinValue = Dist
        return Dist

    def CalculateDiam(self,Cluster):
        """
        计算聚类之中元素的最大距离
        :param Cluster: 输入聚类
        :return: 返回最大值
        """
        Max = float('-inf')#令初始最大值为无限小，保证存在出口
        for ID1 in Cluster:
            for ID2 in Cluster:
                if self.LenTwitter <= 1500:
                    dist = self.JaccardMatrix[ID1][ID2]
                else:
                    dist = self.JaccardDistance(self.tweets[ID1], self.tweets[ID2])
                if dist > Max:
                    Max = dist

        return Max


    def CalculateDI(self):
        """
        计算DI指数
        :return:
        """
        #先计算分子
        DMin = float("inf")  # 表示值为无穷大
        for i in self.Clusters:
            for j in self.Clusters:
                if self.Clusters[i] is self.Clusters[j]:
                    continue
                else:
                    dist = self.CalculateMinValue(self.Clusters[i], self.Clusters[j])
                    if dist < DMin:
                        DMin = dist

        #在计算分母
        DMax = float('-inf')#令初始最大值为无限小，保证存在出口
        for l in self.Clusters:
            dist = self.CalculateDiam(self.Clusters[l])
            if dist > DMax:
                DMax = dist

        return DMin / DMax

    def PrintCluster(self):
        for i in self.Clusters:
            print('\n\nCluster ' + str(i))
            for ID in self.Clusters[i]:#遍历簇中每一个ID以及ID对应的tweet
                print(str(ID) + ' | ' + ' '.join(self.tweets[ID]) + '\n')

    def PrintJaccardMatrix(self):
        for ID in self.tweets:
            for ID2 in self.tweets:
                print(ID, ID2, self.JaccardMatrix[ID][ID2])

    def SaveClusterFile(self, FilePath):
        """以文件的形式保存聚类结果，FilePath为文件路径"""
        #若目录不存在，则创建路径
        CreateDir(FilePath)
        #遍历每一个簇
        for i in self.Clusters:
            TempCache = []#设置缓冲，存储当前簇中所有tweets
            for ID in self.Clusters[i]:#遍历簇中每一个ID以及ID对应的tweet
                #TempCache.append(str(ID) + '|' + self.tweets[ID] + '\n')    #还需要修改了这一部分东西
                TempCache.append(str(ID) + '|' + ' '.join(self.tweets[ID]) + '\n')  # 还需要修改了这一部分东西
            WriteFileLine(FilePath + 'C' + str(i) + '.txt', TempCache, 'w')

    def SaveJaccardMatrix(self, FilePath):
        """以文件的形式保存Jaccard矩阵计算结果，便于下次计算加速"""
        TempCache = []#设置缓冲
        #遍历矩阵之中的每一个元素
        for ID1 in self.tweets:
            for ID2 in self.tweets:
                TempCache.append(str(ID1) + '|' + str(ID2) + '|' + str(self.JaccardMatrix[ID1][ID2]) + '\n')
        #写入文件
        try:
            WriteFileLine(FilePath + 'JaccardMatrix.txt', TempCache, 'w')
        except IOError:
            print("Error! The file fail to create!")

def main():
    tweets = ReadFile('ClusterTest.txt')
    k = 27 #设置k参数
    MaxIterations = 50 #设置最大迭代次数
    kmeans = KMeans(tweets, 27, MaxIterations)
    Iterations = kmeans.Converge()  #方法返回最大迭代次数
    kmeans.SaveClusterFile("ClusterResult/")
    SSE = kmeans.CalculateSSE() #计算SSE
    DI = kmeans.CalculateDI() #计算DI
    print("MaxIterations: " + str(MaxIterations) + "\n" + "SSE: " + str(SSE) + '\n' + "DI: " + str(DI))


if __name__ == "__main__":
    time_start = time.time()  # time.time()为1970.1.1到当前时间的毫秒数
    main()
    time_end = time.time()  # time.time()为1970.1.1到当前时间的毫秒数
    print("the K-Means algorithm time:")
    print (str((time_end - time_start) / 60) + 'min')