# -*- coding: utf-8 -*-
#!/usr/bin/env python2
#
# Created: Thu Jun 20 11:03:24 2013
#
# Site Oficial: http://www.qualoperadora.net/
# O site não é é de minha autoria!!
#
# Programador: Fellipe Pinheiro
# Contato: https://twitter.com/PinheiroFellipe
# Código: https://github.com/delete
#
# Versão 0.1 - beta

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import sys
from operadora import Operadora

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(441, 284)
        #Tamanho da fonte
        font = QtGui.QFont()
        font.setPointSize(12)

        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 80, 94, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.descobrir)

        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 40, 181, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.label_titulo = QtGui.QLabel(Dialog)
        self.label_titulo.setGeometry(QtCore.QRect(160, 10, 91, 16))
        self.label_titulo.setObjectName(_fromUtf8("label_titulo"))

        self.label_num = QtGui.QLabel(Dialog)
        self.label_num.setGeometry(QtCore.QRect(80, 140, 71, 16))

        self.label_num.setFont(font)
        self.label_num.setObjectName(_fromUtf8("label_num"))

        self.label_op = QtGui.QLabel(Dialog)
        self.label_op.setGeometry(QtCore.QRect(80, 170, 91, 16))
        self.label_op.setFont(font)
        self.label_op.setObjectName(_fromUtf8("label_op"))

        self.label_est = QtGui.QLabel(Dialog)
        self.label_est.setGeometry(QtCore.QRect(80, 200, 56, 15))
        self.label_est.setFont(font)
        self.label_est.setObjectName(_fromUtf8("label_est"))

        #Labels com saida de dados
        self.label_numero = QtGui.QLabel(Dialog)
        self.label_numero.setGeometry(QtCore.QRect(200, 140, 171, 16))
        self.label_numero.setText(_fromUtf8(""))
        self.label_numero.setObjectName(_fromUtf8("label_numero"))

        self.label_operadora = QtGui.QLabel(Dialog)
        self.label_operadora.setGeometry(QtCore.QRect(200, 170, 171, 16))
        self.label_operadora.setText(_fromUtf8(""))
        self.label_operadora.setObjectName(_fromUtf8("label_operadora"))

        self.label_estado = QtGui.QLabel(Dialog)
        self.label_estado.setGeometry(QtCore.QRect(200, 200, 171, 16))
        self.label_estado.setText(_fromUtf8(""))
        self.label_estado.setObjectName(_fromUtf8("label_estado"))

        self.label_site = QtGui.QLabel(Dialog)
        self.label_site.setGeometry(QtCore.QRect(260, 250, 61, 20))
        self.label_site.setObjectName(_fromUtf8("label_site"))
        QtCore.QObject.connect(self.label_site, QtCore.SIGNAL("linkActivated(QString)"), self.openUrl)

        self.label_prog = QtGui.QLabel(Dialog)
        self.label_prog.setGeometry(QtCore.QRect(355, 250, 71, 20))
        self.label_prog.setObjectName(_fromUtf8("label_prog"))
        QtCore.QObject.connect(self.label_prog, QtCore.SIGNAL("linkActivated(QString)"), self.openUrl)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Qual Operadora?", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Descobrir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_titulo.setText(QtGui.QApplication.translate("Dialog", "DDD+Número", None, QtGui.QApplication.UnicodeUTF8))
        self.label_num.setText(QtGui.QApplication.translate("Dialog", "Número:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_op.setText(QtGui.QApplication.translate("Dialog", "Operadora:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_est.setText(QtGui.QApplication.translate("Dialog", "Estado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_site.setText(QtGui.QApplication.translate("Dialog", '<a href="http://www.qualoperadora.net">Site Oficial</a></em>', None, QtGui.QApplication.UnicodeUTF8))
        self.label_prog.setText(QtGui.QApplication.translate("Dialog", '<a href="http://www.twitter.com/pinheirofellipe">Programador</a></em>', None, QtGui.QApplication.UnicodeUTF8))

    def descobrir(self):
        numero = self.textEdit.toPlainText()
        p = Operadora()
        p.setNumero(numero)
        try:
            p.configura()
            lista = p.filtro()
            font = QtGui.QFont()
            font.setPointSize(9)
            self.label_numero.setFont(font)
            self.label_numero.setText(QtGui.QApplication.translate("Dialog", lista[0], None, QtGui.QApplication.UnicodeUTF8))
            self.label_operadora.setText(QtGui.QApplication.translate("Dialog", lista[1], None, QtGui.QApplication.UnicodeUTF8))
            self.label_estado.setText(QtGui.QApplication.translate("Dialog", lista[2], None, QtGui.QApplication.UnicodeUTF8))
        except:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.label_numero.setFont(font)
            self.label_numero.setText(QtGui.QApplication.translate("Dialog", 'Número inválido!', None, QtGui.QApplication.UnicodeUTF8))
            self.label_operadora.setText(QtGui.QApplication.translate("Dialog", '', None, QtGui.QApplication.UnicodeUTF8))
            self.label_estado.setText(QtGui.QApplication.translate("Dialog", '', None, QtGui.QApplication.UnicodeUTF8))

    def openUrl(self, URL):
        QtGui.QDesktopServices().openUrl(QUrl(URL))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
