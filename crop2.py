from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import Image
import tempfile
import os

class Crop2(QtWidgets.QDialog):
    def __init__(self, image, parent=None):
        super().__init__(parent)
        self.image = image
        self.initUI()

    def initUI(self):
        # Set up the layout and image view
        self.setWindowTitle("Select Region to Crop")
        self.setGeometry(100, 100, 800, 600)

        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.graphicsView)

        # Load image into QGraphicsScene
        img_pixmap = QtGui.QPixmap.fromImage(self.pil_image_to_qimage(self.image))
        self.image_item = QtWidgets.QGraphicsPixmapItem(img_pixmap)
        self.scene.addItem(self.image_item)
        self.graphicsView.setScene(self.scene)

        # Set up the full-size selection rectangle (border)
        self.selection_rect = QtCore.QRectF(0, 0, img_pixmap.width(), img_pixmap.height())
        self.selection_item = QtWidgets.QGraphicsRectItem(self.selection_rect)
        self.selection_item.setPen(QtGui.QPen(QtCore.Qt.red, 2))
        self.scene.addItem(self.selection_item)

        # Enable mouse dragging for the selection rectangle
        self.selection_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.selection_item.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.selection_item.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges)

        # Connect dialog buttons
        self.buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout().addWidget(self.buttons)

        # Enable resizing via mouse events
        self.resizing = False
        self.graphicsView.viewport().installEventFilter(self)

    def pil_image_to_qimage(self, pil_image):
        # Convert PIL Image to QImage
        img_byte_array = pil_image.convert('RGB').tobytes()
        return QtGui.QImage(img_byte_array, pil_image.width, pil_image.height, pil_image.width * 3, QtGui.QImage.Format_RGB888)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            pos = event.pos()
            scene_pos = self.graphicsView.mapToScene(pos)
            
            # Check if the mouse is near the border for resizing
            if self.is_near_border(scene_pos):
                self.resizing = True
                self.start_pos = scene_pos
                return True
        
        elif event.type() == QtCore.QEvent.MouseMove:
            if self.resizing:
                end_pos = self.graphicsView.mapToScene(event.pos())
                self.resize_selection_rect(end_pos)
                return True
        
        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            self.resizing = False
            return True

        return super().eventFilter(obj, event)

    def is_near_border(self, pos):
        """Check if the mouse position is near the border of the selection rectangle."""
        margin = 10  # Define a margin for detecting proximity to the border
        rect = self.selection_item.rect()
        return (
            abs(pos.x() - rect.left()) < margin or
            abs(pos.x() - rect.right()) < margin or
            abs(pos.y() - rect.top()) < margin or
            abs(pos.y() - rect.bottom()) < margin
        )

    def resize_selection_rect(self, end_pos):
        """Resize the selection rectangle based on the new mouse position."""
        new_rect = QtCore.QRectF(self.selection_item.rect())
        
        if abs(end_pos.x() - new_rect.left()) < 10:  # Resize from left
            new_rect.setLeft(end_pos.x())
        elif abs(end_pos.x() - new_rect.right()) < 10:  # Resize from right
            new_rect.setRight(end_pos.x())
        
        if abs(end_pos.y() - new_rect.top()) < 10:  # Resize from top
            new_rect.setTop(end_pos.y())
        elif abs(end_pos.y() - new_rect.bottom()) < 10:  # Resize from bottom
            new_rect.setBottom(end_pos.y())
        
        # Update the selection rectangle with the new dimensions
        self.selection_item.setRect(new_rect)

    def get_crop_rect(self):
        # Return the updated selection rectangle
        return self.selection_item.rect()
