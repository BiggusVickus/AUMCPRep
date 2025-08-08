import sys
import matlab.engine
import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QPixmap, QImage

class MatlabImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MATLAB Image in PyQt6")
        self.setGeometry(100, 100, 400, 400)

        self.label = QLabel("No image loaded")
        self.label.setScaledContents(True)

        self.button = QPushButton("Load Image from MATLAB")
        self.button.clicked.connect(self.load_matlab_image)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def load_matlab_image(self):
        # Start MATLAB engine
        # eng = matlab.engine.start_matlab()
        # matlab_img = eng.randi([1, 255], 256, 256, 3, 'uint8')  # Returns MATLAB uint8 image (RGB)
        # eng.quit()
        matlab_img = np.random.randint(1, 256, (256, 256, 3), dtype=np.uint8)

        # Convert MATLAB array to NumPy
        np_img = np.array(matlab_img, dtype=np.uint8)
        np_img = np.transpose(np_img, (1, 0, 2))  # MATLAB is column-major, transpose axes

        # Convert NumPy array to QImage
        h, w, ch = np_img.shape
        bytes_per_line = ch * w
        q_img = QImage(np_img.data.tobytes(), w, h, bytes_per_line, QImage.Format.Format_RGB888)

        # Convert to QPixmap and show
        pixmap = QPixmap.fromImage(q_img)
        self.label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = MatlabImageViewer()
    viewer.show()
    sys.exit(app.exec())