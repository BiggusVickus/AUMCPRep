

import sys
import numpy as np
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QFileDialog, QLabel
)
import matlab.engine

class FileFolderSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select File or Folder3")
        self.setGeometry(100, 100, 400, 200)
        self.file_path = None

        layout = QVBoxLayout()

        self.file_label = QLabel("No file selected")

        file_btn = QPushButton("Select File")
        file_btn.clicked.connect(self.select_file)

        denoiser_btn = QPushButton("Run Denoiser")
        denoiser_btn.clicked.connect(self.denoise)

        layout.addWidget(file_btn)
        layout.addWidget(self.file_label)
        layout.addWidget(denoiser_btn)

        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            self.file_path = file_path
            file_path = self.file_label.setText(f"File: {file_path}")

    def denoise(self):
        if self.file_path:
            eng = matlab.engine.start_matlab()
            result = eng.denoise(self.file_path, nargout=1)
            self.file_label.setText(f"Denoised: {result}")
            eng.quit()
            image = np.array(result)
            h, w = image.shape
            bytes_per_line = w * 1
            q_img = QImage(image.tobytes(), w, h, bytes_per_line, QImage.Format.Format_Grayscale8)

            # Convert to QPixmap and show

            label = QLabel(self)
            pixmap = QPixmap.fromImage(q_img)
            label.setPixmap(pixmap)
            self.layout().addWidget(label)
            self.resize(pixmap.width(), pixmap.height())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileFolderSelector()
    window.show()
    sys.exit(app.exec())