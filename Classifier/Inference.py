# Python 3.6

import csv
import time
import itertools
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# data processing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split

# classification
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier  # not used in final version

# evaluation
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#Save
from sklearn.externals import joblib

import re

rule = re.compile(r'[^a-z\s]')

def ReadDataCSV(filepath):
    """
    读入函数，读入CSV文件，X为数据推文，y为情绪标签
    :param filepath:
    :return:
    """
    data = []
    label = []
    with open(filepath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            label.append(row[0])
            data.append(row[1:][0])
    return data, label

class Inference:
    def __init__(self):
        self.tweets = None    #推文数据，字典结构
        self.VecCount = None    #词频，后续直接导入
        self.TrainModel = None  #训练完成的模型
        self.VecTransform = None
        self.Predict = None

    def LoadTweets(self, tweets):
        self.tweets = tweets
        #初始化
        self.ClearTweets()
        self.tweets = self.RemoveNoEmotion()

    def __Clear__(self, tweets):
        tweets = re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+', '', tweets)
        tweets = re.sub(r'@(\w+)', '', tweets)
        tweets = re.sub(r'#(\w+)', '', tweets)
        tweets = tweets.replace('RT', '')
        tweets = tweets.lower()
        tweets = re.sub(r'[^a-z\s]', '', tweets)
        tweets = rule.sub('', tweets)
        return tweets

    def ClearTweets(self):
        """
        按照情绪划分的方式重新清洗数据
        :return:
        """
        for i in self.tweets:
            self.tweets[i] = self.__Clear__(self.tweets[i])

    def RemoveNoEmotion(self):
        tweets = {}
        sid = SentimentIntensityAnalyzer()
        for i in self.tweets:
            ss = sid.polarity_scores(self.tweets[i])
            if ss['neu'] < 0.7:
                tweets[i] = self.tweets[i]
        return tweets


    def LoadModel(self, FilePath):
        self.TrainModel = joblib.load(FilePath)

    def LoadVector(self, FilePath):
        self.VecCount = joblib.load(FilePath)

    def Transform(self):
        self.VecTransform = self.VecCount.transform(self.tweets.values())

    def infer(self):
        self.Predict = self.TrainModel.predict(self.VecTransform)
        return self.Predict

    def CalPredict(self):
        Emotion = {}
        for i in self.Predict:
            if i in Emotion.keys():
                Emotion[i] += 1
            else:
                Emotion[i] = 1
        return Emotion

    def ShowAndSaveResult(self, FilePath):
        Emotion = self.CalPredict()

        rects = plt.bar(range(len(Emotion.values())), Emotion.values(), color='gray')
        index = range(len(Emotion.values()))
        plt.xticks(index, Emotion.keys())
        plt.xlabel("Emotion")
        plt.ylabel("Number")  # Y轴标签
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
        plt.savefig(FilePath)
        plt.show()

class ExtractTopicFile:
    def __init__(self, CluserFilePath, K, LDAFilePath):
        self.CluserFilePath = CluserFilePath
        self.K = K
        self.LDAFilePath = LDAFilePath

        self.Text = {}

    def WriteFile(self, FilePath):
        for i in self.Text:
            f = open(FilePath + str(i) + '.txt', 'w')
            f.write(self.Text[i])
            f.close()

    def ReadFile(self, FilePath):
        text = ""
        f = open(FilePath, 'r')
        while True:
            try:
                line = f.readline()
            except:
                continue
            if not line:
                break
            text += line
        return text


    def __MaxP__(self, data):
        #还需要返回index值
        p = data.split(',')
        fp = []
        for i in p:
            fp.append(float(i))
        MaxValue = max(fp)
        return fp.index(MaxValue), MaxValue

    def Extract(self):
        fr = open(self.LDAFilePath, 'r')
        for i in range(self.K):
            line = fr.readline()
            line = line.strip()
            TopicIndex, MaxP = self.__MaxP__(line.split(':')[1])
            if MaxP > 0.98:
                if TopicIndex in self.Text.keys():
                    self.Text[TopicIndex] += self.ReadFile(self.CluserFilePath + 'C' + str(i) + '.txt')
                    #print(str(TopicIndex) + "topic : " + str(i))
                else:
                    self.Text[TopicIndex] = self.ReadFile(self.CluserFilePath + 'C' + str(i) + '.txt')
                    #print(str(TopicIndex) + "topic : " + str(i))

def test():
    """提取boston内容"""
    CluserFilePath = r'D:/GraduationDesign/PyCharmTest/DataAnalysis/Data/DataProcessing/Boston/KMeans/k-27/'
    K = 27
    LDAFilPath = r'D:\GraduationDesign\PyCharmTest\DataAnalysis\Data\DataProcessing\Boston\LDATrainResult\DocTopicDist.txt'
    et = ExtractTopicFile(CluserFilePath, K, LDAFilPath)
    et.Extract()
    et.WriteFile("analysisData/")

def ReadData(FilePath):
    tweets = {}
    f = open(FilePath, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        tweets[line.split('|')[0]] = line.split('|')[2].strip()

    return tweets

if __name__ == '__main__':
    #test()
    #FilePath = "D:\GraduationDesign\PyCharmTest\DataAnalysis\Data\DataProcessing\Boston\ClusterResult\C11.txt"


    infer = Inference()
    infer.LoadModel("result/VotingClassifier")
    infer.LoadVector("result/CountVectorizer")
    for i in range(4):
        FilePath = "analysisData/" + str(i) + '.txt'
        tweets = ReadData(FilePath)
        infer.LoadTweets(tweets)
        infer.Transform()
        infer.infer()
        infer.ShowAndSaveResult("analysisData/" + str(i) + ".png")
