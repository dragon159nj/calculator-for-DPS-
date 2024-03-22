import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        
        layout1 = QVBoxLayout()

        layout1.addWidget(QLabel("what is the Rounds fired per minute"))

        layout1.addWidget(QDoubleSpinBox())
        layout1.addWidget(QLabel("what is the Rounds fired per minute"))

        layout1.addWidget(QDoubleSpinBox())
        layout1.addWidget(QLabel("what is the Rounds fired per minute"))

        layout1.addWidget(QDoubleSpinBox())
        widget = QWidget()
        widget.setLayout(layout1)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

widget = QLabel("Hello")

"""""
       widgets = [
            QLabel,
            QDoubleSpinBox,
            QLabel,
            QDoubleSpinBox,
            QLabel,
            QDoubleSpinBox,
            QLabel,
            QCheckBox,
            QLabel,
            QDoubleSpinBox,
            QLabel,
            QPushButton,
        ]
"""