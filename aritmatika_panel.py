import os
import cv2
import tempfile
from PIL import Image, ImageOps
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QSlider, QDialog, QVBoxLayout, QHBoxLayout, QSpinBox, QLabel, QLineEdit, QDialogButtonBox, QPushButton, QApplication, QGraphicsPixmapItem, QInputDialog
from aritmatika import Aritmatika

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AritmatikaOperation(object):
    def __init__(self):
        self.imagePath = None
        self.imagePath2 = None
        self.imagefile = None
        self.imagefile2 = None
        self.imageResult = None

    def saveAs(self):
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

    def openImage1(self):
        # Show file dialog to select an image file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.jpeg)", options=options)
        
        if fileName:
            self.imagePath = fileName
            image_path = fileName
            img = Image.open(image_path)
            self.imagefile = img
            # img.show()

            # Load the image and display it in the QGraphicsView
            self.image_pixmap = QtGui.QPixmap(fileName)

            # Get the size of the QGraphicsView
            view_width = self.graphicsView.width()
            view_height = self.graphicsView.height()

            # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
            scaled_pixmap = self.image_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

            self.scene.clear()  # Clear any previous content in the scene
            self.scene.addPixmap(scaled_pixmap)
            # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
            self.graphicsView.setSceneRect(self.scene.itemsBoundingRect())

    def openImage2(self):
        # Show file dialog to select an image file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.jpeg)", options=options)
        
        if fileName:
            self.imagePath2 = fileName
            image_path = fileName
            img = Image.open(image_path)
            self.imagefile2 = img
            # img.show()

            # Load the image and display it in the QGraphicsView
            self.image_pixmap = QtGui.QPixmap(fileName)

            # Get the size of the QGraphicsView
            view_width = self.graphicsView_2.width()
            view_height = self.graphicsView_2.height()

            # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
            scaled_pixmap = self.image_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

            self.scene2.clear()  # Clear any previous content in the scene
            self.scene2.addPixmap(scaled_pixmap)
            # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
            self.graphicsView_2.setSceneRect(self.scene2.itemsBoundingRect())
    
    def addition(self):
        obj = Aritmatika(self.imagePath, self.imagePath2)

        result = obj.penjumlahan()

        self.showImageResult(result)

    def substraction(self):
        obj = Aritmatika(self.imagePath, self.imagePath2)
        
        result = obj.pengurangan()

        self.showImageResult(result)

    def multiplication(self):
        obj = Aritmatika(self.imagePath, self.imagePath2)
        
        result = obj.perkalian()

        self.showImageResult(result)

    def distribution(self):
        obj = Aritmatika(self.imagePath, self.imagePath2)
        
        result = obj.pembagian()

        self.showImageResult(result)

    def or_(self):
        obj = Aritmatika(self.imagePath, self.imagePath2)
        
        result = obj.or_operation()

        self.showImageResult(result)

    def and_(self):
        obj = Aritmatika(self.imagePath, self.imagePath2)
        
        result = obj.and_operation()

        self.showImageResult(result)

    def xor_(self):
        obj = Aritmatika(self.imagePath, self.imagePath2)
        
        result = obj.xor_operation()

        self.showImageResult(result)

    def showImageResult(self, output):
        self.imageResult = output

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file_path = temp_file.name
            output.save(temp_file_path)

        # Load the image from the temporary file into QPixmap
        img_pixmap = QtGui.QPixmap(temp_file_path)

        # Get the size of the QGraphicsView
        view_width = self.graphicsView_3.width()
        view_height = self.graphicsView_3.height()

        # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
        scaled_pixmap = img_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Clear any previous content in the scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())
        
        # delete temp file
        os.remove(temp_file_path)

    def setupUi(self, AritmatikaOperation):
        AritmatikaOperation.setObjectName("AritmatikaOperation")
        AritmatikaOperation.resize(1336, 600)
        self.centralwidget = QtWidgets.QWidget(AritmatikaOperation)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 70, 391, 381))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(480, 70, 391, 381))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.scene2 = QGraphicsScene()
        self.graphicsView_2.setScene(self.scene2)

        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(920, 70, 391, 381))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.sceneOutput = QGraphicsScene()
        self.graphicsView_3.setScene(self.sceneOutput)

        self.label.setGeometry(QtCore.QRect(40, 50, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(930, 50, 81, 16))
        self.label_3.setObjectName("label_3")
        AritmatikaOperation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AritmatikaOperation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1336, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPertitungan = QtWidgets.QMenu(self.menubar)
        self.menuPertitungan.setObjectName("menuPertitungan")
        self.menuNotasi = QtWidgets.QMenu(self.menubar)
        self.menuNotasi.setObjectName("menuNotasi")
        AritmatikaOperation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AritmatikaOperation)
        self.statusbar.setObjectName("statusbar")
        AritmatikaOperation.setStatusBar(self.statusbar)
        self.actionGambar_1 = QtWidgets.QAction(AritmatikaOperation)
        self.actionGambar_1.setObjectName("actionGambar_1")
        self.actionGambar_2 = QtWidgets.QAction(AritmatikaOperation)
        self.actionGambar_2.setObjectName("actionGambar_2")
        self.actionSimpan = QtWidgets.QAction(AritmatikaOperation)
        self.actionSimpan.setObjectName("actionSimpan")
        self.actionClear = QtWidgets.QAction(AritmatikaOperation)
        self.actionClear.setObjectName("actionClear")
        self.actionExit = QtWidgets.QAction(AritmatikaOperation)
        self.actionExit.setObjectName("actionExit")
        self.actionPenjumlahan = QtWidgets.QAction(AritmatikaOperation)
        self.actionPenjumlahan.setObjectName("actionPenjumlahan")
        self.actionPengurangan = QtWidgets.QAction(AritmatikaOperation)
        self.actionPengurangan.setObjectName("actionPengurangan")
        self.actionPembagian = QtWidgets.QAction(AritmatikaOperation)
        self.actionPembagian.setObjectName("actionPembagian")
        self.actionPerkalian = QtWidgets.QAction(AritmatikaOperation)
        self.actionPerkalian.setObjectName("actionPerkalian")
        self.actionOR = QtWidgets.QAction(AritmatikaOperation)
        self.actionOR.setObjectName("actionOR")
        self.actionAND = QtWidgets.QAction(AritmatikaOperation)
        self.actionAND.setObjectName("actionAND")
        self.actionNOT = QtWidgets.QAction(AritmatikaOperation)
        self.actionNOT.setObjectName("actionNOT")
        self.actionXOR = QtWidgets.QAction(AritmatikaOperation)
        self.actionXOR.setObjectName("actionXOR")
        self.menuFile.addAction(self.actionGambar_1)
        self.menuFile.addAction(self.actionGambar_2)
        self.menuFile.addAction(self.actionSimpan)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuPertitungan.addAction(self.actionPenjumlahan)
        self.menuPertitungan.addAction(self.actionPengurangan)
        self.menuPertitungan.addAction(self.actionPembagian)
        self.menuPertitungan.addAction(self.actionPerkalian)
        self.menuNotasi.addAction(self.actionOR)
        self.menuNotasi.addAction(self.actionAND)
        self.menuNotasi.addAction(self.actionNOT)
        self.menuNotasi.addAction(self.actionXOR)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPertitungan.menuAction())
        self.menubar.addAction(self.menuNotasi.menuAction())

        self.actionGambar_1.triggered.connect(self.openImage1)
        self.actionGambar_2.triggered.connect(self.openImage2)
        self.actionPenjumlahan.triggered.connect(self.addition)
        self.actionPengurangan.triggered.connect(self.substraction)
        self.actionPembagian.triggered.connect(self.distribution)
        self.actionPerkalian.triggered.connect(self.multiplication)
        self.actionSimpan.triggered.connect(self.saveAs)
        self.actionOR.triggered.connect(self.and_)
        self.actionAND.triggered.connect(self.or_)
        self.actionXOR.triggered.connect(self.xor_)


        self.retranslateUi(AritmatikaOperation)
        QtCore.QMetaObject.connectSlotsByName(AritmatikaOperation)

    def retranslateUi(self, AritmatikaOperation):
        _translate = QtCore.QCoreApplication.translate
        AritmatikaOperation.setWindowTitle(_translate("AritmatikaOperation", "MainWindow"))
        self.label.setText(_translate("AritmatikaOperation", "Gambar 1"))
        self.label_2.setText(_translate("AritmatikaOperation", "Gambar 2"))
        self.label_3.setText(_translate("AritmatikaOperation", "Hasil"))
        self.menuFile.setTitle(_translate("AritmatikaOperation", "File"))
        self.menuPertitungan.setTitle(_translate("AritmatikaOperation", "Pertitungan"))
        self.menuNotasi.setTitle(_translate("AritmatikaOperation", "Notasi"))
        self.actionGambar_1.setText(_translate("AritmatikaOperation", "Gambar 1"))
        self.actionGambar_2.setText(_translate("AritmatikaOperation", "Gambar 2"))
        self.actionSimpan.setText(_translate("AritmatikaOperation", "Simpan"))
        self.actionClear.setText(_translate("AritmatikaOperation", "Clear"))
        self.actionExit.setText(_translate("AritmatikaOperation", "Exit"))
        self.actionPenjumlahan.setText(_translate("AritmatikaOperation", "Penjumlahan"))
        self.actionPengurangan.setText(_translate("AritmatikaOperation", "Pengurangan"))
        self.actionPembagian.setText(_translate("AritmatikaOperation", "Pembagian"))
        self.actionPerkalian.setText(_translate("AritmatikaOperation", "Perkalian"))
        self.actionOR.setText(_translate("AritmatikaOperation", "OR"))
        self.actionAND.setText(_translate("AritmatikaOperation", "AND"))
        self.actionNOT.setText(_translate("AritmatikaOperation", "NOT"))
        self.actionXOR.setText(_translate("AritmatikaOperation", "XOR"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AritmatikaOperation = QtWidgets.QMainWindow()
    ui = Ui_AritmatikaOperation()
    ui.setupUi(AritmatikaOperation)
    AritmatikaOperation.show()
    sys.exit(app.exec_())
