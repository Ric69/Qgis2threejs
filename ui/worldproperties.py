# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis3\python\developing_plugins\Qgis2threejs\ui\worldproperties.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WorldPropertiesWidget(object):
    def setupUi(self, WorldPropertiesWidget):
        WorldPropertiesWidget.setObjectName("WorldPropertiesWidget")
        WorldPropertiesWidget.resize(268, 411)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(WorldPropertiesWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_1 = QtWidgets.QGroupBox(WorldPropertiesWidget)
        self.groupBox_1.setObjectName("groupBox_1")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_1)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_BaseSize = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_BaseSize.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_BaseSize.setObjectName("lineEdit_BaseSize")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_BaseSize)
        self.label = QtWidgets.QLabel(self.groupBox_1)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_zFactor = QtWidgets.QLineEdit(self.groupBox_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_zFactor.sizePolicy().hasHeightForWidth())
        self.lineEdit_zFactor.setSizePolicy(sizePolicy)
        self.lineEdit_zFactor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_zFactor.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_zFactor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_zFactor.setObjectName("lineEdit_zFactor")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_zFactor)
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_zShift = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_zShift.setObjectName("lineEdit_zShift")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_zShift)
        self.verticalLayout_3.addWidget(self.groupBox_1)
        self.groupBox = QtWidgets.QGroupBox(WorldPropertiesWidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_MaterialType = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_MaterialType.setObjectName("comboBox_MaterialType")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_MaterialType)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(WorldPropertiesWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_Sky = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Sky.setChecked(True)
        self.radioButton_Sky.setObjectName("radioButton_Sky")
        self.verticalLayout_2.addWidget(self.radioButton_Sky)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_Color = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Color.setMinimumSize(QtCore.QSize(110, 0))
        self.radioButton_Color.setObjectName("radioButton_Color")
        self.horizontalLayout_2.addWidget(self.radioButton_Color)
        self.lineEdit_Color = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Color.setEnabled(False)
        self.lineEdit_Color.setObjectName("lineEdit_Color")
        self.horizontalLayout_2.addWidget(self.lineEdit_Color)
        self.toolButton_Color = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_Color.setEnabled(False)
        self.toolButton_Color.setObjectName("toolButton_Color")
        self.horizontalLayout_2.addWidget(self.toolButton_Color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(WorldPropertiesWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_ProjectCRS = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_ProjectCRS.setChecked(True)
        self.radioButton_ProjectCRS.setObjectName("radioButton_ProjectCRS")
        self.verticalLayout.addWidget(self.radioButton_ProjectCRS)
        self.radioButton_WGS84 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_WGS84.setObjectName("radioButton_WGS84")
        self.verticalLayout.addWidget(self.radioButton_WGS84)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(WorldPropertiesWidget)
        self.radioButton_Color.toggled['bool'].connect(self.lineEdit_Color.setEnabled)
        self.radioButton_Color.toggled['bool'].connect(self.toolButton_Color.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(WorldPropertiesWidget)
        WorldPropertiesWidget.setTabOrder(self.lineEdit_BaseSize, self.lineEdit_zFactor)
        WorldPropertiesWidget.setTabOrder(self.lineEdit_zFactor, self.lineEdit_zShift)
        WorldPropertiesWidget.setTabOrder(self.lineEdit_zShift, self.radioButton_Sky)
        WorldPropertiesWidget.setTabOrder(self.radioButton_Sky, self.radioButton_Color)
        WorldPropertiesWidget.setTabOrder(self.radioButton_Color, self.lineEdit_Color)
        WorldPropertiesWidget.setTabOrder(self.lineEdit_Color, self.toolButton_Color)
        WorldPropertiesWidget.setTabOrder(self.toolButton_Color, self.radioButton_ProjectCRS)
        WorldPropertiesWidget.setTabOrder(self.radioButton_ProjectCRS, self.radioButton_WGS84)

    def retranslateUi(self, WorldPropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        WorldPropertiesWidget.setWindowTitle(_translate("WorldPropertiesWidget", "Form"))
        self.groupBox_1.setTitle(_translate("WorldPropertiesWidget", "&Scale and shift"))
        self.label_3.setText(_translate("WorldPropertiesWidget", "Base size"))
        self.label.setText(_translate("WorldPropertiesWidget", "Vertical exaggeration"))
        self.label_2.setText(_translate("WorldPropertiesWidget", "Vertical shift"))
        self.groupBox.setTitle(_translate("WorldPropertiesWidget", "Material"))
        self.label_4.setText(_translate("WorldPropertiesWidget", "Basic type"))
        self.groupBox_2.setTitle(_translate("WorldPropertiesWidget", "&Background"))
        self.radioButton_Sky.setText(_translate("WorldPropertiesWidget", "Sky"))
        self.radioButton_Color.setText(_translate("WorldPropertiesWidget", "Solid color"))
        self.lineEdit_Color.setPlaceholderText(_translate("WorldPropertiesWidget", "0xrrggbb"))
        self.toolButton_Color.setText(_translate("WorldPropertiesWidget", "..."))
        self.groupBox_3.setTitle(_translate("WorldPropertiesWidget", "&Display of coordinates"))
        self.radioButton_ProjectCRS.setText(_translate("WorldPropertiesWidget", "Coordinates in the project CRS"))
        self.radioButton_WGS84.setText(_translate("WorldPropertiesWidget", "Latitude and longitude (WGS84)"))

