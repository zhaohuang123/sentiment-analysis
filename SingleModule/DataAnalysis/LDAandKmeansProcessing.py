#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Classifier, InitialFilter
import nltk
import re
import time
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Repeating words like hurrrryyyyyy
rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE);
def rpt_repl(match):
	return match.group(1)+match.group(1)
rule = re.compile(r'[^a-z\s]')

def RmChinesePunctuation(Review):
    Review = Review.replace('’', ' ')
    Review = Review.replace('‘', ' ')
    Review = Review.replace('“', ' ')
    Review = Review.replace('”', ' ')
    Review = Review.replace('。', ' ')
    Review = Review.replace('，', ' ')
    Review = Review.replace('—', ' ')
    return Review


def PreProcessing(Review):
    """输入参数为当前推文的评论,string类型，对原始数据进行K-means和LDA分析的预处理，"""
    # 过滤包括以下步骤：
    # 去除其中的http https链接
    Review = re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+', '', Review)
    #去除 @字符串、#字符串
    Review = re.sub(r'@(\w+)', '', Review)
    Review = re.sub(r'#(\w+)', '', Review)
    #修正类似与hurrrryyyyyy的字符串
    Review = re.sub(rpt_regex, rpt_repl, Review)
    #去除字符串RT
    Review = Review.replace('RT', '')
    # #替换掉其中可能出现的中文标点符号
    # Review = RmChinesePunctuation(Review)
    # #去除省略号
    # Review = Review.replace('…', ' ')
    # #去除标点符号
    # for c in string.punctuation:
    #     Review = Review.replace(c, ' ')
    # 小写化
    Review = Review.lower()
    #由于推文之中有太多不规范的标点符号，因此，此处不再匹配标点符号，而是去除所有非英文字符
    #Review = re.sub(r'[^a-z\s]', '', Review)
    Review = rule.sub('', Review)
    #------------------------------加入，去掉Boston这个词
    Review = Review.replace('boston', '')
    #分词
    WordLst = nltk.word_tokenize(Review)
    #去除停用词
    WordLst = [w for w in WordLst if w not in stopwords.words('english')]
    #词干化
    # ps = PorterStemmer()
    # WordLst = [ps.stem(w) for w in WordLst]
    #词形还原
    lemmatizer = WordNetLemmatizer()
    WordLst = [lemmatizer.lemmatize(w) for w in WordLst]
    return " ".join(WordLst)

def DealSingleFile(ReadFilePath, WriteFilePath):
    fr = open(ReadFilePath, 'r')
    CacheData = []
    ErrorList = []

    while True:
        try:
            line = fr.readline()
            #line = line.encode('utf-8')
            if not line:
                break
            ProData = PreProcessing(line.split('|')[2])
            if ProData == '':
                continue
            CacheData.append(line.split('|')[0] + '|' + ProData + '\n')
            #fw.write(line.split('|')[0] + '|' + ProData + '\n')
        except Exception as e:
            pass
            ErrorList.append(str(e) + '\t' + line.split('|')[0])
            # print str(e) + '\t' + line.split('|')[0]
            # break
    fr.close()
    Classifier.WriteFileLine(WriteFilePath, CacheData, 'w')#写入到文件之中
    #print ErrorList

def test():
    """对Boston进行测试"""
    ReadFilePath = 'Data/DataProcessing/Boston/FilterData.txt'
    WriteFilePath = 'Data/DataProcessing/Boston/LKProcessingData.txt'
    time_start = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    DealSingleFile(ReadFilePath, WriteFilePath)
    time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    print str((time_end - time_start) / 60) + 'min'

def main():
    """对所有文件进行LDA和K-means的预处理"""
    CityFileNameStr = 'Data/City/City.txt'
    FilePath = 'Data/DataProcessing/'

    CityList = (Classifier.CreateCityDict(CityFileNameStr)).keys()  #创建城市列表
    for i in CityList:  #进行过滤和文件重新整理
        try:
            DealSingleFile(FilePath + str(i) + '/' + 'FilterData.txt',\
                           FilePath + str(i) + '/' + 'LKProcessingData.txt')
        except Exception as e:
            print str(e) + '\t' + i

if __name__ == "__main__":
    time_start = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    test()
    time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    print str((time_end - time_start) / 60) + 'min'