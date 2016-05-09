# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DataPlotDialog
                                 A QGIS plugin
 High level charts
                             -------------------
        begin                : 2016-04-27
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Matteo Ghetta
        email                : matteo.ghetta@gmail.com
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView
from qgis.gui import *
import plotly
import plotly.graph_objs as go


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), '../ui/Bar.ui'))

class BarPlotDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(BarPlotDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.Bar)

        # connect button to choose the file for local saving
        self.browseButton.clicked.connect(self.saveFile)

    # function to store the path of the opened folder when saving the plot
    def saveFile(self):
        self.filePath.setText(QFileDialog.getOpenFileName())



    def Bar(self):

        # get layer and the selected fields (signals and update directly in the UI)
        lay1 = self.Field1.layer()
        lay1_f = self.Field1.currentField()
        lay2 = self.Field2.layer()
        lay2_f = self.Field2.currentField()


        # build the lists from the selected fields
        f1 = []
        for i in lay1.getFeatures():
            f1.append(i[lay1_f])

        f2 = []
        for i in lay2.getFeatures():
            f2.append(i[lay2_f])

        # legend checkbox (default is checked = True)
        if self.legendCheck.isChecked():
            legend = True
        else:
            legend = False



        # initialize the Bar plot with the first trace
        trace = go.Bar(
        x = f1,
        y = f2
        )

        # build the data object
        data = [trace]

        # build the layout object
        layout = go.Layout(
        showlegend = legend
        )

        # build the final figure
        fig = go.Figure(data=data, layout=layout)


        # name of the local file
        name = self.filePath.text() + '.html'
        name = str(name)

        # final function that draws the plot
        plotly.offline.plot(fig, filename=name)