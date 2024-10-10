from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QHBoxLayout, QSpinBox, QSlider, QDialog, QVBoxLayout, QLabel, QPushButton, QApplication, QGraphicsPixmapItem, QInputDialog
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb
from skimage.morphology import skeletonize, thin
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import tempfile
import os
import cv2
from PIL import Image
import numpy as np
from crop2 import Crop2
from histogram2 import Histogram2
from PyQt5 import QtCore, QtGui, QtWidgets
from menuSegmentasi import MenuSegmentasi as ms
from aritmatika_panel import Ui_AritmatikaOperation



from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QHBoxLayout,QSpinBox, QSlider, QDialog, QVBoxLayout, QLabel, QPushButton, QApplication, QGraphicsPixmapItem, QInputDialog



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 30, 461, 421))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(560, 30, 461, 421))
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 25))
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHologram = QtWidgets.QMenu(self.menuView)
        self.menuHologram.setObjectName("menuHologram")
        self.menuShow = QtWidgets.QMenu(self.menubar)
        self.menuShow.setObjectName("menuShow")
        self.menuRGB = QtWidgets.QMenu(self.menuShow)
        self.menuRGB.setObjectName("menuRGB")
        self.menuRGB_to_Grayscale = QtWidgets.QMenu(self.menuShow)
        self.menuRGB_to_Grayscale.setObjectName("menuRGB_to_Grayscale")
        self.menuBrightness = QtWidgets.QMenu(self.menuShow)
        self.menuBrightness.setObjectName("menuBrightness")
        self.menuBit_Depth = QtWidgets.QMenu(self.menuShow)
        self.menuBit_Depth.setObjectName("menuBit_Depth")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImage_Processing = QtWidgets.QMenu(self.menubar)
        self.menuImage_Processing.setObjectName("menuImage_Processing")
        self.menuAritmetical_Operation = QtWidgets.QMenu(self.menubar)
        self.menuAritmetical_Operation.setObjectName("menuAritmetical_Operation")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menuFilter)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuGaussian_Blur = QtWidgets.QMenu(self.menuFilter)
        self.menuGaussian_Blur.setObjectName("menuGaussian_Blur")
        self.menuEdge_Detection_2 = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection_2.setObjectName("menuEdge_Detection_2")
        self.menuMarfologi = QtWidgets.QMenu(self.menubar)
        self.menuMarfologi.setObjectName("menuMarfologi")
        self.menuErosion = QtWidgets.QMenu(self.menuMarfologi)
        self.menuErosion.setObjectName("menuErosion")
        self.menuDilation = QtWidgets.QMenu(self.menuMarfologi)
        self.menuDilation.setObjectName("menuDilation")
        self.menuOpening = QtWidgets.QMenu(self.menuMarfologi)
        self.menuOpening.setObjectName("menuOpening")
        self.menuClosing = QtWidgets.QMenu(self.menuMarfologi)
        self.menuClosing.setObjectName("menuClosing")
        self.menuSegmentasi = QtWidgets.QMenu(self.menubar)
        self.menuSegmentasi.setObjectName("menuSegmentasi")
        self.menuTentang = QtWidgets.QMenu(self.menubar)
        self.menuTentang.setObjectName("menuTentang")
        self.menuTentang.addAction("Kelompok", self.show_group_info)
        self.menubar.addMenu(self.menuTentang)

        self.menuReset = QtWidgets.QMenu(self.menubar)
        self.menuReset.setObjectName("menuReset")
        self.menuGeometri = QtWidgets.QMenu(self.menubar)
        self.menuGeometri.setObjectName("menuGeometri")
        self.menuFlipping = QtWidgets.QMenu(self.menuGeometri)
        self.menuFlipping.setObjectName("menuFlipping")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Initialize a scene for the GraphicsView
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        # Initialize a scene for the output
        self.sceneOutput = QGraphicsScene()
        self.graphicsView_2.setScene(self.sceneOutput)
        self.actionBuka = QtWidgets.QAction(MainWindow)
        self.actionBuka.setCheckable(False)
        self.actionBuka.setObjectName("actionBuka")
        self.actionBuka.triggered.connect(self.openImage)
        self.actionSimpan_Sebagai = QtWidgets.QAction(MainWindow)
        self.actionSimpan_Sebagai.setObjectName("actionSimpan_Sebagai")
        self.actionSimpan_Sebagai.triggered.connect(self.saveAs)
        self.actionKeluar = QtWidgets.QAction(MainWindow)
        self.actionKeluar.setObjectName("actionKeluar")
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.actionInput.triggered.connect(self.histogram_input)
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.triggered.connect(self.histogram_output)
        self.actionOutput.setObjectName("actionOutput")
        self.actionInput_Output = QtWidgets.QAction(MainWindow)
        self.actionInput_Output.setObjectName("actionInput_Output")
        self.actionInput_Output.triggered.connect(self.histogram_input_output)
        self.actionBrightness_Contrast = QtWidgets.QAction(MainWindow)
        self.actionBrightness_Contrast.setObjectName("actionBrightness_Contrast")
        self.actionInvers = QtWidgets.QAction(MainWindow)
        self.actionInvers.setObjectName("actionInvers")
        self.actionInvers.triggered.connect(self.Invers)
        self.actionLog_Brightness = QtWidgets.QAction(MainWindow)
        self.actionLog_Brightness.setObjectName("actionLog_Brightness")
        self.actionLog_Brightness.triggered.connect(self.log_brightness)
        self.actionGamma_Correction = QtWidgets.QAction(MainWindow)
        self.actionGamma_Correction.setObjectName("actionGamma_Correction")
        self.actionGamma_Correction.triggered.connect(self.show_gamma_dialog)
        self.actionKuning = QtWidgets.QAction(MainWindow)
        self.actionKuning.setObjectName("actionKuning")
        self.actionKuning.triggered.connect(self.filter_kuning)
        self.actionOrange = QtWidgets.QAction(MainWindow)
        self.actionOrange.setObjectName("actionOrange")
        self.actionOrange.triggered.connect(self.filter_orange)
        self.actionCyan = QtWidgets.QAction(MainWindow)
        self.actionCyan.setObjectName("actionCyan")
        self.actionCyan.triggered.connect(self.filter_cyan)
        self.actionPurple = QtWidgets.QAction(MainWindow)
        self.actionPurple.setObjectName("actionPurple")
        self.actionPurple.triggered.connect(self.filter_purple)
        self.actionGrey = QtWidgets.QAction(MainWindow)
        self.actionGrey.setObjectName("actionGrey")
        self.actionGrey.triggered.connect(self.filter_grey)
        self.actionCoklat = QtWidgets.QAction(MainWindow)
        self.actionCoklat.setObjectName("actionCoklat")
        self.actionCoklat.triggered.connect(self.filter_coklat)
        self.actionAverage = QtWidgets.QAction(MainWindow)
        self.actionAverage.setObjectName("actionAverage")
        self.actionAverage.triggered.connect(self.average)
        self.actionLightness = QtWidgets.QAction(MainWindow)
        self.actionLightness.setObjectName("actionLightness")
        self.actionLightness.triggered.connect(self.lightness)
        self.actionLuminace = QtWidgets.QAction(MainWindow)
        self.actionLuminace.setObjectName("actionLuminace")
        self.actionLuminace.triggered.connect(self.luminance)
        self.actionContrast = QtWidgets.QAction(MainWindow)
        self.actionContrast.setObjectName("actionContrast")
        self.actionContrast.triggered.connect(self.show_contrast_slider)
        self.action1_bit = QtWidgets.QAction(MainWindow)
        self.action1_bit.setObjectName("action1_bit")
        self.action1_bit.triggered.connect(lambda: self.bit_depht(1))
        self.action2_bit = QtWidgets.QAction(MainWindow)
        self.action2_bit.setObjectName("action2_bit")
        self.action2_bit.triggered.connect(lambda: self.bit_depht(2))
        self.action3_bit = QtWidgets.QAction(MainWindow)
        self.action3_bit.setObjectName("action3_bit")
        self.action3_bit.triggered.connect(lambda: self.bit_depht(3))
        self.action4_bit = QtWidgets.QAction(MainWindow)
        self.action4_bit.setObjectName("action4_bit")
        self.action4_bit.triggered.connect(lambda: self.bit_depht(4))
        self.action5_bit = QtWidgets.QAction(MainWindow)
        self.action5_bit.setObjectName("action5_bit")
        self.action5_bit.triggered.connect(lambda: self.bit_depht(5))
        self.action6_bit = QtWidgets.QAction(MainWindow)
        self.action6_bit.setObjectName("action6_bit")
        self.action6_bit.triggered.connect(lambda: self.bit_depht(6))
        self.action7_bit = QtWidgets.QAction(MainWindow)
        self.action7_bit.setObjectName("action7_bit")
        self.action7_bit.triggered.connect(lambda: self.bit_depht(7))
        self.action8_bit = QtWidgets.QAction(MainWindow)
        self.action8_bit.setObjectName("action8_bit")
        self.action8_bit.triggered.connect(lambda: self.bit_depht(8))
        self.actionHistogram_Equalization = QtWidgets.QAction(MainWindow)
        self.actionHistogram_Equalization.setObjectName("actionHistogram_Equalization")
        self.actionHistogram_Equalization.triggered.connect(self.histogram_equalization)
        self.actionFuzzy_HE_RGB = QtWidgets.QAction(MainWindow)
        self.actionFuzzy_HE_RGB.setObjectName("actionFuzzy_HE_RGB")
        # self.actionFuzzy_HE_RGB.triggered.connect(self.fuzzy_rgb)
        self.actionFUZZY_Grayscale = QtWidgets.QAction(MainWindow)
        self.actionFUZZY_Grayscale.setObjectName("actionFUZZY_Grayscale")
        # self.actionFUZZY_Grayscale.triggered.connect(self.fuzzy_grayscale)
        self.actionIdentify = QtWidgets.QAction(MainWindow)
        self.actionIdentify.setObjectName("actionIdentify")
        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionUnsharp_Masking = QtWidgets.QAction(MainWindow)
        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")
        self.actionAvarage_Filter = QtWidgets.QAction(MainWindow)
        self.actionAvarage_Filter.setObjectName("actionAvarage_Filter")
        self.actionLow_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")
        self.actionHigh_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionHigh_Pass_Filter.setObjectName("actionHigh_Pass_Filter")
        self.actionBandstop_Filter = QtWidgets.QAction(MainWindow)
        self.actionBandstop_Filter.setObjectName("actionBandstop_Filter")
        self.actionEdge_Detection_1 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_1.setObjectName("actionEdge_Detection_1")
        self.actionEdge_Detection_2 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_2.setObjectName("actionEdge_Detection_2")
        self.actionEdge_Detection_3 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_3.setObjectName("actionEdge_Detection_3")
        self.actionGaussian_Blur_3x3 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_3x3.setObjectName("actionGaussian_Blur_3x3")
        self.actionGaussian_Blur_5x5 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_5x5.setObjectName("actionGaussian_Blur_5x5")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionPrewitt.triggered.connect(self.prewitt)
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionSobel.triggered.connect(self.Sobel)
        self.actionCanny = QtWidgets.QAction(MainWindow)
        self.actionCanny.setObjectName("actionCanny")
        self.actionCanny.triggered.connect(self.canny)
        self.actionSquare_3 = QtWidgets.QAction(MainWindow)
        self.actionSquare_3.setObjectName("actionSquare_3")
        self.actionSquare_3.triggered.connect(lambda: self.erosion('square', 3))
        self.actionSquare_5 = QtWidgets.QAction(MainWindow)
        self.actionSquare_5.setObjectName("actionSquare_5")
        self.actionSquare_5.triggered.connect(lambda: self.erosion('square', 5))
        self.actionCross_3 = QtWidgets.QAction(MainWindow)
        self.actionCross_3.setObjectName("actionCross_3")
        self.actionCross_3.triggered.connect(lambda: self.erosion('cross', 3))

        self.actionSquare_4 = QtWidgets.QAction(MainWindow)
        self.actionSquare_4.setObjectName("actionSquare_4")
        self.actionSquare_4.triggered.connect(lambda: self.dilation('square', 4))
        self.actionSquare_6 = QtWidgets.QAction(MainWindow)
        self.actionSquare_6.setObjectName("actionSquare_6")
        self.actionSquare_6.triggered.connect(lambda: self.dilation('square', 6))
        self.actionCross_4 = QtWidgets.QAction(MainWindow)
        self.actionCross_4.setObjectName("actionCross_4")
        self.actionCross_4.triggered.connect(lambda: self.dilation('cross', 4))
        
        self.actionSquare_9 = QtWidgets.QAction(MainWindow)
        self.actionSquare_9.setObjectName("actionSquare_9")
        self.actionSquare_9.triggered.connect(lambda: self.opening('square', 9))
        self.actionSquare_10 = QtWidgets.QAction(MainWindow)
        self.actionSquare_10.setObjectName("actionSquare_10")
        self.actionSquare_10.triggered.connect(lambda: self.closing('square', 10))
        self.actionSturatioin = QtWidgets.QAction(MainWindow)
        self.actionSturatioin.setObjectName("actionSturatioin")
        self.actionSturatioin.triggered.connect(self.show_saturation_slider)
        self.actionlinearBrightness = QtWidgets.QAction(MainWindow)
        self.actionlinearBrightness.setObjectName("actionlinearBrightness")
        self.actionlinearBrightness.triggered.connect(self.show_brightness_slider)
        self.actionScaling_Uniform = QtWidgets.QAction(MainWindow)
        self.actionScaling_Uniform.setObjectName("actionScaling_Uniform")
        self.actionScaling_Uniform.triggered.connect(self.scalingUniform)
        self.actionScaling_Non_Uniform = QtWidgets.QAction(MainWindow)
        self.actionScaling_Non_Uniform.setObjectName("actionScaling_Non_Uniform")
        self.actionScaling_Non_Uniform.triggered.connect(self.scalingNonUniform)
        self.actionCropping = QtWidgets.QAction(MainWindow)
        self.actionCropping.setObjectName("actionCropping")
        self.actionCropping.triggered.connect(self.show_crop_dialog)
        self.actionTranslasi = QtWidgets.QAction(MainWindow)
        self.actionTranslasi.setObjectName("actionTranslasi")
        self.actionTranslasi.triggered.connect(self.translasi)
        self.actionRotasi = QtWidgets.QAction(MainWindow)
        self.actionRotasi.setObjectName("actionRotasi")
        self.actionRotasi.triggered.connect(self.rotasi)
        self.actionFlipping_Horizontal = QtWidgets.QAction(MainWindow)
        self.actionFlipping_Horizontal.setObjectName("actionFlipping_Horizontal")
        self.actionFlipping_Horizontal.triggered.connect(self.flip_Horizontal)
        self.actionFlipping_Vertical = QtWidgets.QAction(MainWindow)
        self.actionFlipping_Vertical.setObjectName("actionFlipping_Vertical")
        self.actionFlipping_Vertical.triggered.connect(self.flip_Vertical)
        self.menuSegmentasi = QtWidgets.QMenu(self.menubar)
        self.menuSegmentasi.setObjectName("menuSegmentasi")
        self.actionRegion_Growing = QtWidgets.QAction(MainWindow)
        self.actionRegion_Growing.setObjectName("actionRegion_Growing")
        self.actionRegion_Growing.triggered.connect(self.show_dialog_regiongrow)
        self.actionKmeans_Clustering = QtWidgets.QAction(MainWindow)
        self.actionKmeans_Clustering.setObjectName("actionKmeans_Clustering")
        self.actionKmeans_Clustering.triggered.connect(self.show_segment_cluster)
        self.actionWatershed_Segmentation = QtWidgets.QAction(MainWindow)
        self.actionWatershed_Segmentation.setObjectName("actionWatershed_Segmentation")
        self.actionWatershed_Segmentation.triggered.connect(self.segment_watershed)
        #global
        self.actionGlobal_Thresholding = QtWidgets.QAction(MainWindow)
        self.actionGlobal_Thresholding.setObjectName("actionGlobal_Thresholding")
        self.actionGlobal_Thresholding.triggered.connect(self.show_segment_globalthreshold)
        self.actionAdaptive_Thresh_Mean = QtWidgets.QAction(MainWindow)
        self.actionAdaptive_Thresh_Mean.setObjectName("actionAdaptive_Thresh_Mean")
        self.actionAdaptive_Thresh_Mean.triggered.connect(self.segment_adaptive_thresh_mean)
        self.actionAdaptive_Thresh_Gaussian = QtWidgets.QAction(MainWindow)
        self.actionAdaptive_Thresh_Gaussian.setObjectName("actionAdaptive_Thresh_Gaussian")
        self.actionAdaptive_Thresh_Gaussian.triggered.connect(self.segment_adaptive_thresh_gaussian)
        
        self.menuAritmetical_Operation = QtWidgets.QMenu(self.menubar)
        self.menuAritmetical_Operation.setObjectName("menuAritmetical_Operation")
        self.menuAritmetical_Operation.aboutToShow.connect(self.show_aritmetical)

        self.actionHitOrMiss = QtWidgets.QAction(MainWindow)
        self.actionHitOrMiss.setObjectName("actionHitOrMiss")
        self.actionHitOrMiss.triggered.connect(self.kernel_hit_or_miss)
        self.actionTinning = QtWidgets.QAction(MainWindow)
        self.actionTinning.setObjectName("actionTinning")
        self.actionTinning.triggered.connect(self.thinned_img)
        self.actionThickening = QtWidgets.QAction(MainWindow)
        self.actionThickening.setObjectName("actionThickening")
        self.actionThickening.triggered.connect(self.thickening)
        self.actionSkeleton = QtWidgets.QAction(MainWindow)
        self.actionSkeleton.setObjectName("actionSkeleton")
        self.actionSkeleton.triggered.connect(self.skeleton)
        self.actionPruning = QtWidgets.QAction(MainWindow)
        self.actionPruning.setObjectName("actionPruning")
        self.actionPruning.triggered.connect(lambda: self.prune_skeleton(2))

        self.menuHologram.addAction(self.actionInput)
        self.menuHologram.addSeparator()
        self.menuHologram.addAction(self.actionOutput)
        self.menuHologram.addSeparator()
        self.menuHologram.addAction(self.actionInput_Output)
        self.menuView.addAction(self.menuHologram.menuAction())
        self.menuRGB.addAction(self.actionKuning)
        self.menuRGB.addAction(self.actionOrange)
        self.menuRGB.addAction(self.actionCyan)
        self.menuRGB.addAction(self.actionPurple)
        self.menuRGB.addAction(self.actionGrey)
        self.menuRGB.addAction(self.actionCoklat)
        self.menuRGB_to_Grayscale.addAction(self.actionAverage)
        self.menuRGB_to_Grayscale.addAction(self.actionLightness)
        self.menuRGB_to_Grayscale.addAction(self.actionLuminace)
        self.menuBrightness.addAction(self.actionContrast)
        self.menuBrightness.addAction(self.actionSturatioin)
        self.menuBrightness.addAction(self.actionlinearBrightness)
        self.menuBit_Depth.addAction(self.action1_bit)
        self.menuBit_Depth.addAction(self.action2_bit)
        self.menuBit_Depth.addAction(self.action3_bit)
        self.menuBit_Depth.addAction(self.action4_bit)
        self.menuBit_Depth.addAction(self.action5_bit)
        self.menuBit_Depth.addAction(self.action6_bit)
        self.menuBit_Depth.addAction(self.action7_bit)
        self.menuBit_Depth.addAction(self.action8_bit)
        self.menuShow.addAction(self.menuRGB.menuAction())
        self.menuShow.addAction(self.menuRGB_to_Grayscale.menuAction())
        self.menuShow.addAction(self.menuBrightness.menuAction())
        self.menuShow.addAction(self.actionInvers)
        self.menuShow.addAction(self.actionLog_Brightness)
        self.menuShow.addAction(self.menuBit_Depth.menuAction())
        self.menuShow.addAction(self.actionGamma_Correction)
        self.menuFile.addAction(self.actionBuka)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSimpan_Sebagai)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionKeluar)
        self.menuImage_Processing.addAction(self.actionHistogram_Equalization)
        self.menuImage_Processing.addAction(self.actionFuzzy_HE_RGB)
        self.menuImage_Processing.addAction(self.actionFUZZY_Grayscale)
        self.menuEdge_Detection.addAction(self.actionEdge_Detection_1)
        self.menuEdge_Detection.addAction(self.actionEdge_Detection_2)
        self.menuEdge_Detection.addAction(self.actionEdge_Detection_3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_3x3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_5x5)
        self.menuFilter.addAction(self.actionIdentify)
        self.menuFilter.addAction(self.menuEdge_Detection.menuAction())
        self.menuFilter.addAction(self.actionSharpen)
        self.menuFilter.addAction(self.menuGaussian_Blur.menuAction())
        self.menuFilter.addAction(self.actionUnsharp_Masking)
        self.menuFilter.addAction(self.actionAvarage_Filter)
        self.menuFilter.addAction(self.actionLow_Pass_Filter)
        self.menuFilter.addAction(self.actionHigh_Pass_Filter)
        self.menuFilter.addAction(self.actionBandstop_Filter)
        self.menuEdge_Detection_2.addAction(self.actionPrewitt)
        self.menuEdge_Detection_2.addAction(self.actionSobel)
        self.menuEdge_Detection_2.addAction(self.actionCanny)
        self.menuErosion.addAction(self.actionSquare_3)
        self.menuErosion.addAction(self.actionSquare_5)
        self.menuErosion.addAction(self.actionCross_3)
        self.menuDilation.addAction(self.actionSquare_4)
        self.menuDilation.addAction(self.actionSquare_6)
        self.menuDilation.addAction(self.actionCross_4)
        self.menuOpening.addAction(self.actionSquare_9)
        self.menuClosing.addAction(self.actionSquare_10)
        self.menuMarfologi.addAction(self.menuErosion.menuAction())
        self.menuMarfologi.addAction(self.menuDilation.menuAction())
        self.menuMarfologi.addAction(self.menuOpening.menuAction())
        self.menuMarfologi.addAction(self.menuClosing.menuAction())
        self.menuMarfologi.addAction(self.actionHitOrMiss)
        self.menuMarfologi.addAction(self.actionTinning)
        self.menuMarfologi.addAction(self.actionThickening)
        self.menuMarfologi.addAction(self.actionSkeleton)
        self.menuMarfologi.addAction(self.actionPruning)
        self.menuFlipping.addAction(self.actionFlipping_Horizontal)
        self.menuFlipping.addAction(self.actionFlipping_Vertical)
        self.menuGeometri.addAction(self.menuFlipping.menuAction())
        self.menuGeometri.addAction(self.actionScaling_Uniform)
        self.menuGeometri.addAction(self.actionScaling_Non_Uniform)
        self.menuGeometri.addAction(self.actionCropping)
        self.menuGeometri.addAction(self.actionTranslasi)
        self.menuGeometri.addAction(self.actionRotasi)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuShow.menuAction())
        self.menubar.addAction(self.menuImage_Processing.menuAction())
        self.menubar.addAction(self.menuAritmetical_Operation.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuEdge_Detection_2.menuAction())
        self.menubar.addAction(self.menuMarfologi.menuAction())
        self.menubar.addAction(self.menuGeometri.menuAction())
        self.menubar.addAction(self.menuSegmentasi.menuAction())
        self.menuSegmentasi.addAction(self.actionRegion_Growing)
        self.menuSegmentasi.addAction(self.actionKmeans_Clustering)
        self.menuSegmentasi.addAction(self.actionWatershed_Segmentation)
        self.menuSegmentasi.addAction(self.actionGlobal_Thresholding)
        self.menuSegmentasi.addAction(self.actionAdaptive_Thresh_Mean)
        self.menuSegmentasi.addAction(self.actionAdaptive_Thresh_Gaussian)
        self.menubar.addAction(self.menuTentang.menuAction())
        self.menubar.addAction(self.menuReset.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHologram.setTitle(_translate("MainWindow", "Histogram"))
        self.menuShow.setTitle(_translate("MainWindow", "Colors"))
        self.menuRGB.setTitle(_translate("MainWindow", "RGB"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuBrightness.setTitle(_translate("MainWindow", "Brightness"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Bit Depth"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuAritmetical_Operation.setTitle(_translate("MainWindow", "Aritmetical Operation"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuGaussian_Blur.setTitle(_translate("MainWindow", "Gaussian Blur"))
        self.menuEdge_Detection_2.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuMarfologi.setTitle(_translate("MainWindow", "Marfologi"))
        self.menuErosion.setTitle(_translate("MainWindow", "Erosion"))
        self.menuDilation.setTitle(_translate("MainWindow", "Dilation"))
        self.menuOpening.setTitle(_translate("MainWindow", "Opening"))
        self.menuClosing.setTitle(_translate("MainWindow", "Closing"))
        self.menuTentang.setTitle(_translate("MainWindow", "Tentang"))
        self.menuReset.setTitle(_translate("MainWindow", "Reset"))
        self.menuGeometri.setTitle(_translate("MainWindow", "Geometri"))
        self.menuFlipping.setTitle(_translate("MainWindow", "Flipping"))
        self.actionBuka.setText(_translate("MainWindow", "Buka"))
        self.actionSimpan_Sebagai.setText(_translate("MainWindow", "Simpan Sebagai ..."))
        self.actionKeluar.setText(_translate("MainWindow", "Keluar"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionInput_Output.setText(_translate("MainWindow", "Input Output"))
        self.actionBrightness_Contrast.setText(_translate("MainWindow", "Brightness - Contrast"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.actionLog_Brightness.setText(_translate("MainWindow", "Log Brightness"))
        self.actionGamma_Correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.actionKuning.setText(_translate("MainWindow", "Kuning"))
        self.actionOrange.setText(_translate("MainWindow", "Orange"))
        self.actionCyan.setText(_translate("MainWindow", "Cyan"))
        self.actionPurple.setText(_translate("MainWindow", "Purple"))
        self.actionGrey.setText(_translate("MainWindow", "Grey"))
        self.actionCoklat.setText(_translate("MainWindow", "Coklat"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.actionLuminace.setText(_translate("MainWindow", "Luminance"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))
        self.action1_bit.setText(_translate("MainWindow", "1 bit"))
        self.action2_bit.setText(_translate("MainWindow", "2 bit"))
        self.action3_bit.setText(_translate("MainWindow", "3 bit"))
        self.action4_bit.setText(_translate("MainWindow", "4 bit"))
        self.action5_bit.setText(_translate("MainWindow", "5 bit"))
        self.action6_bit.setText(_translate("MainWindow", "6 bit"))
        self.action7_bit.setText(_translate("MainWindow", "7 bit"))
        self.action8_bit.setText(_translate("MainWindow", "8 bit"))
        self.actionHistogram_Equalization.setText(_translate("MainWindow", "Histogram Equalization"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionFUZZY_Grayscale.setText(_translate("MainWindow", "FUZZY Grayscale"))
        self.actionIdentify.setText(_translate("MainWindow", "Identify"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        self.actionAvarage_Filter.setText(_translate("MainWindow", "Avarage Filter"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionHigh_Pass_Filter.setText(_translate("MainWindow", "High Pass Filter"))
        self.actionBandstop_Filter.setText(_translate("MainWindow", "Bandstop Filter"))
        self.actionEdge_Detection_1.setText(_translate("MainWindow", "Edge Detection 1"))
        self.actionEdge_Detection_2.setText(_translate("MainWindow", "Edge Detection  2"))
        self.actionEdge_Detection_3.setText(_translate("MainWindow", "Edge Detection 3"))
        self.actionGaussian_Blur_3x3.setText(_translate("MainWindow", "Gaussian Blur 3x3"))
        self.actionGaussian_Blur_5x5.setText(_translate("MainWindow", "Gaussian Blur 5x5"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionCanny.setText(_translate("MainWindow", "Canny"))
        self.actionSquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_4.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_6.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_4.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionSquare_10.setText(_translate("MainWindow", "Square 9"))
        self.actionHitOrMiss.setText(_translate("MainWindow", "Hit or Miss"))
        self.actionTinning.setText(_translate("MainWindow", "Thinning"))
        self.actionThickening.setText(_translate("MainWindow", "Thickening"))
        self.actionSkeleton.setText(_translate("MainWindow", "Skeleton"))
        self.actionPruning.setText(_translate("MainWindow", "Prunning"))
        self.actionSturatioin.setText(_translate("MainWindow", "Saturatioin"))
        self.actionlinearBrightness.setText(_translate("MainWindow", "Linear Brightness"))
        self.actionScaling_Uniform.setText(_translate("MainWindow", "Scaling Uniform"))
        self.actionScaling_Non_Uniform.setText(_translate("MainWindow", "Scaling Non Uniform"))
        self.actionCropping.setText(_translate("MainWindow", "Cropping"))
        self.actionTranslasi.setText(_translate("MainWindow", "Translasi"))
        self.actionRotasi.setText(_translate("MainWindow", "Rotasi"))
        self.actionFlipping_Horizontal.setText(_translate("MainWindow", "Flipping Horizontal"))
        self.actionFlipping_Vertical.setText(_translate("MainWindow", "Flipping Vertical"))
        self.menuSegmentasi.setTitle(_translate("MainWindow", "Segmentasi"))
        self.actionRegion_Growing.setText(_translate("Main Window", "Region Growing"))
        self.actionKmeans_Clustering.setText(_translate("Main Window", "Kmeans Clustering"))
        self.actionWatershed_Segmentation.setText(_translate("Main Window", "Watershed Segmentation"))
        self.actionGlobal_Thresholding.setText(_translate("Main Window", "Global Thresholding"))
        self.actionAdaptive_Thresh_Mean.setText(_translate("Main Window", "Adaptive Thresh Mean"))
        self.actionAdaptive_Thresh_Gaussian.setText(_translate("Main Window", "Adaptive Thresh Gaussian"))
    def __init__(self):
        self.imagePath = None
        self.image_pixmap = None  
        self.imagefile = None
        self.imageResult = None
        self.directory_input = None
        self.directory_output = None
        self.histogram_input_dialog = None  
        self.histogram_output_dialog = None

    
    def clear_scene(self):
        self.scene.clear()
        self.sceneOutput.clear()


    def openImage(self):
        # Show file dialog to select an image file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "Buka Gambar", "", "Image Files (*.png *.jpg *.bmp *.jpeg)", options=options)
        
        if fileName:
            self.imagePath = fileName
            self.directory_input = self.imagePath  # Tambahkan ini agar directory_input diisi
            img = Image.open(fileName)
            self.imagefile = img
            
            # Convert the image to QPixmap and display it
            self.image_pixmap = QtGui.QPixmap(fileName)
            view_width = self.graphicsView.width()
            view_height = self.graphicsView.height()
            scaled_pixmap = self.image_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)
            
            self.scene.clear()  # Clear any previous content in the scene
            self.scene.addPixmap(scaled_pixmap)
            self.graphicsView.setSceneRect(self.scene.itemsBoundingRect())

    def saveAs(self):
        # Periksa apakah ada gambar hasil (self.imageResult)
        if hasattr(self, 'imageResult') and self.imageResult is not None:
            # Buka dialog untuk memilih lokasi dan memberi nama file
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getSaveFileName(None, "Save Image As", "", "PNG Files (*.png);;JPEG Files (*.jpg);;BMP Files (*.bmp)", options=options)
            
            if fileName:
                # Simpan gambar ke lokasi yang dipilih dengan nama file baru
                self.imageResult.save(fileName)
                print(f"Gambar disimpan di: {fileName}")
            else:
                print("Penyimpanan dibatalkan.")
        else:
            print("Tidak ada gambar untuk disimpan.")

    
    def filter_kuning(self):
        image = self.imagefile

        # Pastikan gambar dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_np = np.array(image)

        # Apply yellow filter (increase red and green, remove blue)
        image_np[:, :, 2] = 0  # Remove blue component

        image_out = Image.fromarray(image_np.astype(np.uint8))
        self.imageResult = image_out

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear any previous content in the scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        # delete temp file
        os.remove(temp_file_path)


    def filter_orange(self):
        image = self.imagefile

        # Pastikan gambar dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_np = np.array(image)

        # Apply orange filter (reduce blue component)
        image_np[:, :, 2] = image_np[:, :, 2] // 2  # Reduce blue component

        image_out = Image.fromarray(image_np.astype(np.uint8))
        self.imageResult = image_out

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def filter_cyan(self):
        image = self.imagefile

        # Pastikan gambar dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_np = np.array(image)

        # Apply cyan filter (remove red component)
        image_np[:, :, 0] = 0  # Remove red component

        image_out = Image.fromarray(image_np.astype(np.uint8))
        self.imageResult = image_out

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def filter_purple(self):
        image = self.imagefile

        # Pastikan gambar dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_np = np.array(image)

        # Apply purple filter (remove green component)
        image_np[:, :, 1] = 0  # Remove green component

        image_out = Image.fromarray(image_np.astype(np.uint8))
        self.imageResult = image_out

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def filter_grey(self):
        image = self.imagefile

        # Pastikan gambar dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_np = np.array(image)

        # Convert to greyscale
        grey_image = np.mean(image_np, axis=2).astype(np.uint8)

        image_out = Image.fromarray(grey_image)
        self.imageResult = image_out

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def filter_coklat(self):
        image = self.imagefile

        # Pastikan gambar dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_np = np.array(image)

        # Apply brown filter (adjust red, green, blue components)
        brown_filter = image_np.copy()
        brown_filter[:, :, 0] = brown_filter[:, :, 0] // 2  # Reduce blue
        brown_filter[:, :, 1] = brown_filter[:, :, 1] // 3  # Reduce green

        image_out = Image.fromarray(brown_filter.astype(np.uint8))
        self.imageResult = image_out

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def filter_merah(self):
        image = self.imagefile

        # Pastikan gambar dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_np = np.array(image)

        # Apply red filter (remove green and blue components)
        image_np[:, :, 0] = 0  # Remove blue component
        image_np[:, :, 1] = 0  # Remove green component

        image_out = Image.fromarray(image_np.astype(np.uint8))
        self.imageResult = image_out

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)


    def luminance(self):
        image = self.imagefile
        image_np = np.array(image)

        def rgb_to_grayscale_luminance(image):
            return (0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2]).astype(np.uint8)

        grayscale_image = rgb_to_grayscale_luminance(image_np)

        output_image = Image.fromarray(grayscale_image)
        self.imageResult = output_image

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output_image.save(temp_file_path)

        img_pixmap = QtGui.QPixmap(temp_file_path)

        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  
        self.sceneOutput.addPixmap(scaled_pixmap)
      
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())
        
        # delete temp file
        os.remove(temp_file_path)

    def average(self):
        image = self.imagefile
        image_np = np.array(image)
        def rgb_to_grayscale_average(image):
            return np.mean(image, axis=2).astype(np.uint8)
        grayscale_image = rgb_to_grayscale_average(image_np)
        output_image = Image.fromarray(grayscale_image)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output_image.save(temp_file_path)
        img_pixmap = QtGui.QPixmap(temp_file_path)
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)
        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())
        os.remove(temp_file_path)

    def lightness(self):
    # Pastikan gambar sudah dimuat
        if hasattr(self, 'imagefile'):
            image = self.imagefile
            image_np = np.array(image)

            # Fungsi untuk mengubah RGB ke grayscale menggunakan metode lightness
            def rgb_to_grayscale_lightness(image_np):
                max_rgb = np.max(image_np, axis=2)
                min_rgb = np.min(image_np, axis=2)
                lightness = ((max_rgb + min_rgb) / 2).astype(np.uint8)
                return lightness

            # Konversi gambar ke grayscale menggunakan lightness method
            grayscale_image_np = rgb_to_grayscale_lightness(image_np)
            grayscale_image = Image.fromarray(grayscale_image_np)

            # Simpan gambar hasil grayscale ke self.imageResult agar bisa disimpan
            self.imageResult = grayscale_image

            # Simpan gambar ke file sementara untuk ditampilkan
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                temp_file_path = temp_file.name
                grayscale_image.save(temp_file_path)

            # Muat gambar dari file sementara ke QPixmap
            img_pixmap = QtGui.QPixmap(temp_file_path)

            # Mendapatkan ukuran QGraphicsView
            view_width = self.graphicsView_2.width()
            view_height = self.graphicsView_2.height()

            # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
            scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

            # Bersihkan konten sebelumnya di scene dan tambahkan scaled_pixmap
            self.sceneOutput.clear()
            self.sceneOutput.addPixmap(scaled_pixmap)
            self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

            # Hapus file sementara
            os.remove(temp_file_path)
        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Gambar belum dimuat.")
            
    def Invers(self):
        # Pastikan gambar sudah dimuat
        if hasattr(self, 'imagefile'):
            image = self.imagefile

            # Konversi gambar ke numpy array
            image_np = np.array(image)

            # Terapkan efek negative inverse (255 - pixel value)
            image_np = 255 - image_np

            # Konversi kembali ke format PIL image setelah efek diterapkan
            image_out = Image.fromarray(image_np.astype(np.uint8))

            # Simpan hasil gambar ke self.imageResult agar bisa disimpan
            self.imageResult = image_out

            # Simpan gambar hasil ke file sementara untuk ditampilkan di GUI
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                temp_file_path = temp_file.name
                image_out.save(temp_file_path)

            # Muat gambar dari file sementara ke QPixmap
            img_pixmap = QtGui.QPixmap(temp_file_path)

            # Mendapatkan ukuran QGraphicsView
            view_width = self.graphicsView_2.width()
            view_height = self.graphicsView_2.height()

            # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
            scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

            # Bersihkan konten sebelumnya dan tambahkan pixmap baru ke scene
            self.sceneOutput.clear()
            self.sceneOutput.addPixmap(scaled_pixmap)
            self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

            # Hapus file sementara setelah selesai
            os.remove(temp_file_path)
        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Gambar belum dimuat.")

    def log_brightness(self):
    # Membaca gambar dari direktori sebagai grayscale
        image = cv2.imread(self.imagePath, cv2.IMREAD_GRAYSCALE)

        # Konstanta untuk transformasi logaritmik
        c = 255 / np.log(1 + np.max(image))

        # Melakukan transformasi logaritmik
        log_transformed = c * np.log(1 + image)

        # Normalisasi gambar log transformasi
        log_transformed = (log_transformed - np.min(log_transformed)) / (np.max(log_transformed) - np.min(log_transformed)) * 255
        log_transformed = np.array(log_transformed, dtype=np.uint8)

        # Mengonversi array ke citra
        output_image = Image.fromarray(log_transformed)

        # Simpan gambar log transformasi ke file sementara
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output_image.save(temp_file_path)

        # Load gambar dari file sementara ke QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Mendapatkan ukuran QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Mengatur pixmap untuk skala agar sesuai dengan ukuran QGraphicsView dengan tetap menjaga rasio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        # Bersihkan konten sebelumnya di scene dan tambahkan scaled_pixmap
        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        # Hapus file sementara
        os.remove(temp_file_path)

    def show_gamma_dialog(self):
        # Create a dialog window for gamma correction
        dialog = QDialog(None)  # Set parent to None
        dialog.setWindowTitle("Gamma Correction")

        # Layout for dialog
        layout = QVBoxLayout()

        # Add the gamma slider (INISIALISASI SEBELUM DIGUNAKAN)
        self.gamma_slider = QSlider(Qt.Horizontal)  # Qt should be recognized now
        self.gamma_slider.setMinimum(1)  # Set minimum value (1.0)
        self.gamma_slider.setMaximum(300)  # Set maximum value (3.0 * 100 for precision)
        self.gamma_slider.setValue(100)  # Default value (1.0)
        self.gamma_slider.valueChanged.connect(self.update_gamma_label)  # Update label on slider change
        self.gamma_slider.valueChanged.connect(self.update_gamma)  # Apply gamma correction on slider change
        layout.addWidget(self.gamma_slider)

        # Label to show current gamma value
        self.gamma_label = QLabel(f"Gamma: {self.gamma_slider.value() / 100.0:.2f}")  # Digunakan setelah gamma_slider dibuat
        layout.addWidget(self.gamma_label)

        # OK button to close the dialog
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(dialog.accept)
        layout.addWidget(ok_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def update_gamma_label(self):
        # Update the label when the slider is moved
        gamma_value = self.gamma_slider.value() / 100.0
        self.gamma_label.setText(f"Gamma: {gamma_value:.2f}")
    
    def update_gamma(self):
        # Get gamma value from slider and apply gamma correction
        gamma_value = self.gamma_slider.value() / 100.0  # Convert slider value to gamma (1.0 - 3.0)
        self.gammacorrection(gamma=gamma_value)

    def gammacorrection(self, gamma=1.0):
        image = self.imagefile
        image_np = np.array(image)

        # Apply gamma correction
        gamma_corrected = np.array(255 * (image_np / 255) ** gamma, dtype='uint8')

        image_out = Image.fromarray(gamma_corrected)
        self.imageResult = image_out

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear any previous content in the scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        # Delete temp file
        os.remove(temp_file_path)

    def bit_depht(self, bit):
    # Path gambar input
        image_path = self.imagePath
        num_colors = bit

        # Fungsi kuantisasi citra
        def kuantisasi_image(image_path, num_colors):
            image = Image.open(image_path)
            image = image.convert('RGB')

            img_array = np.array(image)

            min_val = img_array.min()
            max_val = img_array.max()

            step_size = (max_val - min_val) / num_colors

            # Melakukan kuantisasi pada array gambar
            kuantisasi_array = (img_array // step_size) * step_size

            # Mengonversi kembali array yang sudah dikuantisasi ke gambar
            kuantisasi_image = Image.fromarray(kuantisasi_array.astype('uint8'))

            return kuantisasi_image

        # Kuantisasi gambar
        result_image = kuantisasi_image(image_path, num_colors)

        # Simpan gambar kuantisasi ke file sementara
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            result_image.save(temp_file_path)

        # Load gambar dari file sementara ke QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Mendapatkan ukuran QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Mengatur pixmap untuk skala agar sesuai dengan ukuran QGraphicsView dengan tetap menjaga rasio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        # Bersihkan konten sebelumnya di scene dan tambahkan scaled_pixmap
        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        # Hapus file sementara
        os.remove(temp_file_path)

    def histogram_equalization(self):
        image = cv2.imread(self.imagePath, cv2.IMREAD_GRAYSCALE)

        equalized_image = cv2.equalizeHist(image)

        output_image = Image.fromarray(equalized_image)
        self.imageResult = output_image

        # Save image ke temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output_image.save(temp_file_path)
        
        # Load image dari temp file ke QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get ukuran QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # scale pixmap ke QGraphicView
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear() #clear gambar yang ada di QGraphicview_2
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def flip_Horizontal(self):
        # Pastikan gambar telah dimuat ke self.imagefile
        if hasattr(self, 'imagefile'):
            # Mengambil gambar dari self.imagefile
            image = self.imagefile

            # Melakukan flip horizontal pada gambar menggunakan PIL
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

            # Simpan gambar hasil flip ke self.imageResult agar bisa disimpan dengan saveAs
            self.imageResult = flipped_image

            # Simpan gambar hasil ke file sementara
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                temp_file_path = temp_file.name
                flipped_image.save(temp_file_path)

            # Muat gambar dari file sementara ke QPixmap
            img_pixmap = QPixmap(temp_file_path)

            # Mendapatkan ukuran QGraphicsView
            view_width = self.graphicsView_2.width()
            view_height = self.graphicsView_2.height()

            # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
            scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

            # Bersihkan konten sebelumnya dan tambahkan pixmap baru ke scene
            self.sceneOutput.clear()
            self.sceneOutput.addPixmap(scaled_pixmap)
            self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

            # Hapus file sementara
            os.remove(temp_file_path)
        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Gambar belum dimuat.")

    def flip_Vertical(self):
        # Pastikan gambar telah dimuat ke self.imagefile
        if hasattr(self, 'imagefile'):
            # Mengambil gambar dari self.imagefile
            image = self.imagefile

            # Melakukan flip vertical pada gambar menggunakan PIL
            flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)

            # Simpan gambar hasil flip ke self.imageResult agar bisa disimpan dengan saveAs
            self.imageResult = flipped_image

            # Simpan gambar hasil ke file sementara
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                temp_file_path = temp_file.name
                flipped_image.save(temp_file_path)

            # Muat gambar dari file sementara ke QPixmap
            img_pixmap = QPixmap(temp_file_path)

            # Mendapatkan ukuran QGraphicsView
            view_width = self.graphicsView_2.width()
            view_height = self.graphicsView_2.height()

            # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
            scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

            # Bersihkan konten sebelumnya dan tambahkan pixmap baru ke scene
            self.sceneOutput.clear()
            self.sceneOutput.addPixmap(scaled_pixmap)
            self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

            # Hapus file sementara
            os.remove(temp_file_path)
        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Gambar belum dimuat.")

    def translasi(self):
        # Pastikan gambar telah dimuat ke self.imagefile
        if hasattr(self, 'imagefile'):
            # Mengambil gambar dari self.imagefile
            image = self.imagefile
            image_np = np.array(image.convert('RGB'))  # Konversi ke format RGB

            # Meminta pengguna memasukkan nilai tx (geser horizontal)
            tx, ok_tx = QtWidgets.QInputDialog.getInt(
                None, "Translate Image", "Masukkan nilai tx (geser horizontal):")

            if ok_tx:
                # Meminta pengguna memasukkan nilai ty (geser vertikal)
                ty, ok_ty = QtWidgets.QInputDialog.getInt(
                    None, "Translate Image", "Masukkan nilai ty (geser vertikal):")

                if ok_ty:
                    height, width, _ = image_np.shape

                    # Membuat array gambar baru dengan latar belakang hitam
                    translated_image_np = np.zeros_like(image_np)

                    # Melakukan translasi gambar
                    for y in range(height):
                        for x in range(width):
                            x_translated = x + tx
                            y_translated = y + ty
                            # Memeriksa apakah koordinat baru berada dalam batas gambar
                            if 0 <= x_translated < width and 0 <= y_translated < height:
                                translated_image_np[y_translated, x_translated] = image_np[y, x]

                    # Konversi hasil translasi kembali ke Image
                    translated_image = Image.fromarray(translated_image_np)

                    # Simpan hasil translasi ke self.imageResult agar bisa digunakan untuk saveAs
                    self.imageResult = translated_image

                    # Simpan gambar hasil ke file sementara
                    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                        temp_file_path = temp_file.name
                        translated_image.save(temp_file_path)

                    # Muat gambar dari file sementara ke QPixmap
                    img_pixmap = QPixmap(temp_file_path)

                    # Mendapatkan ukuran QGraphicsView
                    view_width = self.graphicsView_2.width()
                    view_height = self.graphicsView_2.height()

                    # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
                    scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

                    # Bersihkan konten sebelumnya dan tambahkan pixmap baru ke scene
                    self.sceneOutput.clear()
                    self.sceneOutput.addPixmap(scaled_pixmap)
                    self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

                    # Hapus file sementara
                    os.remove(temp_file_path)
                else:
                    QtWidgets.QMessageBox.warning(None, "Error", "Masukkan nilai ty yang valid.")
            else:
                QtWidgets.QMessageBox.warning(None, "Error", "Masukkan nilai tx yang valid.")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Gambar belum dimuat.")

        #start menu geometri   
    def rotasi(self):
        # Pastikan imagefile sudah dimuat
        if hasattr(self, 'imagefile'):
            # Mengambil gambar dari self.imagefile
            image = self.imagefile

            # Meminta pengguna memasukkan sudut rotasi
            angle, ok = QtWidgets.QInputDialog.getInt(
                None, "Rotate Image", "Masukkan sudut rotasi (derajat):")

            if ok:
                # Rotasi gambar menggunakan PIL dengan sudut yang dimasukkan
                rotated_image = image.rotate(angle, expand=True)

                # Simpan hasil rotasi ke dalam self.imageResult untuk bisa disimpan nanti
                self.imageResult = rotated_image

                # Simpan gambar hasil ke file sementara untuk ditampilkan
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                    temp_file_path = temp_file.name
                    rotated_image.save(temp_file_path)

                # Muat gambar dari file sementara ke QPixmap
                img_pixmap = QtGui.QPixmap(temp_file_path)

                # Mendapatkan ukuran QGraphicsView
                view_width = self.graphicsView_2.width()
                view_height = self.graphicsView_2.height()

                # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
                scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

                # Bersihkan konten sebelumnya dan tambahkan pixmap baru ke scene
                self.sceneOutput.clear()
                self.sceneOutput.addPixmap(scaled_pixmap)
                self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

                # Hapus file sementara setelah semuanya selesai
                os.remove(temp_file_path)
            else:
                QtWidgets.QMessageBox.warning(
                    None, "Error", "Masukkan sudut rotasi yang valid.")
        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Gambar belum dimuat.")
            
    def show_crop_dialog(self):
        if not self.imagefile:
            QtWidgets.QMessageBox.warning(self, "Warning", "No image loaded.")
            return
        
        # Show the crop dialog
        dialog = Crop2(self.imagefile, MainWindow)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            crop_rect = dialog.get_crop_rect()
            self.crop_image(crop_rect)

    def crop_image(self, rect):
        # Ensure an image is loaded
        if not self.imagefile:
            QtWidgets.QMessageBox.warning(self, "Warning", "No image loaded.")
            return
        
        # Crop the image with the provided coordinates
        left, top, right, bottom = map(int, [rect.left(), rect.top(), rect.right(), rect.bottom()])
        cropped_image = self.imagefile.crop((left, top, right, bottom))
        self.imageResult = cropped_image

        # Save the cropped image to a temporary file and load it into QPixmap
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            cropped_image.save(temp_file_path)
        
        img_pixmap = QtGui.QPixmap(temp_file_path)
        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(img_pixmap)
        self.graphicsView_2.setScene(self.sceneOutput)
        self.graphicsView_2.fitInView(self.sceneOutput.sceneRect(), QtCore.Qt.KeepAspectRatio)
        
        os.remove(temp_file_path)
    
    def histogram_input(self):
    # Pastikan bahwa self.directory_input menunjuk ke file gambar yang valid
        if not hasattr(self, 'directory_input') or not os.path.isfile(self.directory_input):
            QtWidgets.QMessageBox.critical(None, "Error", "File tidak ditemukan atau path tidak valid.")
            return

        # Cek apakah file dapat dibaca oleh OpenCV
        image = cv2.imread(self.directory_input)
        if image is None:
            QtWidgets.QMessageBox.critical(None, "Error", "Tidak dapat membaca file gambar. Periksa path dan format file.")
            return

        # Jika berhasil, lanjutkan membuka dialog histogram
        self.histogram_input_dialog = Histogram2(self.directory_input, 'Histogram Input')
        self.histogram_input_dialog.show()

    def histogram_output(self):
        # Pastikan directory input telah di-set
        if hasattr(self, 'directory_input'):
            output_file = "output.png"  # Nama file output yang akan digunakan

            # Cek apakah self.imageResult ada dan merupakan gambar
            if hasattr(self, 'imageResult'):
                # Gunakan gambar yang ada di self.imageResult (objek PIL.Image)
                output_image = self.imageResult

                # Simpan gambar ke file sementara
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                    temp_file_path = temp_file.name
                    output_image.save(temp_file_path)

                # Muat gambar dari file sementara ke QPixmap
                img_pixmap = QtGui.QPixmap(temp_file_path)

                # Mendapatkan ukuran QGraphicsView
                view_width = self.graphicsView_2.width()
                view_height = self.graphicsView_2.height()

                # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
                scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

                # Bersihkan konten sebelumnya dan tambahkan pixmap baru ke scene
                self.sceneOutput.clear()
                self.sceneOutput.addPixmap(scaled_pixmap)
                self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

                # Tampilkan histogram output dengan dialog khusus
                self.histogram_output_dialog = Histogram2(
                    temp_file_path, 'Histogram Output')
                self.histogram_output_dialog.show()

                # Hapus file sementara
                os.remove(temp_file_path)
            else:
                QtWidgets.QMessageBox.critical(
                    None, "Error", "Tidak ada gambar yang dimuat.")
        else:
            QtWidgets.QMessageBox.critical(
                None, "Error", "Tidak ada gambar yang dimuat.")

    def histogram_input_output(self):
        self.histogram_input()
        self.histogram_output()

    def contrast(self, contrast_factor):
        # Pastikan gambar telah dibaca sebelumnya
        if not hasattr(self, 'image'):
            self.image = cv2.imread(self.imagePath, cv2.COLOR_BGR2RGB)
            
        # Convert to numpy array
        image_np = np.array(self.image, dtype=np.float32)

        # Adjust contrast based on the new factor
        contrast_image = 255 * (image_np / 255) ** (contrast_factor / 100 + 1)  # Normalisasi
        contrast_image = np.clip(contrast_image, 0, 255).astype(np.uint8)

        # Convert back to RGB for displaying
        contrast_image = cv2.cvtColor(contrast_image, cv2.COLOR_BGR2RGB)

        output_image = Image.fromarray(contrast_image)
        self.imageResult = output_image

        # Save image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output_image.save(temp_file_path)

        # Load image from temp file to QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get size of QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale pixmap to QGraphicsView
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear existing image in QGraphicsView
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def show_contrast_slider(self):
        dialog = QDialog(self.centralwidget)
        dialog.setWindowTitle("Adjust Contrast")
        dialog.setStyleSheet("background-color: white;")  # Set background color

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Add margins

        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setMinimum(-100)  # Set minimum to -100
        slider.setMaximum(100)    # Set maximum to 100
        slider.setValue(0)        # Default value at 0
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(20)
        layout.addWidget(QLabel("Adjust Contrast"))

        layout.addWidget(slider)

        value_label = QLabel(f"Contrast: {slider.value()}")
        layout.addWidget(value_label)

        slider.valueChanged.connect(lambda: value_label.setText(f"Contrast: {slider.value()}"))

        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(lambda: self.apply_contrast_change(slider.value(), dialog))
        layout.addWidget(ok_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def apply_contrast_change(self, contrast_value, dialog):
        self.contrast(contrast_value)  # Panggil fungsi kontras dengan nilai slider
        dialog.accept()

    def adjust_saturation(self, saturation_factor):
        # Pastikan gambar telah dibaca sebelumnya
        if not hasattr(self, 'image'):
            self.image = cv2.imread(self.imagePath, cv2.COLOR_BGR2RGB)

        # Jika saturation_factor adalah 0, tampilkan gambar asli
        if saturation_factor == 0:
            saturation_image = self.image
        else:
            # Convert to float32 for processing
            image_float = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV).astype(np.float32)

            # Split the HSV channels
            h, s, v = cv2.split(image_float)

            # Adjust saturation based on the new factor
            s = np.clip(s * (1 + saturation_factor / 100), 0, 255)  # Saturation adjustment

            # Merge the channels back
            saturation_image = cv2.merge((h, s, v)).astype(np.uint8)
            saturation_image = cv2.cvtColor(saturation_image, cv2.COLOR_HSV2BGR)  # Convert back to BGR

        output_image = Image.fromarray(saturation_image)
        self.imageResult = output_image

        # Save image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output_image.save(temp_file_path)

        # Load image from temp file to QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get size of QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale pixmap to QGraphicsView
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear existing image in QGraphicsView
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def show_saturation_slider(self):
        dialog = QDialog(self.centralwidget)
        dialog.setWindowTitle("Adjust Saturation")
        dialog.setStyleSheet("background-color: white;")  # Set background color

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Add margins

        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setMinimum(-100)  # Set minimum to -100
        slider.setMaximum(100)    # Set maximum to 100
        slider.setValue(0)        # Default value at 0
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(20)
        layout.addWidget(QLabel("Adjust Saturation"))

        layout.addWidget(slider)

        value_label = QLabel(f"Saturation: {slider.value()}")
        layout.addWidget(value_label)

        slider.valueChanged.connect(lambda: value_label.setText(f"Saturation: {slider.value()}"))

        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(lambda: self.apply_saturation_change(slider.value(), dialog))
        layout.addWidget(ok_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def apply_saturation_change(self, saturation_value, dialog):
        self.adjust_saturation(saturation_value)  # Panggil fungsi saturasi dengan nilai slider
        dialog.accept()

    def adjust_brightness(self, brightness_factor):
        # Pastikan gambar telah dibaca sebelumnya
        if not hasattr(self, 'image'):
            self.image = cv2.imread(self.imagePath, cv2.IMREAD_COLOR)  # Pastikan gambar dibaca sebagai RGB

        # Convert image to float32 for processing
        image_float = self.image.astype(np.float32)

        # Adjust brightness by adding the brightness factor
        brightness_image = np.clip(image_float + brightness_factor, 0, 255).astype(np.uint8)

        # Convert back to PIL image
        output_image = Image.fromarray(brightness_image)
        self.imageResult = output_image

        # Save image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output_image.save(temp_file_path)

        # Load image from temp file to QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get size of QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale pixmap to QGraphicsView
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear existing image in QGraphicsView
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def show_brightness_slider(self):
        dialog = QDialog(self.centralwidget)
        dialog.setWindowTitle("Adjust Brightness")
        dialog.setStyleSheet("background-color: white;")  # Set background color

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Add margins

        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setMinimum(-100)  # Set minimum to -100
        slider.setMaximum(100)    # Set maximum to 100
        slider.setValue(0)        # Default value at 0
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(20)
        layout.addWidget(QLabel("Adjust Brightness"))

        layout.addWidget(slider)

        value_label = QLabel(f"Brightness: {slider.value()}")
        layout.addWidget(value_label)

        slider.valueChanged.connect(lambda: value_label.setText(f"Brightness: {slider.value()}"))

        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(lambda: self.apply_brightness_change(slider.value(), dialog))
        layout.addWidget(ok_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def apply_brightness_change(self, brightness_value, dialog):
        self.adjust_brightness(brightness_value)  # Panggil fungsi brightness dengan nilai slider
        dialog.accept()


    def show_group_info(self):
        # Define the message box to display group members
        message = QMessageBox()
        message.setWindowTitle("Anggota Kelompok")
        message.setText("Nama Anggota Kelompok:\n"
                        "\nSiti Septiyah Agustin E41221559"
                        "\nJohan Indra Maulana E41221695"
                        "\nPrayoga Kusdiana Ikhsani E41221830"
                        "\nRima Sazkya E41221954"
                        "\nMichael Revaldo E41221079"
                        "\nMuhammad Reza Fadlillah E41221155"
                        "\nSuprianto E41221535")
        message.exec_()

    def erosion(self, kernel_shape='square', kernel_size=4):
        # Konversi gambar ke grayscale
        image = self.imagefile.convert("L")
        image_np = np.array(image)

        # Tentukan bentuk kernel
        if kernel_shape == 'square':
            kernel = np.ones((kernel_size, kernel_size), np.uint8)
        elif kernel_shape == 'cross':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

        # Terapkan operasi erosi
        eroded_image = cv2.erode(image_np, kernel, iterations=1)

        # Konversi array ke gambar
        image_out = Image.fromarray(eroded_image)
        self.imageResult = image_out

        # Proses yang sama untuk menampilkan gambar di QGraphicsView
        self._display_image(image_out)

    def dilation(self, kernel_shape='square', kernel_size=4):
        # Konversi gambar ke grayscale
        image = self.imagefile.convert("L")
        image_np = np.array(image)

        # Tentukan bentuk kernel
        if kernel_shape == 'square':
            kernel = np.ones((kernel_size, kernel_size), np.uint8)
        elif kernel_shape == 'cross':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

        # Terapkan operasi dilasi
        dilated_image = cv2.dilate(image_np, kernel, iterations=1)

        # Konversi array ke gambar
        image_out = Image.fromarray(dilated_image)
        self.imageResult = image_out

        # Proses yang sama untuk menampilkan gambar di QGraphicsView
        self._display_image(image_out)

    def opening(self, kernel_shape='square', kernel_size=4):
        # Konversi gambar ke grayscale
        image = self.imagefile.convert("L")
        image_np = np.array(image)

        # Tentukan bentuk kernel
        if kernel_shape == 'square':
            kernel = np.ones((kernel_size, kernel_size), np.uint8)
        elif kernel_shape == 'cross':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

        # Terapkan operasi opening (erosion diikuti dengan dilation)
        opened_image = cv2.morphologyEx(image_np, cv2.MORPH_OPEN, kernel)

        # Konversi array ke gambar
        image_out = Image.fromarray(opened_image)
        self.imageResult = image_out

        # Proses yang sama untuk menampilkan gambar di QGraphicsView
        self._display_image(image_out)

    def closing(self, kernel_shape='square', kernel_size=4):
        # Konversi gambar ke grayscale
        image = self.imagefile.convert("L")
        image_np = np.array(image)

        # Tentukan bentuk kernel
        if kernel_shape == 'square':
            kernel = np.ones((kernel_size, kernel_size), np.uint8)
        elif kernel_shape == 'cross':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

        # Terapkan operasi closing (dilation diikuti dengan erosion)
        closed_image = cv2.morphologyEx(image_np, cv2.MORPH_CLOSE, kernel)

        # Konversi array ke gambar
        image_out = Image.fromarray(closed_image)
        self.imageResult = image_out

        # Proses yang sama untuk menampilkan gambar di QGraphicsView
        self._display_image(image_out)

    def _display_image(self, image_out):
        # Simpan gambar ke temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load image dari file sementara ke QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Mendapatkan ukuran QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Mengatur pixmap untuk skala agar sesuai dengan ukuran QGraphicsView dengan tetap menjaga rasio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Bersihkan konten sebelumnya di scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        # Hapus file sementara
        os.remove(temp_file_path)

    def prewitt(self):
        # Konversi gambar ke grayscale
        image = self.imagefile.convert("L")  # Pastikan gambar dalam mode grayscale
        
        # Konversi gambar ke array NumPy
        image_np = np.array(image)
        
        # Definisi kernel Prewitt untuk sumbu X dan Y
        kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
        kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        
        # Aplikasi filter Prewitt
        edge_prewitt_x = cv2.filter2D(image_np, -1, kernelx)
        edge_prewitt_y = cv2.filter2D(image_np, -1, kernely)
        
        # Menghitung magnitudo gradien
        edges = np.sqrt(np.square(edge_prewitt_x) + np.square(edge_prewitt_y))
        
        # Normalisasi hasil deteksi tepi
        edges = np.uint8((edges / np.max(edges)) * 255)
        
        # Konversi array hasil ke gambar
        image_out = Image.fromarray(edges)
        self.imageResult = image_out
        
        # Simpan gambar ke temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load gambar dari file sementara ke QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Mendapatkan ukuran QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Mengatur pixmap untuk skala agar sesuai dengan ukuran QGraphicsView dengan tetap menjaga rasio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Bersihkan konten sebelumnya di scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        # Hapus file sementara
        os.remove(temp_file_path)

    def Sobel(self):
        # Konversi gambar ke grayscale
        image = self.imagefile.convert("L")  # Pastikan gambar dalam mode grayscale
        
        # Konversi gambar ke array NumPy
        image_np = np.array(image)
        
        # Aplikasi filter Sobel pada sumbu X dan Y
        sobelx = cv2.Sobel(image_np, cv2.CV_64F, 1, 0, ksize=3)  # Sobel pada arah X
        sobely = cv2.Sobel(image_np, cv2.CV_64F, 0, 1, ksize=3)  # Sobel pada arah Y
        
        # Menghitung magnitudo gradien
        edges = np.sqrt(np.square(sobelx) + np.square(sobely))
        
        # Normalisasi hasil deteksi tepi
        edges = np.uint8((edges / np.max(edges)) * 255)
        
        # Konversi array hasil ke gambar
        image_out = Image.fromarray(edges)
        self.imageResult = image_out
        
        # Simpan gambar ke temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load gambar dari file sementara ke QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Mendapatkan ukuran QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Mengatur pixmap untuk skala agar sesuai dengan ukuran QGraphicsView dengan tetap menjaga rasio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Bersihkan konten sebelumnya di scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        # Hapus file sementara
        os.remove(temp_file_path)

    def show_dialog_regiongrow(self):
        dialog = QDialog(self.centralwidget)
        dialog.setWindowTitle("Masukan konfigurasi Region Grow")

        # Create the main layout as a vertical layout
        layout = QVBoxLayout()

        # Add seed x label and input
        h_layout_x = QHBoxLayout()
        h_layout_x.addWidget(QLabel("Masukkan nilai seed x"))
        seedvalx = QSpinBox()
        seedvalx.setRange(0, 255)
        h_layout_x.addWidget(seedvalx)
        layout.addLayout(h_layout_x)

        # Add seed y label and input
        h_layout_y = QHBoxLayout()
        h_layout_y.addWidget(QLabel("Masukkan nilai seed y"))
        seedvaly = QSpinBox()
        seedvaly.setRange(0, 255)
        h_layout_y.addWidget(seedvaly)
        layout.addLayout(h_layout_y)

        # Add Threshold label and input
        h_layout_threshold = QHBoxLayout()
        h_layout_threshold.addWidget(QLabel("Masukkan nilai Threshold"))
        spin_box_threshold = QSpinBox()
        spin_box_threshold.setRange(0, 255)
        h_layout_threshold.addWidget(spin_box_threshold)
        layout.addLayout(h_layout_threshold)

        # Add Ok button
        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(lambda: self.applyregiongrow(seedvalx.value(), seedvaly.value(), spin_box_threshold.value(), dialog))
        layout.addWidget(ok_button)

        # Set the layout for the dialog
        dialog.setLayout(layout)
        dialog.exec_()


    def applyregiongrow(self, seed_x, seed_y, treshold, dialog):
        self.segment_region_grow((seed_x, seed_y), treshold)
        dialog.accept()

    def segment_region_grow(self, seed, threshold_value):
        output = ms.region_growing(self.imagePath, seed, threshold_value)
        self.display_image(output)

    def show_segment_cluster(self):
        dialog = QDialog(self.centralwidget)
        dialog.setWindowTitle("Kmeans Cluster")

        # Create the main layout
        layout = QVBoxLayout()

        # Add 'k' label and input
        h_layout_k = QHBoxLayout()
        h_layout_k.addWidget(QLabel("Masukkan nilai k:"))
        k_value = QSpinBox()
        k_value.setRange(1, 20)  # Set a range for 'k', you can adjust this
        k_value.setValue(2)      # Set default value
        h_layout_k.addWidget(k_value)
        layout.addLayout(h_layout_k)

        # Add Ok button
        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(lambda: self.segment_kmeans_clustering(k_value.value(), dialog))
        layout.addWidget(ok_button)

        # Set the layout for the dialog
        dialog.setLayout(layout)
        dialog.exec_()

    def segment_kmeans_clustering(self, k, dialog):
        # Perform the K-Means clustering
        output = ms.kmeans_clustering(self.imagePath, k)

        # Display the result
        self.display_image(output)

        # Close the dialog
        dialog.accept()

    def segment_watershed(self):
        output = ms.watershed_segmentation(self.imagePath)
        self.display_image(output)

    def show_segment_globalthreshold(self):
        dialog = QDialog(self.centralwidget)
        dialog.setWindowTitle('Global Threshold')

        layout = QVBoxLayout()

        # Add 'Global Threshold' label and input
        h_layout_k = QHBoxLayout()
        h_layout_k.addWidget(QLabel('Masukan nilai Global Threshold : '))
        k_value = QSpinBox()
        k_value.setRange(1, 200)
        k_value.setValue(100)
        h_layout_k.addWidget(k_value)  # Corrected this line

        layout.addLayout(h_layout_k)

        # Add Ok button
        ok_button = QPushButton("Lanjut")
        ok_button.clicked.connect(lambda: self.segment_Global_Thresholding(k_value.value(), dialog))
        layout.addWidget(ok_button)

        # Set the layout for the dialog
        dialog.setLayout(layout)
        dialog.exec_()

    def segment_Global_Thresholding(self, valtrh, dialog):
        # Perform global thresholding
        output = ms.global_thresholding(self.imagePath, valtrh)
        
        # Display the result
        self.display_image(output)
        
        # Close the dialog
        dialog.accept()

    def segment_adaptive_thresh_mean(self):
        output = ms.adaptive_thresh_mean(self.imagePath)
        self.display_image(output)

    def segment_adaptive_thresh_gaussian(self):
        output = ms.adaptive_thresh_gaussian(self.imagePath)
        self.display_image(output)

    def display_image(self, output):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output.save(temp_file_path)

        img_pixmap = QtGui.QPixmap(temp_file_path)
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        os.remove(temp_file_path)

    def scalingUniform(self):
        # Pastikan gambar telah dimuat ke self.imagefile
        if hasattr(self, 'imagefile'):
            # Mengambil gambar dari self.imagefile
            image = self.imagefile

            # Meminta pengguna memasukkan skala
            scale_factor, ok = QtWidgets.QInputDialog.getDouble(
                None, "Uniform Scaling", "Masukkan skala:"
            )

            if ok and scale_factor > 0:
                # Menghitung ukuran baru berdasarkan faktor skala
                new_width = int(image.width * scale_factor)
                new_height = int(image.height * scale_factor)

                # Mengubah ukuran gambar menggunakan metode resize dari PIL
                scaled_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Simpan hasil scaling ke file sementara
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                    temp_file_path = temp_file.name
                    scaled_image.save(temp_file_path)

                # Muat gambar dari file sementara ke QPixmap
                img_pixmap = QPixmap(temp_file_path)

                # Mendapatkan ukuran QGraphicsView
                view_width = self.graphicsView_2.width()
                view_height = self.graphicsView_2.height()

                # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
                scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

                # Bersihkan konten sebelumnya dan tambahkan pixmap baru ke scene
                self.sceneOutput.clear()
                self.sceneOutput.addPixmap(scaled_pixmap)
                self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

                # Hapus file sementara
                os.remove(temp_file_path)
            else:
                QtWidgets.QMessageBox.warning(
                    None, "Error", "Masukkan bilangan positif yang valid."
                )
        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Gambar belum dimuat."
            )

    def scalingNonUniform(self):
        # Pastikan gambar telah dimuat ke self.imagefile
        if hasattr(self, 'imagefile'):
            # Mengambil gambar dari self.imagefile
            image = self.imagefile

            # Meminta pengguna memasukkan skala untuk sumbu X dan Y
            scale_factor_x, ok_x = QtWidgets.QInputDialog.getDouble(
                None, "Non-Uniform Scaling", "Masukkan skala-X:")
            scale_factor_y, ok_y = QtWidgets.QInputDialog.getDouble(
                None, "Non-Uniform Scaling", "Masukkan skala-Y:")

            if ok_x and ok_y and scale_factor_x > 0 and scale_factor_y > 0:
                # Menghitung ukuran baru berdasarkan faktor skala
                new_width = int(image.width * scale_factor_x)
                new_height = int(image.height * scale_factor_y)

                # Mengubah ukuran gambar menggunakan metode resize dari PIL
                scaled_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Simpan hasil scaling ke self.imageResult agar bisa digunakan untuk saveAs
                self.imageResult = scaled_image

                # Simpan gambar hasil scaling ke file sementara
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                    temp_file_path = temp_file.name
                    scaled_image.save(temp_file_path)

                # Muat gambar dari file sementara ke QPixmap
                img_pixmap = QPixmap(temp_file_path)

                # Mendapatkan ukuran QGraphicsView
                view_width = self.graphicsView_2.width()
                view_height = self.graphicsView_2.height()

                # Skala pixmap agar sesuai dengan QGraphicsView, menjaga aspek rasio
                scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

                # Bersihkan konten sebelumnya dan tambahkan pixmap baru ke scene
                self.sceneOutput.clear()
                self.sceneOutput.addPixmap(scaled_pixmap)
                self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

                # Hapus file sementara
                os.remove(temp_file_path)
            else:
                QtWidgets.QMessageBox.warning(
                    None, "Error", "Masukkan bilangan positif yang valid untuk skala-X dan skala-Y.")
        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Gambar belum dimuat.") 
    def canny(self):
        # Konversi gambar ke grayscale
        image = self.imagefile.convert("L")  # Pastikan gambar dalam mode grayscale
        
        # Konversi gambar ke array NumPy
        image_np = np.array(image)
        
        # Aplikasi filter Canny
        edges = cv2.Canny(image_np, 100, 200)  # Canny Edge Detection dengan threshold 100 dan 200
        
        # Konversi array hasil ke gambar
        image_out = Image.fromarray(edges)
        self.imageResult = image_out
        
        # Simpan gambar ke temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            image_out.save(temp_file_path)

        # Load gambar dari file sementara ke QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Mendapatkan ukuran QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Mengatur pixmap untuk skala agar sesuai dengan ukuran QGraphicsView dengan tetap menjaga rasio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Bersihkan konten sebelumnya di scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())

        # Hapus file sementara
        os.remove(temp_file_path)

    def show_aritmetical(self):
        # Method to show the arithmetic panel
        self.arithmetic_panel = QtWidgets.QMainWindow()  # Create a new window
        self.ui = Ui_AritmatikaOperation()  # Create an instance of the arithmetic panel
        self.ui.setupUi(self.arithmetic_panel)  # Set up the UI in the new window
        self.arithmetic_panel.show()  # Show the arithmetic panel

    def kernel_hit_or_miss(self):
        imagepath = self.imagePath
        
        load_image = cv2.imread(imagepath, 0) 

        if load_image is None:
            print("Error: Could not load image.")
            return

        # Convert BGR to RGB
        _, image = cv2.threshold(load_image, 127, 255, cv2.THRESH_BINARY)

        # kernel hit or miss
        sq_kernel = np.array([[1, 1, 1]
                              ,[0, 1, 0]
                              ,[-1, -1, -1]])

        # morphology opening code
        hitormiss = cv2.morphologyEx(image,cv2.MORPH_HITMISS ,sq_kernel)
        
        output = Image.fromarray(hitormiss)

        self.imageResult = output

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear any previous content in the scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())
        
        # delete temp file
        os.remove(temp_file_path)

    def thinned_img(self):
        imagepath = self.imagePath
        
        # Read the image in grayscale format
        image_load = cv2.imread(imagepath, 0)  # 0 to load as grayscale

        if image_load is None:
            print("Error: Could not load image.")
            return

        # Convert the grayscale image to binary (values 0 or 255)
        _, image = cv2.threshold(image_load, 127, 255, cv2.THRESH_BINARY)

        # thinning code
        thinned = thin(image // 255)  # Divide by 255 to get binary (0 or 1)
        thinned = (thinned * 255).astype(np.uint8)  # Convert back to 255 scale for display

        
        output = Image.fromarray(thinned)

        self.imageResult = output

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear any previous content in the scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())
        
        # delete temp file
        os.remove(temp_file_path)
    
    def thickening(self):
        iamgepath = self.imagePath

        image = cv2.imread(iamgepath)  # Read in BGR format

        # convert binary
        # _, image = cv2.threshold(load_image, 127, 255, cv2.THRESH_BINARY)

        # convert RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if image is None:
            print("Error: Could not load image. Check the image path.")
            return
        
        sq_kernel = np.ones((3, 3), np.uint8)
        
        # erosion code
        erosion = cv2.erode(image, sq_kernel, iterations=1)

        # thickening
        thickening = cv2.dilate(image, sq_kernel, iterations=1) - erosion

        output = Image.fromarray(thickening)

        self.imageResult = output

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear any previous content in the scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())
        
        # delete temp file
        os.remove(temp_file_path)
    
    def skeleton_convert(self):
        iamgepath = self.imagePath

         # Read the image in grayscale format
        image = cv2.imread(iamgepath, 0)  # Load as grayscale

        if image is None:
            print("Error: Could not load image. Check the image path.")
            return

        # Convert the grayscale image to binary (values 0 or 255)
        _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

        # Apply the skeletonize function (expecting binary image with 0 or 1)
        skeleton = skeletonize(binary_image // 255)  # Divide by 255 to get binary (0 or 1)
        skeleton = (skeleton * 255).astype(np.uint8)  # Convert back to 255 scale for display
        
        return skeleton

    def skeleton(self):

        skeleton = self.skeleton_convert()
        
        output = Image.fromarray(skeleton)

        self.imageResult = output

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_2.width()
        view_height = self.graphicsView_2.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear any previous content in the scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
        self.graphicsView_2.setSceneRect(self.sceneOutput.itemsBoundingRect())
        
        # delete temp file
        os.remove(temp_file_path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
