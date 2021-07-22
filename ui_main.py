# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(737, 650)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_edit_server = QLineEdit(self.groupBox_2)
        self.line_edit_server.setObjectName(u"line_edit_server")

        self.horizontalLayout_4.addWidget(self.line_edit_server)

        self.push_button_check_server = QPushButton(self.groupBox_2)
        self.push_button_check_server.setObjectName(u"push_button_check_server")

        self.horizontalLayout_4.addWidget(self.push_button_check_server)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_edit_result_dir = QLineEdit(self.groupBox_3)
        self.line_edit_result_dir.setObjectName(u"line_edit_result_dir")

        self.horizontalLayout_2.addWidget(self.line_edit_result_dir)

        self.line_edit_local_server_port = QLineEdit(self.groupBox_3)
        self.line_edit_local_server_port.setObjectName(u"line_edit_local_server_port")

        self.horizontalLayout_2.addWidget(self.line_edit_local_server_port)

        self.line_edit_local_server_ae_title = QLineEdit(self.groupBox_3)
        self.line_edit_local_server_ae_title.setObjectName(u"line_edit_local_server_ae_title")

        self.horizontalLayout_2.addWidget(self.line_edit_local_server_ae_title)

        self.push_button_start_server = QPushButton(self.groupBox_3)
        self.push_button_start_server.setObjectName(u"push_button_start_server")

        self.horizontalLayout_2.addWidget(self.push_button_start_server)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.push_button_open_file = QPushButton(self.centralwidget)
        self.push_button_open_file.setObjectName(u"push_button_open_file")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_open_file.sizePolicy().hasHeightForWidth())
        self.push_button_open_file.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.push_button_open_file)

        self.push_button_check_file = QPushButton(self.centralwidget)
        self.push_button_check_file.setObjectName(u"push_button_check_file")
        self.push_button_check_file.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.push_button_check_file)

        self.push_button_show_content = QPushButton(self.centralwidget)
        self.push_button_show_content.setObjectName(u"push_button_show_content")
        self.push_button_show_content.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.push_button_show_content)

        self.push_button_anonimize = QPushButton(self.centralwidget)
        self.push_button_anonimize.setObjectName(u"push_button_anonimize")
        self.push_button_anonimize.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.push_button_anonimize)

        self.push_button_send_file = QPushButton(self.centralwidget)
        self.push_button_send_file.setObjectName(u"push_button_send_file")
        self.push_button_send_file.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.push_button_send_file)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.groupBox_files = QGroupBox(self.centralwidget)
        self.groupBox_files.setObjectName(u"groupBox_files")
        self.groupBox_files.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout = QHBoxLayout(self.groupBox_files)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_file_path = QLabel(self.groupBox_files)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_file_path)


        self.verticalLayout.addWidget(self.groupBox_files)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_6 = QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.plain_text_edit_results = QPlainTextEdit(self.tab)
        self.plain_text_edit_results.setObjectName(u"plain_text_edit_results")
        self.plain_text_edit_results.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.plain_text_edit_results)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table_widget_files = QTableWidget(self.tab_2)
        self.table_widget_files.setObjectName(u"table_widget_files")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_widget_files.sizePolicy().hasHeightForWidth())
        self.table_widget_files.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.table_widget_files, 0, 0, 1, 1)

        self.label_image_view = QLabel(self.tab_2)
        self.label_image_view.setObjectName(u"label_image_view")

        self.gridLayout.addWidget(self.label_image_view, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.horizontalLayout_3.addWidget(self.label_status)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.push_button_send_result = QPushButton(self.centralwidget)
        self.push_button_send_result.setObjectName(u"push_button_send_result")

        self.verticalLayout.addWidget(self.push_button_send_result)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 737, 22))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"DICOM Test Sender", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("main_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 PACS-\u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.line_edit_server.setText(QCoreApplication.translate("main_window", u"127.0.0.1:11112", None))
        self.push_button_check_server.setText(QCoreApplication.translate("main_window", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("main_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u0430\u0442\u0430\u043b\u043e\u0433 \u0438 \u043f\u043e\u0440\u0442 \u0441\u0435\u0440\u0432\u0435\u0440\u0430 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.line_edit_result_dir.setText(QCoreApplication.translate("main_window", u"out/", None))
        self.line_edit_local_server_port.setText(QCoreApplication.translate("main_window", u"11113", None))
#if QT_CONFIG(tooltip)
        self.line_edit_local_server_ae_title.setToolTip(QCoreApplication.translate("main_window", u"AE Title", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_local_server_ae_title.setText(QCoreApplication.translate("main_window", u"AE_TEST", None))
        self.push_button_start_server.setText(QCoreApplication.translate("main_window", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.push_button_open_file.setText(QCoreApplication.translate("main_window", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.push_button_check_file.setText(QCoreApplication.translate("main_window", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.push_button_show_content.setText(QCoreApplication.translate("main_window", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.push_button_anonimize.setText(QCoreApplication.translate("main_window", u"\u0410\u043d\u043e\u043d\u0438\u043c\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.push_button_send_file.setText(QCoreApplication.translate("main_window", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.groupBox_files.setTitle(QCoreApplication.translate("main_window", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0430\u043b\u043e\u0433 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 dicom-\u0444\u0430\u0439\u043b\u044b", None))
        self.label_file_path.setText(QCoreApplication.translate("main_window", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main_window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.label_image_view.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main_window", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.label_status.setText(QCoreApplication.translate("main_window", u"?", None))
        self.push_button_send_result.setText(QCoreApplication.translate("main_window", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
    # retranslateUi

