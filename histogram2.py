import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Histogram2(QDialog):
    def __init__(self, image_path, name):
        super().__init__()

        self.imageObj = cv2.imread(image_path)
        self.blue_color = cv2.calcHist(
            [self.imageObj], [0], None, [256], [0, 256])
        self.red_color = cv2.calcHist(
            [self.imageObj], [1], None, [256], [0, 256])
        self.green_color = cv2.calcHist(
            [self.imageObj], [2], None, [256], [0, 256])

        self.initUI(name)

    def initUI(self, name):
        layout = QVBoxLayout()

        # Membuat plot histogram
        self.blue_plot = self.create_histogram_plot(self.blue_color, 'Blue')
        layout.addWidget(self.blue_plot)

        self.green_plot = self.create_histogram_plot(self.green_color, 'Green')
        layout.addWidget(self.green_plot)

        self.red_plot = self.create_histogram_plot(self.red_color, 'Red')
        layout.addWidget(self.red_plot)

        button_close = QPushButton("Tutup")
        button_close.clicked.connect(self.close)
        layout.addWidget(button_close)

        self.setLayout(layout)
        self.setWindowTitle(name)
        self.setFixedSize(800, 600)  # Mengatur ukuran jendela agar lebih baik

    def create_histogram_plot(self, histogram, color):
        fig = Figure()
        ax = fig.add_subplot(111)

        # Memplot histogram dengan peningkatan
        ax.hist(np.arange(256), bins=256, weights=histogram.flatten(), color=color.lower(), alpha=0.8, edgecolor='black')
        ax.set_xlim([0, 255])
        ax.set_ylim([0, max(histogram) * 1.1])  # Menyesuaikan batas y untuk visualisasi yang lebih baik

        # Menyembunyikan angka pada sumbu x dan y
        ax.set_xticks([])  # Menghilangkan tick pada sumbu x
        ax.set_yticks([])  # Menghilangkan tick pada sumbu y

        # Menambahkan grid
        ax.grid(color='gray', linestyle='--', linewidth=0.7, alpha=0.5)

        canvas = FigureCanvas(fig)
        return canvas


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Tidak ada path gambar yang hardcoded, ini akan ditangani oleh logika aplikasi Anda
    sys.exit(app.exec_())
