# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CheckWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QButtonGroup, QCheckBox, QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QProgressBar, QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


class Ui_CheckWindows(object):
    def setupUi(self, CheckWindows):
        if not CheckWindows.objectName():
            CheckWindows.setObjectName("CheckWindows")
        CheckWindows.setWindowModality(Qt.ApplicationModal)
        CheckWindows.resize(410, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CheckWindows.sizePolicy().hasHeightForWidth())
        CheckWindows.setSizePolicy(sizePolicy)
        CheckWindows.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(":/statics/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        CheckWindows.setWindowIcon(icon)
        self.layoutWidget = QWidget(CheckWindows)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 411, 511))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.path_layout = QHBoxLayout()
        self.path_layout.setObjectName("path_layout")
        self.path_lb = QLabel(self.layoutWidget)
        self.path_lb.setObjectName("path_lb")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.path_lb.sizePolicy().hasHeightForWidth())
        self.path_lb.setSizePolicy(sizePolicy1)

        self.path_layout.addWidget(self.path_lb)

        self.path_box = QLineEdit(self.layoutWidget)
        self.path_box.setObjectName("path_box")
        self.path_box.setReadOnly(True)

        self.path_layout.addWidget(self.path_box)

        self.path_btn = QPushButton(self.layoutWidget)
        self.path_btn.setObjectName("path_btn")

        self.path_layout.addWidget(self.path_btn)

        self.path_layout.setStretch(0, 1)
        self.path_layout.setStretch(1, 10)

        self.verticalLayout.addLayout(self.path_layout)

        self.filename_layout = QHBoxLayout()
        self.filename_layout.setObjectName("filename_layout")
        self.filename_lb = QLabel(self.layoutWidget)
        self.filename_lb.setObjectName("filename_lb")
        sizePolicy1.setHeightForWidth(self.filename_lb.sizePolicy().hasHeightForWidth())
        self.filename_lb.setSizePolicy(sizePolicy1)

        self.filename_layout.addWidget(self.filename_lb)

        self.filename_box = QLineEdit(self.layoutWidget)
        self.filename_box.setObjectName("filename_box")

        self.filename_layout.addWidget(self.filename_box)

        self.filename_layout.setStretch(0, 1)
        self.filename_layout.setStretch(1, 10)

        self.verticalLayout.addLayout(self.filename_layout)

        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName("title_layout")
        self.title_lb = QLabel(self.layoutWidget)
        self.title_lb.setObjectName("title_lb")
        sizePolicy1.setHeightForWidth(self.title_lb.sizePolicy().hasHeightForWidth())
        self.title_lb.setSizePolicy(sizePolicy1)

        self.title_layout.addWidget(self.title_lb)

        self.title_box = QLineEdit(self.layoutWidget)
        self.title_box.setObjectName("title_box")

        self.title_layout.addWidget(self.title_box)

        self.title_layout.setStretch(0, 2)
        self.title_layout.setStretch(1, 10)

        self.verticalLayout.addLayout(self.title_layout)

        self.number_lb = QLabel(self.layoutWidget)
        self.number_lb.setObjectName("number_lb")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.number_lb.sizePolicy().hasHeightForWidth())
        self.number_lb.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.number_lb)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(40, 0, 0, 0)
        self.auto_num_rtn = QRadioButton(self.layoutWidget)
        self.is_custom_num_buttonGroup = QButtonGroup(CheckWindows)
        self.is_custom_num_buttonGroup.setObjectName("is_custom_num_buttonGroup")
        self.is_custom_num_buttonGroup.addButton(self.auto_num_rtn)
        self.auto_num_rtn.setObjectName("auto_num_rtn")
        self.auto_num_rtn.setChecked(True)

        self.horizontalLayout.addWidget(self.auto_num_rtn)

        self.custom_num_rtn = QRadioButton(self.layoutWidget)
        self.is_custom_num_buttonGroup.addButton(self.custom_num_rtn)
        self.custom_num_rtn.setObjectName("custom_num_rtn")

        self.horizontalLayout.addWidget(self.custom_num_rtn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.number_fix_layout = QHBoxLayout()
        self.number_fix_layout.setObjectName("number_fix_layout")
        self.number_fix_layout.setContentsMargins(40, -1, -1, -1)
        self.prefix_layout = QHBoxLayout()
        self.prefix_layout.setObjectName("prefix_layout")
        self.prefix_lb = QLabel(self.layoutWidget)
        self.prefix_lb.setObjectName("prefix_lb")

        self.prefix_layout.addWidget(self.prefix_lb)

        self.prefix_box = QLineEdit(self.layoutWidget)
        self.prefix_box.setObjectName("prefix_box")
        self.prefix_box.setEnabled(False)
        self.prefix_box.setReadOnly(False)

        self.prefix_layout.addWidget(self.prefix_box)

        self.number_fix_layout.addLayout(self.prefix_layout)

        self.subfix_layout = QHBoxLayout()
        self.subfix_layout.setObjectName("subfix_layout")
        self.subfix_layout.setContentsMargins(10, -1, -1, -1)
        self.subfix_lb = QLabel(self.layoutWidget)
        self.subfix_lb.setObjectName("subfix_lb")

        self.subfix_layout.addWidget(self.subfix_lb)

        self.subfix_box = QLineEdit(self.layoutWidget)
        self.subfix_box.setObjectName("subfix_box")
        self.subfix_box.setEnabled(False)

        self.subfix_layout.addWidget(self.subfix_box)

        self.number_fix_layout.addLayout(self.subfix_layout)

        self.verticalLayout.addLayout(self.number_fix_layout)

        self.rule_layout = QHBoxLayout()
        self.rule_layout.setObjectName("rule_layout")
        self.rule_layout.setContentsMargins(40, -1, -1, -1)
        self.rule_lb = QLabel(self.layoutWidget)
        self.rule_lb.setObjectName("rule_lb")

        self.rule_layout.addWidget(self.rule_lb)

        self.rule_box = QLineEdit(self.layoutWidget)
        self.rule_box.setObjectName("rule_box")
        self.rule_box.setEnabled(False)

        self.rule_layout.addWidget(self.rule_box)

        self.verticalLayout.addLayout(self.rule_layout)

        self.image_layout = QHBoxLayout()
        self.image_layout.setObjectName("image_layout")
        self.image_lb = QLabel(self.layoutWidget)
        self.image_lb.setObjectName("image_lb")
        sizePolicy2.setHeightForWidth(self.image_lb.sizePolicy().hasHeightForWidth())
        self.image_lb.setSizePolicy(sizePolicy2)

        self.image_layout.addWidget(self.image_lb)

        self.verticalLayout.addLayout(self.image_layout)

        self.image_opt_layout = QHBoxLayout()
        self.image_opt_layout.setObjectName("image_opt_layout")
        self.image_opt_layout.setContentsMargins(40, -1, -1, -1)
        self.is_compress = QCheckBox(self.layoutWidget)
        self.is_compress.setObjectName("is_compress")

        self.image_opt_layout.addWidget(self.is_compress)

        self.verticalLayout.addLayout(self.image_opt_layout)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.progress_layout = QVBoxLayout()
        self.progress_layout.setObjectName("progress_layout")
        self.progress_content_layout = QHBoxLayout()
        self.progress_content_layout.setObjectName("progress_content_layout")
        self.progress_content_layout.setContentsMargins(-1, 10, -1, -1)
        self.progress_lb = QLabel(self.layoutWidget)
        self.progress_lb.setObjectName("progress_lb")
        sizePolicy2.setHeightForWidth(self.progress_lb.sizePolicy().hasHeightForWidth())
        self.progress_lb.setSizePolicy(sizePolicy2)

        self.progress_content_layout.addWidget(self.progress_lb)

        self.current_progress_lb = QLabel(self.layoutWidget)
        self.current_progress_lb.setObjectName("current_progress_lb")
        sizePolicy2.setHeightForWidth(
            self.current_progress_lb.sizePolicy().hasHeightForWidth()
        )
        self.current_progress_lb.setSizePolicy(sizePolicy2)

        self.progress_content_layout.addWidget(self.current_progress_lb)

        self.progress_content_layout.setStretch(0, 1)
        self.progress_content_layout.setStretch(1, 5)

        self.progress_layout.addLayout(self.progress_content_layout)

        self.progress_bar_layout = QHBoxLayout()
        self.progress_bar_layout.setObjectName("progress_bar_layout")
        self.progress_bar_layout.setContentsMargins(0, 10, 0, -1)
        self.progressBar = QProgressBar(self.layoutWidget)
        self.progressBar.setObjectName("progressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setValue(0)

        self.progress_bar_layout.addWidget(self.progressBar)

        self.progress_layout.addLayout(self.progress_bar_layout)

        self.verticalLayout.addLayout(self.progress_layout)

        self.buttom_layout = QHBoxLayout()
        self.buttom_layout.setObjectName("buttom_layout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.buttom_layout.addItem(self.horizontalSpacer)

        self.start_generate_btn = QPushButton(self.layoutWidget)
        self.start_generate_btn.setObjectName("start_generate_btn")

        self.buttom_layout.addWidget(self.start_generate_btn)

        self.verticalLayout.addLayout(self.buttom_layout)

        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 2)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 2)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(10, 2)
        self.verticalLayout.setStretch(11, 2)

        self.retranslateUi(CheckWindows)

        QMetaObject.connectSlotsByName(CheckWindows)

    # setupUi

    def retranslateUi(self, CheckWindows):
        CheckWindows.setWindowTitle(
            QCoreApplication.translate("CheckWindows", "File configs", None)
        )
        # if QT_CONFIG(tooltip)
        self.path_lb.setToolTip(
            QCoreApplication.translate(
                "CheckWindows", "\u5831\u544a\u7684\u8f38\u51fa\u8def\u5f91", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.path_lb.setText(
            QCoreApplication.translate(
                "CheckWindows", "\u8f38\u51fa\u8def\u5f91\uff1a", None
            )
        )
        self.path_btn.setText(
            QCoreApplication.translate("CheckWindows", "\u700f\u89bd", None)
        )
        # if QT_CONFIG(tooltip)
        self.filename_lb.setToolTip(
            QCoreApplication.translate(
                "CheckWindows", "\u5831\u544a\u7684\u6a94\u6848\u540d\u7a31", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.filename_lb.setText(
            QCoreApplication.translate(
                "CheckWindows", "\u6a94\u6848\u540d\u7a31\uff1a", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.title_lb.setToolTip(
            QCoreApplication.translate(
                "CheckWindows", "\u5831\u544a\u5167\u6587\u7684\u6a19\u984c", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.title_lb.setText(
            QCoreApplication.translate("CheckWindows", "\u6a19\u984c\uff1a", None)
        )
        self.number_lb.setText(
            QCoreApplication.translate("CheckWindows", "\u7de8\u865f\uff1a", None)
        )
        # if QT_CONFIG(tooltip)
        self.auto_num_rtn.setToolTip(
            QCoreApplication.translate(
                "CheckWindows",
                "\u7531 Word \u81ea\u52d5\u5efa\u7acb\u7684\u9023\u7e8c\u7de8\u865f\uff0c\u5373\u4f7f\u4e2d\u9593\u88ab\u522a\u9664\u4e5f\u6703\u81ea\u52d5\u91cd\u65b0\u7de8\u6392\uff0c\u4e0d\u9069\u7528\u4e0b\u65b9\u81ea\u8a02\u7de8\u865f\u898f\u5247\u3002",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.auto_num_rtn.setText(
            QCoreApplication.translate(
                "CheckWindows", "Word \u81ea\u52d5\u7de8\u865f", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.custom_num_rtn.setToolTip(
            QCoreApplication.translate(
                "CheckWindows",
                "\u7de8\u865f\u90fd\u662f\u7d14\u6587\u5b57\uff0c\u4e2d\u9593\u88ab\u522a\u9664\u4e0d\u6703\u81ea\u52d5\u91cd\u65b0\u7de8\u6392\uff0c\u53ef\u9078\u7528\u4e0b\u65b9\u81ea\u8a02\u7de8\u865f\u898f\u5247\u3002",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.custom_num_rtn.setText(
            QCoreApplication.translate(
                "CheckWindows", "\u7d14\u6587\u5b57\u7de8\u865f", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.prefix_lb.setToolTip(
            QCoreApplication.translate(
                "CheckWindows",
                "\u5728\u7de8\u865f\u52a0\u5165\u524d\u7db4\uff0c\u5982\uff1a\u7167\u7247 A1 \u3002",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.prefix_lb.setText(
            QCoreApplication.translate("CheckWindows", "\u524d\u7db4\uff1a", None)
        )
        self.prefix_box.setPlaceholderText(
            QCoreApplication.translate("CheckWindows", "\u9078\u586b", None)
        )
        # if QT_CONFIG(tooltip)
        self.subfix_lb.setToolTip(
            QCoreApplication.translate(
                "CheckWindows",
                "\u5728\u7de8\u865f\u52a0\u5165\u5f8c\u7db4\uff0c\u5982\uff1a\u7167\u7247 1B \u3002",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.subfix_lb.setText(
            QCoreApplication.translate("CheckWindows", "\u5f8c\u7db4\uff1a", None)
        )
        self.subfix_box.setPlaceholderText(
            QCoreApplication.translate("CheckWindows", "\u9078\u586b", None)
        )
        # if QT_CONFIG(tooltip)
        self.rule_lb.setToolTip(
            QCoreApplication.translate(
                "CheckWindows",
                "\u6709\u7279\u6b8a\u7684\u7de8\u865f\u9700\u6c42\u6642\u8a2d\u5b9a\uff0c\u5982\uff1a\u300c2,5-8,14,77\u300d",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.rule_lb.setText(
            QCoreApplication.translate("CheckWindows", "\u898f\u5247\uff1a", None)
        )
        self.rule_box.setPlaceholderText(
            QCoreApplication.translate("CheckWindows", "\u9078\u586b", None)
        )
        self.image_lb.setText(
            QCoreApplication.translate(
                "CheckWindows", "\u5716\u7247\u9078\u9805\uff1a", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.is_compress.setToolTip(
            QCoreApplication.translate(
                "CheckWindows",
                "\u5716\u7247\u5728\u63d2\u5165\u524d\u5148\u9032\u884c\u58d3\u7e2e\uff0c\u4ee5\u6e1b\u5c11\u5831\u544a\u6a94\u6848\u5927\u5c0f\u3002",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.is_compress.setText(
            QCoreApplication.translate("CheckWindows", "\u58d3\u7e2e", None)
        )
        self.progress_lb.setText(
            QCoreApplication.translate("CheckWindows", "\u9032\u5ea6\uff1a", None)
        )
        self.current_progress_lb.setText(
            QCoreApplication.translate(
                "CheckWindows", "\u53c3\u6578\u8a2d\u5b9a\u4e2d", None
            )
        )
        self.start_generate_btn.setText(
            QCoreApplication.translate("CheckWindows", "\u958b\u59cb\u751f\u6210", None)
        )

    # retranslateUi
