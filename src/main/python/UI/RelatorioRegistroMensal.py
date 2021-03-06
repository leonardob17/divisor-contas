# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/UI/RelatorioRegistroMensal.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RelatorioRegistroMensal(object):
    def setupUi(self, RelatorioRegistroMensal):
        RelatorioRegistroMensal.setObjectName("RelatorioRegistroMensal")
        RelatorioRegistroMensal.resize(883, 557)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/svg/neutral_trading.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RelatorioRegistroMensal.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(RelatorioRegistroMensal)
        self.gridLayout.setObjectName("gridLayout")
        self.sair = QtWidgets.QPushButton(RelatorioRegistroMensal)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/svg/export.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon1)
        self.sair.setObjectName("sair")
        self.gridLayout.addWidget(self.sair, 3, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(RelatorioRegistroMensal)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.totais = QtWidgets.QTableWidget(self.groupBox_3)
        self.totais.setObjectName("totais")
        self.totais.setColumnCount(4)
        self.totais.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.totais.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.totais.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.totais.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.totais.setHorizontalHeaderItem(3, item)
        self.horizontalLayout.addWidget(self.totais)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(RelatorioRegistroMensal)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.emprestimos = QtWidgets.QTableWidget(self.groupBox)
        self.emprestimos.setObjectName("emprestimos")
        self.emprestimos.setColumnCount(4)
        self.emprestimos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.emprestimos)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(RelatorioRegistroMensal)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contas = QtWidgets.QTableWidget(self.groupBox_2)
        self.contas.setObjectName("contas")
        self.contas.setColumnCount(4)
        self.contas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.contas)
        self.totalLabel = QtWidgets.QLabel(self.groupBox_2)
        self.totalLabel.setTextFormat(QtCore.Qt.RichText)
        self.totalLabel.setObjectName("totalLabel")
        self.verticalLayout_2.addWidget(self.totalLabel)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.titulo = QtWidgets.QLabel(RelatorioRegistroMensal)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.titulo.setFont(font)
        self.titulo.setTextFormat(QtCore.Qt.RichText)
        self.titulo.setObjectName("titulo")
        self.gridLayout.addWidget(self.titulo, 0, 0, 1, 2)

        self.retranslateUi(RelatorioRegistroMensal)
        QtCore.QMetaObject.connectSlotsByName(RelatorioRegistroMensal)

    def retranslateUi(self, RelatorioRegistroMensal):
        _translate = QtCore.QCoreApplication.translate
        RelatorioRegistroMensal.setWindowTitle(_translate("RelatorioRegistroMensal", "Relatório Mensal"))
        self.sair.setText(_translate("RelatorioRegistroMensal", "Sair"))
        self.groupBox_3.setTitle(_translate("RelatorioRegistroMensal", "Totais"))
        item = self.totais.horizontalHeaderItem(0)
        item.setText(_translate("RelatorioRegistroMensal", "Morador"))
        item = self.totais.horizontalHeaderItem(1)
        item.setText(_translate("RelatorioRegistroMensal", "Total"))
        item = self.totais.horizontalHeaderItem(2)
        item.setText(_translate("RelatorioRegistroMensal", "Pago"))
        item = self.totais.horizontalHeaderItem(3)
        item.setText(_translate("RelatorioRegistroMensal", "Falta Pagar"))
        self.groupBox.setTitle(_translate("RelatorioRegistroMensal", "Empréstimos e Outros Valores"))
        item = self.emprestimos.horizontalHeaderItem(0)
        item.setText(_translate("RelatorioRegistroMensal", "Descrição"))
        item = self.emprestimos.horizontalHeaderItem(1)
        item.setText(_translate("RelatorioRegistroMensal", "De"))
        item = self.emprestimos.horizontalHeaderItem(2)
        item.setText(_translate("RelatorioRegistroMensal", "Para"))
        item = self.emprestimos.horizontalHeaderItem(3)
        item.setText(_translate("RelatorioRegistroMensal", "Valor"))
        self.groupBox_2.setTitle(_translate("RelatorioRegistroMensal", "Contas"))
        item = self.contas.horizontalHeaderItem(0)
        item.setText(_translate("RelatorioRegistroMensal", "Valor"))
        item = self.contas.horizontalHeaderItem(1)
        item.setText(_translate("RelatorioRegistroMensal", "Tipo de Conta"))
        item = self.contas.horizontalHeaderItem(2)
        item.setText(_translate("RelatorioRegistroMensal", "Descrição"))
        item = self.contas.horizontalHeaderItem(3)
        item.setText(_translate("RelatorioRegistroMensal", "Pago"))
        self.totalLabel.setText(_translate("RelatorioRegistroMensal", "<html><head/><body><p><span style=\" font-weight:600;\">Total: </span><span style=\" font-weight:600; font-style:italic;\">R$valor</span></p></body></html>"))
        self.titulo.setText(_translate("RelatorioRegistroMensal", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Contas do Período:</span> mes_ano</p></body></html>"))


from . import ImageResources
