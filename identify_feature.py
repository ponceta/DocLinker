from qgis.gui import QgsMapTool, QgsMapToolIdentify
from qgis.core import QgsMapLayer, QgsFeature, QgsFeatureRequest, QgsGeometry, QgsMessageLog
from PyQt4.QtGui import QCursor, QPixmap
from PyQt4.QtCore import Qt
from PyQt4 import QtCore
from document_linker_dialog import DocumentLinkerDialog

class IdentifyFeature(QgsMapToolIdentify):

    signal_select = QtCore.pyqtSignal(QgsFeature)

    def __init__(self, canvas):

        super(QgsMapToolIdentify, self).__init__(canvas)
        self.canvas = canvas
        self.cursor = QCursor(Qt.CrossCursor)
        self.dlg = DocumentLinkerDialog(self)
        self.signal_select.connect(self.openDialog)
        self.signal_select.connect(self.dlg.updateFeatureFilename)

    def activate(self):
        self.canvas.setCursor(self.cursor)

    def canvasReleaseEvent(self, mouseEvent):
        x = mouseEvent.x()
        y = mouseEvent.y()
        QgsMessageLog.logMessage("Feature x: {}  y: {}".format(x, y), 'DocLinker')
        id_feat = self.identify(x,y,self.ActiveLayer,self.VectorLayer)
        #QgsMessageLog.logMessage("Feature ID: {} ".format(id_feat[0].mFeature.attribute('ID')), 'DocLinker')
        # Afficher la fenetre lors du clic sur le feature
        if id_feat[0] is not None:
            self.signal_select.emit(id_feat[0].mFeature)
        else:
            pass

    def openDialog(self, feature):
        # show the dialog
        self.dlg.lineEdit_ID.setText(str(feature.attribute('ID')))
        self.dlg.lineEdit_TYPE.setText(feature.attribute('TYPE').encode('UTF8'))
        self.dlg.lineEdit_REMARK.setText(feature.attribute('REMARK').encode('UTF8'))
        self.dlg.show()


