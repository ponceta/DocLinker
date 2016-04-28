# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DocumentLinkerDialog
                                 A QGIS plugin
 This plugin enables to drag and store a file to qgis 
                             -------------------
        begin                : 2016-04-27
        git sha              : $Format:%H$
        copyright            : (C) 2016 by QWAT Users Lausanne
        email                : arnaud.poncet-montanges@outlook.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from qgis.core import QgsMessageLog


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'document_linker_dialog_base.ui'))


class DocumentLinkerDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent):
        """Constructor."""
        super(DocumentLinkerDialog, self).__init__(None)
        self.parent = parent
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def dragEnterEvent(self, event):
        #Tester le mimetype du fichier draguer
        if self.parent.canvas.currentLayer().isEditable():
            event.acceptProposedAction()
        QgsMessageLog.logMessage("On est dans dragEnterEvent", 'DocLinker')

    def dropEvent(self, event):
        QgsMessageLog.logMessage("On est dans dropEvent", 'DocLinker')
        if event.mimeData().hasUrls():
            self.image_url = event.mimeData().urls()[0]
            QgsMessageLog.logMessage("URL du fichier: {}".format(self.image_url), 'DocLinker')
            file_dialog = QtGui.QFileDialog(self)
            file_dialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
            file_dialog.setDirectory(os.path.expanduser('~'))
            file_dialog.show()
            file_dialog.fileSelected.connect(self.updateDialog)

    def updateDialog(self, filename):
        self.lineEdit_LINK_IMAGE.setText(filename)
        myImage = QtGui.QPixmap()
        myImage.load(self.image_url.path())
        self.dropzoneLabel.setPixmap(myImage)
        myImage.save(filename)

    def updateFeatureFilename(self, feature):
        feature.setAttribute('LINK_IMAGE', self.lineEdit_LINK_IMAGE.text())
