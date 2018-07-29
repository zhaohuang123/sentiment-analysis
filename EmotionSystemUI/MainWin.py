# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#导入库
import function
import IterationKMeans
import LDAModel
import EmotionInference
import ExtractClusterFile

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 851, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.Cluster = QtWidgets.QWidget()
        self.Cluster.setObjectName("Cluster")
        self.label = QtWidgets.QLabel(self.Cluster)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label.setObjectName("label")
        self.graphicsViewClusterDI = QtWidgets.QGraphicsView(self.Cluster)
        self.graphicsViewClusterDI.setGeometry(QtCore.QRect(10, 40, 410, 310))
        self.graphicsViewClusterDI.setObjectName("graphicsViewClusterDI")
        self.label_5 = QtWidgets.QLabel(self.Cluster)
        self.label_5.setGeometry(QtCore.QRect(430, 10, 131, 31))
        self.label_5.setObjectName("label_5")
        self.graphicsViewClusterSSE = QtWidgets.QGraphicsView(self.Cluster)
        self.graphicsViewClusterSSE.setGeometry(QtCore.QRect(430, 40, 410, 310))
        self.graphicsViewClusterSSE.setObjectName("graphicsViewClusterSSE")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.Cluster)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 390, 431, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditSatrt = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEditSatrt.setObjectName("lineEditSatrt")
        self.horizontalLayout_4.addWidget(self.lineEditSatrt)
        self.lineEditEnd = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEditEnd.setObjectName("lineEditEnd")
        self.horizontalLayout_4.addWidget(self.lineEditEnd)
        self.lineEditInterval = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEditInterval.setObjectName("lineEditInterval")
        self.horizontalLayout_4.addWidget(self.lineEditInterval)
        self.pushButtonLoad = QtWidgets.QPushButton(self.Cluster)
        self.pushButtonLoad.setGeometry(QtCore.QRect(470, 390, 180, 41))
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.pushButtonAnalysis = QtWidgets.QPushButton(self.Cluster)
        self.pushButtonAnalysis.setGeometry(QtCore.QRect(660, 390, 180, 41))
        self.pushButtonAnalysis.setObjectName("pushButtonAnalysis")
        self.label_11 = QtWidgets.QLabel(self.Cluster)
        self.label_11.setGeometry(QtCore.QRect(10, 370, 61, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Cluster)
        self.label_12.setGeometry(QtCore.QRect(160, 370, 61, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Cluster)
        self.label_13.setGeometry(QtCore.QRect(300, 370, 61, 21))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.Cluster, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEditKParamenter = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditKParamenter.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEditKParamenter.setObjectName("lineEditKParamenter")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 161, 31))
        self.label_4.setObjectName("label_4")
        self.pushButtonLDA = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonLDA.setGeometry(QtCore.QRect(230, 20, 111, 23))
        self.pushButtonLDA.setObjectName("pushButtonLDA")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 54, 21))
        self.label_3.setObjectName("label_3")
        self.graphicsViewLDAPerplexity = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsViewLDAPerplexity.setGeometry(QtCore.QRect(20, 80, 410, 310))
        self.graphicsViewLDAPerplexity.setObjectName("graphicsViewLDAPerplexity")
        self.tableWidgetTopicWord = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetTopicWord.setGeometry(QtCore.QRect(460, 80, 370, 160))
        self.tableWidgetTopicWord.setObjectName("tableWidgetTopicWord")
        self.tableWidgetTopicWord.setColumnCount(0)
        self.tableWidgetTopicWord.setRowCount(0)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(460, 40, 161, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(460, 250, 161, 31))
        self.label_7.setObjectName("label_7")
        self.tableWidgetDocTopic = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetDocTopic.setGeometry(QtCore.QRect(460, 280, 370, 160))
        self.tableWidgetDocTopic.setObjectName("tableWidgetDocTopic")
        self.tableWidgetDocTopic.setColumnCount(0)
        self.tableWidgetDocTopic.setRowCount(0)
        self.pushButtonLDALoad = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonLDALoad.setGeometry(QtCore.QRect(370, 20, 111, 23))
        self.pushButtonLDALoad.setObjectName("pushButtonLDALoad")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 371, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.lineEditTopicNum = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEditTopicNum.setObjectName("lineEditTopicNum")
        self.horizontalLayout_2.addWidget(self.lineEditTopicNum)
        self.pushButtonEmotionExtract = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonEmotionExtract.setObjectName("pushButtonEmotionExtract")
        self.horizontalLayout_2.addWidget(self.pushButtonEmotionExtract)
        self.graphicsViewEmotionExtract = QtWidgets.QGraphicsView(self.tab)
        self.graphicsViewEmotionExtract.setGeometry(QtCore.QRect(140, 80, 480, 360))
        self.graphicsViewEmotionExtract.setObjectName("graphicsViewEmotionExtract")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(500, 10, 331, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.comboBoxModel = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBoxModel.setToolTipDuration(-1)
        self.comboBoxModel.setObjectName("comboBoxModel")
        self.horizontalLayout_3.addWidget(self.comboBoxModel)
        self.pushButtonLoadModel = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonLoadModel.setObjectName("pushButtonLoadModel")
        self.horizontalLayout_3.addWidget(self.pushButtonLoadModel)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 121, 41))
        self.label_10.setObjectName("label_10")
        self.pushButtonFileExtract = QtWidgets.QPushButton(self.tab)
        self.pushButtonFileExtract.setGeometry(QtCore.QRect(384, 30, 91, 23))
        self.pushButtonFileExtract.setObjectName("pushButtonFileExtract")
        self.lineEditCluster = QtWidgets.QLineEdit(self.tab)
        self.lineEditCluster.setGeometry(QtCore.QRect(720, 160, 113, 20))
        self.lineEditCluster.setObjectName("lineEditCluster")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(640, 160, 81, 21))
        self.label_14.setObjectName("label_14")
        self.pushButtonEmotionExtract2 = QtWidgets.QPushButton(self.tab)
        self.pushButtonEmotionExtract2.setGeometry(QtCore.QRect(720, 200, 111, 21))
        self.pushButtonEmotionExtract2.setObjectName("pushButtonEmotionExtract2")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(643, 130, 61, 21))
        self.label_15.setObjectName("label_15")
        self.lineEditKParamenter_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEditKParamenter_2.setGeometry(QtCore.QRect(720, 130, 113, 20))
        self.lineEditKParamenter_2.setObjectName("lineEditKParamenter_2")
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 470, 431, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBoxCItyList = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBoxCItyList.setObjectName("comboBoxCItyList")
        self.horizontalLayout.addWidget(self.comboBoxCItyList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBoxModel.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 调用函数
        try:
            self.SetComBox()  # 设置两个ComBox值
            # 聚类
            self.pushButtonLoad.clicked.connect(self.LoadFunction)  # 设置Load槽
            self.pushButtonAnalysis.clicked.connect(self.AnalysisFunction)  # 设置分析槽
            # LDA主题事件分析
            self.pushButtonLDA.clicked.connect(self.LDADetection)  # 设置LDA检测槽
            self.pushButtonLDALoad.clicked.connect(self.LDALoad)  # 设置LDA导入槽
            # 情绪分析
            self.infer = EmotionInference.Inference()
            self.pushButtonLoadModel.clicked.connect(self.ModelLoad)  # 分类器模型导入槽
            self.pushButtonFileExtract.clicked.connect(self.ExtarctFile)  # 文件提取槽
            self.pushButtonEmotionExtract.clicked.connect(self.EmotionExtract)  # 情绪分析槽
            self.pushButtonEmotionExtract2.clicked.connect(self.EmotionExtractSingle)  # 单个聚类文件情绪分析槽
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Critical", str(e))

    def SetComBox(self):
        """设置combox，包括城市ComBox和模型ComBox"""
        # 设置城市ComBox
        filename = 'Data/City.txt'
        CityList = function.CreateCityDict(filename)
        for i in CityList:
            self.comboBoxCItyList.addItem(i)
        # 设置模型索引
        ModelList = function.ModelList()
        for i in ModelList:
            self.comboBoxModel.addItem(i)

    def LoadFunction(self):
        """
        触发Load按钮时的槽函数
        函数功能导入两张图片到框中
        """
        city = self.comboBoxCItyList.currentText()
        filepath = 'Data/DataProcessing/' + city + '/KMeans/'
        # 设置DI
        pngDI = QtGui.QPixmap(filepath + 'DI.png')
        pngDI = pngDI.scaled(400, 300)
        sceneDI = QtWidgets.QGraphicsScene()
        sceneDI.addItem(QtWidgets.QGraphicsPixmapItem(pngDI))
        self.graphicsViewClusterDI.setScene(sceneDI)
        # 设置SSE
        pngSSE = QtGui.QPixmap(filepath + 'SSE.png')
        pngSSE = pngSSE.scaled(400, 300)
        sceneSSE = QtWidgets.QGraphicsScene()
        sceneSSE.addItem(QtWidgets.QGraphicsPixmapItem(pngSSE))
        self.graphicsViewClusterSSE.setScene(sceneSSE)

        QtWidgets.QMessageBox.about(self.centralwidget, str("K-Means"), "Load Success!")

    def AnalysisFunction(self):
        """
        聚类分析函数
        :return:
        """
        # 获取各项参数
        city = self.comboBoxCItyList.currentText()
        filepath = 'Data/DataProcessing/' + city + '/'
        tweets = function.ReadFile(filepath + 'LKProcessingData.txt')
        startNum = int(self.lineEditSatrt.text())
        EndNum = int(self.lineEditEnd.text())
        IntervalNum = int(self.lineEditInterval.text())
        k = range(startNum, EndNum, IntervalNum)

        kIter = IterationKMeans.InteractionKMeans(tweets, k, 50, filepath + 'KMeans/')
        kIter.Interaction()
        self.LoadFunction()

        QtWidgets.QMessageBox.about(self.centralwidget, str("K-Means"), "Analysis Success!")

    def LDADetection(self):
        """
        进行关于LDA的分析
        :return:
        """
        # 获取各项参数
        city = self.comboBoxCItyList.currentText()
        filepath = 'Data/DataProcessing/' + city + '/'
        kparam = self.lineEditKParamenter.text()
        # 设置各项参数
        DocLst = function.ReadDocList(filepath + 'KMeans/k-' + kparam + '/', int(kparam))
        DocSet = function.GetWordNum(DocLst)
        n_topics = range(1, int(kparam), 1)  # 根据k决定
        MaxIter = 8000
        n_top_words = 15
        MaxFeatures = len(DocSet)

        # 主题分析
        lda = LDAModel.LDATrain \
            (DocLst, n_topics, MaxIter, MaxFeatures)  # 创建对象
        lda.LDACountVectorizer()
        lda.IterationLDATrain()
        function.CreateDir(filepath + 'LDATrainResult/')
        lda.SaveTopicWords(n_top_words, filepath + 'LDATrainResult/')
        lda.SaveDocTopicDist(filepath + 'LDATrainResult/')
        lda.SaveBestModel(filepath + 'LDATrainResult/')
        lda.SavePerplexityCurveAndText(filepath + 'LDATrainResult/')
        lda.SaveConfigFile(filepath + 'LDATrainResult/')

        # 内容导入
        self.LDALoad()
        # 原始数据提取---不再做原始数据提取了
        # ex = ExtractClusterFile.Extract()
        # ex.ReadTwitter(filepath +  'FilterData.txt')
        # function.CreateDir(filepath + 'ClusterResult/')
        # for i in range(int(kparam)):
        #     path = filepath + 'KMeans/k-' + kparam + '/C' + str(i) + '.txt'
        #     WritePath = filepath + 'ClusterResult/C' + str(i) + '.txt'
        #     ex.SaveExtractFile(WritePath)

        QtWidgets.QMessageBox.about(self.centralwidget, str("LDA"), "LDA Detection Success!")

    def LDALoad(self):
        # 图片导入
        city = self.comboBoxCItyList.currentText()
        filepath = 'Data/DataProcessing/' + city + '/'
        pngPerplex = QtGui.QPixmap(filepath + 'LDATrainResult/PerplexityTrend.png')
        pngPerplex = pngPerplex.scaled(400, 300)
        scenePerplex = QtWidgets.QGraphicsScene()
        scenePerplex.addItem(QtWidgets.QGraphicsPixmapItem(pngPerplex))
        self.graphicsViewLDAPerplexity.setScene(scenePerplex)
        # 主题关键词导入
        TopicWord = function.ReadTable(filepath + 'LDATrainResult/TopicWords.txt')
        self.tableWidgetTopicWord.setColumnCount(2)
        self.tableWidgetTopicWord.setRowCount(len(TopicWord))
        horizontalHeader = ["Topic #", "KeyWords"]
        self.tableWidgetTopicWord.setHorizontalHeaderLabels(horizontalHeader)
        self.tableWidgetTopicWord.setColumnWidth(0, 70)
        self.tableWidgetTopicWord.setColumnWidth(1, 300)
        Rowindex = 0
        for i in TopicWord:
            self.tableWidgetTopicWord.setItem(Rowindex, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidgetTopicWord.setItem(Rowindex, 1, QtWidgets.QTableWidgetItem(TopicWord[i]))
            Rowindex += 1
        # 文档主题概率矩阵的导入
        DocTopic = function.ReadTable(filepath + 'LDATrainResult/DocTopicDist.txt')
        self.tableWidgetDocTopic.setColumnCount(2)
        self.tableWidgetDocTopic.setRowCount(len(DocTopic))
        horizontalHeader = ["Document #", " Probability"]
        self.tableWidgetDocTopic.setHorizontalHeaderLabels(horizontalHeader)
        self.tableWidgetDocTopic.setColumnWidth(0, 70)
        self.tableWidgetDocTopic.setColumnWidth(1, 300)
        Rowindex = 0
        for i in DocTopic:
            self.tableWidgetDocTopic.setItem(Rowindex, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidgetDocTopic.setItem(Rowindex, 1, QtWidgets.QTableWidgetItem(DocTopic[i]))
            Rowindex += 1

        QtWidgets.QMessageBox.about(self.centralwidget, str("LDA"), "LDA Load Success!")

    def ModelLoad(self):
        """导入训练好的词频模型和分类器模型"""
        self.infer.LoadVector("Data/model/CountVectorizer")  # 导入词频模型
        classifer = self.comboBoxModel.currentText()  # 获取当前选择模型
        self.infer.LoadModel("Data/model/" + classifer)  # 导入分类器模型

        QtWidgets.QMessageBox.about(self.centralwidget, str("Emotion"), classifer + "Model Load Success!")

    def EmotionExtract(self):
        """进行情绪分析"""
        # 参数信息获取
        city = self.comboBoxCItyList.currentText()
        filepath = 'Data/DataProcessing/' + city + '/'
        TopicNo = self.lineEditTopicNum.text()

        # 主题相关文件提取
        # self.ExtarctFile()

        # 情绪分析
        tweets = function.ReadData(filepath + "analysisData/" + str(TopicNo) + '.txt', city)
        self.infer.LoadTweets(tweets)
        self.infer.Transform()
        self.infer.infer()
        self.infer.ShowAndSaveResult(filepath + "analysisData/" + str(TopicNo) + ".png")

        # 导入结果
        pngResult = QtGui.QPixmap(filepath + "analysisData/" + str(TopicNo) + ".png")
        pngResult = pngResult.scaled(480, 360)
        sceneResult = QtWidgets.QGraphicsScene()
        sceneResult.addItem(QtWidgets.QGraphicsPixmapItem(pngResult))
        self.graphicsViewEmotionExtract.setScene(sceneResult)

        QtWidgets.QMessageBox.about(self.centralwidget, str("Emotion"), "Emotion Extract Success!")

    def EmotionExtractSingle(self):
        # 参数信息获取
        city = self.comboBoxCItyList.currentText()
        filepath = 'Data/DataProcessing/' + city + '/' + "KMeans/"
        k = self.lineEditKParamenter_2.text()
        ClusterNo = self.lineEditCluster.text()

        # 情绪分析
        tweets = function.ReadData(filepath + 'K-' + k + '/' + 'C' + ClusterNo + '.txt', city)
        self.infer.LoadTweets(tweets)
        self.infer.Transform()
        self.infer.infer()
        self.infer.ShowAndSaveResult(filepath + 'K-' + k + '/' + 'C' + ClusterNo + '.png')

        # 导入结果
        pngResult = QtGui.QPixmap(filepath + 'K-' + k + '/' + 'C' + ClusterNo + '.png')
        pngResult = pngResult.scaled(480, 360)
        sceneResult = QtWidgets.QGraphicsScene()
        sceneResult.addItem(QtWidgets.QGraphicsPixmapItem(pngResult))
        self.graphicsViewEmotionExtract.setScene(sceneResult)

        QtWidgets.QMessageBox.about(self.centralwidget, str("Emotion"), "Emotion Extract Success!")

    def ExtarctFile(self):
        # 参数获取
        city = self.comboBoxCItyList.currentText()
        filepath = 'Data/DataProcessing/' + city + '/'
        K = function.GetKParam(filepath + 'LDATrainResult/Config.txt')

        # 提取原始推文数据，从未经预处理的文件之中
        # ex = ExtractClusterFile.Extract()
        # ex.ReadTwitter(filepath + 'FilterData.txt')
        # function.CreateDir(filepath + 'ClusterResult/')
        # for i in range(K):
        #     path = filepath + 'KMeans/k-' + str(K) + '/C' + str(i) + '.txt'
        #     WritePath = filepath + 'ClusterResult/C' + str(i) + '.txt'
        #     ex.ExtractTwitter(path)
        #     ex.SaveExtractFile(WritePath)
        # 从上文的推文数据之中，提取到最后的推文文件
        et = EmotionInference.ExtractTopicFile(filepath + 'KMeans/k-' + str(K) + '/', K,
                                               filepath + 'LDATrainResult/DocTopicDist.txt')
        et.Extract()
        SavePath = filepath + 'AnalysisData/'
        function.CreateDir(SavePath)
        et.WriteFile(SavePath)

        QtWidgets.QMessageBox.about(self.centralwidget, str("Emotion"), "Extract File Success!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "The Cluster Result DI"))
        self.label_5.setText(_translate("MainWindow", "The Cluster Result SSE"))
        self.pushButtonLoad.setText(_translate("MainWindow", "Load"))
        self.pushButtonAnalysis.setText(_translate("MainWindow", "Analysis"))
        self.label_11.setText(_translate("MainWindow", "Start"))
        self.label_12.setText(_translate("MainWindow", "End"))
        self.label_13.setText(_translate("MainWindow", "Interval"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cluster), _translate("MainWindow", "Cluster"))
        self.label_4.setText(_translate("MainWindow", "Perplexity Trend Graph"))
        self.pushButtonLDA.setText(_translate("MainWindow", "Start Detection"))
        self.label_3.setText(_translate("MainWindow", "K param"))
        self.label_6.setText(_translate("MainWindow", "The Topic KeyWords"))
        self.label_7.setText(_translate("MainWindow", "The Doccument-Topic Matrix"))
        self.pushButtonLDALoad.setText(_translate("MainWindow", "Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "LDA Detection"))
        self.label_8.setText(_translate("MainWindow", "The Topic No."))
        self.pushButtonEmotionExtract.setText(_translate("MainWindow", "Emotion Extract"))
        self.label_9.setText(_translate("MainWindow", "Classifier Model"))
        self.pushButtonLoadModel.setText(_translate("MainWindow", "LoadModel"))
        self.label_10.setText(_translate("MainWindow", "Predict Result"))
        self.pushButtonFileExtract.setText(_translate("MainWindow", "File Extract"))
        self.label_14.setText(_translate("MainWindow", "Cluster File"))
        self.pushButtonEmotionExtract2.setText(_translate("MainWindow", "Emotion Extract"))
        self.label_15.setText(_translate("MainWindow", "K param"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Emotion Extract"))
        self.label_2.setText(_translate("MainWindow", "Choose The City"))
        self.menu.setTitle(_translate("MainWindow", "基于社交平台中用户地理位置的多粒度情感分析研究"))

