# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DocumentLinker
                                 A QGIS plugin
 This plugin enables to drag and store a file to qgis 
                             -------------------
        begin                : 2016-04-27
        copyright            : (C) 2016 by QWAT Users Lausanne
        email                : arnaud.poncet-montanges@outlook.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DocumentLinker class from file DocumentLinker.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .document_linker import DocumentLinker
    return DocumentLinker(iface)
