#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


def create_action(main_window, text=None, signal="triggered()", slot=None,
        shortcut=None, icon=None, tip=None):
    """
    Helper method to create QtAction objects.
    """

    icon_str = ":/%s.png"
    action = QtGui.QAction(main_window)
    if text is not None:
        action.setText(text)
    if icon is not None:
        action.setIcon(QtGui.QIcon(icon_str % icon))
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if slot is not None:
        main_window.connect(action, QtCore.SIGNAL(signal), slot)
    return action
