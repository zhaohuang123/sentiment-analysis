#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""LDA算法实现，
"""

#  功能函数
import os

def CreateDir(FilePath):
    if not os.path.exists(FilePath):  # 目录不存在时，创建目录
        os.mkdir(FilePath)

import time
import matplotlib.pyplot as plt

#import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.externals import joblib

class LDATrain:
    def __init__(self, DocLst, NumTopics, MaxIter):
        """初始化，DocLst为输入的训练或测试文档"""
        self.DocLst = DocLst    #输入参数，List类型数据结构，List中每一个元素为一个文档
        self.NumTopics = NumTopics  #话题数目
        self.MaxIter = MaxIter  #最大迭代数据
        #self.MaxFeatures = MaxFeatures  #进行词频统计的最大数目

        #计算词频时需要用到的变量
        self.TFVectorizer = None
        self.TF = None  #词频统计结果
        #进行模型迭代时需要的变量
        self.LDAModelLst = []   #迭代产生的LDA模型列表
        self.PerplexityLst = [] #困惑度列表
        self.BestIndex = None
        self.BestLDAModel = None    #最佳LDA 模型
        self.BestLDAModelPerplexity = None  #最佳LDA模型的困惑度
        self.BestTopicNum = None    #最合适的主题数

    def LDACountVectorizer(self, MaxDf = 0.95, MinDf = 2):#这个值还有待确认
        """统计词频函数，调用CountVectorizer完成"""
        self.TFVectorizer = CountVectorizer(max_df = MaxDf,\
                                       min_df = MinDf,\
                                       #max_features = self.MaxFeatures
                                            )
        self.TF = self.TFVectorizer.fit_transform(self.DocLst)

    def LDASaveTF(self, TFModelPath):
        """保存词频"""
        joblib.dump(self.TF, TFModelPath)

    def LDALoadVectorizer(self, TFModelPath):
        """导入之前计算得到的词频统计结果"""
        self.TF = joblib.load(TFModelPath)

    def __LDATrain(self, NumTopic, MaxIter):
        """一次LDA训练，NumTopic为当前训练的主题数，MaxIter为最大迭代数"""
        LDAResult = LatentDirichletAllocation(n_components = NumTopic, \
                                              max_iter = MaxIter,\
                                              learning_method = 'batch',\
                                              # evaluate_every = 200, \
                                              # perp_tol = 0.01
                                              )
        # LDAResult.fit(self.TF)
        # TrainGamma = LDAResult.transform(self.TF)
        # TranPerplexity = LDAResult.perplexity(self.TF, TrainGamma)
        # return TrainGamma, TranPerplexity
        return LDAResult.fit(self.TF), LDAResult.perplexity(self.TF)

    def  IterationLDATrain(self):
        """迭代训练最佳的LDA模型，
        NumTopics为包括所有可能的主题数一个list，
        MaxIter为一次LDA训练的最大迭代数"""
        #开始进行迭代训练
        index = 0
        for NumTopic in self.NumTopics:
            lda, perplexity = self.__LDATrain(NumTopic, self.MaxIter)
            self.LDAModelLst.append(lda)
            self.PerplexityLst.append(perplexity)
            print(index)
            index += 1
        #保存最佳模型到
        BestIndex = self.PerplexityLst.index(min(self.PerplexityLst))#获取最佳模型的索引
        self.BestLDAModelPerplexity = min(self.PerplexityLst)
        self.BestTopicNum = self.NumTopics[BestIndex]
        self.BestLDAModel = self.LDAModelLst[BestIndex]
        self.BestIndex = BestIndex

    def TransformBestModel(self):
        for doc in self.TF:
            print(self.BestLDAModel.transform(doc))

    def __print_top_Words(self, model, FeatureNames, NumTopWords):
        for topic_idx, topic in enumerate(model.components_):
            print("Topic #%d:" % topic_idx)
            print(" ".join([FeatureNames[i]
                            for i in topic.argsort()[:-NumTopWords - 1:-1]]))

    def SaveTopicWords(self, NumTopWords, FilePath):
        """保存主题关键词，NumTopWord表示前多少个词"""
        TopicWords = ""
        FeatureNames = self.TFVectorizer.get_feature_names()
        for topic_idx, topic in enumerate(self.BestLDAModel.components_):
            TopicWords += "Topic #%d:" % topic_idx
            TopicWords += " ".join([FeatureNames[i]
                            for i in topic.argsort()[:-NumTopWords - 1:-1]]) +'\n'
        f = open(FilePath + 'TopicWords.txt', 'w')
        f.write(TopicWords)
        f.close()

    def PrintBestModelAndPerplexity(self, NumTopWords):
        """打印出最佳模型"""
        print("Best Number of Topic in LDA Model is ", self.BestTopicNum)
        print("the min Perplexity is", self.BestLDAModelPerplexity)
        print("Best Model is \n")
        self.__print_top_Words(self.BestLDAModel, self.TFVectorizer.get_feature_names(), NumTopWords)

    def SaveAllLDAMode(self, FilePath):
        """保存所有LDAModel"""
        #检查该目录是否存在，若不存在则创建
        CreateDir(FilePath)
        index = 0
        for m in self.LDAModelLst:
            joblib.dump(m, FilePath + 'LDA-model-' + str(index) + '.model')
            index += 1

    def SaveBestModel(self, FilePath):
        """保存最好的LDAmodel"""
        joblib.dump(self.BestLDAModel, FilePath + 'BestModel.model')

    def SavePerplexityCurveAndText(self, FilePath):
        """保存所有的困惑度（Perplexity），对应的曲线图像"""
        #检查该目录是否存在，若不存在则创建
        CreateDir(FilePath)
        # 保存perplexity结果
        with open(FilePath + 'Perplexity.txt', 'w') as f:
            PerplexityLstStr = ""
            index = 0
            for x in self.PerplexityLst:
                PerplexityLstStr += str(index) + '|' + str(self.NumTopics[index]) + '|' + str(x) + '\n'
                index += 1
            f.write(PerplexityLstStr)
        #绘制曲线并保存
        plt.close('all')
        Figure = plt.figure()
        ax = Figure.add_subplot(1, 1, 1)
        ax.plot(self.NumTopics, self.PerplexityLst)
        ax.set_xlabel("# of topics")
        ax.set_ylabel("Approximate Perplexity")
        plt.grid(True)
        plt.savefig(FilePath + 'PerplexityTrend.png')
        #plt.show()

    def PrintDocTopicDist(self):
        """打印出文档关于主题的矩阵，每一行表示文档，列表示是当前主题概率"""
        doc_topic_dist = self.BestLDAModel.transform(self.TF)
        for idx, dist in enumerate(doc_topic_dist):
            # 注意：由于sklearn LDA函数限制，此函数中输出的topic_word矩阵未normalize
            dist = [str(x) for x in dist]
            print(str(idx + 1) + ',')
            print(','.join(dist) + '\n')

    def SaveDocTopicDist(self, FilePath):
        """保存出文档关于主题的矩阵，每一行表示文档，列表示是当前主题概率"""
        doc_topic_dist = self.BestLDAModel.transform(self.TF)
        DocTopic = ''
        for idx, dist in enumerate(doc_topic_dist):
            # 注意：由于sklearn LDA函数限制，此函数中输出的topic_word矩阵未normalize
            dist = [str(x) for x in dist]
            DocTopic += 'Document ' + str(idx + 1) + ':' +','.join(dist) + '\n'
            # print str(idx + 1) + ','
            # print ','.join(dist) + '\n'
        f = open(FilePath + 'DocTopicDist.txt', 'w')
        f.write(DocTopic)
        f.close()

class LDATest:
    def __init__(self, DocLst, MaxFeatures):
        """初始化，DocLst为输入的训练或测试文档"""
        self.DocLst = DocLst    #输入参数，List类型数据结构，List中每一个元素为一个文档
        self.MaxFeatures = MaxFeatures
        self.odel = None
        self.TFVectorizer = None
        self.TF = None

        #运行词频统计函数
        self.LDACountVectorizer()

    def LDACountVectorizer(self, MaxDf = 0.95, MinDf = 2):#这个值还有待确认
        """统计词频函数，调用CountVectorizer完成"""
        self.TFVectorizer = CountVectorizer(max_df = MaxDf,\
                                       min_df = MinDf,\
                                       max_features = self.MaxFeatures)
        self.TF = self.TFVectorizer.fit_transform(self.DocLst)

    def LoadModel(self, FilePath):
        """导入模型"""
        self.Model = joblib.load(FilePath)

    def PrintDocTopicDist(self):
        """打印出文档关于主题的矩阵，每一行表示文档，列表示是当前主题概率"""
        doc_topic_dist = self.Model.transform(self.TF)
        for idx, dist in enumerate(doc_topic_dist):
            # 注意：由于sklearn LDA函数限制，此函数中输出的topic_word矩阵未normalize
            dist = [str(x) for x in dist]
            print(str(idx + 1) + ',')
            print(','.join(dist) + '\n')

    def SaveDocTopicDist(self, FilePath):
        doc_topic_dist = self.Model.transform(self.TF)
        DocTopic = ''
        for idx, dist in enumerate(doc_topic_dist):
            # 注意：由于sklearn LDA函数限制，此函数中输出的topic_word矩阵未normalize
            dist = [str(x) for x in dist]
            DocTopic += 'Document ' + str(idx + 1) + ':' +','.join(dist) + '\n'
            # print str(idx + 1) + ','
            # print ','.join(dist) + '\n'
        f = open(FilePath + 'DocTopicDist.txt', 'w')
        f.write(DocTopic)
        f.close()

    def PrintTopicWords(self, NumTopWords):
        FeatureNames = self.TFVectorizer.get_feature_names()
        for topic_idx, topic in enumerate(self.Model.components_):
            print("Topic #%d:" % topic_idx)
            print(" ".join([FeatureNames[i]
                            for i in topic.argsort()[:-NumTopWords - 1:-1]]))

    def SaveTopicWords(self, NumTopWords, FilePath):
        """保存主题关键词，NumTopWord表示前多少个词"""
        TopicWords = ""
        FeatureNames = self.TFVectorizer.get_feature_names()
        for topic_idx, topic in enumerate(self.Model.components_):
            TopicWords += "Topic #%d:" % topic_idx
            TopicWords += " ".join([FeatureNames[i]
                            for i in topic.argsort()[:-NumTopWords - 1:-1]]) +'\n'
        f = open(FilePath + 'TopicWords.txt', 'w')
        f.write(TopicWords)
        f.close()


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

def TestTrain():
    DocLst = ReadDocList('ClusterResult/', 27)
    n_topics = range(1, 27, 1)  #根据k决定
    MaxIter = 8000
    n_top_words = 15

    lda = LDATrain(DocLst, n_topics, MaxIter)
    lda.LDACountVectorizer()
    lda.IterationLDATrain()
    lda.PrintBestModelAndPerplexity(n_top_words)
    CreateDir('LDATrainResult/')
    lda.SaveTopicWords(n_top_words, 'LDATrainResult/')
    lda.PrintDocTopicDist()
    lda.SaveDocTopicDist('LDATrainResult/')
    lda.SaveAllLDAMode('LDATrainResult/')
    lda.SaveBestModel('LDATrainResult/')
    lda.SavePerplexityCurveAndText('LDATrainResult/')
    # lda.PrintDocTopicDist()

    # TFVectorizer = CountVectorizer(max_df = 0.95, min_df = 2, max_features = 2500)
    # tf = TFVectorizer.fit_transform(DocLst)
    # print tf

def TestLDATesy():
    FilePath = 'Data/DataProcessing/Boston/'
    DocLst = ReadDocList(FilePath + 'KMeans/k-7/', 7)
    n_top_words = 15
    MaxFeatures = 2500

    lda = LDATest(DocLst, MaxFeatures)
    lda.LoadModel(FilePath + 'LDATrainResult/BestModel.model')
    CreateDir(FilePath + 'LDATest/')
    lda.SaveDocTopicDist(FilePath + 'LDATest/')
    lda.SaveTopicWords(n_top_words, FilePath + 'LDATest/')

if __name__ == "__main__":
    time_start = time.time()  # time.time()为1970.1.1到当前时间的毫秒数
    TestTrain()
    time_end = time.time()  # time.time()为1970.1.1到当前时间的毫秒数
    print("the Iteration LDA Training time:")
    print(str((time_end - time_start) / 60) + 'min')