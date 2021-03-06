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
from plotly.graph_objs import Scatter, Box, Layout




FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/data_plot_dialog_base.ui'))


class DataPlotDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(DataPlotDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.scatterButton.clicked.connect(self.ScatterPlot)
        self.boxplotButton.clicked.connect(self.BoxPlot)
        self.barplotButton.clicked.connect(self.BarPlot)
        self.histogramplotButton.clicked.connect(self.HistogramPlot)
        self.pieplotButton.clicked.connect(self.PiePlot)
        self.scatter3DButton.clicked.connect(self.Scatter3DPlot)
        self.distplotButton.clicked.connect(self.DistPlot)
        self.polarButton.clicked.connect(self.PolarPlot)

    # Each function is linked to the button and it imports and allows to run the code of that plot type

    # Open scatter plot dialog
    def ScatterPlot(self):
        import plots.scatter_dialog as Scatter
        dlg = Scatter.ScatterPlotDialog()
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        dlg.exec_()


    # Open boxplot dialog
    def BoxPlot(self):
        import plots.box_dialog as Box
        dlg = Box.BoxPlotDialog()
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        dlg.exec_()


    # Open barplot dialog
    def BarPlot(self):
        import plots.bar_dialog as Bar
        dlg = Bar.BarPlotDialog()
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        dlg.exec_()


    # Open histogram dialog
    def HistogramPlot(self):
        import plots.histogram_dialog as Histogram
        dlg = Histogram.HistogramPlotDialog()
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        dlg.exec_()


    # Open pie plot dialog
    def PiePlot(self):
        import plots.pie_dialog as Pie
        dlg = Pie.PiePlotDialog()
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        dlg.exec_()


    # Open scatter 3D plot dialog
    def Scatter3DPlot(self):
        import plots.scatter3D_dialog as Scatter3D
        dlg = Scatter3D.Scatter3DPlotDialog()
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        dlg.exec_()

    # Open distplot dialog
    def DistPlot(self):
        import plots.distplot_dialog as Dist
        dlg = Dist.DistPlotDialog()
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        dlg.exec_()

    # Open polar plot dialog
    def PolarPlot(self):
        import plots.polar_plot_dialog as Polar
        dlg = Polar.PolarPlotDialog()
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        dlg.exec_()
