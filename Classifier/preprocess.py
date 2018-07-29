
#!/usr/bin/python
# -*- coding: UTF-8 -*-
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
    #修正类似与hurrrryyyyyy的字符串
    #Review = re.sub(rpt_regex, rpt_repl, Review)
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
    Review = re.sub(r'[^a-z\s]', '', Review)
    Review = rule.sub('', Review)
    #------------------------------加入，去掉Boston这个词
    #Review = Review.replace('boston', '')
    #分词
    # WordLst = nltk.word_tokenize(Review)
    # #去除停用词
    # WordLst = [w for w in WordLst if w not in stopwords.words('english')]
    #词干化
    # ps = PorterStemmer()
    # WordLst = [ps.stem(w) for w in WordLst]
    #词形还原
    # lemmatizer = WordNetLemmatizer()
    # WordLst = [lemmatizer.lemmatize(w) for w in WordLst]
    #return " ".join(WordLst)
    return Review

def DealSingleFile(ReadFilePath, WriteFilePath):
    fr = open(ReadFilePath, 'r')
    CacheData = []
    ErrorList = []

    text = ""
    k = 0
    f = open(WriteFilePath, 'w')
    while True:
        k += 1
        try:
            line = fr.readline()
            if not line:
                break
            ProData = PreProcessing(line.split(';')[1])
            if ProData == '':
                continue
            #CacheData.append(line.split('|')[0] + '|' + ProData + '\n')
            text += line.split(';')[0] + ';' + ProData + '\n'
            #fw.write(line.split('|')[0] + '|' + ProData + '\n')
        except Exception as e:
            pass
        if k > 200000:
            f.write(text)
            text = ""
            k = 0
    fr.close()


    f.write(text)
    f.close()
    #print ErrorList

def WriteFileLine(FilePath, DataList, style):
    try:
        f = open(FilePath, style)
        for DataLine in DataList:
            f.write(DataLine)
        f.close()
    except Exception as e:
        print ('Create File ERROR' + str(e))

def Process(text):
    text = text.replace("https", "")
    text = text.replace("http", "")
    text = text.replace("ftp", "")
    return text

def ReadProcess(ReadFilePath, WriteFilePath):
    fr = open(ReadFilePath, 'r')
    f = open(WriteFilePath, 'w')
    k = 0
    text = ""
    while True:
        k += 1
        try:
            line = fr.readline()
            if not line:
                break
            # if line == '\n':
            #     continue
            ProData = Process(line.split(';')[1])
            if ProData == '\n':
                continue
            # CacheData.append(line.split('|')[0] + '|' + ProData)
            text += line.split(';')[0] + ';' + ProData
            # fw.write(line.split('|')[0] + '|' + ProData + '\n')
        except Exception as e:
            pass
        if k > 200000:
            f.write(text)
            text = ""
            k = 0
    fr.close()
    f.write(text)
    f.close()

def test():
    """对Boston进行测试"""
    ReadFilePath = 'ProcessCorpus.csv'
    WriteFilePath = 'ProcessCorpus2.csv'
    time_start = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    ReadProcess(ReadFilePath, WriteFilePath)
    time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    print (str((time_end - time_start) / 60) + 'min')


if __name__ == "__main__":
    time_start = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    test()
    time_end = time.time();  # time.time()为1970.1.1到当前时间的毫秒数
    print (str((time_end - time_start) / 60) + 'min')