import csv
import time
import itertools
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

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

emotion = ['fear','happiness','surprise', 'anger', 'sadness', 'disgust']

def ReadData(filepath):
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
            if row[0] not in emotion:
                continue
            label.append(row[0])
            data.append(row[1:][0])
    return data, label


def VectorizeData(data, FilePath):
    """
    词向量化，主要是词频统计和TF-IDF，其中需要对词频化结果进行保存
    :param data: 输入数据，List数据类型
    :param FilePath: 词频化结果保存路径
    :return: 返回词向量化结果
    """
    vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 2))
    DataFit = vectorizer.fit(data)
    joblib.dump(DataFit, FilePath + 'CountVectorizer')
    VectorizeCount = vectorizer.fit_transform(data)
    # from counts to term frequencies
    # (idf is unneccesary as we have only one document class)
    # TfIdf = TfidfTransformer(use_idf=False)
    # return TfIdf.fit_transform(VectorizeCount)
    return VectorizeCount


def print_emotion_ratio(label):
    """
    保存语料中情绪比率
    :param label: 情绪标签
    :return:
    """
    c = Counter(label)
    print("Label distribution in the data:")
    for emotion, frequency in c.most_common():
        print("\t{}: {} ({:.2f}%)".format(emotion, frequency, frequency / len(label) * 100))
    print()

def SaveEmotionRatio(label, FilePath):
    """
    保存语料中情绪比率
    :param label: 情绪标签
    :param FilePath: 保存路径
    :return:
    """
    c = Counter(label)
    Textstr = "Label distribution in the data:\n"
    for emotion, frequency in c.most_common():
        Textstr += "\t{}: {} ({:.2f}%)\n".format(emotion, frequency, frequency / len(label) * 100)
    f = open(FilePath, 'w')
    f.write(Textstr)
    f.close()

def essemble_classifier(clf_list):
    """This function collects the names of the classifiers and passes them to
    the Voting Classifier. For consistency reasons, it returns a list with a
    single element (the VotingClassifier)."""
    clf_names = []
    for clf in clf_list:
        clf_names.append(type(clf).__name__)
    # the VotingClassifier expects a list of tuples in the format of
    # (name_of_classifier, classifier)
    return [VotingClassifier(list(zip(clf_names, clf_list)))]


def plot_confusion_matrix(cm, classes, title='Confusion matrix', cmap=plt.cm.Greens):
    """打印混淆矩阵"""
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    # coloring (the higher the number, the more saturated the color)
    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.20)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def WriteFile(str, FilePath, style):
    f = open(FilePath, style)
    f.write(str)
    f.close()

def train_and_evaluate(DataTrain, LabelTrain, DataTest, LabelTest, classifiers, FilePath):
    """
    进行数据额训练和评估，并将训练模型保存下来
    :param DataTrain:训练数据
    :param LabelTrain: 训练标签
    :param DataTest: 测试数据
    :param LabelTest: 测试标签
    :param classifiers: 分类器，List
    :return:
    """
    timestr = ""
    for clf in classifiers:
        # 训练分类器
        start_time = time.time()
        clf.fit(DataTrain, LabelTrain)
        joblib.dump(clf, FilePath + str(type(clf).__name__))
        timestr += "Training of {} completed in {:.2f} seconds\n".format(type(clf).__name__, time.time() - start_time)

        # 测试分类器
        Result = ""
        Predict = clf.predict(DataTest)
        # print("Evaluation:\t\t\t  accuracy\n\t\t\t\t    {:6.2f}\n".format(clf.score(DataTest, LabelTest)))
        # print(classification_report(LabelTest, Predict, target_names=list(set(LabelTest))))
        Result += "Evaluation:\t\t\t  accuracy\n\t\t\t\t    {:6.2f}\n".format(clf.score(DataTest, LabelTest))
        Result += classification_report(LabelTest, Predict, target_names=list(set(LabelTest)))
        WriteFile(Result, FilePath + str(type(clf).__name__) + '.txt', 'w')
        # 计算混淆矩阵
        cnf_matrix = confusion_matrix(LabelTest, Predict)
        # 对混淆矩阵进行可视化操作
        plt.figure()
        plot_confusion_matrix(cnf_matrix, classes=set(LabelTest),
                              title='Confusion matrix ' + str(type(clf).__name__))
        plt.savefig(FilePath + str(type(clf).__name__) + '.png')

    WriteFile(timestr, FilePath + 'time.txt', 'a')

import os
def CreateDir(FilePath):
    if not os.path.exists(FilePath):  # 目录不存在时，创建目录
        os.mkdir(FilePath)

def VecData(X, FilePath):
    XVecCount = joblib.load(FilePath)
    XT = XVecCount.transform(X)
    return XT
    tfidf_transformer = TfidfTransformer(use_idf=False)
    return tfidf_transformer.fit_transform(XT)

def test():
    print("开始进行数据处理")

    FilePath = "result/"
    CreateDir(FilePath)
    # 读取文本语料信息
    data, label = ReadData('PreProcessCorpus.csv')
    SaveEmotionRatio(label, FilePath + 'EmotionRatio.txt')
    # 对文本进行向量化
    DataVec = VectorizeData(data, FilePath)
    #DataVec = VecData(data, "result/CountVectorizer")
    # 利用train_test_split函数进行训练集和测试集划分，
    # 按照label进行划分，保证每一种情绪都会出现在测试集和训练集中
    DataTrain, DataTest, LabelTrain, LabelTest = train_test_split(DataVec, label, test_size=0.25,
                                                                  random_state=42, stratify=label)
    SaveEmotionRatio(LabelTrain, FilePath + 'EmotionRatioTrain.txt')
    SaveEmotionRatio(LabelTest, FilePath + 'EmotionRatioTest.txt')
    print("数据处理完成")

    #print_emotion_ratio(label)
    #SaveEmotionRatio(label, FilePath)

    print("开始进行分类器的训练和评估")
    # 使用到了三种算法进行情绪分类
    clf_list = [MultinomialNB(),  # 朴素贝叶斯,naive_bayes
                LinearSVC(),  # SVM支持向量机
                LogisticRegression(random_state=42)  # 逻辑回归
                ]
    # 训练
    train_and_evaluate(DataTrain, LabelTrain, DataTest, LabelTest, clf_list, FilePath)
    # train and evaluate with an essemble method (using all of the classifiers)
    train_and_evaluate(DataTrain, LabelTrain, DataTest, LabelTest, essemble_classifier(clf_list), FilePath)
    print("Evalution complete. Plotting confusion matrices...")
    # show all figures
    plt.show()

def test2():
    clf = joblib.load("1526630651.3175988")
    X,y = ReadData("../data/test.csv")
    X_vec = VecData(X, 'vec')
    y_pre = clf.predict(X_vec)
    cnf_matrix = confusion_matrix(y, y_pre)
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=set(y), title='Confusion matrix ' + str(type(clf).__name__))
    plt.show()

def GetTestData():
    data, label = ReadData('PreProcessCorpus.csv')
    DataVec = VectorizeData(data, "")
    DataTrain, DataTest, LabelTrain, LabelTest = train_test_split(DataVec, label,
                                                                 test_size=0.05, random_state=42, stratify=label)
    Strtmp = ""
    for em, data in LabelTest, DataTest:
        Strtmp += em + ';' + data
    WriteFile(Strtmp, 'DataTes.csv', 'w')

if __name__ == "__main__":
    test()
