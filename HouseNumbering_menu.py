#from __future__ import absolute_import
# --------------------------------------------------------
#    QuickMultiAttributeEdit_menu - QGIS plugins menu class
#
#    begin                : May 9, 2011
#    copyright            : (c) 2011 by Marco Braida
#    email                : marcobra.ubuntu at gmail.com
#
#   QuickMultiAttributeEdit is free software and is offered 
#   without guarantee or warranty. You can redistribute it 
#   and/or modify it under the terms of version 2 of the 
#   GNU General Public License (GPL v2) as published by the 
#   Free Software Foundation (www.gnu.org).
# --------------------------------------------------------
from builtins import object
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *

from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *

from .HouseNumbering_dialogs import *

# ---------------------------------------------

class HouseNumbering_menu:
	def __init__(self, iface):
		self.iface = iface
		self.dlg = None

	def initGui(self):
		icon = QIcon(os.path.dirname(__file__) + "/icons/housenumbering.png")
		self.update_selected_action = QAction(icon, "Auto numbering field of selected features", self.iface.mainWindow())

		self.update_selected_action.triggered.connect(self.update_selected)
		self.iface.registerMainWindowAction(self.update_selected_action, "F9") # self.update_selected_action is triggered by the F12

		self.iface.addToolBarIcon(self.update_selected_action)
		self.iface.addPluginToMenu("&HouseNumbering", self.update_selected_action)
		#self.iface.layerMenu().findChild(QMenu, 'menuNew').addAction(self.action)


	def unload(self):
		self.iface.unregisterMainWindowAction(self.update_selected_action)
		self.iface.removeToolBarIcon(self.update_selected_action)
		self.iface.removePluginMenu("&HouseNumbering", self.update_selected_action)

	def update_selected(self):
		dialog = HouseNumbering_update_selected_dialog(self.iface)
		dialog.exec_()

	
