from qgis.gui import QgsMapTool, QgsMapToolIdentify
from qgis.core import QgsMapLayer, QgsFeature, QgsFeatureRequest, QgsGeometry, QgsMessageLog
from PyQt4.QtGui import QCursor, QPixmap
from PyQt4.QtCore import Qt


class IdentifyFeature(QgsMapToolIdentify):

    def __init__(self, canvas):

        super(QgsMapToolIdentify, self).__init__(canvas)
        self.canvas = canvas
        self.cursor = QCursor(Qt.CrossCursor)

    def activate(self):
        self.canvas.setCursor(self.cursor)

    def canvasReleaseEvent(self, mouseEvent):
        x = mouseEvent.x()
        y = mouseEvent.y()
        QgsMessageLog.logMessage("Feature x: {}  y: {}".format(x, y), 'DocLinker')
        id_feat = self.identify(x,y,self.ActiveLayer,self.VectorLayer)
        QgsMessageLog.logMessage("Feature ID: {} ".format(id_feat[0].mFeature.attribute('ID')), 'DocLinker')
        # Afficher la fenêtre lors du clic sur le feature
