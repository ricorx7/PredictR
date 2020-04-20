# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'predictor_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RoweTechPredictor(object):
    def setupUi(self, RoweTechPredictor):
        RoweTechPredictor.setObjectName("RoweTechPredictor")
        RoweTechPredictor.resize(1590, 1005)
        self.centralWidget = QtWidgets.QWidget(RoweTechPredictor)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1572, 987))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(360, 900))
        self.widget.setMaximumSize(QtCore.QSize(360, 16777214))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.systemSettingsGroupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.systemSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.systemSettingsGroupBox.setSizePolicy(sizePolicy)
        self.systemSettingsGroupBox.setMaximumSize(QtCore.QSize(16777215, 210))
        self.systemSettingsGroupBox.setObjectName("systemSettingsGroupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.systemSettingsGroupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.systemSettingsGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ceiDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.systemSettingsGroupBox)
        self.ceiDoubleSpinBox.setMaximum(99999.99)
        self.ceiDoubleSpinBox.setProperty("value", 1.0)
        self.ceiDoubleSpinBox.setObjectName("ceiDoubleSpinBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ceiDoubleSpinBox)
        self.label_3 = QtWidgets.QLabel(self.systemSettingsGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cwsSpinBox = QtWidgets.QSpinBox(self.systemSettingsGroupBox)
        self.cwsSpinBox.setProperty("value", 35)
        self.cwsSpinBox.setObjectName("cwsSpinBox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cwsSpinBox)
        self.label_5 = QtWidgets.QLabel(self.systemSettingsGroupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cwtSpinBox = QtWidgets.QSpinBox(self.systemSettingsGroupBox)
        self.cwtSpinBox.setMinimum(-100)
        self.cwtSpinBox.setMaximum(100)
        self.cwtSpinBox.setProperty("value", 10)
        self.cwtSpinBox.setObjectName("cwtSpinBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cwtSpinBox)
        self.label_6 = QtWidgets.QLabel(self.systemSettingsGroupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.ctdSpinBox = QtWidgets.QSpinBox(self.systemSettingsGroupBox)
        self.ctdSpinBox.setMaximum(10000)
        self.ctdSpinBox.setObjectName("ctdSpinBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ctdSpinBox)
        self.label_7 = QtWidgets.QLabel(self.systemSettingsGroupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.speedOfSoundSpinBox = QtWidgets.QDoubleSpinBox(self.systemSettingsGroupBox)
        self.speedOfSoundSpinBox.setMinimum(1.0)
        self.speedOfSoundSpinBox.setMaximum(20000.0)
        self.speedOfSoundSpinBox.setProperty("value", 1490.0)
        self.speedOfSoundSpinBox.setObjectName("speedOfSoundSpinBox")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.speedOfSoundSpinBox)
        self.verticalLayout_3.addWidget(self.systemSettingsGroupBox)
        self.dataGroupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataGroupBox.sizePolicy().hasHeightForWidth())
        self.dataGroupBox.setSizePolicy(sizePolicy)
        self.dataGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.dataGroupBox.setMaximumSize(QtCore.QSize(16777215, 110))
        self.dataGroupBox.setObjectName("dataGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.dataGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.dataGroupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.dataFormatComboBox = QtWidgets.QComboBox(self.dataGroupBox)
        self.dataFormatComboBox.setObjectName("dataFormatComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dataFormatComboBox)
        self.label_4 = QtWidgets.QLabel(self.dataGroupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_9 = QtWidgets.QLabel(self.dataGroupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.coordinateTransformComboBox = QtWidgets.QComboBox(self.dataGroupBox)
        self.coordinateTransformComboBox.setObjectName("coordinateTransformComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.coordinateTransformComboBox)
        self.cerecordCheckBox = QtWidgets.QCheckBox(self.dataGroupBox)
        self.cerecordCheckBox.setText("")
        self.cerecordCheckBox.setObjectName("cerecordCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cerecordCheckBox)
        self.verticalLayout_3.addWidget(self.dataGroupBox)
        self.subsystemConfigGroupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subsystemConfigGroupBox.sizePolicy().hasHeightForWidth())
        self.subsystemConfigGroupBox.setSizePolicy(sizePolicy)
        self.subsystemConfigGroupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.subsystemConfigGroupBox.setObjectName("subsystemConfigGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.subsystemConfigGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.subsystemComboBox = QtWidgets.QComboBox(self.subsystemConfigGroupBox)
        self.subsystemComboBox.setObjectName("subsystemComboBox")
        self.verticalLayout_5.addWidget(self.subsystemComboBox)
        self.addSubsystemButton = QtWidgets.QPushButton(self.subsystemConfigGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSubsystemButton.sizePolicy().hasHeightForWidth())
        self.addSubsystemButton.setSizePolicy(sizePolicy)
        self.addSubsystemButton.setObjectName("addSubsystemButton")
        self.verticalLayout_5.addWidget(self.addSubsystemButton)
        self.verticalLayout_3.addWidget(self.subsystemConfigGroupBox)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.deploymentDurationSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.deploymentDurationSpinBox.setMinimum(1)
        self.deploymentDurationSpinBox.setMaximum(9999)
        self.deploymentDurationSpinBox.setObjectName("deploymentDurationSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deploymentDurationSpinBox)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.batteryTypeComboBox = QtWidgets.QComboBox(self.groupBox)
        self.batteryTypeComboBox.setObjectName("batteryTypeComboBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.batteryTypeComboBox)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.numBatteriesSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.numBatteriesSpinBox.setProperty("value", 2)
        self.numBatteriesSpinBox.setObjectName("numBatteriesSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numBatteriesSpinBox)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.storageSizeSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.storageSizeSpinBox.setMaximum(99999)
        self.storageSizeSpinBox.setSingleStep(32)
        self.storageSizeSpinBox.setProperty("value", 32)
        self.storageSizeSpinBox.setObjectName("storageSizeSpinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.storageSizeSpinBox)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.commandFileGroupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandFileGroupBox.sizePolicy().hasHeightForWidth())
        self.commandFileGroupBox.setSizePolicy(sizePolicy)
        self.commandFileGroupBox.setMaximumSize(QtCore.QSize(16777215, 350))
        self.commandFileGroupBox.setObjectName("commandFileGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.commandFileGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.commandFileTextBrowser = QtWidgets.QTextBrowser(self.commandFileGroupBox)
        self.commandFileTextBrowser.setObjectName("commandFileTextBrowser")
        self.verticalLayout_4.addWidget(self.commandFileTextBrowser)
        self.saveCommandsButton = QtWidgets.QPushButton(self.commandFileGroupBox)
        self.saveCommandsButton.setObjectName("saveCommandsButton")
        self.verticalLayout_4.addWidget(self.saveCommandsButton)
        self.verticalLayout_3.addWidget(self.commandFileGroupBox)
        self.revLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.revLabel.sizePolicy().hasHeightForWidth())
        self.revLabel.setSizePolicy(sizePolicy)
        self.revLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.revLabel.setObjectName("revLabel")
        self.verticalLayout_3.addWidget(self.revLabel)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.predictionGroupBox = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predictionGroupBox.sizePolicy().hasHeightForWidth())
        self.predictionGroupBox.setSizePolicy(sizePolicy)
        self.predictionGroupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.predictionGroupBox.setObjectName("predictionGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.predictionGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.predictionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.powerLabel = QtWidgets.QLabel(self.predictionGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.powerLabel.setFont(font)
        self.powerLabel.setText("")
        self.powerLabel.setObjectName("powerLabel")
        self.horizontalLayout_2.addWidget(self.powerLabel)
        self.label_17 = QtWidgets.QLabel(self.predictionGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.numBatteriesLabel = QtWidgets.QLabel(self.predictionGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.numBatteriesLabel.setFont(font)
        self.numBatteriesLabel.setText("")
        self.numBatteriesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numBatteriesLabel.setObjectName("numBatteriesLabel")
        self.verticalLayout_2.addWidget(self.numBatteriesLabel)
        self.batteryProgressBar = QtWidgets.QProgressBar(self.predictionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryProgressBar.sizePolicy().hasHeightForWidth())
        self.batteryProgressBar.setSizePolicy(sizePolicy)
        self.batteryProgressBar.setProperty("value", 24)
        self.batteryProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.batteryProgressBar.setObjectName("batteryProgressBar")
        self.verticalLayout_2.addWidget(self.batteryProgressBar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label_29 = QtWidgets.QLabel(self.predictionGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_2.addWidget(self.label_29)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dataUsageLabel = QtWidgets.QLabel(self.predictionGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.dataUsageLabel.setFont(font)
        self.dataUsageLabel.setText("")
        self.dataUsageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dataUsageLabel.setObjectName("dataUsageLabel")
        self.verticalLayout_6.addWidget(self.dataUsageLabel)
        self.dataUsageProgressBar = QtWidgets.QProgressBar(self.predictionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataUsageProgressBar.sizePolicy().hasHeightForWidth())
        self.dataUsageProgressBar.setSizePolicy(sizePolicy)
        self.dataUsageProgressBar.setProperty("value", 24)
        self.dataUsageProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.dataUsageProgressBar.setObjectName("dataUsageProgressBar")
        self.verticalLayout_6.addWidget(self.dataUsageProgressBar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.recordingLabel = QtWidgets.QLabel(self.predictionGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recordingLabel.setFont(font)
        self.recordingLabel.setText("")
        self.recordingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.recordingLabel.setObjectName("recordingLabel")
        self.horizontalLayout_2.addWidget(self.recordingLabel)
        self.salinityLabel = QtWidgets.QLabel(self.predictionGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.salinityLabel.setFont(font)
        self.salinityLabel.setText("")
        self.salinityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.salinityLabel.setObjectName("salinityLabel")
        self.horizontalLayout_2.addWidget(self.salinityLabel)
        self.verticalLayout.addWidget(self.predictionGroupBox)
        self.tabSubsystem = QtWidgets.QTabWidget(self.widget_2)
        self.tabSubsystem.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabSubsystem.sizePolicy().hasHeightForWidth())
        self.tabSubsystem.setSizePolicy(sizePolicy)
        self.tabSubsystem.setMinimumSize(QtCore.QSize(775, 0))
        self.tabSubsystem.setObjectName("tabSubsystem")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabSubsystem.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabSubsystem.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabSubsystem)
        self.horizontalLayout.addWidget(self.widget_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        RoweTechPredictor.setCentralWidget(self.centralWidget)

        self.retranslateUi(RoweTechPredictor)
        self.tabSubsystem.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RoweTechPredictor)

    def retranslateUi(self, RoweTechPredictor):
        _translate = QtCore.QCoreApplication.translate
        RoweTechPredictor.setWindowTitle(_translate("RoweTechPredictor", "MainWindow"))
        self.systemSettingsGroupBox.setTitle(_translate("RoweTechPredictor", "System Settings"))
        self.label_2.setText(_translate("RoweTechPredictor", "CEI (s)"))
        self.label_3.setText(_translate("RoweTechPredictor", "CWS (ppt)"))
        self.label_5.setText(_translate("RoweTechPredictor", "CWT (C)"))
        self.label_6.setText(_translate("RoweTechPredictor", "CTD (m)"))
        self.label_7.setText(_translate("RoweTechPredictor", "Speed of Sound (m/s)"))
        self.dataGroupBox.setTitle(_translate("RoweTechPredictor", "Data"))
        self.label_8.setText(_translate("RoweTechPredictor", "Data Format"))
        self.label_4.setText(_translate("RoweTechPredictor", "Record To Internal SD Card"))
        self.label_9.setText(_translate("RoweTechPredictor", "Coordinate Transform"))
        self.subsystemConfigGroupBox.setTitle(_translate("RoweTechPredictor", "Subsystem Configurations"))
        self.addSubsystemButton.setText(_translate("RoweTechPredictor", "ADD"))
        self.groupBox.setTitle(_translate("RoweTechPredictor", "Deployment"))
        self.label.setText(_translate("RoweTechPredictor", "Deployment Duration (Days)"))
        self.label_10.setText(_translate("RoweTechPredictor", "Battery Type"))
        self.label_11.setText(_translate("RoweTechPredictor", "Number of Batteries"))
        self.label_12.setText(_translate("RoweTechPredictor", "Storage Size (GB)"))
        self.commandFileGroupBox.setTitle(_translate("RoweTechPredictor", "Command File"))
        self.saveCommandsButton.setText(_translate("RoweTechPredictor", "Save to File"))
        self.revLabel.setText(_translate("RoweTechPredictor", "TextLabel"))
        self.predictionGroupBox.setTitle(_translate("RoweTechPredictor", "Total Prediction"))
        self.label_16.setText(_translate("RoweTechPredictor", "Total Power Usage: "))
        self.label_17.setText(_translate("RoweTechPredictor", "Total Num Batteries: "))
        self.label_29.setText(_translate("RoweTechPredictor", "Total Data Usage: "))
        self.tabSubsystem.setTabText(self.tabSubsystem.indexOf(self.tab_3), _translate("RoweTechPredictor", "Tab 1"))
        self.tabSubsystem.setTabText(self.tabSubsystem.indexOf(self.tab_4), _translate("RoweTechPredictor", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RoweTechPredictor = QtWidgets.QMainWindow()
    ui = Ui_RoweTechPredictor()
    ui.setupUi(RoweTechPredictor)
    RoweTechPredictor.show()
    sys.exit(app.exec_())
