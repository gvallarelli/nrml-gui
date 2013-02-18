#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

import sys
import os
import csv

import resources
import utils

__version__ = "0.0.1"


class MainWindow(QtGui.QMainWindow):

    def _create_bars(self):
        # Create actions
        fileNewAction = utils.create_action(
                self, "&New", slot=self.file_new,
                shortcut=QtGui.QKeySequence.New, icon="new",
                tip="Create a new exposure")

        fileOpenAction = utils.create_action(
                self, "&Open...", slot=self.file_open,
                shortcut=QtGui.QKeySequence.Open, icon="open",
                tip="Exposure in csv format")

        fst_separator = utils.create_action(self, None)
        fst_separator.setSeparator(True)

        fileSaveAction = utils.create_action(
                self, "&Save", slot=self.file_save,
                shortcut=QtGui.QKeySequence.Save, icon="save",
                tip="Save current changes")

        fileSaveAsAction = utils.create_action(
                self, "&Save As...", slot=self.file_saveas,
                shortcut=QtGui.QKeySequence.SaveAs, icon="saveas",
                tip="Save file as...")

        snd_separator = utils.create_action(self, None)
        snd_separator.setSeparator(True)

        fileCloseAction = utils.create_action(
                self, "&Quit", slot=self.file_close,
                shortcut=QtGui.QKeySequence.Quit, icon="quit",
                tip="Close the application")

        # Associate actions to MenuBar
        menu_bar = self.menuBar()
        file = menu_bar.addMenu('&File')
        file.addAction(fileNewAction)
        file.addAction(fileOpenAction)
        file.addAction(fst_separator)
        file.addAction(fileSaveAction)
        file.addAction(fileSaveAsAction)
        file.addAction(snd_separator)
        file.addAction(fileCloseAction)

        # Associate actions to ToolBar
        tool_bar = self.addToolBar('ToolBar')
        tool_bar.addAction(fileNewAction)
        tool_bar.addAction(fileOpenAction)
        tool_bar.addAction(fileSaveAction)
        tool_bar.addAction(fileSaveAsAction)
        tool_bar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(640, 480)
        self.setWindowTitle('OpenQuake NRML')
        self._create_bars()
        layout = QtGui.QVBoxLayout()

        self.table = QtGui.QTableWidget(12, 10)
        # Resize mode to stretch
        self.table.horizontalHeader().setResizeMode(1)
        self.table.verticalHeader().setResizeMode(1)
        layout.addWidget(self.table)
        self.setCentralWidget(self.table)

    def file_new(self):
        print "pressed ctrl-n"


    def file_open(self):
        fname = QtGui.QFileDialog.getOpenFileName(
                self, 'Open file', os.path.expanduser("~"), 'Data *.csv')
        print fname

    def file_close(self):
        QtGui.QApplication.quit()

    def file_save(self):
        print 'pressed ctrl-s file save'

    def file_saveas(self):
        print 'pressed ctrl-something file save as'

def main():
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName("GEM Foundation")
    app.setOrganizationDomain("openquake.org")
    app.setApplicationName("Openquake NRML")
    app.setWindowIcon(QtGui.QIcon(":/logo.png"))

    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
